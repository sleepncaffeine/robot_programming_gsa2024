#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
import time

# Create your objects here.
ev3 = EV3Brick()

ml = Motor(Port.B)
mr = Motor(Port.C)

cll = ColorSensor(Port.S1)
crr = ColorSensor(Port.S3)
cl = ColorSensor(Port.S2)
cr = ColorSensor(Port.S4)

THRESHOLD = 40
# WHITE =


def read_sensors():
    return [cll.reflection(), cl.reflection(), cr.reflection(), crr.reflection()]


def move_forward():
    ml.run(100)
    mr.run(100)


def turn_left():
    ml.run(-100)
    mr.run(100)


def turn_right():
    ml.run(100)
    mr.run(-100)


def stop_motors():
    ml.stop()
    mr.stop()


while True:
    refl = read_sensors()
    print(refl)
    time.sleep(0.1)

    if refl[0] > THRESHOLD and refl[3] > THRESHOLD:  # normal turn case
        if refl[1] < THRESHOLD and refl[2] < THRESHOLD:  # straight line
            move_forward()
        if refl[1] > THRESHOLD and refl[2] < THRESHOLD:  # normal right
            ml.run(150)
            mr.run(80)
        elif refl[2] > THRESHOLD and refl[1] < THRESHOLD:  # normal left
            ml.run(80)
            mr.run(150)

    # Detecting junctions
    elif (
        refl[0] < THRESHOLD
        and refl[3] < THRESHOLD
        and (refl[1] < THRESHOLD or refl[2] < THRESHOLD)
    ):
        ev3.speaker.beep(659)
        print("Junction detected, turning left")
        stop_motors()
        time.sleep(0.1)
        turn_left()
        time.sleep(0.5)
        refl = read_sensors()
        while refl[1] > THRESHOLD and refl[2] > THRESHOLD:
            turn_left()
            refl = read_sensors()
        stop_motors()

    # 90 deg turn cases
    elif refl[0] < THRESHOLD and refl[1] < THRESHOLD:  # 90deg left
        print("90deg left")
        ev3.speaker.beep(523)
        while not (refl[0] > THRESHOLD and refl[3] > THRESHOLD and refl[2] > THRESHOLD):
            turn_left()
            refl = read_sensors()
    elif refl[3] < THRESHOLD and refl[2] < THRESHOLD:  # 90deg right
        print("90deg right")
        ev3.speaker.beep(783)
        while not (refl[0] > THRESHOLD and refl[3] > THRESHOLD and refl[1] > THRESHOLD):
            turn_right()
            refl = read_sensors()
