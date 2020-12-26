import os
import json
import pickle


def getJson(item):
    return json.dumps(item, ensure_ascii=False)


def getPickle(item):
    return pickle.dumps(item)


def createJsonFile(item, filename):
    if type(filename) != str:
        return (False, 'Имя файла должно быть строкой')
    filename += ".json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(item, f)
    return (True, 'Файл сохранен в формате json')


def createPickleFile(item, filename):
    if type(filename) != str:
        return (False, 'Имя файла должно быть строкой')
    filename += ".pickle"
    with open(filename, 'wb') as f:
        pickle.dump(item, f)
    return (True, 'Файл сохранен в формате pickle')


if __name__ == "__main__":
    print(os.getcwd())
    myFavouriteGroup = \
        {'name': 'Г.М.О.',
         'tracks': ['Последний месяц осени', 'Шапито'],
         'Albums': [{'name': 'Делать панк-рок', 'year': 2016},
                    {'name': 'Шапито', 'year': 2014}]}
    jsonString = getJson(myFavouriteGroup)
    print(type(jsonString))
    print(jsonString)
    pickledObject = getPickle(myFavouriteGroup)
    print(type(pickledObject))
    print(pickledObject)
    createJsonFile(myFavouriteGroup, './PythonIntroduction/resources/group')
    createPickleFile(myFavouriteGroup, './PythonIntroduction/resources/group')
