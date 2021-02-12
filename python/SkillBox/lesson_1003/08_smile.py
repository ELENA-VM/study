# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd
import random as rd
# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


def print_smile(x, y, color):
    point = sd.get_point(x, y)
    sd.circle(center_position=point, radius=50, width=2, color=color)
    point = sd.get_point(x-20, y+10)
    sd.circle(center_position=point, radius=4, width=2, color=color)
    point = sd.get_point(x+20, y+10)
    sd.circle(center_position=point, radius=4, width=2, color=color)

    start_point = sd.get_point(x, y-2)
    end_point = sd.get_point(x, y-15)
    sd.line(start_point, end_point,color=color, width=2)

    start_point = sd.get_point(x-15, y-25)
    end_point = sd.get_point(x+15, y-25)
    sd.line(start_point, end_point,color=color, width=2)


sd.resolution = (1200, 600)

for _ in range(10):
    print_smile(rd.randint(10, 900), rd.randint(10, 600),  sd.random_color())

sd.pause()
