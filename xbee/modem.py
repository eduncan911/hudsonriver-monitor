# Copyright (c) 2019 Eric Duncan (eduncan911@gmail.com)
# The MIT License (MIT) - see https://eduncan911.mit-license.org
"""XBee modem communications"""

def send(xb, location, readings, timeout=30):
    """Reads all GPS input, parse, average, and return.
    xb: an already initialized xbee module.
    timeout: seconds before giving up"""
