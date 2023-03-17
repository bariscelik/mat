cmake_minimum_required(VERSION 3.15)

find_package(EIGEN3 REQUIRED)

add_library(cgcustommath cgcustommath.cpp)

# install(TARGETS mat
#    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR})

target_link_libraries(cgcustommath Eigen3::Eigen)