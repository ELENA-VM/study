# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd


# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

def print_brick(x1, y1, x2, y2):
    sd.line(sd.get_point(x1, y1), sd.get_point(x1, y2), sd.COLOR_RED, 2)
    sd.line(sd.get_point(x1, y2), sd.get_point(x2, y2), sd.COLOR_RED, 2)
    sd.line(sd.get_point(x2, y2), sd.get_point(x2, y1), sd.COLOR_RED, 2)
    sd.line(sd.get_point(x2, y1), sd.get_point(x1, y1), sd.COLOR_RED, 2)


sd.resolution = (1200, 600)

y1 = 1
y2 = 50

for i in range(1, 13):
    x1 = -50 if i % 2 == 0 else 1
    x2 = x1 + 100

    for _ in range(1, 14):
        print_brick(x1, y1, x2, y2)
        x1 = x2
        x2 += 100
    y1 = y2
    y2 += 50

sd.pause()
