cmake_minimum_required(VERSION 3.10)

project(SudokuSolver C)

add_executable(sudoku_solver 
    src/puzzle.c
    src/sudoku.c
)

set_property(TARGET sudoku_solver PROPERTY CMAKE_C_STANDARD 11)
set_property(TARGET sudoku_solver PROPERTY CMAKE_C_STANDARD_REQUIRED TRUE)

target_compile_options(sudoku_solver PRIVATE
    -Wall
    -Wextra
    -pedantic
    -Werror
    -Wformat=2
    -Wnull-dereference
    -Wstrict-prototypes

    $<$<CONFIG:Debug>:-g>
    $<$<CONFIG:Debug>:-O0>

    $<$<CONFIG:Release>:-O3>
    $<$<CONFIG:Release>:-DNDEBUG>
    $<$<CONFIG:Release>:-march=native>
)

target_include_directories(sudoku_solver PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/inc
)
