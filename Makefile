SHELL = /bin/bash

# TODO: convert to bash scripts to clean up
# TODO: add to CICD server

build-all: clean
	echo "Building microPython modules to build/ ..." \
	&& pushd xbee \
	&& python -m mpy_cross main.py micropyGPS.py sensors.py gps.py \
	&& mkdir -p build \
	&& mv *.mpy build/ \
	&& popd
	echo "Build golang lambda function to build/ ..." \
	&& pushd server \
	&& GOOS=linux GOARCH=amd64 go build -o ../build/hudsonriver-monitor \
	&& popd

clean:
	rm -rf build/

