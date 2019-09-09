"""Main program entry"""

import machine
import time
import xbee
import gps
import modem
import sensors

# Theory of Operation - We will go into a loop and will read
# various devices and sensors using micro python to process
# and interrupt the data into a summary result.
#
# Finally, the summary result will be sent over the modem and
# some type of acknowledgement received.
#
# All persisted state will be handled by the remote server,
# including any location comparisons.  These are out of scope
# for this device.
#

# configuration
sleep_in_minutes = 1
gps_reads = 10

# TODO:
#   - possibly wake to a low-powered/airplane mode? then enable
#     the cellular modem when ready to send. this can save bat
#     time as the GPS can take some time to get a stable lock.
#

# to keep things on the heap, we'll define vars globally
xb = xbee.XBee()
readings = ("n/a", "n/a", "n/a")
location = ("lat", "long", "alt")

while True:
    with xb.wake_lock:
        readings = sensors.read(xb)
        print("readings: " + readings)

        location = gps.read(xb, gps_reads)
        print("location: " + location)

        modem.send(xb, location, readings)
        print("sent readings and locations")

    # all done. now sleep
    print("sleeping for %u minutes" % sleep_in_minutes)
    slept = xb.sleep_now(sleep_in_minutes * 60 * 1000, False)
    print("WAKE UP: slept for %u ms" % slept)
