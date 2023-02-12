import math

with open('truefalse.txt', 'w') as file:
    file.write('')

with open('area.txt', 'w') as file:
    file.write('')

try:
    while True:
        x1 = int(float(input('Введите координату x1: ')))
        y1 = int(float(input('Введите координату y1: ')))
        x2 = int(float(input('Введите координату x2: ')))
        y2 = int(float(input('Введите координату y2: ')))
        x3 = int(float(input('Введите координату x3: ')))
        y3 = int(float(input('Введите координату y3: ')))
        print('Ваши ответы были записаны в отдельные файлы ')


        def len_sides(x1, y1, x2, y2):
            return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)


        def len_sides2(x2, y2, x3, y3):
            return round(math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2), 2)


        def len_sides3(x3, y3, x1, y1):
            return round(math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2), 2)


        def triangle_area(a, b, c):
            p = (a + b + c) / 2
            return round(math.sqrt((p * (p - a) * (p - b) * (p - c))), 2)


        a = len_sides(x1, y1, x2, y2)
        b = len_sides2(x2, y2, x3, y3)
        c = len_sides3(x3, y3, x1, y1)
        area = triangle_area(a, b, c)
        with open('area.txt', 'a') as file:
            file.write(
                f'Площадь треугольника: {area}'
            )

        if a ** 2 + b ** 2 == c ** 2:
            with open('truefalse.txt', 'a') as file:
                file.write(
                    'True'
                )
        elif a ** 2 + c ** 2 == b ** 2:
            with open('truefalse.txt', 'a') as file:
                file.write(
                    'True'
                )
        else:
            if c ** 2 + b ** 2 == a ** 2:
                with open('truefalse.txt', 'a') as file:
                    file.write(
                        'True'
                    )
            else:
                with open('truefalse.txt', 'a') as file:
                    file.write(
                        'False'
                    )

except ValueError:
    print('Вы где-то допустили ошибку ')
