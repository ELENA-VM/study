# -*- coding: utf-8 -*-

import simple_draw as sd
import random as rd

sd.resolution = (1200, 600)

def draw_circle(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2,color=sd.random_color())

# Нарисовать 10 пузырьков в ряд
point = sd.get_point(100, 100)

# for i in range(10):
#     point = sd.get_point(200 + i*100, 200)
#     draw_circle(point, 10)

# Нарисовать три ряда по 10 пузырьков
# for j in range(3):
#     for i in range(10):
#         point = sd.get_point(100 + i*100, 100 + j*170)
#         draw_circle(point, 10)


# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for i in range(100):
    point = sd.get_point(100 + i * rd.randint(0, 100), 100 + i * rd.randint(0, 100))
    draw_circle(point, 10,)

sd.pause()


