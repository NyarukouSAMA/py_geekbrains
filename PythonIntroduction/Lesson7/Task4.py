def numericParadaize(number):
    if (number == 13):
        raise ValueError(1, "Чертова дюжина не может попасть в рай для чисел")
    return number


try:
    angelNumber = numericParadaize(int(input('Вы умерли, введите число: ')))
except ValueError as e:
    print(e.args[1]) if e.args[0] == 1 else print('Ой, вы сломали рай :(')
except Exception:
    print('Ой, вы сломали рай :(')
else:
    print('Добро пожаловать домой, ваш номер {}'.format(angelNumber))
