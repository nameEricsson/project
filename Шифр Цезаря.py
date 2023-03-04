
eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
symbol = [" ", ",", ".", "!", "?"]

print('Будем шифровать(введите 1) или дешифровать(введите 2)?')
chifr1 = int(input())
print('Какой язык выберем русский(введите 1) или английский(введите 2)?')
language1 = int(input())
print('Какой шаг сдвига? Введите число')
step1 = int(input())
print('Введите текст')
text = input()


def cezar(chifr, language, step):
    text_change = ''
    if chifr == 1:
        if language == 1:
            for i in text:
                if (rus_lower_alphabet.find(i) + step) <= 31 and i in rus_lower_alphabet:
                    text_change += rus_lower_alphabet[(rus_lower_alphabet.find(i) + step)]
                elif (rus_upper_alphabet.find(i) + step) <= 31 and i in rus_upper_alphabet:
                    text_change += rus_upper_alphabet[(rus_upper_alphabet.find(i) + step)]
                elif (rus_lower_alphabet.find(i) + step) >= 32 and i in rus_lower_alphabet:
                    text_change += rus_lower_alphabet[(rus_lower_alphabet.find(i) + step) - 32]
                elif (rus_lower_alphabet.find(i) + step) >= 32 and i in rus_lower_alphabet:
                    text_change += rus_upper_alphabet[(rus_upper_alphabet.find(i) + step) - 32]
                else:
                    text_change += i
        elif language == 2:
            for i in text:
                if (eng_lower_alphabet.find(i) + step) <= 25 and i in eng_lower_alphabet:
                    text_change += eng_lower_alphabet[(eng_lower_alphabet.find(i) + step)]
                elif (eng_upper_alphabet.find(i) + step) <= 25 and i in eng_upper_alphabet:
                    text_change += eng_upper_alphabet[(eng_upper_alphabet.find(i) + step)]
                elif (eng_lower_alphabet.find(i) + step) >= 26 and i in eng_lower_alphabet:
                    text_change += eng_lower_alphabet[(eng_lower_alphabet.find(i) + step) - 26]
                elif (eng_upper_alphabet.find(i) + step) >= 26 and i in eng_upper_alphabet:
                    text_change += eng_upper_alphabet[(eng_upper_alphabet.find(i) + step) - 26]
                else:
                    text_change += i


    elif chifr == 2:
        if language == 1:
            for i in text:
                if (rus_lower_alphabet.find(i) - step) <= 31 and i in rus_lower_alphabet:
                    text_change += rus_lower_alphabet[(rus_lower_alphabet.find(i) - step)]
                elif (rus_upper_alphabet.find(i) - step) <= 31 and i in rus_upper_alphabet:
                    text_change += rus_upper_alphabet[(rus_upper_alphabet.find(i) - step)]
                elif (rus_lower_alphabet.find(i) - step) >= 32 and i in rus_lower_alphabet:
                    text_change += rus_lower_alphabet[(rus_lower_alphabet.find(i) - step) + 32]
                elif (rus_upper_alphabet.find(i) - step) >= 32 and i in rus_upper_alphabet:
                    text_change += rus_upper_alphabet[(rus_upper_alphabet.find(i) - step) + 32]
                else:
                    text_change += i
        elif language == 2:
            for i in text:
                if (eng_lower_alphabet.find(i) - step) <= 25 and i in eng_lower_alphabet:
                    text_change += eng_lower_alphabet[(eng_lower_alphabet.find(i) - step)]
                elif (eng_upper_alphabet.find(i) - step) <= 25 and i in eng_upper_alphabet:
                    text_change += eng_upper_alphabet[(eng_upper_alphabet.find(i) - step)]
                elif (eng_lower_alphabet.find(i) - step) >= 26 and i in eng_lower_alphabet:
                    text_change += eng_lower_alphabet[(eng_lower_alphabet.find(i) - step) + 26]
                elif (eng_upper_alphabet.find(i) - step) >= 26 and i in eng_upper_alphabet:
                    text_change += eng_upper_alphabet[(eng_upper_alphabet.find(i) - step) + 26]
                else:
                    text_change += i
    return text_change
print(cezar(chifr1, language1, step1))