cmake_minimum_required(VERSION 3.20.0)
include($ENV{REACTOR_UC_PATH}/cmake/lfc.cmake)

set(PLATFORM "ZEPHYR" CACHE STRING "Platform to target")
set(BOARD "native_sim")
set(LF_MAIN "HelloWorld")
find_package(Zephyr REQUIRED HINTS ${CMAKE_CURRENT_SOURCE_DIR}/deps/zephyr)
project(${LF_MAIN})

lf_setup()
lf_run_lfc(${CMAKE_CURRENT_SOURCE_DIR}/src ${LF_MAIN})
lf_build_generated_code(app ${CMAKE_CURRENT_SOURCE_DIR}/src-gen/${LF_MAIN})

