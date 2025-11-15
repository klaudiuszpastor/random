import os
import subprocess
import json
import sys
from pathlib import Path
import shutil

#
# Constants
#

CONFIG_FILE = 'build_config.json'
BUILD_DIR = 'build'
OPENCV_PATH_KEY = 'OPENCV_PREFIX_PATH'
BUILD_TYPE_KEY = 'BUILD_TYPE'
PROJECT_ROOT = Path(__file__).parent

#
# Detect number of CPU cores
#

SYSTEM_CORES = os.cpu_count() or 4

def load_config():
    try:
        with open(PROJECT_ROOT / CONFIG_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_config(config):
    with open(PROJECT_ROOT / CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)

def get_build_type(config):
    saved_type = config.get(BUILD_TYPE_KEY)

    if saved_type:
        print(f"\n--- Build Configuration Type ---")
        print(f"Saved build type found: {saved_type}")
        return saved_type

    print("\n--- Build Configuration Type ---")

    choice = input("Select build type: [D]ebug, [R]elease [D]: ").strip().lower()

    if choice == 'r':
        return 'Release'
    elif choice == 'd' or choice == '':
        return 'Debug'
    else:
        print("Invalid input. Please choose 'D' for Debug or 'R' for Release.")

def get_opencv_path(config):
    path = config.get(OPENCV_PATH_KEY)

    if path and Path(path).is_dir():
        print(f"Using previously saved OpenCV path: {path}")
        return path

    print("\n--- OpenCV Path Setup ---")
    print("OpenCV prefix path not found or invalid.")
    print("Please enter the **root installation directory** of your custom OpenCV build.")

    while True:
        new_path = input("Enter CMAKE_PREFIX_PATH: ").strip()

        #
        # Expand user path (~/) and resolve it to an absolute path
        #

        expanded_path = Path(new_path).expanduser().resolve()

        if expanded_path.is_dir():
            print(f"Path accepted: {expanded_path}")
            return str(expanded_path)
        else:
            print(f"Error: Directory not found at '{new_path}'. Please try again.")

def run_command(command, cwd=None):
    print(f"\n---> Executing: {' '.join(command)}")
    try:
        # Check=True will raise an exception if the command fails
        subprocess.run(command, check=True, cwd=cwd or PROJECT_ROOT)
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n!!! COMMAND FAILED with exit code {e.returncode} !!!")
        print(f"Error output:\n{e.stdout.decode()}")
        return False
    except FileNotFoundError:
        print(f"\n!!! COMMAND FAILED: Make sure '{command[0]}' is installed and in your PATH. !!!")
        return False

def configure_project(opencv_path, build_type):
    build_path = PROJECT_ROOT / BUILD_DIR
    build_path.mkdir(exist_ok=True)
    os.chdir(build_path)

    cmake_command = [
        'cmake',
        '-G', 'Ninja',
        '-D', f'CMAKE_BUILD_TYPE={build_type}',
        '-D', f'CMAKE_PREFIX_PATH={opencv_path}',
        '..'
    ]

    return run_command(cmake_command, cwd=build_path)

def build_project():
    build_path = PROJECT_ROOT / BUILD_DIR
    if not build_path.is_dir():
        print(f"Error: Build directory '{BUILD_DIR}' does not exist. Run 'python builder.py build' first.")
        return False

    print(f"\n--- Ninja Compilation ---")
    print(f"Using {SYSTEM_CORES} threads for maximum build speed.")

    #
    # Ninja command: ninja -j<num_cores>
    #

    ninja_command = ['ninja', '-j', str(SYSTEM_CORES)]

    return run_command(ninja_command, cwd=build_path)

def clean_project():
    build_path = PROJECT_ROOT / BUILD_DIR
    
    if build_path.is_dir():
        print(f"\n--- Cleaning Project ---")
        print(f"Removing build directory: {build_path}")
        try:
            shutil.rmtree(build_path)
            print("Clean successful.")
            return True
        except Exception as e:
            print(f"Error during cleaning: {e}")
            return False
    else:
        print(f"Build directory '{BUILD_DIR}' does not exist. Nothing to clean.")
        return True

def reset_config():
    """Removes the configuration file."""
    config_path = PROJECT_ROOT / CONFIG_FILE
    
    if config_path.exists():
        print(f"\n--- Resetting Configuration ---")
        try:
            os.remove(config_path)
            print(f"Successfully removed configuration file: {CONFIG_FILE}")
            return True
        except Exception as e:
            print(f"Error removing configuration file: {e}")
            return False
    else:
        print(f"Configuration file '{CONFIG_FILE}' does not exist. Nothing to reset.")
        return True


def show_help():
    """Displays help information."""
    print("\n==============================================")
    print("CMake Project Builder (using Ninja)")
    print("----------------------------------------------")
    print(f"Usage: python {Path(__file__).name} <command>")
    print("\nCommands:")
    print("  build       : Configure (if needed) and compile the project using Ninja (default).")
    print("  clean       : Remove the entire build directory.")
    print("  reset-config: Remove the saved configuration file (build_config.json).")
    print("==============================================")

def main():
    command = sys.argv[1].lower() if len(sys.argv) > 1 else 'build'

    if command == 'clean':
        clean_project()
        return

    if command == 'reset-config':
        reset_config()
        return

    if command == 'build':
        #
        # Load configuration and get/validate OpenCV path
        #

        config = load_config()
        opencv_path = get_opencv_path(config)
        build_type = get_build_type(config)

        #
        # Save the path if it's new or was just validated
        #

        if config.get(OPENCV_PATH_KEY) != opencv_path or config.get(BUILD_TYPE_KEY) != build_type:
             config[OPENCV_PATH_KEY] = opencv_path
             config[BUILD_TYPE_KEY] = build_type
             save_config(config)
             print("\nConfiguration saved.")

        print(f"\nConfiguration: {build_type} | Cores: {SYSTEM_CORES}")

        #
        # Configure CMake
        #

        if not configure_project(opencv_path, build_type):
            print("\n--- CMake Configuration FAILED ---")
            return

        #
        # Ninja build
        #

        if not build_project():
            print("\n--- Compilation FAILED ---")
            return

        print("\n==============================================")
        print(f"SUCCESS! Project built in the '{BUILD_DIR}/' directory.")
        print(f"Type: {build_type}")
        print("Run the executable: ./build/hand_gesture_recognition")
        print("==============================================")
        return
        
    # If command is unknown
    show_help()

if __name__ == '__main__':
    main()
