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

import random

gr = GyroSensor(Port.S2, direction=Direction.CLOCKWISE)
ml = Motor(Port.B)
mr = Motor(Port.C)
# gr.reset_angle(0)

while gr.angle() < 360:
    ml.run(200)
    print(gr.angle())
ml.hold()
