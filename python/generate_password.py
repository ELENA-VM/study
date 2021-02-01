import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

def generate_password(length, chars):
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    return password

count_password = int(input('Количество паролей для генерации\n'))
len_password = int(input('Длину одного пароля\n'))
include_digit = input('Включать цифры 0123456789 (да/нет)?\n')
include_upper_letter = input('Включать прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ (да/нет)?\n')
include_lower_letter = input('Включать строчные буквы abcdefghijklmnopqrstuvwxyz(да/нет)?\n')
include_spec_symbol = input('Включать символы !#$%&*+-=?@^_(да/нет)?\n')
exclude_symbol = input('Исключать ли неоднозначные символы il1Lo0O(да/нет)?\n')

char = ''

if include_digit.upper() == 'да'.upper():
    char += digits

if include_upper_letter.upper() == 'да'.upper():
    char += uppercase_letters

if include_lower_letter.upper() == 'да'.upper():
    char += lowercase_letters

if include_spec_symbol.upper() == 'да'.upper():
    char += punctuation

if exclude_symbol.upper() == 'да'.upper():
    for c in 'il1Lo0O':
        char = char.replace(c, '')

list_password = []

for el in range(count_password+1):
    list_password.append(generate_password(len_password, char))

print(*list_password, sep='\n')