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

import time

ev3 = EV3Brick()

# 좌, 우 모터, 팔 및 초음파 센서 초기화
mtr_l = Motor(Port.B)
mtr_r = Motor(Port.C)
hand = Motor(Port.A)
us = UltrasonicSensor(Port.S4)

# 시작 시간 기록
start = time.time()

# 팔은 올린 상태로 시작

while True:
    # 전진 및 매 반복마다 거리 측정
    mtr_l.run(300)
    mtr_r.run(300)
    dist = us.distance()

    # 5cm 이내로 들어오면
    if dist <= 50:
        # 멈춤 및 시간 기록
        mtr_l.stop()
        mtr_r.stop()
        end = time.time()

        # 팔을 내림(약 130도)
        hand.run_target(100, -130)

        # 걸린 시간 계산
        # 현재 시간 이용한 계산이기 때문에 팔을 내린 후 계산
        dt = time.time() + end - start

        # 전진한 시간 만큼 후진
        while time.time() < dt:
            mtr_l.run(-300)
            mtr_r.run(-300)

        # 멈추고 팔을 올림
        mtr_l.stop()
        mtr_r.stop()
        wait(100)
        hand.run_target(100, 0)

        wait(1000)

        break
