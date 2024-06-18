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
from pybricks.messaging import BluetoothMailboxServer, TextMailbox


ev3 = EV3Brick()
mlr = Motor(Port.D)
push = TouchSensor(Port.S1)
fwd = TouchSensor(Port.S3)
bwd = TouchSensor(Port.S4)
THRESHOLD = 10

x = ["LEFT", "RIGHT", "CENTER"]
y = ["BACKWARD", "FORWARD", "CENTER"]

lr = 2
bf = 2
btn = 0


ev3.speaker.beep()
mlr.reset_angle(0)

while True:
    # read motor value and print
    s = int(mlr.angle())
    if s < -THRESHOLD:
        lr = 0
    elif s > THRESHOLD:
        lr = 1
    else:
        lr = 2
    if fwd.pressed():
        bf = 1
    elif bwd.pressed():
        bf = 0
    else:
        bf = 2
    print(x[lr], y[bf], push.pressed())
