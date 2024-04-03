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

import time

ev3 = EV3Brick()
ml = Motor(Port.B)
mr = Motor(Port.C)
hand = Motor(Port.A)
cs = ColorSensor(Port.S3)
ts = TouchSensor(Port.S1)
us = UltrasonicSensor(Port.S4)
csr = cs.reflection()
wait(500)
ev3.speaker.beep()
speed = 200

########################Calibration########################
count = 0
white = 0
line = 0

while True:
    if count == 1:
        white = cs.reflection()
    if count == 2:
        line = cs.reflection()
    if count == 3:
        break

    if ts.pressed():
        if not pressed:
            count += 1
            pressed = True
    else:
        pressed = False


THRESHOLD = (white + line) / 2
print(THRESHOLD)
########################Calibration########################

start = time.time()

while True:
    ml.run(300)
    mr.run(300)
    dist = us.distance()

    if dist <= 50:
        ml.stop()
        mr.stop()

        end = time.time()

        hand.run_target(100, -160)

        dt = time.time() + end - start

        while time.time() < dt:
            ml.run(-300)
            mr.run(-300)

        ml.stop()
        mr.stop()
        wait(100)
        # hand.run_target(100, 0)

        # wait(1000)

        break

while True:
    light_value = cs.reflection()
    if light_value > THRESHOLD:
        ml.run(speed)
        mr.run(0)
    elif light_value < THRESHOLD:
        ml.run(0)
        mr.run(speed)
