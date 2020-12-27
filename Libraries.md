# Frequently used libraries

## import re (standard)

<code>re.findall(patternString, text)</code> - find all income pattern-string in text.

Pattern symbols:
- **.** - point means any symbol
- \d - number
- \D - not a number
- \s - whitespace
- \S - not whitespace
- \w - letter, number, _
- \W - not \w

Another things:
- \+ - 1 and more times quantificator
- \* - 0 and more times quantificator
- ? - 0 or 1 time quantificator
- () - round brackets uses to designate group of symbols; if used in search, then regex returns only symbols inside the group


<code>re.sub(patternString, replaceString, text)</code> - replace all income **patternString** in text to **replaceString**

<code>pattern = re.compile(patternString)</code> - returns pattern object. Needed for using library re in OOP-style. Includes different methods for work with text. For example: <code>pattern.findall(text)</code>

<code>re.search(patternString, text)</code> - returns first income of **patternString** in **text**. Returns object that include information about first and last index of found income (and a little bit more information)

<code>re.match(patternString, text)</code> - finds patternString income into text starting from first symbol; returns indexes of first and last occurrence. If not finds, return **None**.

<code>re.split(patternString, text)</code> - returns list from text, where patternString used as delimiter.

## import bs (pip install beautifulsoup4)

It's very convenient libraries. It helps to find patternString incomes into html and xml texts.

<code>from bs4 import BeautifulSoup as BS</code> - that's the way we are working with bs4, importing this class and then creating object of this class: <code>soup = BS(s, 'html.parser')</code> - where **s** it is some string contains html-text and **'html.parser'** - indicator of filetype. For example in this example we use **'html.parser'** because text in **s** variable of type html.

<code>soup.prettify()</code> - returns formatted html(xml)-text

<code>soup.get_text()</code> - returns text without tags and comments

<code>soup.title</code> - get title of the page

<code>soup.div</code> - get first **div** occurrence in text

<code>soup.div["class"]</code> - returns attribute of searched tag

<code>soup.find_all('div')</code> - returns list of all searched tag occurrence in text (for example **div** like in example), each tag is something similar to the dictionary. It contains different attributes and other specific information. 

<code>someTag.get("someAttribute", "DefaultValue")</code> - this code returns value of **someAttribute**, if tag not include such attribute, then it returns **DefaultValue**

## import requests (pip install requests)

This library is used to send requests to servers and get responses from them.

<code>response = requests.get('url')</code> - this code returns response object of get request from server. It contains <code>response.code</code> that indicates code of response. Although it contains <code>response.text</code> property, that includes text of server response.