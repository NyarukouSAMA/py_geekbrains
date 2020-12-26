import pickle
import json

with open('group.dat', 'rb') as f:
    groupP = pickle.load(f)

print('pickle=', groupP)

with open('group.json', 'r', encoding="utf-8") as f:
    groupJ = json.load(f)

print('json=', groupJ)
