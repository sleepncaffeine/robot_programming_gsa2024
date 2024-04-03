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

cs = ColorSensor(Port.S3)
ev3.speaker.beep()
print(cs.color())
wait(300)

while True:
    ncol = cs.color()
    ev3.screen.print(ncol)

    if ncol == Color.BLACK:
        ev3.light.off()
        ev3.speaker.play_file(SoundFile.BLACK)
        wait(500)
    elif ncol == Color.BLUE:
        ev3.light.off()
        ev3.speaker.play_file(SoundFile.BLUE)
        wait(500)
    elif ncol == Color.GREEN:
        ev3.light.on(Color.GREEN)
        ev3.speaker.play_file(SoundFile.GREEN)
        wait(500)
    elif ncol == Color.YELLOW:
        ev3.light.off()
        ev3.speaker.play_file(SoundFile.YELLOW)
        wait(500)
    elif ncol == Color.RED:
        ev3.light.on(Color.RED)
        ev3.speaker.play_file(SoundFile.RED)
        wait(500)
    elif ncol == Color.WHITE:
        ev3.light.off()
        ev3.speaker.play_file(SoundFile.WHITE)
        wait(500)
    else:
        ev3.light.off()
