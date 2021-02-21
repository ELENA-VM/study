# -*- coding: utf-8 -*-

import simple_draw as sd
import snowfall as sf

# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall


sd.resolution = (1200, 600)
sf.create_flake(10)

while True:
    sf.draw_flake(color=sd.background_color)
    sf.move_flake()
    sf.draw_flake(color=sd.COLOR_PURPLE)

    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
