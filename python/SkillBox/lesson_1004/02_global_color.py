# -*- coding: utf-8 -*-
import simple_draw as sd


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE

def draw_figure(point, angle, length, step, side, color=sd.COLOR_YELLOW):
    for line in range(side):
        v = sd.Vector(start_point=point, direction=angle + line * step, length=length)
        v.draw(color=color, width=2)
        point = v.end_point


def draw_triangle(point, angle, length, color):
    draw_figure(point=point, angle=angle, length=length, step=120, side=3, color=color)


def draw_square(point, angle, length, color):
    draw_figure(point=point, angle=angle, length=length, step=90, side=4, color=color)


def draw_pentagon(point, angle, length, color):
    draw_figure(point=point, angle=angle, length=length, step=72, side=5, color=color)


def draw_hexagon(point, angle, length, color):
    draw_figure(point=point, angle=angle, length=length, step=60, side=6, color=color)


def get_color(color):
    if color == 0:
        return sd.COLOR_RED
    elif color == 1:
        return sd.COLOR_ORANGE
    elif color == 2:
        return sd.COLOR_YELLOW
    elif color == 3:
        return sd.COLOR_GREEN
    elif color == 4:
        return sd.COLOR_CYAN
    elif color == 5:
        return sd.COLOR_BLUE
    else:
        return sd.COLOR_PURPLE


sd.resolution = (1200, 600)

print('Возможные цвета:')
print('  0: red')
print('  1: orange')
print('  2: yellow')
print('  3: green')
print('  4: cyan')
print('  5: blue')
print('  6: purple')

while True:
    need_color = int(input('Введите желаемы цвет '))
    if not (0 <= need_color < 7):
        print('Вы ввели неправильный номер')
        continue

    color = get_color(need_color)

    point_0 = sd.get_point(500, 200)
    draw_triangle(point_0, 0, 200, color)
    point_0 = sd.get_point(100, 100)
    draw_square(point_0, 0, 200, color)
    point_0 = sd.get_point(400, 50)
    draw_pentagon(point_0, 0, 100, color)
    point_0 = sd.get_point(350, 350)
    draw_hexagon(point_0, 0, 100, color)
    break

sd.pause()
