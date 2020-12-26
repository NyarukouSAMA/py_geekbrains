number = int(input("Введите число от 0 до 10 "))

while 0 >= number or number >= 10:
    print ("Неверный диапазон")
    number = int(input("Введите число от 0 до 10 "))

print ("Ваше число в 2 степени = ", number**2)
