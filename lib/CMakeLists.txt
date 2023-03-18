cmake_minimum_required(VERSION 3.15)

find_package(EIGEN3 REQUIRED)

set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)
add_library(cgcustommath SHARED cgcustommath.cpp)

target_link_libraries(cgcustommath Eigen3::Eigen)