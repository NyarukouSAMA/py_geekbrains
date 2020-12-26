import re
from bs4 import BeautifulSoup as BS

# TAsk1
with open('resources\index.html', encoding='utf_8') as f:
    s = f.read()

comments = re.compile("<!--.*?-->", re.DOTALL)
scripts = re.compile("<script.*?</script>", re.DOTALL)
tags = re.compile("<[^<]*>")

s = comments.sub("", s)
s = scripts.sub("", s)
s = tags.sub("", s)

li = re.findall("Нас уже [\d\s]{1,} человек", s)
print(li[0])
input()

# Task2
with open('resources\index.html', encoding='utf_8') as f:
    s = f.read()

soup = BS(s, "html.parser")

li = soup.find_all("span")

total = list(
    filter(lambda elem: "total-users" in elem.get("class", ""), li))[0].string

print(total)
