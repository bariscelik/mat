cmake_minimum_required(VERSION 3.15)

project(mat LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(EIGEN3 REQUIRED)

add_executable(mat main.cpp)

# install(TARGETS mat
#    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR})

add_subdirectory(lib)

include_directories(lib)

target_link_libraries(mat Eigen3::Eigen cgcustommath)
