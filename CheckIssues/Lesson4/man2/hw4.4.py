#Давайте усложним предыдущее задание. Измените сущности,
# добавив новый параметр - armor = 1.2 (величина брони персонажа)
#Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
#Следовательно, у вас должно быть 2 функции:
#Наносит урон. Это улучшенная версия функции из задачи 3.
#Вычисляет урон по отношению к броне.
#Примечание. Функция номер 2 используется внутри функции номер 1
# для вычисления урона и вычитания его из здоровья персонажа.

import random

def randomVal():
    random.random()
    return random.randint(5, 45)

def setEntity():
    return {'name':input("Имя персонажа: "), 'health':randomVal() + 50, 'damage':randomVal(), 'armor':1.2}

def getDamage(damage, armor):
    return int(damage / armor)

def attack(attacker, defenser):
    defenser['health'] -= getDamage(attacker['damage'], defenser['armor'])

adolf = setEntity()
print(f"У {adolf['name']} было {adolf['health']} здоровья")

mao = setEntity()
print(f"а у {mao['name']} - палка на {mao['damage']} дамага")

attack(mao, adolf)
print(f"после встречи {adolf['name']} полегчал до {adolf['health']} здоровья")