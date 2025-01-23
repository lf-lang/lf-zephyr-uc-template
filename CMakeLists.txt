cmake_minimum_required(VERSION 3.20.0)
include($ENV{REACTOR_UC_PATH}/cmake/lfc.cmake)

set(PLATFORM "ZEPHYR" CACHE STRING "Platform to target")
set(BOARD "native_sim")
set(LF_MAIN "HelloWorld")
find_package(Zephyr REQUIRED HINTS deps/zephyr)
project(reactor-uc-zephyr)

lf_setup()
lf_run_lfc(src ${LF_MAIN})
lf_build_generated_code(app src-gen/${LF_MAIN})

