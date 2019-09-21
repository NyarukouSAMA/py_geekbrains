number = int(input('Введите число: '))
n = 0

while n <= number:
    if n % 2 == 0:
        print(n, end='; ' if number - n > 1 else '\n')
    n += 1
else:
    print('Вывод завершен')
