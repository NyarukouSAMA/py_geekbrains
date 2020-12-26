import os

def new_dirs ():
    for i in range (1, 10):
        new_path = os.path.join (os.getcwd(), 'dir_{}'.format (i))
        os.mkdir (new_path)

# следующая функция удалит созданные папки
def remove_dirs ():
    for i in range (1, 10):
        path = os.path.join (os.getcwd(), 'dir_{}'.format (i))
        os.rmdir (path)

new_dirs ()
remove_dirs()
