ru_lower_lst = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
ru_upper_lst = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
en_lower_lst = 'abcdefghijklmnopqrstuvwxyz'
en_upper_lst = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_,."'

def get_len(word):
    for c in punctuation:
        word = word.replace(c, '')
    return len(word)

def encrypt_str(cur_str, type_dic, shift):
    result = ''
    for c in cur_str:
        if type_dic == 'ru':
            if c in ru_lower_lst:
                ind = ru_lower_lst.index(c) % len(ru_lower_lst)
                result += ru_lower_lst[(ind + shift) % len(ru_lower_lst)]
            elif c in ru_upper_lst:
                ind = ru_upper_lst.index(c) % len(ru_upper_lst)
                result += ru_upper_lst[(ind + shift) % len(ru_upper_lst)]
            else:
                result += c
        else:
            if c in en_lower_lst:
                ind = en_lower_lst.index(c) % len(en_lower_lst)
                result += en_lower_lst[(ind + shift) % len(en_lower_lst)]

            elif c in en_upper_lst:
                ind = en_upper_lst.index(c) % len(en_upper_lst)
                result += en_upper_lst[(ind + shift) % len(en_upper_lst)]
            else:
                result += c

    return result

def decrypt_str(cur_str, type_dic, shift):
    result = ''
    for c in cur_str:
        if type_dic == 'ru':
            if c in ru_lower_lst:
                ind = ru_lower_lst.index(c)
                result += ru_lower_lst[(ind - shift)% len(ru_lower_lst)]
            elif c in ru_upper_lst:
                ind = ru_upper_lst.index(c)
                result += ru_upper_lst[(ind - shift)% len(ru_upper_lst)]
            else:
                result += c
        else:
            if c in en_lower_lst:
                ind = en_lower_lst.index(c)
                result += en_lower_lst[(ind - shift)% len(en_lower_lst)]
            elif c in en_upper_lst:
                ind = en_upper_lst.index(c)
                result += en_upper_lst[(ind - shift)% len(en_upper_lst)]
            else:
                result += c

    return result

s = input()
list = s.split()
res_list = []
for i in range(len(list)):
    res_list.append(encrypt_str(list[i], 'en', get_len(list[i])))

print(' '.join(res_list))

#print(encrypt_str(s, 'en', len(s)))

#rn = int(input('Iput right border\n'))

#for i in range(rn+1):
#    print(i, decrypt_str('Hawnj pk swhg xabkna ukq nqj.', 'en', i))
