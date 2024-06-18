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


client = BluetoothMailboxClient()
SERVER = "parkjj"
mbox = TextMailbox("joystick", client)

print("establishing connection...")
client.connect(SERVER)
print("connected!")
ev3.speaker.beep()

while True:
    s = mbox.read()
    if s:
        print(s)
        x, y, pressed = s.split()
        if x == "LEFT":
            if mlr.angle() > -580:
                mlr.run(-300)
        elif x == "RIGHT":
            if not btn.pressed():
                mlr.run(300)
        else:
            mlr.stop()

        if y == "BACKWARD":
            if not ts.pressed():
                mud.run(100)
        elif y == "FORWARD":
            if mud.angle() < 380:
                mud.run(-100)
        else:
            mud.stop()

        if pressed == "True":
            if mclaw.angle() < 70:
                mclaw.run(300)
            else:
                mclaw.stop()
        else:
            mclaw.run_target(300, 0)
        wait(100)
    else:
        wait(100)
        print("no message")
