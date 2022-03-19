from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QHBoxLayout, QPushButton, QGroupBox, QLabel, QVBoxLayout, QFileDialog
from PyQt5.QtGui import QPixmap
import sys
import tensorflow as tf
import cv2
import numpy as np
import os

class ClassificationAI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('이미지 분류 AI')

        self.group_box1 = QGroupBox('메뉴')
        self.group_box2 = QGroupBox('이미지')
        self.group_box3 = QGroupBox('분류 예측')

        self.button1 = QPushButton('데이터 불러오기')
        self.button1.clicked.connect(self.button1_click)
        self.button2 = QPushButton('모델 학습')
        self.button2.clicked.connect(self.button2_click)
        self.button3 = QPushButton('모델 저장')
        self.button3.clicked.connect(self.button3_click)
        self.button4 = QPushButton('모델 불러오기')
        self.button4.clicked.connect(self.button4_click)
        self.button5 = QPushButton('이미지 분류')
        self.button5.clicked.connect(self.button5_click)

        self.image_label = QLabel(self)

        self.text_label = QLabel(self)
        self.text_label.setText(' ')

        self.hbox_layout = QHBoxLayout()
        self.hbox_layout.addWidget(self.button1)
        self.hbox_layout.addWidget(self.button2)
        self.hbox_layout.addWidget(self.button3)
        self.hbox_layout.addWidget(self.button4)
        self.hbox_layout.addWidget(self.button5)

        self.vbox_layout = QVBoxLayout()
        self.vbox_layout.addWidget(self.image_label)

        self.vbox_layout2 = QVBoxLayout()
        self.vbox_layout2.addWidget(self.text_label)

        self.group_box1.setLayout(self.hbox_layout)
        self.group_box2.setLayout(self.vbox_layout)
        self.group_box3.setLayout(self.vbox_layout2)

        self.main_layout = QGridLayout()
        self.main_layout.addWidget(self.group_box1, 0, 0, 1, 2)
        self.main_layout.addWidget(self.group_box2, 1, 0, 7, 1)
        self.main_layout.addWidget(self.group_box3, 1, 1, 7, 1)

        self.setLayout(self.main_layout)

    # 데이터 불러오기
    def button1_click(self):
        self.train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
            '../classification_data/',
            image_size=(224, 224),
            label_mode='categorical'
        )
        self.class_names = self.train_dataset.class_names
        self.button1.setEnabled(False)
        self.button1.setText('데이터 불러오기 완료')

    # 모델 학습
    def button2_click(self):
        self.model = tf.keras.models.load_model('../models/mymodel.h5')

        if not os.path.exists('../logs'):
            os.mkdir('../logs')

        tensorboard = tf.keras.callbacks.TensorBoard(log_dir='../logs')

        learning_rate = 0.001
        self.model.compile(
            loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True),
            optimizer=tf.keras.optimizers.RMSprop(learning_rate=learning_rate),
            metrics=['accuracy']
        )
        # 학습 할 횟수 = 5
        self.model.fit(self.train_dataset, epochs=5)
        self.button2.setEnabled(False)
        self.button2.setText('모델 학습 완료')

    # 모델 저장
    def button3_click(self):
        if not os.path.exists('../models'):
            os.mkdir('../models')
        self.model.save('../models/classification_model.h5')
        self.button3.setEnabled(False)
        self.button3.setText('모델 저장 완료')

    # 모델 불러오기
    def button4_click(self):
        self.model = tf.keras.models.load_model('../models/classification_model.h5')
        self.button4.setEnabled(False)
        self.button4.setText('모델 불러오기 완료')

    # 이미지 분류
    def button5_click(self):
        # 이미지를 가져올 경로
        path, _ = QFileDialog.getOpenFileName(self, 'ABCD', '../classification_data', 'Image Files (*.jpg *.png)')
        if path == '':
            # 이미지를 선택하지 않았을 때.
            print('취소')
        else:
            # 이미지를 선택하였을때 그경로 표시하기.
            print('PATH', path)
            self.button5.setEnabled(False)
            self.button5.setText('모델 불러오기 완료')
            pixmap = QPixmap(path)
            self.image_label.setPixmap(pixmap)
            result = self.predict(path)
            self.text_label.setText(result)


    # 예측
    def predict(self, path):
        image = cv2.imread(path)
        resize_image = cv2.resize(image, (224, 224))
        data = np.array([resize_image])
        predict = self.model.predict(data)
        index = np.argmax(predict)
        return self.class_names[index]

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    classification_ai = ClassificationAI()
    classification_ai.show()
    sys.exit(app.exec())