# 1: Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py).
# В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой запущен данный код.
# Затем создайте вторую функцию удаляющую эти папки. Проверьте работу функций в этом же модуле.

import os, sys
name = 'dir'

def create_dir():
    for i in range(1,10):
        new_path = os.path.join(os.getcwd(), '{}_{}'.format(name, i))
        os.mkdir(new_path)

create_dir()

def delete_dir():
    for m in range(1,10):
        new_path = os.path.join(os.getcwd(), '{}_{}'.format(name, m))
        os.rmdir(new_path)

delete_dir()

# 2: Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент.
# Если список пустой функция должна вернуть None. Проверьте работу функций в этом же модуле.

import random
random_list = [1, 2, 3, 4]
random_none = []

def rand_element(x):
    if x == []:
        print(None)
    else: print(random.choice(x))

rand_element(random_list)
rand_element(random_none)
