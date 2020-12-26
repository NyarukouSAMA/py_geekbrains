import re
from bs4 import BeautifulSoup as BS

with open("geekbrains.html", 'r', encoding='utf-8') as f:
    s = f.read()

soup = BS(s, "html.parser")
# print(soup.prettify())
li3 = re.findall("Нас уже \d\s\d+\s\d+ человек", s)
# Прошу сообщить почему ошибка?
li2 = re.findall("<span class=\"total-users\">([^\>]+)</span>", s)

print(li3)
print(li2)
# !!!!!!!!!!!  почему у меня   тег span  выдает другие данные ?
print(soup.span.string)
