#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QApplication,
    QLabel, QLineEdit, QComboBox)

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # lineedit
        self.lbl = QLabel(self)
        qle = QLineEdit(self)

        qle.move(20, 30)
        self.lbl.move(20, 10)

        qle.textChanged[str].connect(self.onChanged)

        # combobox
        self.lbl1 = QLabel('ubuntu', self)

        combo = QComboBox(self)
        combo.addItem('ubuntu')
        combo.addItem('mandriva')
        combo.addItem('fedora')
        combo.addItem('arch')
        combo.addItem('gentoo')

        combo.move(20, 70)
        self.lbl1.move(20, 100)

        combo.activated[str].connect(self.onActivated)

        self.setGeometry(300, 300, 300, 250)
        self.setWindowTitle('widget 1')
        self.show()

    def onActivated(self, text):
        self.lbl1.setText(text)
        self.lbl1.adjustSize()

    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
