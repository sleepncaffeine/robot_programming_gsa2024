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
ml = Motor(Port.B)
mr = Motor(Port.C)

ev3.speaker.beep()
server = BluetoothMailboxServer()
mbox = TextMailbox("greeting", server)

# The server must be started before the client!
print("waiting for connection...")
server.wait_for_connection()
print("connected!")
mbox.wait()
ev3.screen.print(mbox.read())
mbox.send("HI!")

while True:
    s = str(ml.angle()) + " " + str(mr.angle())
    print(s)
    mbox.send(s)
    print("sent")
    mbox.wait()
    print(mbox.read())
    wait(100)
