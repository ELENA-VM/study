import requests
list_sites = ['https://iti.bsuir.by/', 'https://galaktika.ru/',\
              'https://webmax.by', 'https://www.karandash.by/',\
              'https://mila.by/']

for el in list_sites:
    print(el, '-'*10)
    for i in range(1, 501):
        response = requests.get(el)
        print(i, response.status_code)
