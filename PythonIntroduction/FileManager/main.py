import sys
import os
from Core import itemsWorker
from Core.safeCast import safeCast
from Games.gessNum import gesNum
from Games.RPG import rpg

rwd = itemsWorker.dirBuild((sys.argv[0]), os.getcwd(), True)
os.chdir(rwd)

itemsWorker.saveInfo('Старт', rwd)

if len(sys.argv) >= 2:
    command = sys.argv[1]
else:
    command = ''

itemsWorker.getCurrentWorkingDir()

if command == 'list':
    if len(sys.argv) == 3 and safeCast(sys.argv[2], int) != None:
        itemsWorker.getList(safeCast(sys.argv[2], int))
    elif len(sys.argv) > 3 or len(sys.argv) == 3 and safeCast(sys.argv[2], int) == None:
        print('Часть аргументов при запросе списка файлов была введена неправильно')
        itemsWorker.saveInfo(
            'Часть аргументов при запросе списка файлов была введена неправильно', rwd)
        itemsWorker.getList()
    else:
        itemsWorker.getList()
elif command == 'createFile':
    if len(sys.argv) == 3 and safeCast(sys.argv[2], str) != None:
        name = sys.argv[2]
        itemsWorker.createFile(name)
    else:
        itemsWorker.saveInfo(f'Комманда {command} введена неверно', rwd)
        print('Комманда введена неверно')
        itemsWorker.printHelp()
elif command == 'createFolder':
    if len(sys.argv) == 3 and safeCast(sys.argv[2], str) != None:
        name = sys.argv[2]
        itemsWorker.createFolder(name)
    else:
        itemsWorker.saveInfo(f'Комманда {command} введена неверно', rwd)
        print('Комманда введена неверно')
        itemsWorker.printHelp()
elif command == 'copy':
    if len(sys.argv) == 3 and safeCast(sys.argv[2], str) != None and safeCast(sys.argv[3], str) != None:
        name = sys.argv[2]
        new_name = sys.argv[3]
        itemsWorker.copyItem(name, new_name)
    else:
        itemsWorker.saveInfo(f'Комманда {command} введена неверно', rwd)
        print('Комманда введена неверно')
        itemsWorker.printHelp()
elif command == 'delete':
    if len(sys.argv) == 3 and safeCast(sys.argv[2], str) != None:
        name = sys.argv[2]
        itemsWorker.deleteItem(name)
    else:
        itemsWorker.saveInfo(f'Комманда {command} введена неверно', rwd)
        print('Комманда введена неверно')
        itemsWorker.printHelp()
elif command == 'currentDir':
    itemsWorker.currentDir()
elif command == 'cd':
    if len(sys.argv) == 3 and safeCast(sys.argv[2], str) != None:
        name = sys.argv[2]
        itemsWorker.setCurrentWorkingDir(name, rwd)
    else:
        itemsWorker.saveInfo(f'Комманда {command} введена неверно', rwd)
        print('Комманда введена неверно')
        itemsWorker.printHelp()
elif command == 'play':
    if len(sys.argv) == 3 and safeCast(sys.argv[2], int) != None:
        whatToPlay = safeCast(sys.argv[2], int)
        if whatToPlay == 1:
            gesNum()
        elif whatToPlay == 2:
            rpg()
        else:
            itemsWorker.saveInfo(f'Комманда {command} введена неверно', rwd)
            print(
                'Комманда введена неверно, в качестве второго аргумента должно быть 1 или 2')
    else:
        itemsWorker.saveInfo(f'Комманда {command} введена неверно', rwd)
        print('Комманда введена неверно')
        itemsWorker.printHelp()
else:
    itemsWorker.printHelp()

itemsWorker.saveInfo('Финиш', rwd)
