import cv2
import os
import json

file_names = os.listdir('data/images')
f = open('../data/labels/labels.json')
labels = json.load(f)
image = cv2.imread('../data/images/' + file_names )
image2 = image.copy()

a = 0

if not os.path.exists('../classification_data'):
    os.mkdir('../classification_data')
if not os.path.exists('../classification_data/car'):
    os.mkdir('../classification_data/car')
if not os.path.exists('../classification_data/traffic sign'):
    os.mkdir('../classification_data/traffic sign')
if not os.path.exists('../classification_data/traffic light'):
    os.mkdir('../classification_data/traffic light')

for lable in labels:
    if lable['name'] == file_names:
        for l in lable['labels']:
            if 'box2d' in l:
                print(l['box2d']['x1'], l['box2d']['y1'], l['box2d']['x2'], l['box2d']['y2'])
                x1 = int(l['box2d']['x1'])
                x2 = int(l['box2d']['x2'])
                y1 = int(l['box2d']['y1'])
                y2 = int(l['box2d']['y2'])

                crop_image = image2[y1:y2, x1:x2]

                if l['category'] == 'car':
                    cv2.imwrite('../classification_data/car/'+ str(a) +'.jpg', crop_image)
                if l['category'] == 'bus':
                    cv2.imwrite('../classification_data/bus/'+ str(a) +'.jpg', crop_image)
                if l['category'] == 'traffic sign':
                    cv2.imwrite('../classification_data/traffic sign/'+ str(a) +'.jpg', crop_image)
                if l['category'] == 'traffic light':
                    cv2.imwrite('../classification_data/traffic light/'+ str(a) +'.jpg', crop_image)

                if not os.path.exists('../classification_data/' + l['category']):
                    os.mkdir('../classification_data/' + l['category'])
                    cv2.imwrite('../classification_data/' + l['category'] +'/'+ str(a) + '.jpg', crop_image)

                a += 1

                cv2.rectangle(image, (x1, y1), (x2, y2), (255, 255, 255), 3)
                cv2.putText(image, l['category'], (x1, y1), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2, cv2.LINE_AA)


cv2.imshow('image', image)
cv2.waitKey(0)

