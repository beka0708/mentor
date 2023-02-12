import datetime

time_user = int(input('Сколько раз вы хотите ввести ваши данные: '))
time_list = []
for i in range(time_user):
    while True:
        user = input(f'Ваш ответ  {i + 1} должен быть в формате (час:минуты:cекунды) - ')
        try:
            valid_time = datetime.datetime.strptime(user, '%H:%M:%S')
            if valid_time in time_list:
                print(f'Время {valid_time} уже имеется . введите другое время !!!')
                continue
            time_list.append(valid_time)
            break
        except ValueError:
            print(f'Формат времени {user} неправильный !!!\n Вводите в формате - |час:минуты:cекунды| ')
hour = []
minute = []
seconds = []

for valid_time in time_list:
    hour.append(valid_time.hour)
    minute.append(valid_time.minute)
    seconds.append(valid_time.second)

print("Cписок часов: ", hour)
print("Cписок минут : ", minute)
print("Cписок секунд: ", seconds)
print("Отсортировка окончена...")
