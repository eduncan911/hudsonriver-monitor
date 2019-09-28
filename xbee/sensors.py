"""Handles all sensor inputs for the XBee module."""

import machine
import sht31

# setup I2C for SHT31
i2c = machine.I2C(id=1, freq=400000)
sht31sensor = sht31.SHT31(i2c)

def fahrenheit(celsius):
    """Converts celsius to fahrenheit"""
    return (celsius * (9/5)) + 32

def tempSHT31():
    """Read temp and humidity from SHT31"""

    return sht31sensor.get_temp_humi()

def read(xb, timeout=15):
    """Reads all sensor inputs from the XBee module.
    xb: an already initialized xbee module.
    timeout: the time to wait for all sensor inputs."""

    readings = {}

    temp, humidity = tempSHT31()
    readings['temp'] = temp
    readings['humidity'] = humidity

    # TODO: add other sensors (light, pH, salt, water-temp, etc)

    return readings
