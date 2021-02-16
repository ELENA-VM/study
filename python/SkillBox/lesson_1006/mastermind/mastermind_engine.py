import random

str_number = ''
count_try = 0


def guess_number():
    digits = []
    digits = [x for x in range(10)]
    random.shuffle(digits)
    number = digits[:4]

    if number[0] == 0:
        number[0] = number[1]
        number[1] = 0

    global count_try
    count_try = 0

    global str_number
    str_number = str(number)


def check_number(answer):
    global count_try
    count_try += 1
    dict_zoo = {'bulls': 0, 'cows': 0}
    
    for i in range(4):
        if answer[i] == str_number[i]:
            dict_zoo['bulls'] += 1
        elif answer[i] in str_number:
            dict_zoo['cows'] += 1

    return dict_zoo


def get_count_try():
    return count_try

