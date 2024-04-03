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

import random

ev3 = EV3Brick()

# 좌, 우 모터 및 초음파 센서 초기화
mtr_l = Motor(Port.B)
mtr_r = Motor(Port.C)
us = UltrasonicSensor(Port.S4)

# DriveBase 객체 이용해 로봇 초기화
robot = DriveBase(mtr_l, mtr_r, 56, 114)

while True:
    # 거리 측정
    dist = us.distance()

    # 20cm 이내면
    if dist < 200:
        # 비프음
        ev3.speaker.beep()
        # 랜덤한 각도 생성
        x = random.randint(90, 180)
        # 생성된 각도만큼 우회전
        robot.turn(x)
    else:
        # 전진
        robot.drive(100, 0)
