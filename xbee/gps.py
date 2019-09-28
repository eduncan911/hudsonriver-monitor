"""Handles all GPS input, parsing, and results"""

from micropyGPS import MicropyGPS

def read(xb, gps_reads=10, timeout=10):
    """Reads all GPS input, parse, average, and return.
    xb: an already initialized xbee module for UART reads.
    gps_reads: number of inputs to average.
    timeout: seconds before giving up"""

    return {}