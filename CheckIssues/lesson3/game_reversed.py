min_number = 0
max_number = 100
number = int((min_number+max_number)/2)
while True:
    print(f'Моё число - {number}. Ваше число больше? 1 - да, 2 - нет, 3 - равно.')
    answer = int(input())
    if answer == 1:
        min_number = number
        number = int((min_number+max_number)/2)
    elif answer == 2:
        max_number = number
        number = int((min_number+max_number)/2)
    elif answer == 3:
        print('Ура, я победил!')
        break
    else:
        print('Вы ввели неизвестное число. Пожалуйста, попробуйте снова.')