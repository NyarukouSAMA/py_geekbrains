def getDayString(dayNumber):
    strDayDict = {
        1: 'первое', 2: 'второе', 3: 'третье', 4: 'четвертое', 5: 'пятое',
        6: 'шестое', 7: 'седьмое', 8: 'восьмое', 9: 'девятое', 10: 'десятое',
        11: 'одинадцатое', 12: 'двенадцатое', 13: 'тринадцатое', 14: 'четырнадцатое', 15: 'пятнадцатое',
        16: 'шестнадцатое', 17: 'семнадцатое', 18: 'восемнадцатое', 19: 'девятнадцатое', 20: 'двадцатое', 30: 'тридцатое'
    }
    strTensDict = {1: 'десять', 2: 'двадцать', 3: 'тридцать'}
    if 1 <= dayNumber % 100 <= 20 or dayNumber % 100 == 30:
        return strDayDict[dayNumber % 100]
    else:
        return '{} {}'.format(strTensDict[dayNumber//10], strDayDict[dayNumber % 10])


def getMonthStr(monthNumber):
    monthList = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря', ]
    return monthList[monthNumber - 1]


exitCond = False
while not exitCond:
    someiInput = [x for x in input(
        'Введите дату в формате dd.mm.yyyy и нажмите Enter\n').split('.')]
    if len(someiInput) != 3 or not someiInput[0].isdigit() or not someiInput[1].isdigit() or not someiInput[2].isdigit():
        print('Вы ввели что-то не то, попробуйте еще раз')
        continue
    days = int(someiInput[0])
    month = int(someiInput[1])
    year = int(someiInput[2])
    if days > 31 or days < 1 or month < 1 or month > 12:
        print('Такого числа не существует впринципе, попробуйте еще раз')
        continue
    print('{} {} {} года'.format(getDayString(days), getMonthStr(month), year))
    exitInput = input(
        'Повторить ввод? (Нажмите \'y\' затем Enter (при нажатии на любую другую клавишу и Enter программа завершится) \n')
    if exitInput != 'y':
        exitCond = True
