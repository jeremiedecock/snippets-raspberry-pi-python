#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This demo is inspired by
# http://www.oppedijk.com/robotics/control-dynamixel-with-raspberrypi
#
# The values are hardcoded to move Dynamixel #1:
# - "FF FF": packet header
# - "01": dynamixel ID to move
# - "05": "execute an action"
# - "03": number of bytes of data
# - "1E": "move" command
# - "32 03" or "CD 00": position to reach
# - "A3" or "0B": checksum
#
# A small sleep is required after writing (0.1) and a longer sleep is required
# after switching port 18 (HIGH/LOW).

import serial
import time
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.OUT)

port = serial.Serial("/dev/ttyAMA0", baudrate=57600, timeout=3.0)

while True:
    gpio.output(18, gpio.HIGH)
    port.write(bytearray.fromhex("FF FF 01 05 03 1E 32 03 A3"))
    time.sleep(0.1)
    gpio.output(18, gpio.LOW)
    time.sleep(3)

    gpio.output(18, gpio.HIGH)
    port.write(bytearray.fromhex("FF FF 01 05 03 1E CD 00 0B"))
    time.sleep(0.1)
    gpio.output(18, gpio.LOW)
    time.sleep(3)

