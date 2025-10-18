cmake_minimum_required(VERSION 3.10)

project(HandGestureRecognition CXX)

# CMake will now rely on system paths or the -D CMAKE_PREFIX_PATH argument.

find_package(OpenCV REQUIRED)

add_executable(hand_gesture_recognition
    src/main.cc
    src/utils.cc
    src/vision_analysis.cc
)

set_property(TARGET hand_gesture_recognition PROPERTY CXX_STANDARD 20)
set_property(TARGET hand_gesture_recognition PROPERTY CXX_STANDARD_REQUIRED TRUE)

target_compile_options(hand_gesture_recognition PRIVATE
    -Wall
    -Wextra
    -pedantic

    $<$<CONFIG:Debug>:-g -O0>

    $<$<CONFIG:Release>:-O3>
)

target_include_directories(hand_gesture_recognition PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/inc
)

target_link_libraries(hand_gesture_recognition PRIVATE
    opencv_core      # core functionality
    opencv_imgproc   # image processing
    opencv_highgui   # user interface and display
    opencv_imgcodecs # reading/writing images
)
