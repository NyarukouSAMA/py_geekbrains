Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 23 2015, 02:52:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
>>> text
'\n    Привет! Отправь, пожалуйста, письмо\n    нашим коллегам: vladamir@v.ru, vladimir2@v.ru;\n    про Оксану и Ольгу не забудь: oksana@v.ru,olga@v.ru\n\n    отошли копию партнерам: adidas@das.ru &nike@ne.ki\n\n    спасибо! @@твой босс\n'
>>> li = text.split()
>>> li
['Привет!', 'Отправь,', 'пожалуйста,', 'письмо', 'нашим', 'коллегам:', 'vladamir@v.ru,', 'vladimir2@v.ru;', 'про', 'Оксану', 'и', 'Ольгу', 'не', 'забудь:', 'oksana@v.ru,olga@v.ru', 'отошли', 'копию', 'партнерам:', 'adidas@das.ru', '&nike@ne.ki', 'спасибо!', '@@твой', 'босс']
>>> li = [n for n in li if "@" in n]
>>> li
['vladamir@v.ru,', 'vladimir2@v.ru;', 'oksana@v.ru,olga@v.ru', 'adidas@das.ru', '&nike@ne.ki', '@@твой']
>>> ================================ RESTART ================================
>>> 
>>> re.findall("vlad.mir", text)
['vladamir', 'vladimir']
>>> re.findall("\w+", text)
['Привет', 'Отправь', 'пожалуйста', 'письмо', 'нашим', 'коллегам', 'vladamir', 'v', 'ru', 'vladimir2', 'v', 'ru', 'про', 'Оксану', 'и', 'Ольгу', 'не', 'забудь', 'oksana', 'v', 'ru', 'olga', 'v', 'ru', 'отошли', 'копию', 'партнерам', 'adidas', 'das', 'ru', 'nike', 'ne', 'ki', 'спасибо', 'твой', 'босс']
>>> re.findall("\w+@\w+\.\w+", text)
['vladamir@v.ru', 'vladimir2@v.ru', 'oksana@v.ru', 'olga@v.ru', 'adidas@das.ru', 'nike@ne.ki']
>>> li = re.findall("\w+@\w+\.\w+", text)
>>> li
['vladamir@v.ru', 'vladimir2@v.ru', 'oksana@v.ru', 'olga@v.ru', 'adidas@das.ru', 'nike@ne.ki']
>>> 
