import re

text1 = """Франция одержала победу над хорватами в финале чемпионата мира по футболу 2018 года и стала победителем турнира. Об этом сообщает корреспондент «Ленты.ру» (Россия).Матч состоялся на стадионе «Лужники» и завершился со счетом 4:2. Опять французы вышли вперед на 18-й минуте благодаря автоголу нападающего соперника Марио Манджукича. На 28-й минуте полузащитник хорватов Иван Перишич сравнял счет. На 38-й минуте в ворота Хорватии был назначен пенальти, который реализовал форвард Антуан Гризманн.Во втором тайме преимущество сборной Франции увеличили хавбек Поль Погба (59-я минута) и нападающий Килиан Мбаппе (65-я минута). На 69-й минуте Манджукич сократил отставание сборной Хорватии.Сборная Франции во второй раз выиграла мундиаль. До этого команда побеждала на турнире 1998 года во Франции."""
text2 = """На 6-й минуте «шашечные» отметились подобным наступлением. Ребич избавился от опеки Кудряшова на правом фланге и выполнил хороший прострел, который успешно прервал Акинфеев.На 16-й минуте хорваты заработали многообещающий штрафной. Данный стандарт решил исполнить Ракитич и пробил над перекладиной.Гости же на 28-й минуте всё-таки проникли внутрь штрафной площади россиян, после чего Перишич пробил головой метров с двенадцати, но в створ не попал."""
text3 = """Эден на 15-й минуте откатил Витселю, который издали пробил с рикошетом. Потом перевод Эдена скинул в центр штрафной Менье – Лукаку не обратил внимания на двух японцев и пробил с разворота на угловой. Дожимать бельгийцы не стали – чуть ослабили хватку после отрезка давления. Втихаря Лукаку на 20-й минуте подкрался к штрафной, получил там мяч и пробил со второго касания. Нагатомо успел блокировать."""


pattern1 = "Франци."
pattern2 = "Россия"






