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
c1 = ColorSensor(Port.S1)
c2 = ColorSensor(Port.S4)
c3 = ColorSensor(Port.S3)

cross = [False, False, False]
gray = [40, 40, 40]
gcnt = 0
cnt = 0
back = False


def go():
    ml.run(80)
    mr.run(200)
    if c1.reflection() < 40:
        ml.run(100)
        mr.run(100)
        wait(500)
        print(c1.reflection(), c2.reflection(), c3.reflection())
        if c3.reflection() < 40 and c2.reflection() < 40 and c1.reflection() < 40:
            ml.run_angle(1000, 360, Stop.BRAKE, False)
            mr.run_angle(1000, -360, Stop.BRAKE, True)
            ml.run(100)
            mr.run(100)
            wait(1000)
        else:
            ml.run(-100)
            mr.run(-100)
            wait(500)
            turnLeft()
    while c2.reflection() > gray[1]:
        ml.run(50)
        mr.run(-50)


def turnLeft():
    ml.run_angle(200, 140, Stop.BRAKE, False)
    mr.run_angle(200, 140, Stop.BRAKE, True)
    ml.run_angle(200, -180, Stop.BRAKE, False)
    mr.run_angle(200, 180, Stop.BRAKE, True)


while True:
    go()

    if c1.reflection() < 40:
        ml.run(100)
        mr.run(100)
        wait(500)
        print(c1.reflection(), c2.reflection(), c3.reflection())
        if c3.reflection() < 40 and c2.reflection() < 40 and c1.reflection() < 40:
            ml.run_angle(1000, 360, Stop.BRAKE, False)
            mr.run_angle(1000, -360, Stop.BRAKE, True)
            ml.run(100)
            mr.run(100)
            wait(1000)
        else:
            ml.run(-100)
            mr.run(-100)
            wait(500)
            turnLeft()
