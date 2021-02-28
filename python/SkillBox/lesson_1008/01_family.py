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
        print(f'{self.name} покушал: fullness {self.fullness}')
        return True

    def act(self):
        if self.fullness < 10 or self.happiness < 0:
            print(f'{self.name} умер')
            return True

        if self.fullness <= 20 and self.house.eat > 0:
            if self.eat():
                return True

        if self.house.dirt >= 90:
            self.happiness -= 10
            return True

        return False


class House:

    def __init__(self):
        self.money = 100
        self.eat = 50
        self.dirt = 0

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
        dice = randint(1, 3)

        if super().act():
            return
        elif self.happiness <= 10:
            self.gaming()
        elif self.house.money <= 10:
            self.work()
        elif dice == 1 and self.house.eat >= 30:
            self.eat()
        elif dice == 2:
            self.gaming()
        else:
            self.work()

    def work(self):
        self.fullness -= 10
        self.house.money += 150
        print(f'{self.name} сходил на работу: money {self.house.money}')

    def gaming(self):
        self.fullness += 20
        print(f'{self.name} поиграл: fullness {self.fullness}')


class Wife(Man):

    def __init__(self, name, house):
        super().__init__(name, house)

    def __str__(self):
        return super().__str__()

    def act(self):
        dice = randint(1, 4)

        if super().act():
            return
        elif self.house.money >= 10 and self.house.eat <= 30:
            self.shopping()
        elif self.house.money >= 350 and self.happiness < 20:
            self.buy_fur_coat()
        elif self.house.dirt >= 90:
            self.clean_house()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.shopping()
        elif dice == 3 and self.house.money >= 350:
            self.buy_fur_coat()
        else:
            self.clean_house()

    def shopping(self):
        self.fullness -= 10

        count_food = randint(1, self.house.money // 10)

        self.house.money -= 10*count_food
        self.house.eat += 10*count_food
        print(f'{self.name} шоппинг: fullness {self.fullness} money {self.house.money}')

    def buy_fur_coat(self):
        self.fullness += 60
        self.house.money -= 350
        print(f'{self.name} покупка шубы: fullness {self.fullness} money {self.house.money}')

    def clean_house(self):
        self.fullness -= 10
        self.house.dirt -= 100
        if self.house.dirt < 0:
            self.house.dirt = 0

        print(f'{self.name} уборка квартиры: fullness {self.fullness} dirt {self.house.dirt}')


home = House()
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    home.add_dirt()
    serge.act()
    masha.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(home, color='cyan')


# TODO после реализации первой части - отдать на проверку учителю

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self):
        pass

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

    def soil(self):
        pass


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child:

    def __init__(self):
        pass

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass
