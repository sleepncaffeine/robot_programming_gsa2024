#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.parameters import Button

ev3 = EV3Brick()

while True:
    buttons = ev3.buttons.pressed()
    if Button.CENTER in buttons:
        ev3.speaker.say("center")
    elif Button.UP in buttons:
        ev3.speaker.say("up")
    elif Button.DOWN in buttons:
        ev3.speaker.say("down")
