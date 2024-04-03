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

pressed = False
white = 0
black = 0
count = 0

while True:
    if count == 1:
        white = cs.reflection()
    if count == 2:
        black = cs.reflection()
    if count == 3:
        break

    if ts.pressed():
        if not pressed:
            count += 1
            pressed = True
    else:
        pressed = False


THRESHOLD = (white + black) / 2
print(THRESHOLD)

speed = 50

while True:
    light_value = cs.reflection()
    if light_value > THRESHOLD:
        ml.dc(speed)
        mr.dc(0)
    elif light_value < THRESHOLD:
        ml.dc(0)
        mr.dc(speed)
