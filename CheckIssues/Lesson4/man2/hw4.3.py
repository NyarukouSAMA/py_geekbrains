# Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health = 100,
# damage = 50.
# Поэкспериментируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2).
# Примечание: имена аргументов можете указать свои.
# Функция в качестве аргумента будет принимать атакующего и атакуемого.
# В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
# Функция должна сама работать со словарями и изменять их значения.
import random

def randomVal():
    random.random()
    return random.randint(5, 45)

def setEntity():
    # name = input('Имя персонажа')
    return {'name':input("Имя персонажа: "), 'health':randomVal() + 50, 'damage':randomVal()}

def attack(attacker, defenser):
    defenser['health'] -= attacker['damage']

adolf = setEntity()
print(f"У {adolf['name']} было {adolf['health']} здоровья")

mao = setEntity()
print(f"а у {mao['name']} - палка на {mao['damage']} дамага")

attack(mao, adolf)
print(f"после встречи {adolf['name']} полегчал до {adolf['health']} здоровья")