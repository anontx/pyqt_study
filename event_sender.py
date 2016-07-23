#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        btn1 = QPushButton('button1', self)
        btn1.move(30, 50)

        btn2 = QPushButton('button2', self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 300, 250)
        self.setWindowTitle('event sender')
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
