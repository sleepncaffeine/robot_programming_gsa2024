#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
import time

# Create your objects here.
ev3 = EV3Brick()

ml = Motor(Port.B)
mr = Motor(Port.C)

cll = ColorSensor(Port.S1)
crr = ColorSensor(Port.S3)
cl = ColorSensor(Port.S2)
cr = ColorSensor(Port.S4)

THRESHOLD = 30


def read_sensors():
    return [cll.reflection(), cl.reflection(), cr.reflection(), crr.reflection()]


while True:
    sensors = read_sensors()
    print(sensors)
    time.sleep(0.1)
