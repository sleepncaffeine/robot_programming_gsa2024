#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase


ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# 좌측 모터, 우측 모터, 바퀴 반경, 바퀴 사이 거리
robot = DriveBase(left_motor, right_motor, 56, 114)

# DriveBase 사용 시 자동으로 거리 계산해 이동

# 500mm 전진
robot.straight(500)
robot.stop(Stop.BRAKE)
