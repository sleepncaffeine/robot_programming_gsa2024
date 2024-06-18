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
mlr = Motor(Port.C)
mud = Motor(Port.B)
mclaw = Motor(Port.D)
btn = TouchSensor(Port.S4)
ts = TouchSensor(Port.S3)

ev3.speaker.beep()

while not btn.pressed():
    mlr.run(100)
mlr.stop()
mlr.reset_angle(0)

while not ts.pressed():
    mud.run(-100)
mud.stop()
mud.reset_angle(0)


ev3.speaker.beep()


while True:
    lr = mlr.angle()
    ud = mud.angle()
    claw = mclaw.angle()
    print(lr, ud, claw)
