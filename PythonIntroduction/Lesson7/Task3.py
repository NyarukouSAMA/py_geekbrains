import copy
import random
import math


def getRandomElement(demantion):
    if demantion == 0:
        return random.randint(-100, 100)
    else:
        return [getRandomElement(innerDemantion) for innerDemantion
                in [random.randint(0, demantion - 1) for i in range(random.randint(1, 10))]]


def generateListByDemantionNumber(demantionNum):
    if demantionNum <= 0:
        raise Exception(
            'Число измерений в данном пространстве должно принадлежать множеству натуральных без нуля')
    return [getRandomElement(demantion) for demantion in [random.randint(0, demantionNum - 1) for i in range(random.randint(15, 25))]]


def generateSqrtList(structure):
    newStructure = copy.deepcopy(structure)
    return [generateSqrtList(element) if type(element) == list else math.sqrt(
        element) if element > 0 else element for element in newStructure]


superStructure = generateListByDemantionNumber(
    int(input('Введите число измерений (настоятельно не рекомендую цифру больше 6) и нажмите Enter: ')))
print('\nСтруктура после извлечения корней на положительных числах:\n{}\n'.format(
    generateSqrtList(superStructure)))
print('Исходная структура:\n{}'.format(superStructure))
