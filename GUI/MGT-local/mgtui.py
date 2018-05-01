#!/usr/bin/env python

from PyQt5 import QtWidgets
from MGT_ui import Ui_MainWindow

class MainGui(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)