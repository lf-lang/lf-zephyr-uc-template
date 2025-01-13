cmake_minimum_required(VERSION 3.20.0)
set(PLATFORM "ZEPHYR" CACHE STRING "Platform to target")
set(BOARD "native_posix")

if (NOT DEFINED LF_MAIN)
  set(LF_MAIN "HelloWorld")
endif()

if (NOT DEFINED LOG_LEVEL)
  set(LOG_LEVEL "LF_LOG_LEVEL_WARN")
endif()

find_package(Zephyr REQUIRED HINTS ${CMAKE_CURRENT_SOURCE_DIR}/deps/zephyr)
project(reactor-uc-zephyr)

# Run LFC
set(LFC_COMMAND $ENV{REACTOR_UC_PATH}/lfc/bin/lfc-dev ${CMAKE_CURRENT_SOURCE_DIR}/src/${LF_MAIN}.lf)
execute_process(COMMAND echo "Running LFC: ${LFC_COMMAND}")
execute_process(
    COMMAND ${LFC_COMMAND}
    ECHO_OUTPUT_VARIABLE
    COMMAND_ERROR_IS_FATAL ANY
)

file(GLOB_RECURSE LF_SOURCES ${CMAKE_CURRENT_SOURCE_DIR}/src/*.lf)
set_property(DIRECTORY APPEND PROPERTY CMAKE_CONFIGURE_DEPENDS ${LF_SOURCES})
message(STATUS "Found LF sources: ${LF_SOURCES}")


# Build the generated C code.
include(src-gen/${LF_MAIN}/CMakeLists.txt)
add_subdirectory(${REACTOR_UC_PATH})
target_sources(app PRIVATE ${LFC_GEN_MAIN} ${LFC_GEN_SOURCES})
target_include_directories(app PRIVATE ${LFC_GEN_INCLUDE_DIRS})
target_link_libraries(app PUBLIC reactor-uc)

target_compile_definitions(reactor-uc PUBLIC LF_LOG_LEVEL_ALL=${LOG_LEVEL})
