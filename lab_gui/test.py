from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QHBoxLayout, QPushButton, QGroupBox, QLabel, QVBoxLayout, QFileDialog
from PyQt5.QtGui import QPixmap
import sys

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


        self.hbox_layout = QHBoxLayout()
        self.hbox_layout.addWidget(self.button1)
        self.hbox_layout.addWidget(self.button2)
        self.hbox_layout.addWidget(self.button3)
        self.hbox_layout.addWidget(self.button4)
        self.hbox_layout.addWidget(self.button5)

        self.vbox_layout = QVBoxLayout()
        self.vbox_layout.addWidget(self.image_label)

        self.group_box1.setLayout(self.hbox_layout)
        self.group_box2.setLayout(self.vbox_layout)

        self.main_layout = QGridLayout()
        self.main_layout.addWidget(self.group_box1, 0, 0, 1, 2)
        self.main_layout.addWidget(self.group_box2, 1, 0, 7, 1)
        self.main_layout.addWidget(self.group_box3, 1, 1, 7, 1)

        self.setLayout(self.main_layout)

    def button1_click(self):
        path, _ = QFileDialog.getOpenFileName(self, 'ABCD', '../classification_data', 'Image Files (*.jpg *.png)')
        if path == '':
            print('취소')
        else:
            print('PATH', path)
            self.button1.setEnabled(False)
            self.button1.setText('데이터 불러오기 완료')
            pixmap = QPixmap(path)
            self.image_label.setPixmap(pixmap)

    def button2_click(self):
        self.button2.setEnabled(False)

    def button3_click(self):
        self.button3.setEnabled(False)

    def button4_click(self):
        self.button4.setEnabled(False)

    def button5_click(self):
        self.button5.setEnabled(False)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    classification_ai = ClassificationAI()
    classification_ai.show()
    sys.exit(app.exec())