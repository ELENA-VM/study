# -*- coding: utf-8 -*-

import simple_draw as sd


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

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
point_0 = sd.get_point(300, 300)

print('Возможные фигуры:')
print('  0: triangle')
print('  1: square')
print('  2: pentagon')
print('  3: hexagon')

while True:
    need_shape = int(input('Введите желаемую фигуру '))
    if not (0 <= need_shape < 4):
        print('Вы ввели неправильный номер')
        continue

    if need_shape == 0:
        draw_triangle(point_0, 0, 200)
    elif need_shape == 1:
        draw_square(point_0, 0, 200)
    elif need_shape == 2:
        draw_pentagon(point_0, 0, 100)
    else:
        draw_hexagon(point_0, 0, 100)
    break


sd.pause()
