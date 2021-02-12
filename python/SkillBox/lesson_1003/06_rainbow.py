# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


def draw_circle(point, color):
    radius = 300
    sd.circle(center_position=point, radius=radius, width=4, color=color)


# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
sd.resolution = (1200, 600)

for i in range(7):
    point = sd.get_point(50+i*2, 50+i*2)
    draw_circle(point, rainbow_colors[i])

sd.pause()
