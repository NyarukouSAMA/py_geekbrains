import random


def getRndFromList(items):
    if type(items) is not list or len(items) == 0:
        return None
    return random.choice(items)


if __name__ == "__main__":
    someList = [1, 2, 3, 4]
    print(getRndFromList(someList))
