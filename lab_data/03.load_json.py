import json

f = open('../data/labels/labels.json')
label = json.load(f)

for box2d in label[0]['labels']:
    print(box2d.keys())
    if box2d in dict:
    print(box2d.keys())
