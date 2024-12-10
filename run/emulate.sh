#!/bin/env bash
set -e

usage() {
  echo "Usage: $0 -m <main_file>"
  exit 1
}
# Parse arguments
while getopts ":m:" opt; do
  case ${opt} in
    m )
      LF_MAIN=$OPTARG
      ;;
    \? )
      echo "Invalid option: -$OPTARG" 1>&2
      usage
      ;;
    : )
      echo "Invalid option: -$OPTARG requires an argument" 1>&2
      usage
      ;;
  esac
done
shift $((OPTIND -1))

# Check if LF_MAIN is set
if [ -z "${LF_MAIN}" ]; then
  usage
fi

./run/build.sh -m $LF_MAIN -b qemu_cortex_m3

# Run picotool with the specified main file
EMULATE_COMMAND="west build -t run"
echo "Running command: ${EMULATE_COMMAND}"
${EMULATE_COMMAND}