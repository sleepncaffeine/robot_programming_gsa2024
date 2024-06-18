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
from pybricks.messaging import BluetoothMailboxClient, TextMailbox


ev3 = EV3Brick()
ml = Motor(Port.B)
mr = Motor(Port.C)

ev3.speaker.beep()
# This is the name of the remote EV3 or PC we are connecting to.
SERVER = "parkjj"  # 서버 이름

client = BluetoothMailboxClient()
mbox = TextMailbox("greeting", client)

print("establishing connection...")
client.connect(SERVER)
print("connected!")
ev3.speaker.beep()


while True:
    mbox.wait()
    if mobox.read():
        a = mbox.read().split()
    print(a)
    ml.run_target(100, int(a[0]), Stop.COAST, False)
    mr.run_target(100, int(a[1]), Stop.COAST, True)
    mbox.send(".")
