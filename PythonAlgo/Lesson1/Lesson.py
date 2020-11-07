# Task 2
num = input("Введите 3-значное число: ")
num = int(num)
a = num // 100
b = num % 100 // 10
c = num % 10
summa = a + b + c
mult = a * b * c
print(f'Сумма = {summa}, Произведение = {mult}')
