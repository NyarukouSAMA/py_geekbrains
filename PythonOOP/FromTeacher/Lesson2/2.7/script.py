import re
from bs4 import BeautifulSoup as BS

with open("index.html", encoding='utf-8') as f:
    s = f.read()

soup = BS(s, "html.parser")

link_example = """ <a href="LINK">CONTENT</a> """

li = soup.find_all("a")
for n in li:
    print(type(n))
    print(n.get("href", ""))
