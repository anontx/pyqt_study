#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QApplication,
    QCheckBox, QPushButton, QFrame, QSlider, QLabel,
    QProgressBar, QCalendarWidget)
from PyQt5.QtCore import Qt, QBasicTimer, QDate
from PyQt5.QtGui import QColor

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):

        # checkbox
        cb = QCheckBox('show title', self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        # toggle button
        self.col = QColor(0, 0, 0)

        redb = QPushButton('red', self)
        redb.setCheckable(True)
        redb.move(20, 40)
        redb.clicked[bool].connect(self.setColor)

        greenb = QPushButton('green', self)
        greenb.setCheckable(True)
        greenb.move(20, 60)
        greenb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('blue', self)
        blueb.setCheckable(True)
        blueb.move(20, 80)
        blueb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet('QWidget {background-color: %s}' %
            self.col.name())

        # slider
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(20, 160, 100, 20)
        sld.valueChanged[int].connect(self.changeValue)

        self.label = QLabel('0', self)
        self.label.setGeometry(140, 155, 80, 30)

        # progressbar
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(20, 200, 200, 25)

        self.btn = QPushButton('start', self)
        self.btn.move(20, 230)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0

        # calendar
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20, 300)
        cal.clicked[QDate].connect(self.showDate)

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.move(20, 280)

        self.setGeometry(300, 300, 400, 550)
        self.setWindowTitle('widgets')
        self.show()

    def showDate(self, date):
        self.lbl.setText(date.toString())

    def timerEvent(self, e):

        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('finished')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(100, self)
            self.btn.setText('stop')

    def changeValue(self, value):
        self.label.setText(str(value))

    def setColor(self, pressed):
        source = self.sender()

        if pressed:
            val = 255
        else:
            val = 0

        if source.text() == 'red':
            self.col.setRed(val)
        elif source.text() == 'green':
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)

        self.square.setStyleSheet('QFrame {background-color: %s}' %
            self.col.name())


    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('widgets')
        else:
            self.setWindowTitle('')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
