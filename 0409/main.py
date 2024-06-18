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

ev3 = EV3Brick()
ev3.speaker.beep()

ml = Motor(Port.B)
mr = Motor(Port.C)
hand = Motor(Port.A)

ts = TouchSensor(Port.S1)
us = UltrasonicSensor(Port.S4)
gs = GyroSensor(Port.S2, direction=Direction.COUNTERCLOCKWISE)
cs = ColorSensor(Port.S3)


def line_go():
    global color
    while not stop_flag:
        if color == Color.WHITE:
            ml.run(200)
            mr.run(100)
        else:
            ml.run(100)
            mr.run(200)


while ts.pressed() == 0:
    {}
while ts.pressed() == 1:
    {}

stop_flag = False
color = cs.color()

t = threading.Thread(target=line_go)
t.start()

gs.reset_angle(0)

red_cnt = 0
on_red = False

####################################

while True:
    color = cs.color()
    if color == Color.RED:
        if not on_red:
            on_red = True
            red_cnt += 1
    else:
        on_red = False

    if red_cnt == 2:
        stop_flag = True
        break

ev3.speaker.beep(784)

#######################################

ml.run_time(300, 100, wait=False)
mr.run_time(-300, 100, wait=True)

ml.run_time(-300, 900, wait=False)
mr.run_time(300, 900, wait=True)

ev3.speaker.beep(784)

######################################

start = time.time()
DT = 0

while True:
    ml.run(200)
    mr.run(200)
    dist = us.distance()

    if dist <= 50:
        ml.stop()
        mr.stop()
        end = time.time()

        hand.run_target(100, -160)

        ev3.speaker.beep(840)

        DT = end - start
        dt = DT + time.time()

        while time.time() < dt:
            ml.run(-200)
            mr.run(-200)

        break

while gs.angle() >= 120:
    ml.run(100)
    mr.run(-100)

ev3.speaker.beep(784)

#################################3

stop_flag = False
red_cnt = 0
t = threading.Thread(target=line_go)
t.start()

while True:
    color = cs.color()
    if color == Color.RED:
        if not on_red:
            on_red = True
            red_cnt += 1
    else:
        on_red = False

    if red_cnt == 4:
        stop_flag = True
        break

ev3.speaker.beep(784)

#######################################

ml.run_time(300, 100, wait=False)
mr.run_time(-300, 100, wait=True)

ml.run_time(-300, 900, wait=False)
mr.run_time(300, 900, wait=True)

ev3.speaker.beep(784)

######################################

start = time.time()

ml.run_time(200, 1000 * DT, wait=False)
mr.run_time(200, 1000 * DT, wait=True)

hand.run_target(100, 0)

ml.run_time(-200, 1000 * DT, wait=False)
mr.run_time(-200, 1000 * DT, wait=True)


ml.run_time(300, 900, wait=False)
mr.run_time(-300, 900, wait=True)

ev3.speaker.beep(784)

#######################################

stop_flag = False
red_cnt = 0
t = threading.Thread(target=line_go)
t.start()

while True:
    color = cs.color()
    if color == Color.RED:
        if not on_red:
            on_red = True
            red_cnt += 1
    else:
        on_red = False

    if red_cnt == 3:
        stop_flag = True
        break

ev3.speaker.beep(1046)
