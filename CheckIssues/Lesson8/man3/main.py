import sys
from core import creat_file, create_folder, get_list, delete_file, copy_file, save_info, go_dir

save_info('Start')

command = sys.argv[1]

if command == 'list':
    get_list()

elif command == 'go_dir':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутсвует название папки')
    else:
        go_dir(name)
elif command == 'create_file':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутсвует название файла')
    else:
        creat_file(name)
elif command == 'create_folder':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутсвует название папки')
    else:
        create_folder(name)
elif command == 'delete_file':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутсвует название файла')
    else:
        delete_file(name)
elif command == 'copy_file':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутсвует имя файла для копирования')
    try:
        new_name = sys.argv[3]
    except IndexError:
        print('Отсутсвует название нового файла')
    else:
        copy_file(name, new_name)
elif command == 'help':
    print('create_file')
    print('create_folder')
    print('delete_file')
    print('copy_file')
    print('create_file')
    print('game')

elif command == 'game':
    import random
    random = random.randint(1, 100)
    start = input('загадайте число от 1 до 100 и нажмите Ввод:')
    print('Если загаданное число больше, введите ">"')
    print('Если загаданное число меньше, введите "<"')
    print('Если число угадано, введите "="')
    print(random)
    val = None
    left = int(1)
    right = int(100)
    while val != "=":
        val = input(' ')
        if val == "<":
            right = random
            random = (right - left) // 2 + left
            print(random)
        else:
            left = random
            random = (right - left) // 2 + left
            print(random)
    print("Win!!!")

save_info('Finish')
