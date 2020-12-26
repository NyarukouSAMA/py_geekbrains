import random
def list():
    list = [1,5,3,7]
    if not len(list):
        return (None)
    else:
        return random.choice (list)
print(list())