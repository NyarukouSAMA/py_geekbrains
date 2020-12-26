import os
import shutil


def make_dirs():
    for i in range(1, 10):
        dir = 'dir_%s' % i
        if not os.path.exists(dir):
            os.mkdir('dir_%s' % i)


def del_dirs():
    for i in range(1, 10):
        dir = 'dir_%s' % i
        if os.path.exists(dir):
            shutil.rmtree(dir)


if __name__ == '__main__':
    make_dirs()
    input()
    del_dirs()
