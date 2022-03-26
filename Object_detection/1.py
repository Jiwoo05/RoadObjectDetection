import yolov3
import cv2

model = yolov3.YOLO_V3()
model.build()
model.load()

path = '../data/images/3b59c8a5-f0b031cc.jpg'
image = cv2.imread(path)
result = model.predict(image)
cv2.imshow('image', image)
cv2.imshow('result', result)
cv2.waitKey(0)
