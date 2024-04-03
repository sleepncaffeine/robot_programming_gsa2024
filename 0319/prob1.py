#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase


ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

while True:
    if Button.LEFT in ev3.buttons.pressed():
        left_motor.run_angle(500, 720, Stop.HOLD, False)
        right_motor.run_angle(500, 720, Stop.HOLD, True)

    if Button.CENTER in ev3.buttons.pressed():
        break
