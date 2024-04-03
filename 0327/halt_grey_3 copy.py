#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (
    Motor,
    TouchSensor,
    ColorSensor,
    InfraredSensor,
    UltrasonicSensor,
    GyroSensor,
)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font
import random

ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
ts = TouchSensor(Port.S1)
cs = ColorSensor(Port.S3)
wait(300)
ev3.speaker.beep()
cs.reflection()


count = 0
while count < 3:
    left_motor.run(200)
    right_motor.run(200)
    fixed = cs.reflection()
    if fixed <= 60 and fixed >= 40:
        count += 1
        while cs.reflection() <= 60 and cs.reflection() >= 40:
            fixed = 100
left_motor.stop()
right_motor.stop()
