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
# ev3.speaker.beep()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
us = UltrasonicSensor(Port.S4)
dis = 0

while True:
    left_motor.run(300)
    right_motor.run(300)
    dis = us.distance()
    print(dis)
    if dis < 100:
        left_motor.stop()
        right_motor.stop()
        ev3.light.on(Color.RED)
    else:
        ev3.light.off()
