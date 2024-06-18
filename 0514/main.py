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
import threading
import time


# Create your objects here.
ev3 = EV3Brick()

ml = Motor(Port.B)
mr = Motor(Port.C)

cll = ColorSensor(Port.S1)
crr = ColorSensor(Port.S3)
cl = ColorSensor(Port.S2)
cr = ColorSensor(Port.S4)

refl = [0, 0, 0, 0]
THRESHOLD = 40


while True:
    # refl[0] = cll.reflection()
    # refl[1] = cl.reflection()
    # refl[2] = cr.reflection()
    # refl[3] = crr.reflection()
    refl = [cll.reflection(), cl.reflection(), cr.reflection(), crr.reflection()]
    time.sleep(0.1)

    if all(x > THRESHOLD for x in refl):  # straight line
        ml.run(100)
        mr.run(100)
    if refl[0] > THRESHOLD and refl[3] > THRESHOLD:  # normal turn case
        if refl[1] < THRESHOLD:  # normal right
            ml.run(80)
            mr.run(150)
        elif refl[2] < THRESHOLD:  # normal left
            ml.run(150)
            mr.run(80)

    # T-junction or +-juction case
    elif all(x < THRESHOLD for x in refl):
        print("T-junction or +-junction")
        # consider as 90deg left
        # while not (refl[0] > THRESHOLD and refl[3] > THRESHOLD):
        #     ml.run(80)
        #     mr.run(150)
        #     refl[0] = cll.reflection()
        #     refl[1] = cl.reflection()
        #     refl[2] = cr.reflection()
        #     refl[3] = crr.reflection()

    # 90 deg turn case
    elif refl[0] < THRESHOLD and refl[1] < THRESHOLD:  # 90deg left
        print("90deg left")
        while not (refl[0] > THRESHOLD and refl[3] > THRESHOLD and refl[2] > THRESHOLD):
            ml.run(-100)
            mr.run(100)
            refl = [
                cll.reflection(),
                cl.reflection(),
                cr.reflection(),
                crr.reflection(),
            ]

    elif refl[3] < THRESHOLD and refl[2] < THRESHOLD:  # 90deg right
        print("90deg right")
        while not (refl[0] > THRESHOLD and refl[3] > THRESHOLD and refl[1] > THRESHOLD):
            ml.run(100)
            mr.run(-100)
            refl = [
                cll.reflection(),
                cl.reflection(),
                cr.reflection(),
                crr.reflection(),
            ]
