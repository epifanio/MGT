#!/usr/bin/env python

from PyQt5 import QtWidgets

#from GrassCommand_ui import Ui_MainWindow

from GrassWidget_ui import Ui_Form

#class MainGui(QtWidgets.QMainWindow, Ui_MainWindow):
#    def __init__(self):
#        QtWidgets.QMainWindow.__init__(self)
#        self.setupUi(self)



class MainGui(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)