cmake_minimum_required(VERSION 3.10)
project(kinhw LANGUAGES CXX VERSION 1.0)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)
#set(CMAKE_CXX_COMPILER "g++")
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)


# add executables
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/bin)
file(GLOB_RECURSE SOURCES ${CMAKE_SOURCE_DIR}/src/*.cpp)
add_executable(${PROJECT_NAME} ${SOURCES})

# add yaml support for config files
find_package(yaml-cpp REQUIRED)

# add eigen
find_package(Eigen3 3.3 REQUIRED NO_MODULE)

target_include_directories(${PROJECT_NAME} PRIVATE
    ${EIGEN3_INCLUDE_DIRS}
    ${YAML_CPP_INCLUDE_DIRS}
)
target_link_libraries(${PROJECT_NAME} PRIVATE
    Eigen3::Eigen 
    yaml-cpp::yaml-cpp
)

# Custom flags for Debug
set(DEBUG_FLAGS 
    -Wall
    -Wextra
    -Wshadow
    -Wconversion
    -Wnull-dereference
)

set(DEBUG_SANITIZERS 
    -fsanitize=undefined
    #-fsanitize=address
    -fno-sanitize-recover=all
)


target_compile_options(${PROJECT_NAME} PRIVATE 
    $<$<CONFIG:Debug>:${DEBUG_FLAGS} ${DEBUG_SANITIZERS} -O0 -g -DDEBUG>
    $<$<CONFIG:Release>:-O3 -DNDEBUG>
) 
target_link_options(${PROJECT_NAME} PRIVATE
    $<$<CONFIG:Debug>:${DEBUG_SANITIZERS}>
)

message(STATUS "Build type: ${CMAKE_BUILD_TYPE}")
