name = (input('Введите ваше имя: '))
surname = (input('Введите вашу фамилию: '))
age = int(input('Введите ваш возраст: '))
weight = int(input('Введите ваш вес: '))
if age < 30 and (120 > weight > 50):
    print (name, surname, ',', age, 'год,', 'вес', weight, '- хорошее состояние')
elif age > 30 and (50 > weight > 120):
    print(name, surname, ',', age, 'год,', 'вес', weight, '- следует заняться собой')
elif age > 40 and (50 > weight > 120):
    print(name, surname, ',', age, 'год,', 'вес', weight, '- следует обратиться к врачу')
