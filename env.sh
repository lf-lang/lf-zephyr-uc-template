# Oneliner from: https://stackoverflow.com/questions/59895/how-do-i-get-the-directory-where-a-bash-script-is-located-from-within-the-script
here=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

# Source zephyr environment
source $here/deps/zephyr/zephyr-env.sh

# Source reactor-uc environment
source $here/deps/reactor-uc/env.bash
