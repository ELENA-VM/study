import random
words_list = ['человек', 'слово', 'лицо', 'дверь', 'земля', 'работа', 'ребенок', 'история', 'женщина',
              'развитие', 'власть', 'правительство', 'начальник', 'спектакль', 'автомобиль', 'экономика',
              'литература', 'граница', 'магазин', 'председатель', 'сотрудник', 'республика', 'личность']

def get_word():
    return random.choice(words_list).upper()

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     ⎛▼⎞
           |     ⎛  ⎞
           |    
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     ⎛▼⎞
           |     ⎛ 
           |
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     ⎛▼⎞
           |
           |
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     ⎛▼
           |
           |
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      ▼
           |
           |
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]

def print_word(word, g_letters):
    for c in word:
        if c in g_letters:
            print(c, end='')
        else:
            print('_', end='')

def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток

    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(word_completion)

    while True:
        user_answer = input('Введите букву или слово: ').upper()

        if not user_answer.isalpha():
            print('Введене неккоректное значение')
            continue

        if (user_answer in guessed_letters) or (user_answer in guessed_words):
            print('Введено повторно')
            continue

        if len(user_answer) > 1 and user_answer == word:
            print('Congratulation, you winner!')
            break
        else:
            guessed_words.append(user_answer)
            tries -=1

            if tries == 0:
                print('Вы не смогли угадать слово')
                print(display_hangman(tries))
                break

            print('Вы неугадали, осталось попыток', tries)
            print(display_hangman(tries))
            continue

        if user_answer in word:
            for c in word:
                if c not in guessed_letters:
                    print('Угадали букву')
                    guessed_letters.append(user_answer)
                    print_word(word, guessed_letters)
                    guessed = False
                    break
                guessed = True

            if guessed:
                print_word(word, guessed_letters)
                print('Поздравляем, вы угадали слово! Вы победили!')
                break

            tries -=1

            if tries == 0:
                print('Вы не смогли угадать слово', word)
                print(display_hangman(tries))
                break
print('Hello, start the "Hangman"')

while True:
    generate_word = get_word()
    play(generate_word)

    next_game = input('Чтобы продолжить игру напиши "да"\n')
    if next_game.lower() != 'да':
        break

print('Возвращайся.....')







