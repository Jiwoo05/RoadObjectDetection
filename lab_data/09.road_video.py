import yolov3
import cv2

model = yolov3.YOLO_V3()
model.build()
model.load()
path = '../data/videos/cabc30fc-e7726578.mov'
cap = cv2.VideoCapture(path)
while cap.isOpened():
    ret, image = cap.read()
    if not ret:
        break
    video = cv2.imread(path)
    result = model.predict(video)
    cv2.imshow('result', result)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()