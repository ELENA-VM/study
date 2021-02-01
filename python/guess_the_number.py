import random

def is_valid(el):
    if el.isdigit() and (1 <= int(el) <= 100):
        return True
    else:
        return False

def start_game(num):
    count = 0
    while True:
        count += 1
        pn = input('Введите число от 1 до 100\n')
        if not is_valid(pn):
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
        else:
            pn = int(pn)
            if pn < num:
                print('Ваше число меньше загаданного, попробуйте еще разок')
            elif pn > num:
                print('Ваше число больше загаданного, попробуйте еще разок')
            else:
                print('Вы угадали, поздравляем!', 'Количество попыток = ' + str(count))
                break

    next_n = input('Чтобы продолжить игру, напиши "да"\n')
    if next_n.lower() == 'да':
        rb = int(input('Ввеите правое ограничение\n'))
        next_num = random.randrange(1, rb)
        start_game(next_num)

print('Добро пожаловать в числовую угадайку')
r = int(input('Введите правое ограничение\n'))
n = random.randrange(1, r)

start_game(n)

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
