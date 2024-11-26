# Lingua Franca West Template
This is a west-centric project template for Lingua Franca applications targeting the Zephyr RTOS.

## Requirements
- docker

## Getting started
1. Open the template with a prebuilt docker container with the Zephyr toolchain

```shell
docker run -ti -v $(PWD)/lf-west-template/:/workdir 
```

2. Pull down the Zephyr RTOS sources into `deps/zephyr`. This will take several minutes

```shell
west update
west zephyr-export
```

3. Setup the environment

```shell
source env.sh
```

## Try an example app
```
cd HelloWorld
west lfc --build
west build -t run
```


## Next steps
It is recommended to install 