import sys
from game import game
from core import create_file, create_folder, get_list, delete_file, save_info, copy_file, chdir

save_info('Старт')
command = None

try:
    command = sys.argv[1]
except IndexError:
    print('Все в порядке')

if command == 'list':
        get_list()
elif command == 'create_file':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует название файла')
    else:
        create_file(name)
elif command == 'create':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует название файла')
    else:
        create_folder(name)
elif command == 'delete':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует название файла')
    else:
        delete_file(name)
elif command == 'copy':
    try:
        name = sys.argv[2]
        new_name = sys.argv[3]
    except IndexError:
        print('Недостает данных о файле')
    else:
        copy_file(name, new_name)
elif command == 'chdir':
    try:
        path = sys.argv[2]
    except IndexError:
        print('Введите путь к директории')
    else:
        chdir(path)
elif command == 'help':
    print('list - список файлов и папок')
    print('create_file - создание файла')
    print('create_folder - создание папки')
    print('delete - удаление файла или папки')
    print('copy - копирование файла или папки')
    print('dir - смена текущей директории')
elif command == 'game':
    game()


save_info('Конец')

