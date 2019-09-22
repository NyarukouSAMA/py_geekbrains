import random


def getNotDublicated(element, someNumericList):
    count = 0
    for n in someNumericList:
        if n == element:
            count += 1
    return count == 1


def getDublicated(element, someNumericList):
    count = 0
    for n in someNumericList:
        if n == element:
            count += 1
    return count > 1


exitCondition = False
someNumericList = None
menuText = '''Меню:
Сгенерировать новый список (нажмите 1 и Enter)
Вывести список целиком (нажмите 2 и Enter)
Вывести уникальные значения (нажмите 3 и Enter)
Вывести дубли (нажмите 4 и Enter)
Вызвать меню (нажмите 5 и Enter)
Завершить программу (любая другая клавиша и/или Enter)\n'''
print(menuText)
while not exitCondition:
    menuInput = input()
    if menuInput == '1' or someNumericList is None:
        someNumericList = [x + int(random.uniform(3, 10)) for x in range(0,
                                                                         int(random.uniform(10, 50)), int(random.uniform(1, 2)))]
        setFromNumericList = set(someNumericList)
    if menuInput == '1':
        continue
    elif menuInput == '2':
        print('Список целиком:\n{}'.format(someNumericList))
    elif menuInput == '3':
        print('Уникальные значения:\n{}'.format(list(filter(lambda element: getNotDublicated(
            element, someNumericList), setFromNumericList))))
    elif menuInput == '4':
        print('Дубли:\n{}'.format(list(filter(lambda element: getDublicated(
            element, someNumericList), setFromNumericList))))
    elif menuInput == '5':
        print(menuText)
    else:
        exitCondition = True
