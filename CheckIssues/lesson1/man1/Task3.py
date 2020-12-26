#Задание 3
name = input('Ваше имя: ')
surname = input('Ваша фамилия: ')
age = int(input('Ваш возраст: '))
weight = int(input('Ваш вec: '))
if weight < 50 or weight > 120:
    if age > 40:
        print ('Вам нужно обратиться ко врачу!')
    else:
        if age > 30:
            print ('Вам нужно заняться собой!')
        else:
            print ('Вам нужно обратиться к диетологу')
else:
    if age <= 30:
        print ('Хорошее состояние')
    else:
        print ('Пройдите проверку через год')