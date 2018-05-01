#!/usr/bin/env python

from PyQt5 import QtWidgets
from taskManager_ui import Ui_taskmanager

class taskManagerUi(QtWidgets.QWidget, Ui_taskmanager):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)