#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait



ev3 = EV3Brick()


ev3.screen.clear()
ev3.screen.print("Welcome!")


while True:
    if Button.LEFT in ev3.buttons.pressed():
        ev3.
        ev3.light.on(Color.RED)
        ev3.speaker.beep()
        ev3.screen.clear()
        ev3.screen.print("LED: Red")

    elif Button.RIGHT in ev3.buttons.pressed():
        ev3.light.on(Color.GREEN)
        ev3.speaker.beep()
        ev3.screen.clear()
        ev3.screen.print("LED: Green")

    elif Button.UP in ev3.buttons.pressed():
        ev3.light.on(Color.ORANGE)
        ev3.speaker.beep()
        ev3.screen.clear()
        ev3.screen.print("LED: Orange")

    elif Button.DOWN in ev3.buttons.pressed():
        ev3.screen.clear()
        ev3.screen.print("Exiting...")
        wait(1000)
        break

    wait(200)
