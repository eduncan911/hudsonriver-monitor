# Hudson River Monitor

This is an educational project we are building to introduce the kids at a local school to electronics.

See detailed information: 

https://forum.allaboutcircuits.com/blog/school-study-hudson-river-the-river-that-flows-both-ways.1594/

# Layout

This repositor has a number of sub-projects.  Below is a list of the overall files.

- server/ - Golang code running on AWS lambda to process incoming requests.
- xbee/ - MicroPython code for the XBee3 Cellular Module.
- certs.* - Encrypted certs used to self-sign all TLS communications betwee xbee and server.
- Makefile - Used to build the entire or a portion of the sub-projects.

# Building

    make [server,xbee]

This will create a `build/` directory where all artifacts will be placed for deployment.

# TODO

- Add Travis CICD
- Git tag (per CICD)

# Licensing

This repo is published under the MIT license to be as open and transparent to use.