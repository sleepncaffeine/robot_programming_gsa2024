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
ml = Motor(Port.B)
mr = Motor(Port.C)
c1 = ColorSensor(Port.S1)
c2 = ColorSensor(Port.S2)
c3 = ColorSensor(Port.S4)
c4 = ColorSensor(Port.S3)

Threshold = 40
# v, Kp 조절
v = 50
error = 0
Kp = 2.2

# # P제어
# while True:
#     wait(1)
#     error = c2.reflection() - Threshold
#     ml.run(v + (error * Kp))
#     mr.run(v - (error * Kp))

# # PI제어 (비례 적분)
# v = 50
# error = 0
# esum = 0
# Kp, Ki = 2.2, 0.0005

# while True:
#     wait(1)
#     error = c2.reflection() - Threshold
#     esum = esum + error
#     ml.run(v + (error * Kp + esum * Ki))
#     mr.run(v - (error * Kp + esum * Ki))


# PID 제어(비례 적분 미분)
v = 50
error = 0
esum = 0
diff = 0
last_error = 0
Kp = 2.2  # 오차 반영 비율, 비례 상수
Ki = 0.0005  # 누적된 오차의 반영 비율, 적분 상수
Kd = 100  # 오차와 직전 오차의 변화량의 반영 비율, 비분 상수

while True:
    error = c2.reflection() - Threshold
    esum = esum + error
    diff = error - last_error
    ml.run(v + (error * Kp + esum * Ki + diff * Kd))
    mr.run(v - (error * Kp + esum * Ki + diff * Kd))
    last_error = error
