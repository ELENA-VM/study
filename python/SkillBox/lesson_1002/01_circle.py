#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть значение радиуса круга
import math


def print_distance(p, r):
    distance = round((p[0] ** 2 + p[1] ** 2) ** .5, 4)

    if distance <= r:
        print('Point in circle', True, 'distance = ', distance)
    else:
        print('Point in circle', False, 'distance = ', distance)


radius = 42
print('S = ', round(math.pi * radius ** 2, 4))

# Далее, пусть есть координаты точки
point = (23, 34)
print_distance(point, radius)

point_2 = (30, 30)
print_distance(point_2, radius)
