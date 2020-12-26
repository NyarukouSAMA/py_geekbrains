print("Медицинская анкета")
name = input("Введите ваши имя и фамилию ")
age = int(input("Введите ваш возраст "))
weight = int(input("Введите ваш вес "))

if age < 30 and 50 < weight < 120:
    print(name, "возраст", age, "вес", weight, " - хорошее состояние")

elif 40 > age > 30 and (50 > weight or weight > 120):
    print(name, "возраст", age, "вес", weight, " - следует заняться собой")

elif age > 40 and (50 > weight or weight > 120):
    print(name, "возраст", age, "вес", weight, " - следует обратится к врачу!")

else:
    print(name, "возраст", age, "вес", weight,
          " - требуется уточнить дополнительные параметры")
