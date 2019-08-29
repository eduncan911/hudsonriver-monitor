"""
# Copyright (c) 2019 Eric Duncan (eduncan911@gmail.com)
# The MIT License (MIT) - see https://eduncan911.mit-license.org
"""
from machine import Pin
import time
import xbee
import gps
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
sleep_in_minutes = 30
gps_reads = 10

# TODO:
#   - possibly wake to a low-powered/airplane mode? then enable
#     the cellular modem when ready to send. this can save bat
#     time as the GPS can take some time to get a stable lock.
#

xb = xbee.XBee()

while True:
    with xb.wake_lock:
        readings - sensors.read()
        print("readings: " + readings)

        location = gps.read(gps_reads)
        print("location: " + location)

        modem.send(location, readings)
        print("send readings and locations")

    # all done. now sleep
    sleep_time = sleep_in_minutes * 60 * 1000
    print("sleeping for %u ms" % sleep_time)
    slept = x.sleep_now(sleep_time, False)
    print("slept for %u ms" % slept)
