#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication


if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(300, 250)
    w.move(300, 300)
    w.setWindowTitle('simple')
    w.show()

    sys.exit(app.exec_())
