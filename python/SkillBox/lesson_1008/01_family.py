# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.

class Man:
    def __init__(self, name, house):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = house

    def __str__(self):
        return f'Name {self.name}, fullness {self.fullness}, happiness {self.happiness}'

    def eat(self):

        count_eat = 30
        if self.house.eat < 30:
            count_eat = self.house.eat

        self.fullness += count_eat
        self.house.eat -= count_eat
        self.house.total_eat += count_eat
        print(f'{self.name} покушал: fullness {self.fullness}')
        return True

    def pet_cat(self):
        self.happiness += 5
        print(f'{self.name} погладили кота: happiness {self.happiness}')

    def act(self):
        if self.fullness < 10 or self.happiness <= 0:
            print(f'{self.name} умер')
            return True

        if self.fullness <= 30 and self.house.eat > 0:
            if self.eat():
                return True

        if self.house.dirt >= 90:
            self.happiness -= 10
            return False

        if self.happiness < 40:
            self.pet_cat()
            return True

        return False


class House:
    total_money = 0
    total_eat = 0

    def __init__(self):
        self.money = 100
        self.eat = 50
        self.dirt = 0
        self.cat_food = 30

    def __str__(self):
        return f'money {self.money}, eat {self.eat}, dirt {self.dirt}'

    def add_dirt(self):
        self.dirt += 5


class Husband(Man):

    def __init__(self, name, house):
        super().__init__(name, house)

    def __str__(self):
        result = super().__str__()
        return result

    def act(self):
        dice = randint(1, 4)

        if super().act():
            return
        elif self.happiness <= 30:
            self.gaming()
        elif self.house.money <= 10:
            self.work()
        elif dice == 1 and self.house.eat >= 30:
            self.eat()
        elif dice == 2:
            self.gaming()
        elif dice == 3:
            self.work()
        elif dice == 4:
            self.pet_cat()
        else:
            self.gaming()

    def work(self):
        self.fullness -= 10
        self.house.money += 150
        self.house.total_money += 150
        print(f'{self.name} сходил на работу: money {self.house.money}')

    def gaming(self):
        self.happiness += 20
        self.fullness -= 10
        print(f'{self.name} поиграл: happiness {self.happiness} fullness {self.fullness}')


class Wife(Man):
    total_coat = 0

    def __init__(self, name, house):
        super().__init__(name, house)

    def __str__(self):
        return super().__str__()

    def act(self):
        dice = randint(1, 5)

        if super().act():
            return
        elif self.house.money >= 10 and self.house.eat <= 30:
            self.shopping()
        elif self.house.money >= 350 and self.happiness <= 20:
            self.buy_fur_coat()
        elif self.house.dirt >= 90:
            self.clean_house()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.shopping()
        elif dice == 3 and self.house.money >= 350:
            self.buy_fur_coat()
        elif dice == 4:
            self.clean_house()
        else:
            self.pet_cat()

    def shopping(self):
        self.fullness -= 10

        count_food = randint(1, self.house.money / 2 // 10)

        self.house.money -= (10 * count_food + 10)
        self.house.eat += 10 * count_food
        self.house.cat_food += 10
        print(f'{self.name} шоппинг: fullness {self.fullness} money {self.house.money}')

    def buy_fur_coat(self):
        self.happiness += 60
        self.fullness -= 10
        self.house.money -= 350
        self.total_coat += 1

        print(f'{self.name} покупка шубы: happiness {self.happiness} money {self.house.money} fullness {self.fullness}')

    def clean_house(self):
        self.fullness -= 10
        self.house.dirt -= 100
        if self.house.dirt < 0:
            self.house.dirt = 0

        print(f'{self.name} уборка квартиры: fullness {self.fullness} dirt {self.house.dirt}')

class Child(Man):

    def __init__(self, name, house):
        self.happiness = 100
        self.fullness = 10
        self.house = house
        self.name = name

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.fullness <= 10:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        self.fullness += 10
        print(f'{self.name} покушал: fullness {self.fullness} ')

    def sleep(self):
        self.fullness -= 5
        print(f'{self.name} поспал: fullness {self.fullness} ')


class Cat:

    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.fullness = 30

    def __str__(self):
        return f'Pet {self.name}, fullness {self.fullness}'

    def act(self):
        if self.fullness <= 0:
            print(f'{self.name} умер')
            return

        dice = randint(1, 3)

        if self.fullness <= 10:
            self.eat()
        elif dice == 1:
            self.sleep()
        elif dice == 2:
            self.tear()
        else:
            self.eat()

    def eat(self):
        self.fullness += 20
        self.house.cat_food -= 10

    def sleep(self):
        self.fullness -= 10

    def tear(self):
        self.fullness -= 10
        self.house.dirt += 5

    def soil(self):
        self.house.dirt += 5


home = House()
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)
jack = Cat(name='Jack', house=home)
baby = Child(name='Саша', house=home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    home.add_dirt()
    serge.act()
    masha.act()
    jack.act()
    baby.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(jack, color='cyan')
    cprint(baby, color='cyan')
    cprint(home, color='cyan')

cprint('Всего заработано денег {}'.format(home.total_money), color='yellow')
cprint('Всего куплено еды {}'.format(home.total_eat), color='yellow')
cprint('Всего куплено шуб {}'.format(masha.total_coat), color='yellow')


