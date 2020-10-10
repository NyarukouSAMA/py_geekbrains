import requests
import re

req = requests.get("https://yandex.ru")
text = req.text

li = re.findall(
    "<a class=\"home-link home-link_black_yes\" aria-label=\"([^\"]+)\" href=", text)

print(li)
input()
