def max_number():
    numbers = []

    for i in range (3):
        number = int(input("Введите число: "))
        numbers.append(number)
    print (max(numbers))

max_number()