import random

answer = {1: 'Бесспорно', 2: 'Предрешено', 3: 'Никаких сомнений', 4: 'Определённо да', 5: 'Можешь быть уверен в этом',
          6: 'Мне кажется - да', 7: 'Вероятнее всего', 8: 'Хорошие перспективы', 9: 'Знаки говорят - да', 10: 'Да',
          11: 'Пока неясно, попробуй снова', 12: 'Спроси позже', 13: 'Лучше не рассказывать', 14: 'Сейчас нельзя предсказать', 15: 'Сконцентрируйся и спроси опять',
          16: 'Даже не думай',17: 'Мой ответ - нет', 18: 'По моим данным - нет', 19: 'Перспективы не очень хорошие', 20: 'Весьма сомнительно'}

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name_user = input('Как Вас зовут?\n')
print('Привет', name_user)

while True:
    question = input('Задавайте свой вопрос\n')
    print(random.choice(answer))

    next_question = input('Чтобы задать следующий вопрос, напиши "да"\n')
    if next_question.lower() != 'да':
        break

print('Возвращайся если возникнут вопросы!')