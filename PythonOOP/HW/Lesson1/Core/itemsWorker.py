import os
import shutil
import datetime
import re


def createFile(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def createFolder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая папка уже есть')


def getList(foldersOnly=False):
    print([f for f in os.listdir() if os.path.isdir(f)]
          if foldersOnly else os.listdir())


def deleteItem(name):
    os.rmdir(name) if os.path.isdir(name) else os.remove(name)


def copyItem(name, new_name):
    try:
        shutil.copytree(name, new_name) if os.path.isdir(
            name) else shutil.copy(name, new_name)
    except FileExistsError:
        print('Такая папка уже есть')


def currentDir():
    print(os.getcwd())


def dirBuild(name, rwd, endWithFile=False):
    if '\\\\' in name or '//' in name or ('\\' in name and '/' in name):
        print('В имени пути не может быть сдвоенных слэшей, обратных сдвоенных слэшей и разых слэшей')
        saveInfo(
            'В имени пути не может быть сдвоенных слэшей и обратных сдвоенных слэшей и разых слэшей', rwd)
        return
    pathList = name.split('\\')
    if(len(pathList) == 1):
        pathList = name.split('/')

    if pathList.count('.') > 1 or pathList.count('.') == 1 and pathList.index('.') > 0:
        print('''Если используется относительный путь, то он должен начинаться с символа 1 точки.
Символ одной точки не может быть где-то по серединке''')
        saveInfo('Проблема с точками', rwd)
        return

    newPath = ''
    if pathList[0] == '.' or pathList[0] == '..':
        newPath = os.getcwd()
    if re.match(r'\w:', pathList[0]):
        newPath = f'{pathList[0]}\\'
    if not os.path.exists(newPath) or not os.path.isdir(newPath):
        saveInfo('Такого пути не существует', rwd)
        print('Такого пути не существует')
        return
    if len(pathList) > 1:
        pathList = pathList[1:]
        for i in range(len(pathList)):
            if pathList[i] == '.':
                newPath = newPath
            elif pathList[i] == '..':
                newPath = os.path.split(newPath)[0]
            else:
                newPath = os.path.join(newPath, pathList[i])

            if os.path.exists(newPath) and os.path.isdir(newPath):
                continue
            elif endWithFile and os.path.isfile(newPath) and i == len(pathList) - 1:
                newPath = os.path.split(newPath)[0]
                break
            else:
                saveInfo('Такого пути не существует', rwd)
                print('Такого пути не существует')
                return
    return newPath


def setCurrentWorkingDir(name, workingDir):
    newPath = dirBuild(name, workingDir)
    os.chdir(workingDir)
    if newPath == None:
        return
    with open('currentDir.txt', 'w', encoding='utf=8') as f:
        f.write(newPath)


def getCurrentWorkingDir():
    try:
        if os.path.exists(os.path.join(os.getcwd(), 'currentDir.txt')):
            with open('currentDir.txt', 'r', encoding='utf-8') as f:
                os.chdir(f.readline())
    except:
        print('В механизме директорий что-то сломалось, удалите файл currentDir')


def saveInfo(message, initDir):
    curDir = os.getcwd()
    os.chdir(initDir)
    curTime = datetime.datetime.now()
    result = f'{curTime} - {message}\n'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result)
    os.chdir(curDir)


def printHelp():
    print(
        'list - список файлов и папок; [foldersOnly] = 1 OR 0 - отобразить все содержимое или только список папок')
    print('createFile - создание файла; name - имя файла')
    print('createFolder - создание папки; name - имя папки')
    print('delete - удаление файла или папки; name - имя объекта')
    print('copy - копирование; name - имя истоника; newName - имя приемника')
    print('currentDir - попказать текущую рабочую директорию')
    print('cd - смена директории; второй аргумент - путь, либо относительный, либо абсолютный')
    print('playgame - поиграть; доп аргумент 1 - это угадывание числа; 2 - это рпг')


if __name__ == "__main__":
    res = re.match(r'\w\:', 'Lf\\')
    print(res)
