import re

text = """
Франция одержала победу над хорватами в финале чемпионата мира по футболу 2018 года и стала победителем турнира. Об этом сообщает корреспондент «Ленты.ру».
Матч состоялся на стадионе «Лужники» и завершился со счетом 4:2. Опять французы вышли вперед на 18-й минуте благодаря автоголу нападающего соперника Марио Манджукича. На 28-й минуте полузащитник хорватов Иван Перишич сравнял счет. На 38-й минуте в ворота Хорватии был назначен пенальти, который реализовал форвард Антуан Гризманн.
Во втором тайме преимущество сборной Франции увеличили хавбек Поль Погба (59-я минута) и нападающий Килиан Мбаппе (65-я минута). На 69-й минуте Манджукич сократил отставание сборной Хорватии.
Сборная Франции во второй раз выиграла мундиаль. До этого команда побеждала на турнире 1998 года во Франции.
"""

text = re.sub("[Фф]ранцузы", "Россияне", text)
text = re.sub("Франц", "Росс", text)

#text = re.sub("\d+", "число", text)
text = re.sub("\d{1,2}\-[йя]", "n", text)

print(text)




