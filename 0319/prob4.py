#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase


ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# 정지 옵션
# Stop.BRAKE : 모터를 정지할 때 브레이크를 사용하여 정지한다.
# Stop.COAST : 모터를 정지할 때 브레이크를 사용하지 않고 정지한다.
# Stop.HOLD : 모터를 정지할 때 브레이크를 사용하여 정지하고, 모터의 위치를 유지한다.

left_motor.run_angle(1000, 720, Stop.BRAKE, False)
right_motor.run_angle(1000, 720, Stop.BRAKE, True)
wait(1000)

left_motor.run_angle(1000, 720, Stop.COAST, False)
right_motor.run_angle(1000, 720, Stop.COAST, True)
wait(1000)

left_motor.run_angle(1000, 720, Stop.HOLD, False)
right_motor.run_angle(1000, 720, Stop.HOLD, True)
wait(1000)

# | Type       | 마찰 | 역 EMF | 속도 0 유지 | 각도 target에 유지 |
# | ---------- | ---- | ------ | ----------- | ------------------ |
# | Stop.COAST | O    | X      | X           | X                  |
# | Stop.BRAKE | O    | O      | X           | X                  |
# | Stop.HOLD  | O    | O      | O           | O                  |
