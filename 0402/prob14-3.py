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
from threading import Thread


def color_result():
    global csr
    while not stop_flag:
        csr = cs.reflection()


def line_go():
    while not stop_flag:
        if csr > G_THRESHOLD and csr < B_THRESHOLD:
            ml.run(200)
            mr.run(100)
        else:
            ml.run(100)
            mr.run(200)


count = 0
white = 0
grey = 0
black = 0

speed = 50

ev3 = EV3Brick()
ml = Motor(Port.B)
mr = Motor(Port.C)
cs = ColorSensor(Port.S3)
ts = TouchSensor(Port.S1)
csr = cs.reflection()
wait(500)
ev3.speaker.beep()

pressed = False

while True:
    if count == 1:
        white = cs.reflection()
    if count == 2:
        grey = cs.reflection()
    if count == 3:
        black = cs.reflection()
    if count == 4:
        break

    if ts.pressed():
        if not pressed:
            count += 1
            pressed = True
    else:
        pressed = False


stop_flag = False

G_THRESHOLD = (grey + white) / 2
B_THRESHOLD = (black + white) / 2
BG_THRESHOLD = (black + grey) / 2

t1 = Thread(target=color_result)
t1.start()
t2 = Thread(target=line_go)
t2.start()

on_black = False
black_cnt = 0

while True:
    print(csr)

    if csr > BG_THRESHOLD:
        if not on_black:
            on_black = True
            black_cnt += 1
            ev3.speaker.beep()
    else:
        on_black = False

    if black_cnt > 3:
        stop_flag = True
        ml.stop()
        mr.stop()
        break
