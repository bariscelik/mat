cmake_minimum_required(VERSION 3.15)

find_package(EIGEN3 REQUIRED)

set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)
add_library(cgcustommath SHARED cgcustommath.cpp)

target_link_libraries(cgcustommath Eigen3::Eigen)

if(APPLE)
    set_target_properties(cgcustommath PROPERTIES
        XCODE_ATTRIBUTE_LD_RUNPATH_SEARCH_PATHS         "@executable_path/../Frameworks/libcgcustommath.dyld"
    )
endif()