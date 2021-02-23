# -*- coding: utf-8 -*-

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    def __init__(self, x, y, length):
        self.x = x
        self.y = y
        self.length = length

    def draw(self, color=sd.COLOR_WHITE):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length, color=color)
        sd.finish_drawing()

    def clear_previous_picture(self):
        self.draw(sd.background_color)

    def move(self):
        self.x += sd.random_number(-25, 25)
        self.y -= sd.random_number(1, 25)

    def can_fall(self):
        pass


def get_flakes(count):
    array_flake = []
    for _ in range(count):
        array_flake.append(Snowflake(sd.random_number(0, 900), sd.random_number(500, 600), sd.random_number(20, 40)))

    return array_flake


# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
flakes = get_flakes(count=20)  # создать список снежинок

while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()

    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
