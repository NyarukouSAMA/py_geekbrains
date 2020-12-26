import re
from bs4 import BeautifulSoup as BS

print("Задание №1")

with open("index.html", "r", encoding="utf-8") as f:
    s = f.read()

comments = re.compile("<!--.*?-->", re.DOTALL)
scripts = re.compile("<script.*?</script>", re.DOTALL)
tags = re.compile("<[^<]*>")

s = comments.sub("", s)
s = scripts.sub("", s)
s = tags.sub("", s)

s = re.sub("[ ]+", " ", s)
s = re.sub("\s{2,}", "\n", s)
s = re.findall("[0-9]+\s*[0-9]+\s*[0-9]+\s*человек", s)

print(s)


print("Задание №2")

with open("index.html", "r", encoding="utf-8") as f:
    li = f.read()

soup = BS(li, "html.parser")

print(soup.find('span', 'total-users').text)

