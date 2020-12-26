import re

with open("index.html") as f:
    s = f.read()

li = re.findall("<a class=\"home-link home-link_black_yes\" aria-label=\"([^\"]+)\" href=", s)

print(li)
