list_1 = [1, 3, 5, 7, 9, 0, 8, 6, 4, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_2 = []
for number in list_1:
    if list_1.count(number) == 1:
        list_2.append(number)
print(list_2)
