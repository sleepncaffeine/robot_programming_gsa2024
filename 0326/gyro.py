#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor, TouchSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog


import random

gr = GyroSensor(Port.S2, direction=Direction.CLOCKWISE)
ml = Motor(Port.B)
mr = Motor(Port.C)
gr.reset_angle(0)

while gr.angle() <= 360:
    ml.run(50)
    mr.run(-50)
    print(gr.angle())
ml.hold()
mr.hold()
