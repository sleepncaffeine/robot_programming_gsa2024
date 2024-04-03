#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.parameters import Button
from pybricks.tools import wait

# Initialize the EV3.
ev3 = EV3Brick()


ev3.speaker.beep(200, 100)
ev3.speaker.play_notes(["C4/4", "C4/4", "G4/4", "G4/4"], tempo=120)
ev3.speaker.say("")
