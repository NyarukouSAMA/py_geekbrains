import subprocess as sp


def gesNum():
    sp.call('cls', shell=True)
    input('Здравствуй, давай сыграем в игру! (Нажмите Enter, что бы продолжить)')

    sp.call('cls', shell=True)
    input('''Правила простые, вы загадаете число от 1 до 100, а я буду угадывать!
    Если я ошибусь, нажмите > если число больше, и < если число меньше а затем Enter.
    Если я угадаю, просто нажмите Enter. Вы готовы? (Нажмите Enter, что бы продолжить)''')

    endCond = False
    start = 0
    end = 100

    while not endCond:
        result = (end - start) // 2 + start
        inp = input('Вы загадали {}, я угадал?'.format(result))
        if inp == '>':
            start = result
        elif inp == '<':
            end = result
        else:
            input('Ура! (Нажмите Enter что бы продолжить)')
            endCond = True
