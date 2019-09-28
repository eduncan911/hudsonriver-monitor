SHELL = /bin/bash

# TODO: convert to bash scripts to clean up
# TODO: add to CICD server

MPY_CROSS_DIR = ./xbee

build-all: clean
	@echo "Building microPython modules to build/ ..." \
	&& pushd xbee > /dev/null \
	&& for f in ./*.py; do python -m mpy_cross $${f}; done \
	&& popd > /dev/null \
	&& mkdir -p ./build \
	&& mv xbee/*.mpy ./build/ \
	&& echo "Build golang lambda function to build/ ..." \

clean:
	@rm -rf build/ \
	&& rm -rf xbee/*.mpy

