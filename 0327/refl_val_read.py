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
refl = [-1] * 2
pressed = False

while cnt < 2:
    if ts.pressed():
        if not pressed:
            pressed = True
            refl[cnt] = cs.reflection()
            cnt += 1
    else:
        pressed = False

thres = (refl[0] + refl[1]) / 2

print("바닥: ", refl[0])
print("라인: ", refl[1])
print("경계: ", thres)

# white - 95~100
# grey - 75~77
# black - 6~10
