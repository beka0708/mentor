import re
from collections import Counter

try:
    while True:
        def most_common_word(sentence):
            words = re.findall(r'\w+', sentence)
            word_count = Counter(words)
            return word_count.most_common(1)[0]


        print("Первое введите слово которое нужно найти")
        sentence = str(input('Введите текст: '))
        most_common = most_common_word(sentence)
        print(f'Cлово "{most_common[0]}" было использовано {most_common[1]} раз')
except ValueError:
    print('Вы где-то допустили ошибку')