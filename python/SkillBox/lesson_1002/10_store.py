#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
lamp_quantity = store[goods['Лампа']][0]['quantity']
lamp_cost = lamp_quantity * store[goods['Лампа']][0]['price']
print('Лампа -', lamp_quantity, 'шт, стоимость', lamp_cost, 'руб')

table_quantity = store[goods['Стол']][0]['quantity'] + \
                 store[goods['Стол']][1]['quantity']
table_cost = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price'] + \
             store[goods['Стол']][1]['quantity'] * store[goods['Стол']][1]['price']
print('Стол -', table_quantity, 'шт, стоимость', table_cost, 'руб')

sofa_quantity = store[goods['Диван']][0]['quantity'] + \
                store[goods['Диван']][1]['quantity']
sofa_cost = store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price'] + \
            store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price']

print('Диван -', sofa_quantity, 'шт, стоимость', sofa_cost, 'руб')

chair_quantity = store[goods['Стул']][0]['quantity'] + \
                 store[goods['Стул']][1]['quantity'] + \
                 store[goods['Стул']][2]['quantity']

chair_cost = store[goods['Стул']][0]['quantity'] * store[goods['Стул']][0]['price'] + \
             store[goods['Стул']][1]['quantity'] * store[goods['Стул']][1]['price'] + \
             store[goods['Стул']][2]['quantity'] * store[goods['Стул']][2]['price']

print('Стул -', chair_quantity, 'шт, стоимость', chair_cost, 'руб')
