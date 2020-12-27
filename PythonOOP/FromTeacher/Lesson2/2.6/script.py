import re
from bs4 import BeautifulSoup as BS

with open("index.html", encoding='utf8') as f:
    s = f.read()

soup = BS(s, "html.parser")
print(soup.prettify())

print(soup.get_text())

def old_foo():
    global s
    comments = re.compile("<!--.*?-->", re.DOTALL)
    scripts = re.compile("<script.*?</script>", re.DOTALL)
    tags = re.compile("<[^<]*>")

    s = comments.sub("", s)
    s = scripts.sub("", s)
    s = tags.sub("", s)

    s = re.sub("[ ]+", " ", s)
    s = re.sub("\s{2,}", "\n", s)

    print(s)
