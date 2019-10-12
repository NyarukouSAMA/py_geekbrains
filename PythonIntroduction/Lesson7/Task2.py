import random


def taskCondition(num):
    return num % 3 == 0 and num > 0 and num % 4 != 0


numericList = [random.randint(-50, 50) for i in range(random.randint(15, 25))]
print('Исходный список: {}\nФильтрованный список: {}'
      .format(numericList, [num for num in numericList if taskCondition(num)]))
