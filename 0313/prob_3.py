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

pressed = set()
end = False

ev3.speaker.set_volume(10)


while end == False:
    for btn in ev3.buttons.pressed():
        if btn not in pressed:
            pressed.add(btn)
            ev3.light.on(Color.GREEN)
            wait(100)
            ev3.speaker.beep()
            wait(100)
            ev3.speaker.beep()
            ev3.light.off()
        else:
            ev3.light.on(Color.RED)
            ev3.speaker.beep(1000, 2000)
            end = True
