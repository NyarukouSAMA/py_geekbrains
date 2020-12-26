import random
def get_rand_el(li: list):
    if not li:
        return
    x = random.randrange(0, len(li))
    return li[x]
if __name__ == '__main__':
    li = [1, 2, 3, 4]
    print(get_rand_el(li))