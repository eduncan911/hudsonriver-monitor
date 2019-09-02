# Hudson River Monitor

This is an educational project we are building to introduce the kids at a local school to electronics.

For overall project information, plesae refer to this blog post: 

https://forum.allaboutcircuits.com/blog/school-study-hudson-river-the-river-that-flows-both-ways.1594/

# Repository

This repositor has a number of sub-projects seperated by directories.

- diagrams/ - PoC schema, breadboard, and other supporting files
- xbee/ - MicroPython code for the XBee3 Cellular Module
- server/ - Golang code running on AWS lambda to process incoming requests
- bin/ - CICD bash scripts. Can be ignored.
- Makefile - Controls cicd testing, packaging, and deployments from local dev machine(s)

## Sensors and GPS

We will be connecting all sensors and GPS devices directly to the XBee module for parsing with MicroPython.  The advantage of MicroPython is that it allows us to process and format the data in real-time, while also minimizing the data being sent.

For the type of sensors and GPS, and how they be used, please refer to the diagrams below.

Schema

![XBee Schema](https://raw.githubusercontent.com/eduncan911/hudsonriver-monitor/master/diagrams/hudsonriver-schema.png)

Breadboard

![XBee Breadboard](https://raw.githubusercontent.com/eduncan911/hudsonriver-monitor/master/diagrams/hudsonriver-monitor-breadboard.png)

## Building

    make setup # tip: use python virtualdirs
    make test
    make build

`make build` will create a `build/` directory where all artifacts will be placed for deployment.

## TODO

- Add pipelines
- Git tag (per CICD)
- Is there an X

# Licensing

This repo is published under the MIT license to be as open and transparent to use.