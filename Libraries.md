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

<code>re.search(patternString, text)</code> - returns first income of **patternString** in **text**. Returns object that include information about furst and last index of found income (and a little bit more information)

<code>re.match(patternString, text)</code> - finds patternString income into text starting from first symbol; returns indexes of first and last occurance. If not finds, return **None**.

<code>re.split(patternString, text)</code> - returns list from text, where patternString used as delimiter.

## import bs (pip install beautifulsoup4)

