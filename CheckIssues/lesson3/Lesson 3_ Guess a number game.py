print ("Игра 'Угадай число'")
print ("")
print ("Правила игры:")
print ("Загадайте любое целое число в диапазоне от 1 до 100 включительно, а компьютер попробует его угадать")
print ("")
print ("Начнем? Сначала загадайте число")
print ("")

import random
min = 1
max = 100
user_answer = None

while user_answer !=0:
    guess_number = random.randint(min, max)
    print(f"Вы загадали число {guess_number}? ")
    user_answer = int(input(f"Если я угадал, введите 0. Если загаданное число больше {guess_number} введите 1, меньше - 2. "))
    if user_answer == 1:
        print("Тогда еще одна попытка.")
        min = guess_number + 1
        guess_number = random.randint(min, max)
    elif user_answer == 2:
        print("Тогда еще одна попытка.")
        max = guess_number - 1
        guess_number = random.randint(min, max)

print("Ура! Я угадал")
