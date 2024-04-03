#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor, TouchSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog


ev3 = EV3Brick()
ev3.screen.clear()

ts = TouchSensor(Port.S1)
count = 0
ev3.speaker.beep()

# while True:
#     if ts.pressed() == True:
#         count += 1
#         print(count)

pressed = False
while True:
    if ts.pressed():
        if not pressed:
            count += 1
            pressed = True
            print(count)
    else:
        pressed = False
