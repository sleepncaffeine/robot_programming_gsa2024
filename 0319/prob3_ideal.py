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

short = 297  # mm
long = 420  # mm
turn = 424
wheel_radii = 56
padding = 30

robot = DriveBase(left_motor, right_motor, wheel_radii, 114)

# 설정한 DriveBase 바퀴 크기와 차륜거리에 따라 이동
for _ in range(2):
    robot.straight(short + wheel_radii + padding)
    robot.turn(turn)
    robot.straight(long + wheel_radii + padding)
    robot.turn(turn)
    robot.straight(short + wheel_radii + padding)
    robot.turn(turn)
    robot.straight(long + wheel_radii + padding)
    robot.turn(turn)

robot.stop(Stop.BRAKE)
