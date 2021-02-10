#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pprint import pprint

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Лена', 'Артур', 'Джек']

# список списков приблизителного роста членов вашей семьи
my_family_height = [[my_family[0], 164],
                    [my_family[1], 186],
                    [my_family[2], 30]]
pprint(my_family_height)
# Выведите на консоль рост отца в формате
print('Height Артура', my_family_height[1][1])

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
common_height = 0
for el in my_family_height:
    common_height += el[1]

print('Common height', common_height)