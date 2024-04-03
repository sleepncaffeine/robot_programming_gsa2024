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

while True:
    if Button.UP in ev3.buttons.pressed():
        ev3.light.on(Color.GREEN)
        ev3.screen.load_image(ImageFile.FORWARD)
        ev3.speaker.say("앞으로")

    elif Button.RIGHT in ev3.buttons.pressed():
        ev3.light.on(Color.ORANGE)
        ev3.screen.load_image(ImageFile.RIGHT)
        ev3.speaker.say("오른쪽")

    elif Button.LEFT in ev3.buttons.pressed():
        ev3.light.on(Color.RED)
        ev3.screen.load_image(ImageFile.LEFT)
        ev3.speaker.say("왼쪽")

    elif Button.DOWN in ev3.buttons.pressed():
        ev3.light.off()
        ev3.screen.load_image(ImageFile.BACKWARD)
        ev3.speaker.say("뒤로")

    elif Button.CENTER in ev3.buttons.pressed():
        ev3.speaker.say("종료합니다")
        break
