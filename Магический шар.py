import random

answers = ['Бесспорно',
           'Предрешено',
           'Никаких сомнений',
           'Определённо да',
           'Можешь быть уверен в этом',
           'Мне кажется - да',
           'Вероятнее всего',
           'Хорошие перспективы',
           'Знаки говорят - да',
           'Да',
           'Пока неясно, попробуй снова',
           'Спроси позже',
           'Лучше не рассказывать',
           'Сейчас нельзя предсказать',
           'Сконцентрируйся и спроси опять',
           'Даже не думай',
           'Мой ответ - нет',
           'По моим данным - нет',
           'Перспективы не очень хорошие',
           'Весьма сомнительно']
print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
print('Как тебя зовут?')
a = input()
print('Привет, '+a)
while True:
    print('Задай мне свой вопрос')
    b = input()
    print(random.choice(answers))
    print('Хочешь задать мне еще вопрос? можешь просто сказать "да"')
    c = input()
    if c in ['Да', 'ДА', 'да', 'Yes', 'YES', 'yes', 'y', 'д']:
        continue
    elif c in ['Нет', 'НЕТ', 'No', 'NO', 'no', 'нет', 'n', 'н']:
        print('Возвращайся если возникнут вопросы!')
        break
