import random


def get_word():
    word_list = [
        ["свинья", "лошадь", "кошка", "корова", "собака", "овца", "козел", "курица"],  # Категория животные
        ["футбол", "хоккей", "теннис", "регби", "гольф", "биатлон", "дзюдо", "бокс"] , # Категория спорт
        ["обезьяна", "жираф", "носорог", "слон", "бегемот", "зебра", "лев", "буйвол", "антилопа"] # Категория африканские животные
    ]
    print('Хотите угадывать в случайной категории слов? или Выберете категорию сами?')
    print('В игре присутвует категория слов "случайная", "животные", "спорт", "африканские животные"')
    print('Можно выбрать цифрами или написать категорию слов')
    kategoria = input()
    if kategoria in ['случайная', 'СЛУЧАЙНАЯ', '1']:
        g = random.randint(0, 2)
        return play(random.choice(word_list[g]).upper(), kategoria)
    elif kategoria in ['животные', 'ЖИВОТНЫЕ', '2']:
        return play(random.choice(word_list[0]).upper(), kategoria)
    elif kategoria in ['спорт', 'СПОРТ', '3']:
        return play(random.choice(word_list[1]).upper(), kategoria)
    elif kategoria in ['африканские животные', 'АФРИКАНСКИЕ ЖИВОТНЫЕ', '4']:
        return play(random.choice(word_list[2]).upper(), kategoria)


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
        # голова, торс, обе руки, одна нога
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
        # голова, торс, обе руки
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
        # голова, торс и одна рука
        '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
        # голова и торс
        '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
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


def welcome():
    print('Давайте играть в угадайку слов!')
    print('У вас есть 6 попыток отгадать слово, за каждый промах на висилеце будет появлятся одна часть тела')
    print('Начнем')
    get_word()


def play(word, сategoria):
    # word = random.choice(word_list).upper() # рандомное слово
    word_completion = ['_' for i in range(len(word))]  # список из _ по длинне скрытого слова
    word_random = [j for j in word]  # список букв из рандомного слова
    guessed_letters = []  # список угаданных букв
    guessed_words = []  # список угаданных слов
    print(f'Я загадал слово из категории {сategoria}  ', *word_completion)
    print('Назовите букву которая может быть в этом слове (вводить нужно русскую букву)')
    tries = 6
    while tries > 0:
        s = input().upper()
        if s.isalpha():
            if len(s) > 1:
                if s == word:
                    print('Вы победили!!!')
                    print('Правильное слово ', word, sep='')
                    guessed_words.append(s)
                    new_game()
                if s in guessed_words:
                    print('Вы уже называли такое слово')
                    continue
            if s in word:
                if s in guessed_letters:
                    print('Вы уже называли такую букву')
                    continue
                elif s not in guessed_letters:
                    for i in range(len(word)):
                        if word[i] == s:
                            guessed_letters.append(s)
                            word_completion.pop(i)
                            word_completion.insert(i, s)
                    print(*word_completion, sep='')
                continue
            if s not in word:
                print('Уууупс вы не угадали, к виселице добавилась часть тела')
                tries -= 1
                print(display_hangman(tries))
                continue
        else:
            print('Нужно ввести букву или слово на русском языке')
    if tries == 0:
        print('Вы проиграли')
        print(display_hangman(tries))
        new_game()


def new_game():
    print('Хочешь продолжить игру? или закончим?')
    print('Напиши "да" или "нет"')
    enter = input()
    if enter in ['YES', 'yes', 'y', 'ДА', 'да', 'д']:
        print('Прекрасно давай играть')
        get_word()
    elif enter in ['NO', 'no', 'n', 'НЕТ', 'нет', 'н']:
        print('Хорошо, увидимся...')
    else:
        print('Необходимо ввести на русском "да" или "нет"')


welcome()
