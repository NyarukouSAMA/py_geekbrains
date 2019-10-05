import random


def getDemage(damage, armor):
    return damage/armor


def attack(person1, person2, attackMultiplier=1):
    damageValue = getDemage(person1.get('damage') *
                            attackMultiplier, person2.get('armor'))
    enemyHealth = person2.get('health')
    return enemyHealth - int(damageValue)


player = {
    'health': random.randint(20, 40),
    'damage': random.randint(4, 6),
    'armor': random.randint(3, 6) / 4
}

enemy = {
    'health': random.randint(20, 40),
    'damage': random.randint(4, 6),
    'armor': random.randint(1, 4) / 4
}

player['name'] = input('Введите свое имя: ')
enemy['name'] = input('Введите имя противника: ')

escCondition = False

print('{} Здоровье: {} Урон: {} Броня: {}'.format(
    player.get('name'), player.get('health'), player.get('damage'), player.get('armor')))
print('{} Здоровье: {} Урон: {} Броня: {}'.format(
    enemy.get('name'), enemy.get('health'), enemy.get('damage'), enemy.get('armor')))
print('Начикаем драку')
while not escCondition:
    input('Брость кубик')
    attackMultiplier = random.randint(1, 6) / 4
    enemy['health'] = attack(player, enemy, attackMultiplier)
    print('{} атакует {}. Урон атакующего: {}. Здоровье атакуемого: {}'.format(
        player.get('name'),
        enemy.get('name'),
        int(getDemage(player.get('damage') * attackMultiplier, enemy.get('armor'))),
        enemy.get('health')))
    if(enemy.get('health') <= 0):
        escCondition = True
        print('{} победил!'.format(player.get('name')))
        continue
    player['health'] = attack(enemy, player)
    print('{} атакует {}. Урон атакующего: {}. Здоровье атакуемого: {}'.format(
        enemy.get('name'),
        player.get('name'),
        int(getDemage(enemy.get('damage'), player.get('armor'))),
        player.get('health')))
    if(player.get('health') <= 0):
        escCondition = True
        print('Вас убил {}. Вы проиграли!'.format(enemy.get('name')))
        continue
    print('{} Здоровье: {}'.format(
        player.get('name'), player.get('health')))
    print('{} Здоровье: {}'.format(
        enemy.get('name'), enemy.get('health')))
