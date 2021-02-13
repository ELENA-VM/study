# -*- coding: utf-8 -*-

import simple_draw as sd


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

def draw_branches(point, angle, length):
    if length < 10:
        return

    random_with = sd.random_number(1, 3)
    random_angle = sd.random_number(-12, 12)
    angle_1 = angle + 30 + random_angle
    v1 = sd.get_vector(start_point=point, angle=angle_1, length=length, width=random_with)
    v1.draw()
    angle_2 = angle - 30 + random_angle
    v2 = sd.get_vector(start_point=point, angle=angle_2, length=length, width=random_with)
    v2.draw()

    random_length = sd.random_number(-15, 15)/100
    draw_branches(point=v1.end_point, angle=angle_1, length=length * (.75+random_length))
    draw_branches(point=v2.end_point, angle=angle_2, length=length * (.75+random_length))


sd.resolution = (1200, 600)

point_0 = sd.get_point(300, 30)
draw_branches(point_0, 90, 100)

sd.pause()
