name_player = input("Введите имя вашего персонажа: ")
name_enemy= input("Введите имя вашего противника: ")

import random

player = {"name" : name_player, "health" : random.randint(50, 100), "damage" : random.randint(10, 100), "armor" : random.randint(0, 5)}
enemy = {"name" : name_enemy, "health" : random.randint(50, 100), "damage" : random.randint(10, 100), "armor" : random.randint(0, 5)}

print ("Ваш персонаж: ", player)
print ("Ваш противник: ",enemy)

def attack (attacking, defending):
    print ("Атака началась")
    print("Атакует: ", attacking ["name"])
    print("Защищается: ", defending ["name"])
    def real_damage():
        return attacking ["damage"] / defending ["armor"]

    print("Нанесенный урон: ", real_damage())
    defending ["health"] = defending ["health"] - real_damage()
    print ("Результат атаки:")
    print(player)
    print(enemy)

player_decision = None
computer_decision = None
if_battle = None

while if_battle != 0:
    player_decision = int(input("Хотите атаковать? 0 - нет, 1 - да: "))
    computer_decision = random.randint(0, 1)
    if_battle = player_decision + computer_decision

    if player_decision == 1:
        print("Вы атакуете!")
        attack(player, enemy)

    if computer_decision == 1:
        print("Вас атакуют!")
        attack(enemy, player)

print("Битва завершена")





