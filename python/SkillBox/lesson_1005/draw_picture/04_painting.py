# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
import simple_draw as sd
import draw_rainbow as dr
import draw_wall as dw
import draw_figure as df
import draw_tree as dt
import draw_smile as ds
import draw_flake as dflake


sd.resolution = (1200, 600)
dr.draw_rainbow()
dw.draw_wall(start_x=150, end_x=400, start_y=30, end_y=350)
df.draw_square(sd.get_point(100, 30), 0, 300)
df.draw_triangle(sd.get_point(100, 330), 0, 300)
dt.draw_branches(sd.get_point(800, 30), 90, 65)
ds.print_smile(500, 250,  sd.COLOR_PURPLE )
dflake.show_snow(20)


sd.pause()
