# Copyright (c) 2019 Eric Duncan (eduncan911@gmail.com)
# The MIT License (MIT) - see https://eduncan911.mit-license.org
"""Handles all GPS input, parsing, and results"""

from micropyGPS import MicropyGPS

def read(xb, gps_reads=10, timeout=10):
    """Reads all GPS input, parse, average, and return.
    xb: an already initialized xbee module for UART reads.
    gps_reads: number of inputs to average.
    timeout: seconds before giving up"""

    return ("lat", "long", "alt")
