import pickle
import json

my_favourite_group = [
    {
    'name': 'Г.М.О.',
    'tracks': ['Последний месяц осени', 'Шапито'],
    'Albums': [{'name': 'Делать панк-рок', 'year': 2016},
               {'name': 'Шапито', 'year': 2014}]},
{
    'name': 'КИШ',
    'tracks': ['Смельчак и ветер', 'Камнем по голове'],
    'Albums': [{'name': 'Камнем по голове', 'year': 1996}]
}
]

with open('group.dat', 'wb') as f:
    pickle.dump(my_favourite_group, f)

print('Записан pickle')

with open('group.json', 'w', encoding='utf-8') as f:
    json.dump(my_favourite_group, f)

print('Записан json')
