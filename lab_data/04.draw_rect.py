import cv2

file_name = '3b59c8a5-f0b031cc.jpg'
image = cv2.imread('../data/images/'+file_name)

cv2.rectangle(image, (10, 10), (100, 100), (0, 0, 225), 3)

cv2.imshow('image', image)
cv2.waitKey(0)