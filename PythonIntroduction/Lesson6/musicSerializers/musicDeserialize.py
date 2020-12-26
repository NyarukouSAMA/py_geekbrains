import os.path
import pickle
import json


def getFromPickle(filename):
    filename += ".pickle"
    with open(filename, 'rb') as f:
        return pickle.load(f)


def getFromJson(filename):
    filename += ".json"
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)


if __name__ == "__main__":
    print(getFromPickle('./resources/group'))
    print(getFromJson('./resources/group'))
