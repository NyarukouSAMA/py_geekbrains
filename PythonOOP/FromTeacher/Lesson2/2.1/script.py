import re

with open("index.html") as f:
    s = f.read()

li = re.findall("([0-9\-\+]+) °C", s)

print(li)