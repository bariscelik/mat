cmake_minimum_required(VERSION 3.15)

find_package(EIGEN3 REQUIRED)

set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)
add_library(cgcustommath SHARED cgcustommath.cpp cgcustommath.h)

target_link_libraries(cgcustommath Eigen3::Eigen)

if(APPLE)
    set_target_properties(cgcustommath PROPERTIES
        #XCODE_ATTRIBUTE_LD_RUNPATH_SEARCH_PATHS         "@executable_path/../Frameworks/libcgcustommath.dyld"
        FRAMEWORK TRUE
        FRAMEWORK_VERSION A
        MACOSX_FRAMEWORK_IDENTIFIER com.baris.cgcustommath
        VERSION 1.0.0
        SOVERSION 1.0.0
        PUBLIC_HEADER cgcustommath.h
        #XCODE_ATTRIBUTE_CODE_SIGN_IDENTITY "Apple Development"
    )
endif()