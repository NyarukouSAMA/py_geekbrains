# Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы, например:
# С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал.
# Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.

my_favourite_group = {
    'name': 'Г.М.О.',
    'tracks': ['Последний месяц осени', 'Шапито'],
    'Albums': [{'name': 'Делать панк-рок','year': 2016},
               {'name': 'Шапито','year': 2014}]}

def serializeWithPickle(dictionary) :
    import pickle

    print (pickle.dumps(dictionary))

    with open('group.pickle', 'wb') as pickleFile:
        pickle.dump(dictionary, pickleFile)

    print('done')

def serializeWithJson(dictionary) :
    import json

    print (json.dumps(dictionary))
    with open('group.json', 'w', encoding='utf-8') as jsonFile:
        json.dump(dictionary, jsonFile)

    print('done')

if __name__ == '__main__' :
    print('Преобразование в JSON')
    serializeWithJson(my_favourite_group)
    print('Преобразование в Pickle')
    serializeWithPickle(my_favourite_group)