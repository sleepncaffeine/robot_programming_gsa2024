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
import threading
import time

ev3 = EV3Brick()

# 좌, 우 모터, 팔 및 초음파 센서 초기화
ml = Motor(Port.B)
mr = Motor(Port.C)
hand = Motor(Port.A)
us = UltrasonicSensor(Port.S4)
gs = GyroSensor(Port.S2)
cs = ColorSensor(Port.S3)
ts = TouchSensor(Port.S1)


def line_go():
    global color
    while not stop_flag:
        if color == Color.WHITE:
            ml.run(200)
            mr.run(100)
        else:
            ml.run(100)
            mr.run(200)


ev3.speaker.beep()
while ts.pressed() == 0:
    {}
while ts.pressed() == 1:
    {}

data = DataLog("time", "ml_angle", "mr_angle", "gyro", "us", "color")
watch = StopWatch()
stop_flag = False
color = cs.color()

t = threading.Thread(target=line_go)
t.start()

while True:
    time = watch.time()
    ml_angle = ml.angle()
    mr_angle = mr.angle()
    gyro = gs.angle()
    distance = us.distance()
    color = cs.color()
    data.log(time, ml_angle, mr_angle, gyro, distance, color)
