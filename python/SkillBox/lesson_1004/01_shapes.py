# -*- coding: utf-8 -*-

import simple_draw as sd


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны

def draw_figure(point, angle, length, step, side):
    for line in range(side):
        v = sd.get_vector(start_point=point, angle=angle + line * step, length=length, width=2)
        v.draw()
        point = v.end_point


def draw_triangle(point, angle, length):
    draw_figure(point=point, angle=angle, length=length, step=120, side=3)


def draw_square(point, angle, length):
    draw_figure(point=point, angle=angle, length=length, step=90, side=4)


def draw_pentagon(point, angle, length):
    draw_figure(point=point, angle=angle, length=length, step=72, side=5)


def draw_hexagon(point, angle, length):
    draw_figure(point=point, angle=angle, length=length, step=60, side=6)


sd.resolution = (1200, 600)

point_0 = sd.get_point(500, 200)
draw_triangle(point_0, 0, 200)
point_0 = sd.get_point(100, 100)
draw_square(point_0, 0, 200)
point_0 = sd.get_point(400, 50)
draw_pentagon(point_0, 0, 100)
point_0 = sd.get_point(350, 350)
draw_hexagon(point_0, 0, 100)

sd.pause()
