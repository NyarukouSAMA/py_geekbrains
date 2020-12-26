# Создать модуль music_deserialize.py.
# В этом модуле открыть файлы group.json и group.pickle, прочитать из них информацию.
# И получить объект: словарь из предыдущего задания.

def deSerializeWithPickle() :
    dictionary = None
    import pickle

    with open('group.pickle', 'rb') as pickleFile:
        dictionary = pickle.load(pickleFile)

    return dictionary

def deSerializeWithJson() :
    dictionary = None
    import json

    print (json.dumps(dictionary))
    with open('group.json', 'r', encoding='utf-8') as jsonFile:
        dictionary = json.load(jsonFile)

    return dictionary

if __name__ == '__main__' :
    print(f'Из JSON: {deSerializeWithJson()}')
    print(f'Из Pickle: {deSerializeWithPickle()}')