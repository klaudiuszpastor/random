cmake_minimum_required(VERSION 3.10)
project(OpenCVProject)

set(OpenCV_DIR "~/Projects/random/openCV-stuff/opencv-install/lib/cmake/opencv4")

find_package(OpenCV REQUIRED core highgui)

add_executable(my_app main.cpp)

target_link_libraries(my_app ${OpenCV_LIBS})
