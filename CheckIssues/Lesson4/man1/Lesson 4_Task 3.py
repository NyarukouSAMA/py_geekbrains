name_player = input("Введите имя вашего персонажа: ")
name_enemy= input("Введите имя вашего противника: ")

player = {"name" : name_player, "health" : 100, "damage" : 50}
enemy = {"name" : name_enemy, "health" : 50, "damage" : 25}

print (player)
print (enemy)

def attack (attacking, defending):
    defending ["health"] = defending ["health"] - attacking ["damage"]
    print ("Результат атаки:")
    print(player)
    print(enemy)

attack(player, enemy)