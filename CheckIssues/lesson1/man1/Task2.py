#Задание 2
name = int(input('Введите число: '))
while name >= 10 or name <= 0:
    if name >=10:
        print ('Неверно.Нужно поменьше')
    else:
        print ('Неверно.Нужно побольше')
    name = int(input('Введите число: '))
print ('Подойдет')
name = name ** 2
print (name)