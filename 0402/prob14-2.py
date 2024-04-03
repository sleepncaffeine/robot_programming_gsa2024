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


ev3 = EV3Brick()
ml = Motor(Port.B)
mr = Motor(Port.C)
cs = ColorSensor(Port.S3)
ts = TouchSensor(Port.S1)
wait(300)
ev3.speaker.beep()

on_black = False
black_cnt = 0

count = 0
white = 0
line = 0

speed = 50

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


while black_cnt < 3:
    color = cs.color()
    light_value = cs.reflection()

    if color == Color.BLACK:
        if not on_black:
            on_black = True
            black_cnt += 1
            print(black_cnt)
            ev3.speaker.beep()
    else:
        on_black = False

    if light_value > THRESHOLD:
        mr.dc(speed)
        ml.dc(0)
    elif light_value < THRESHOLD:
        mr.dc(0)
        ml.dc(speed)
