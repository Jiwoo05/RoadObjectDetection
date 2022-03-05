from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QHBoxLayout, QPushButton, QGroupBox
import sys


class ClassificationAI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('제목')

        self.group_box1 = QGroupBox('그룹1')
        self.group_box2 = QGroupBox('그룹2')

        self.button1 = QPushButton('-1')
        self.button2 = QPushButton('+1')

        self.hbox_layout = QHBoxLayout()
        self.hbox_layout.addWidget(self.button1)
        self.hbox_layout.addWidget(self.button2)

        self.group_box1.setLayout(self.hbox_layout)


        self.main_layout = QGridLayout()
        self.main_layout.addWidget(self.group_box1, 0, 0, 1, 1)
        self.main_layout.addWidget(self.group_box2, 1, 0, 1, 1)

        self.setLayout(self.main_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    classification_ai = ClassificationAI()
    classification_ai.show()
    sys.exit(app.exec())