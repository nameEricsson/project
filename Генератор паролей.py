import random
print('Генератор паролей')

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

print('Сколько паролей нужно?')
num = int(input())
print('Какая длина пароля?')
length = int(input())
print('Включать ли цифры 0123456789?; д = да, н = нет')
chisla = input()
print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?; д = да, н = нет')
upper = input()
print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?; д = да, н = нет')
lower = input()
print('Включать ли символы !#$%&*+-=?@^_?; д = да, н = нет')
symbols = input()
print('Исключать ли неоднозначные символы il1Lo0O?; д = да, н = нет')
similar_symbols = input()

if chisla in ['д', 'YES', 'yes', 'y', 'Да', 'ДА']:
    chars += chisla
if upper in ['д', 'YES', 'yes', 'y', 'Да', 'ДА']:
    chars += upper
if lower in ['д', 'YES', 'yes', 'y', 'Да', 'ДА']:
    chars += lower
if symbols in ['д', 'YES', 'yes', 'y', 'Да', 'ДА']:
    chars += symbols
if similar_symbols in ['д', 'YES', 'yes', 'y', 'Да', 'ДА']:
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

def generate_password():
    passw = ''
    for i in range(length):
        passw += random.choice(chars)
    return passw

for c in range(num):
    print(generate_password())
