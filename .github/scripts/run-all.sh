#!/usr/bin/env bash
set -e

run_with_timeout() {
    local duration=$1
    shift
    local command="$@"

    # Run the command but disable exit on error (because timeout will cause an error)
    set +e
    timeout "$duration" $command

    # Get the exit status of the command and then re-enable exit on error (after forcing a true return value)
    exit_status=$?
    true
    set -e

    # Check the exit status of the timeout command
    if [ $exit_status -eq 124 ]; then
        echo "Command timed out (success)."
        return 0
    elif [ $exit_status -eq 0 ]; then
        echo "Command completed successfully within $duration."
        return 0
    else
        echo "Command failed."
        return 1
    fi
}

build_test() {
    local program=$1
    local board=$2
    west build -p always -b $board -- -DLF_MAIN=$program
}

run_test_native() {
    local program=$1
    build_test $program native_posix
    run_with_timeout 10s west build -t run -- -DLF_MAIN=$program
}


run_test_native HelloWorld
build_test Blinky adafruit_feather
