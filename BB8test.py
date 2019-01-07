#!/usr/bin/python
from bluepy import btle
import struct
import time
import BB8_driver
import sys
import logging

logging.basicConfig(filename="BB8_log.log", level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug("===Log started===")

print "connecting"
bb8 = BB8_driver.Sphero()
bb8.connect()
print "connected"

bb8.start()
time.sleep(2)

#telemetry request
bb8.bt.cmd(0x02, 0x11, [0, 80, 0, 1, 0x80, 0, 0, 0,   0]) #IMU Pitch and Yaw

time.sleep(2)
for i in range(5):
	bb8.set_rgb_led(255,0,0,0,True)
	print "red"
	time.sleep(2)
	bb8.set_rgb_led(0,255,0,0,True)
	print "green"
	time.sleep(2)
	bb8.set_rgb_led(0,0,255,0,True)
	print "blue"
	time.sleep(2)

bb8.join()
bb8.disconnect()
print "disconnected"
logging.debug("===End of Script===")
sys.exit(1)
