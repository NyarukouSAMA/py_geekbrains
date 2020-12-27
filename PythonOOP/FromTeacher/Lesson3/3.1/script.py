import requests
import re

req = requests.get("https://yandex.ru")
s = req.text

li = re.findall("([0-9\-\+]+) °C", s)

print(li)
