# from FileManager.Core.itemsWorker import dirBuild
import re
import sys
import os
from Core.itemsWorker import dirBuild

rwd = dirBuild((sys.argv[0]), os.getcwd(), True)
os.chdir(rwd)

# Task1

text = ''

with open('someText.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Task2

pattern = r'[\.\!\?]\s'
l1 = re.split(pattern, text)

# Task3

pattern = r'\w{4,}'
li2 = re.findall(pattern, text)
wordSet = {(item, li2.count(item)) for item in li2}
wordSet = sorted(wordSet, key=lambda wordTuple: wordTuple[1], reverse=True)

print([wordSet[i] for i in range(10)])

# Task4
pattern = r'(\w+\.(mail\.ru|ru|com)(/\w+)?)'
pat = re.compile(pattern)
li3 = [elem[0] for elem in pat.findall(text)]
print(li3)

# Task5
pattern = r'([\.\w]+\.ru)/?'
pat = re.compile(pattern)
li4 = pat.findall(text)


wordSet = {(item, li4.count(item)) for item in li4}
print(sorted(wordSet, key=lambda wordTuple: wordTuple[1], reverse=True)[0])

# Task6
pattern = r'(\w+\.(mail\.ru|ru|com)(/\w+)?)'
pat = re.compile(pattern)
print(re.sub(pat, 'Ссылка отобразится после регистрации', text))
