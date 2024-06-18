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

THRESHOLD = 40


def turn_left():
    ml.stop()
    mr.stop()

    ml.run_time(-100, 1800, wait=False)
    mr.run_time(100, 1800, wait=True)


def turn_right():
    ml.stop()
    mr.stop()

    ml.run_time(100, 1800, wait=False)
    mr.run_time(-100, 1800, wait=True)


def u_turn():
    ml.stop()
    mr.stop()

    ml.run_time(-100, 3600, wait=False)
    mr.run_time(100, 3600, wait=True)


ml.run_time(100, 1000, wait=False)
mr.run_time(100, 1000, wait=True)

u_turn()
