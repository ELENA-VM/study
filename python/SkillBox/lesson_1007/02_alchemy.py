# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Water:

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()

        if isinstance(other, Fire):
            return Steam()

        if isinstance(other, Ground):
            return Dirt()

    def __str__(self):
        return 'Вода'


class Air:
    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()

        if isinstance(other, Ground):
            return Dust()

    def __str__(self):
        return 'Воздух'


class Fire:
    def __add__(self, other):
        if isinstance(other, Ground):
            return Lava()

    def __str__(self):
        return 'Огонь'


class Ground:
    def __str__(self):
        return 'Земля'


class Storm:
    def __str__(self):
        return 'Шторм'


class Steam:
    def __str__(self):
        return 'Пар'


class Dirt:
    def __str__(self):
        return 'Грязь'


class Lightning:
    def __str__(self):
        return 'Молния'


class Dust:
    def __str__(self):
        return 'Пыль'


class Lava:
    def __str__(self):
        return 'Лава'


print(Water(), '+', Air(), '=', Water() + Air())
print(Fire(), '+', Air(), '=', Fire() + Air())
print(Water(), '+', Fire(), '=', Water() + Fire())
print(Water(), '+', Ground(), '=', Water() + Ground())
print(Air(), '+', Fire(), '=', Air() + Fire())
print(Air(), '+', Ground(), '=', Air() + Ground())
print(Fire(), '+', Ground(), '=', Fire() + Ground())
