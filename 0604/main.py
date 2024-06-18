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
from pybricks.messaging import BluetoothMailboxServer, TextMailbox
from socket import *

HOST = "192.168.0.7"
PORT = 9999
BUFSIZE = 1024
ADDR = (HOST, PORT)

ev3 = EV3Brick()
ml = Motor(Port.B)
mr = Motor(Port.C)


clientSocket = socket(AF_INET, SOCK_STREAM)  # 서버에 접속하기 위한 소켓을 생성한다.

ev3.speaker.beep()
clientSocket.connect(ADDR)
msg = clientSocket.recv(1024)
dmsg = msg.decode("utf-8")
ev3.screen.print(dmsg)
while True:
    msg = clientSocket.recv(1024)
    dmsg = msg.decode("utf-8")
    # ev3.screen.print(dmsg)
    if dmsg == "bye":
        break
    elif dmsg == "left":
        ml.run_time(-100, 1000, wait=False)
        mr.run_time(100, 1000, wait=True)
    elif dmsg == "right":
        ml.run_time(100, 1000, wait=False)
        mr.run_time(-100, 1000, wait=True)
    elif dmsg == "forward":
        ml.run_time(100, 1000, wait=False)
        mr.run_time(100, 1000, wait=True)
    elif dmsg == "backward":
        ml.run_time(-100, 1000, wait=False)
        mr.run_time(-100, 1000, wait=True)
    elif dmsg == "stop":
        ml.stop()
        mr.stop()
    else:
        ev3.screen.print(dmsg)
