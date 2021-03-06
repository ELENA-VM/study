# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from pprint import pprint
from district.central_street.house1.room1 import folks as central_street_h1_room_1
from district.central_street.house1.room2 import folks as central_street_h1_room_2
from district.central_street.house2.room1 import folks as central_street_h2_room_1
from district.central_street.house2.room2 import folks as central_street_h2_room_2
from district.soviet_street.house1.room1 import folks as soviet_street_h1_room_1
from district.soviet_street.house1.room2 import folks as soviet_street_h1_room_2
from district.soviet_street.house2.room1 import folks as soviet_street_h2_room_1
from district.soviet_street.house2.room2 import folks as soviet_street_h2_room_2

list_folks = central_street_h1_room_1
list_folks.extend(central_street_h1_room_2)
list_folks.extend(central_street_h2_room_1)
list_folks.extend(central_street_h2_room_2)
list_folks.extend(soviet_street_h1_room_1)
list_folks.extend(soviet_street_h1_room_2)
list_folks.extend(soviet_street_h2_room_1)
list_folks.extend(soviet_street_h2_room_2)

pprint(', '.join(list_folks))
