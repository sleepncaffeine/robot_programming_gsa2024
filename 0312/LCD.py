#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.media.ev3dev import Font, Image, ImageFile
from pybricks.parameters import Color
from pybricks.tools import wait

# 화면 삭제
ev3 = EV3Brick()

# 화면 삭제
ev3.screen.clear()

font = Font(size=30, bold=True)
ev3.screen.set_font(font)

# 화면에 텍스트 그리기
ev3.screen.draw_text(
    2, 100, "Hello World", text_color=Color.BLACK, background_color=None
)
wait(3000)
ev3.screen.clear()

# 화면에 텍스트 출력
ev3.screen.print("Hello World")
wait(2000)


# #화면 중앙에 소스 이미지 그리기
ev3.screen.load_image(ImageFile.AWAKE)
wait(1000)

ev3.screen.clear()
ev3.screen.draw_line(0, 0, 177, 127, color=Color.BLACK)
ev3.screen.draw_line(0, 127, 177, 0, color=Color.BLACK)
wait(1000)
