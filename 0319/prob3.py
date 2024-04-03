#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase


ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# A1 사이즈 크기를 기준으로 사각형으로 돌아 제자리로 돌아오기

short = 720
long = 980
turn = 424


right_motor.run_angle(500, 720, Stop.BRAKE, False)
left_motor.run_angle(500, 720, Stop.BRAKE)
wait(100)
right_motor.run_angle(500, 424, Stop.BRAKE)
wait(100)

right_motor.run_angle(500, 985, Stop.BRAKE, False)
left_motor.run_angle(500, 985, Stop.BRAKE)
wait(100)
right_motor.run_angle(500, 426, Stop.BRAKE)
wait(100)

right_motor.run_angle(500, 760, Stop.BRAKE, False)
left_motor.run_angle(500, 760, Stop.BRAKE)
wait(100)
right_motor.run_angle(500, 424, Stop.BRAKE)
wait(100)

right_motor.run_angle(500, 980, Stop.BRAKE, False)
left_motor.run_angle(500, 980, Stop.BRAKE)
wait(100)
right_motor.run_angle(500, 424, Stop.BRAKE)
wait(100)

robot.stop(Stop.BRAKE)
