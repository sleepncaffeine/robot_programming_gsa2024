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


ev3 = EV3Brick()

ev3.screen.clear()

x1 = 50
y1 = 50
x2 = x1 + 50
y2 = y1 + 50

ev3.screen.draw_box(x1, y1, x2, y2, r=0, fill=True, color=Color.BLACK)

while True:
    if Button.UP in ev3.buttons.pressed():
        y1 -= 5
        y2 -= 5
    elif Button.DOWN in ev3.buttons.pressed():
        y1 += 5
        y2 += 5
    elif Button.LEFT in ev3.buttons.pressed():
        x1 -= 5
        x2 -= 5
    elif Button.RIGHT in ev3.buttons.pressed():
        x1 += 5
        x2 += 5
    elif Button.CENTER in ev3.buttons.pressed():
        break

    ev3.screen.clear()
    ev3.screen.draw_box(x1, y1, x2, y2, r=0, fill=True, color=Color.BLACK)
    wait(100)
