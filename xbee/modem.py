"""XBee modem communications"""

def send(xb, location, readings, timeout=30):
    """Reads all GPS input, parse, average, and return.
    xb: an already initialized xbee module.
    timeout: seconds before giving up"""
