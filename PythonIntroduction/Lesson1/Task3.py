def checkState(age, weight):
    if age < 30 and weight > 50 and weight < 120:
        return 'хорошее состояние'
    elif weight < 50 or weight > 120:
        if age > 40:
            return 'следует обратиться к врачу'
        elif age > 30:
            return 'следует заняться собой'
    return 'пациент либо здоров полностью, либо слишком поздно'


def getStringWithEndDefByAge(age):
    num = age % 100
    if num > 10 and num < 21:
        return 'лет'
    else:
        num = age % 10
        if num == 1:
            return 'год'
        elif num > 1 and num < 5:
            return 'года'
        else:
            return 'лет'


name, surname, age, weight = (x for x in input(
    'Введите ваше имя, фамилию возраст и вес через символ ; без пробелов и нажмите Enter\n').split(';'))
age = int(age)
weight = int(weight)

print('{} {}, {} {}, вес {} - {}'.format(name, surname, age,
                                         getStringWithEndDefByAge(age), weight, checkState(age, weight)))
