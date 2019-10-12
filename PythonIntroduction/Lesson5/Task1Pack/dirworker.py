import os


def createDirs():
    curDirPath = os.getcwd()
    for secondNamePart in range(1, 10):
        dirPathToCreate = os.path.join(
            curDirPath, "dir_{}".format(secondNamePart))
        os.mkdir(dirPathToCreate)


def delDirs():
    curDirPath = os.getcwd()
    for secondNamePart in range(1, 10):
        dirPathToCreate = os.path.join(
            curDirPath, "dir_{}".format(secondNamePart))
        os.rmdir(dirPathToCreate)


if __name__ == "__main__":
    createDirs()
    input("Папки созданы. Удалить папки?")
    delDirs()
