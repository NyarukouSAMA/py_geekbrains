import random
random = random.randint(1,100)
start = input('загадайте число от 1 до 100 и нажмите Ввод:')
print('Если загаданное число больше, введите ">"')
print('Если загаданное число меньше, введите "<"')
print('Если число угадано, введите "="')
print(random)
val = None
left = int(1)
right = int(100)
while val != "=":
    val = input(' ')
    if val == "<":
        right = random
        random = (right - left)//2 + left
        print(random)
    else:
        left = random
        random = (right - left)//2 + left
        print(random)
print("Win!!!")


