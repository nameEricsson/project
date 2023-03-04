import random

print('Добро пожаловать в числовую угадайку',
      'В каком диапазоне чисел вы хотите, чтобы я загадал число? ', sep='\n')

def new_game():
    print('Введите свой вариант или введите от 1 до 100', sep='\n')
    granica()


def granica():
    min1, max1 = int(input()), int(input())
    if min1 > max1:
        min1, max1 = max1, min1
    print(f'Прекрасно, я загадал число в диапазоне от {min1} до {max1}',
          'Теперь попробуйте отгадать, какое это число. Введите число', sep='\n')
    compare_num(min1, max1)


def input_num(a, b):
    while True:
        num = input()
        if num.isdigit() and a <= int(num) <= b:
            return int(num)
        else:
            print(f'А может быть все-таки введем целове число от {a} до {b}?')


def compare_num(a, b):
    count = 0
    g = random.randint(a, b)
    while True:
        number = input_num(a, b)
        if number > g:
            count += 1
            print('Слишком много')
        elif number < g:
            count += 1
            print('Слишком мало')
        else:
            count += 1
            print('Поздравляю вы угадали с', count, 'попытки')
            end_game()


def end_game():
    print('Хотите попробовать еще раз?')
    y = input()
    if y in ['Да', 'ДА', 'да', 'Yes', 'YES', 'yes', 'y', 'д']:
        print('Хорошо, введите число, чтобы угадать.')
        new_game()
    elif y in ['Нет', 'НЕТ', 'No', 'NO', 'no', 'нет', 'n', 'н']:
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
new_game()