#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from pybricks.parameters import Color

ev3 = EV3Brick()

ev3.light.on(Color.RED)
wait(1000)
ev3.light.off()
