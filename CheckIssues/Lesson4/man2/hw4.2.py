# Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

def maxOfThree (one, two, three) :
    return max(one, two, three)

one = int(input('Число 1:'))
two = int(input('Число 2:'))
three = int(input('Число 3:'))
print(f'Максимальное число: {maxOfThree(one, two, three)}')

