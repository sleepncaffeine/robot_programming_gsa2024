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
from pybricks.media.ev3dev import SoundFile, ImageFile


ev3 = EV3Brick()
ml = Motor(Port.B)
mr = Motor(Port.C)
ts = TouchSensor(Port.S1)
cs = ColorSensor(Port.S3)

cnt = 0
on_black = False

while cnt < 3:
    if cs.reflection() < 11:
        if not on_black:
            on_black = True
            cnt += 1
    else:
        on_black = False

    ml.run(200)
    mr.run(200)

ml.brake()
mr.brake()

# white - 95~100
# grey - 75~77
# black - 6~10
