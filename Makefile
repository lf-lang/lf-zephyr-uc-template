SRCS = $(wildcard src/*.lf)
ELFS = $(patsubst src/%.lf, build/%.elf, $(SRCS))

build/%.elf: src/%.lf
	./run/build.sh -m $^ -b adafruit_feather

.PHONY: test
test: ${ELFS}

.PHONY: clean
clean:
	rm -rf src-gen/
	rm -rf bin/
	rm -rf include/
	rm -rf build/
	rm -rf target/