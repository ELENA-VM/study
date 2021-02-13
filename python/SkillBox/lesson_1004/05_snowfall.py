# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные
def draw_flake(x, y, length, color):
    point = sd.get_point(x, y)
    sd.start_drawing()
    sd.snowflake(center=point, length=length, color=color)


def show_snow(count_flake):
    snow_params = []

    for _ in range(count_flake):
        snow_params.append([sd.random_number(0, 1000), sd.random_number(500, 600), sd.random_number(20, 40)])

    while True:
        for flake in snow_params:
            x, y, length = flake
            draw_flake(x, y, length, sd.COLOR_WHITE)

        sd.finish_drawing()
        sd.sleep(0.1)

        for key, flake in enumerate(snow_params):
            x, y, length = flake
            draw_flake(x, y, length, sd.background_color)

            snow_params[key][0] += sd.random_number(-25, 25)
            snow_params[key][1] -= sd.random_number(1, 25)

        if y < 0:
            break

        if sd.user_want_exit():
            break


sd.resolution = (1200, 600)

N = 50

show_snow(N)
sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
