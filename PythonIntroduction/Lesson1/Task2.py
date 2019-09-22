def condCheck(number):
    return number is None or number <= 0 or number >= 10


number = None

while condCheck(number):
    number = int(input('Введите число: '))
    if condCheck(number):
        print(number, 'не принадлежит (0; 10).')
        continue
else:
    print(number ** 2)
