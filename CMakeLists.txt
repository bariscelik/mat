cmake_minimum_required(VERSION 3.15)

project(mat LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(EIGEN3 REQUIRED)

add_executable(mat main.cpp)

add_subdirectory(lib)
include_directories(lib)

target_link_libraries(mat PRIVATE cgcustommath)

if(WIN32)
add_custom_command ( TARGET mat POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy_if_different
    $<TARGET_FILE:cgcustommath> $<TARGET_FILE_DIR:mat>
)
endif()

if(APPLE)
    set_target_properties(mat PROPERTIES
        XCODE_EMBED_FRAMEWORKS							"cgcustommath"
        XCODE_ATTRIBUTE_LD_RUNPATH_SEARCH_PATHS         "@executable_path/../Frameworks"
        XCODE_EMBED_FRAMEWORKS_CODE_SIGN_ON_COPY		"YES"
        XCODE_EMBED_FRAMEWORKS_REMOVE_HEADERS_ON_COPY	"YES"
        XCODE_ATTRIBUTE_ENABLE_HARDENED_RUNTIME			"YES"
        XCODE_ATTRIBUTE_CODE_SIGN_STYLE                 "Automatic"
        MACOSX_BUNDLE                                   true
        MACOSX_BUNDLE_GUI_IDENTIFIER                    com.bariscelik.mat
        MACOSX_BUNDLE_BUNDLE_NAME                       mat
        MACOSX_BUNDLE_BUNDLE_VERSION                    "0.1"
        MACOSX_BUNDLE_SHORT_VERSION_STRING              "0.1"
    )
endif()