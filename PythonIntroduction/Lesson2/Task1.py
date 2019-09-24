import random

someList1 = [x + int(random.uniform(1, 5)) for x in range(0,
                                                          int(random.uniform(10, 50)), int(random.uniform(1, 4)))]
someList2 = [x + int(random.uniform(1, 5)) for x in range(0,
                                                          int(random.uniform(10, 50)), int(random.uniform(1, 4)))]

print(someList1)
print(someList2)
someList1 = [x for x in someList1 if x not in someList2]
print(someList1)
