# reactor-uc zephyr-west template

![Zephyr Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Zephyr_RTOS_logo_2015.svg/640px-Zephyr_RTOS_logo_2015.svg.png)

- **Git:** <https://github.com/zephyrproject-rtos/zephyr/>
- **Supported Boards:** <https://docs.zephyrproject.org/latest/boards/index.html>
- **Documentation:** <https://docs.zephyrproject.org/latest/>

______

This is a west-centric project template for Lingua Franca applications targeting the Zephyr RTOS using the micro-c (uc) target of Lingua Franca.

## 1. Prerequisites

### 1.1. Basic

You must use one of the following operating systems:

- `Linux` Officially supported are Debian & Ubuntu
- `macOS`

Your system must have the following software packages (you likely have at least some of these already):

- `git` — [a distributed version control system](https://git-scm.com/)
- `java` — [Java 17](https://openjdk.org/projects/jdk/17)

### 1.2. Micro C Target for Lingua Franca

This template uses [reactor-uc](https://github.com/lf-lang/reactor-uc), the "micro C" target for Lingua Franca. Clone this repo with one of the following commands:

#### Clone via HTTPS

```bash
git clone https://github.com/lf-lang/reactor-uc.git --recurse-submodules
```

#### Or Clone via SSH

```bash
git clone git@github.com:lf-lang/reactor-uc.git --recurse-submodules
```

And make sure that the `REACTOR_UC_PATH` environment variable is pointing to it.

### Getting started

Press `Use template` in the upper right corner and choose `Create a new repository`. Then clone this new repository to your machine.
To start developing in your new repo, you must first install the Zephyr dependencies, toolchains and SDK.
This requires you to follow selected parts of the Zephyr official Getting Started guide.

1. Install the dependencies used by Zephyr by following the steps in [Install Dependencies](https://docs.zephyrproject.org/3.7.0/develop/getting_started/index.html#install-dependencies)

2. Then install the Zephyr toolchains and SDK by following the steps in [Install the Zephyr SDK](https://docs.zephyrproject.org/3.7.0/develop/getting_started/index.html#install-the-zephyr-sdk)

Within your newly cloned project, create and activate a virtual environment for this project.

```sh
python3 -m venv ./venv
source ./venv/bin/activate
```

**IMPORTANT**: Remember to always activate the virtual environment before using the template.

Install the west, the Zephyr build tool

```sh
pip install west
```

Pull down the Zephyr RTOS sources using west (this can take a while)

```sh
west update
```

Install Python dependencies

```sh
pip install -r deps/zephyr/scripts/requirements.txt
```

Export a CMake package

```sh
west zephyr-export
```

## HelloWorld

To build and emulate the provided [HelloWorld.lf](./src/HelloWorld.lf) using the `native_posix` target, do:

```sh
west build -t run
```

## Changing the target board

To build for a different board, e.g. the `qemu_cortex_m3` emulation. Either change the `BOARD` variable in [CMakeLists.txt](./CMakeLists.txt), or using `west`:

```sh
west build -b qemu_cortex_m3 -p always -t run
```

Note the `-p always` which is a `west` option for cleaning the build directory. This must be used when changing the target board. Alternatively `west clean` can be run in between.

## Changing the LF application

The `LF_MAIN` CMake variable decides which LF application to build. This can either be modified in [CMakeLists.txt](/CMakeLists.txt) or from the command line. To build [Blinky.lf](/src/Blinky.lf) for Adafruit Feather do:

```sh
west build -b adafruit_feather -p always -- -DLF_MAIN=Blinky
```

With `west`, CMake arguments are separated from `west` arguments with a `--`.

## Log level

The log level of the LF app can be changed by setting the variable `LOG_LEVEL` in [CMakeLists.txt](./CMakeLists.txt) or by modifying it on the command line:

```sh
west build -t run -p always -- -DLOG_LEVEL=LF_LOG_LEVEL_DEBUG
```

## Cleaning all build artifacts

By passing `-p always` to `west`, the `build` folder is cleaned and the project is reconfigured by CMake. However, this does not clean the files generated by `lfc`. For this we provide a custom west command `west clean` defined in [clean.py](./scripts/clean.py) which also cleans the files generated by LFC. Use it to do a complete reset.

```sh
west clean
```

## Flashing to a board

To flash an application onto a board, simply use `west flash`. This may require the installation of additional, vendor-specific tools. See the [official docs](https://docs.zephyrproject.org/3.7.0/develop/west/build-flash-debug.html#west-flashing) for more information.

## West-centric development

This template integrates the Lingua Franca compiler `lfc` into a `west`-based project. This requires that the user understands how to use `west` and zephyr. Please refer to the [official docs](https://docs.zephyrproject.org/3.7.0/index.html) for more information.

## Troubleshooting

```sh
Command 'west' not found, did you mean:
```

or

```sh
Traceback (most recent call last):
  File "/home/erling/dev/lf-west-template/deps/zephyr/scripts/build/gen_kobject_list.py", line 62, in <module>
    import elftools
ModuleNotFoundError: No module named 'elftools'
```

Activate the virtual environment where the Zephyr dependencies are installed.
