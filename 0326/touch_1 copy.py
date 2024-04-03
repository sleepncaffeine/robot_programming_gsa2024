#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor, TouchSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog


ev3 = EV3Brick()
ev3.screen.clear()

ts = TouchSensor(Port.S1)
ml = Motor(Port.B)
mr = Motor(Port.C)
count = 0
ev3.speaker.beep()

pressed = False
while True:
    if not count % 2:
        ml.stop()
        mr.stop()
    elif count % 4 == 1:
        ml.run(100)
        mr.run(100)
    elif count % 4 == 3:
        ml.run(-100)
        mr.run(-100)

    if ts.pressed():
        if not pressed:
            count += 1
            pressed = True
            # print(count)
    else:
        pressed = False
