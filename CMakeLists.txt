cmake_minimum_required(VERSION 3.20.0)
set(PLATFORM "ZEPHYR" CACHE STRING "Platform to target")
set(LF_MAIN_NAME "" CACHE STRING "Name of the LF application")
set(LF_SRC_GEN_PATH "" CACHE STRING "Name of the LF application")

find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})
project(reactor-uc-zephyr)

# Build the generated C code.
include(${LF_SRC_GEN_PATH}/${LF_MAIN_NAME}/CMakeLists.txt)
add_subdirectory(${REACTOR_UC_PATH})
target_sources(app PRIVATE ${LFC_GEN_MAIN} ${LFC_GEN_SOURCES})
target_include_directories(app PRIVATE ${LFC_GEN_INCLUDE_DIRS})
target_link_libraries(app PRIVATE reactor-uc)
