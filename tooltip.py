#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QToolTip, QPushButton
from PyQt5.QtGui import QFont

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SanSerif', 10))

        self.setToolTip('this is a <b> QWidget </b> widget')

        btn = QPushButton('button', self)
        btn.setToolTip('this is a <b> QPushButton </b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 250)
        self.setWindowTitle('tooltips')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
