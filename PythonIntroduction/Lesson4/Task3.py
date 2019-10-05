import random


def attack(person1, person2, attackMultiplier=1):
    damageValue = person1.get('damage') * attackMultiplier
    enemyHealth = person2.get('health')
    return enemyHealth - int(damageValue)


player = {
    'health': random.randint(20, 40),
    'damage': random.randint(4, 6)
}

enemy = {
    'health': random.randint(20, 40),
    'damage': random.randint(4, 6)
}

player['name'] = input('Введите свое имя: ')
enemy['name'] = input('Введите имя противника: ')

escCondition = False

print('{} Здоровье: {} Урон: {}'.format(
    player.get('name'), player.get('health'), player.get('damage')))
print('{} Здоровье: {} Урон: {}'.format(
    enemy.get('name'), enemy.get('health'), enemy.get('damage')))
print('Начикаем драку')
while not escCondition:
    input('Брость кубик')
    attackMultiplier = random.randint(1, 6) / 4
    enemy['health'] = attack(player, enemy, attackMultiplier)
    print('{} атакует {}. Урон атакующего: {}. Здоровье атакуемого: {}'.format(
        player.get('name'),
        enemy.get('name'),
        int(player.get('damage') * attackMultiplier),
        enemy.get('health')))
    if(enemy.get('health') <= 0):
        escCondition = True
        print('{} победил!'.format(player.get('name')))
        continue
    player['health'] = attack(enemy, player)
    print('{} атакует {}. Урон атакующего: {}. Здоровье атакуемого: {}'.format(
        enemy.get('name'),
        player.get('name'),
        enemy.get('damage'),
        player.get('health')))
    if(player.get('health') <= 0):
        escCondition = True
        print('Вас убил {}. Вы проиграли!'.format(enemy.get('name')))
        continue
    print('{} Здоровье: {}'.format(
        player.get('name'), player.get('health')))
    print('{} Здоровье: {}'.format(
        enemy.get('name'), enemy.get('health')))
