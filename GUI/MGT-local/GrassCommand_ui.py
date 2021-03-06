#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
# Form implementation generated from reading ui file '/Users/epi/PycharmProjects/imagedisplay/htmap/qtui/GrassCommand_ui.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 721)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.commandbox = QtWidgets.QGroupBox(self.centralwidget)
        self.commandbox.setTitle("")
        self.commandbox.setObjectName("commandbox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.commandbox)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.commandboxlayout = QtWidgets.QHBoxLayout()
        self.commandboxlayout.setObjectName("commandboxlayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.commandboxlayout.addItem(spacerItem)
        self.closecommand = QtWidgets.QPushButton(self.commandbox)
        self.closecommand.setObjectName("closecommand")
        self.commandboxlayout.addWidget(self.closecommand)
        self.runcommand = QtWidgets.QPushButton(self.commandbox)
        self.runcommand.setObjectName("runcommand")
        self.commandboxlayout.addWidget(self.runcommand)
        self.copycommand = QtWidgets.QPushButton(self.commandbox)
        self.copycommand.setObjectName("copycommand")
        self.commandboxlayout.addWidget(self.copycommand)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.commandboxlayout.addItem(spacerItem1)
        self.horizontalLayout_4.addLayout(self.commandboxlayout)
        self.gridLayout.addWidget(self.commandbox, 2, 0, 1, 1)
        self.headerbox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.headerbox.sizePolicy().hasHeightForWidth())
        self.headerbox.setSizePolicy(sizePolicy)
        self.headerbox.setMaximumSize(QtCore.QSize(16777215, 150))
        self.headerbox.setTitle("")
        self.headerbox.setObjectName("headerbox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.headerbox)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.headerboxlayout = QtWidgets.QHBoxLayout()
        self.headerboxlayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.headerboxlayout.setObjectName("headerboxlayout")
        self.grassicon = QtWidgets.QLabel(self.headerbox)
        self.grassicon.setMinimumSize(QtCore.QSize(15, 15))
        self.grassicon.setMaximumSize(QtCore.QSize(40, 40))
        self.grassicon.setText("")
        self.grassicon.setPixmap(QtGui.QPixmap(":/icon/Grass_GIS.svg"))
        self.grassicon.setScaledContents(True)
        self.grassicon.setObjectName("grassicon")
        self.headerboxlayout.addWidget(self.grassicon)
        self.commanddescription = QtWidgets.QLabel(self.headerbox)
        self.commanddescription.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.commanddescription.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.commanddescription.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.commanddescription.setObjectName("commanddescription")
        self.headerboxlayout.addWidget(self.commanddescription)
        self.horizontalLayout_2.addLayout(self.headerboxlayout)
        self.gridLayout.addWidget(self.headerbox, 0, 0, 1, 1)
        self.commandtab = QtWidgets.QTabWidget(self.centralwidget)
        self.commandtab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.commandtab.setObjectName("commandtab")
        self.CommandOutput = QtWidgets.QWidget()
        self.CommandOutput.setObjectName("CommandOutput")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.CommandOutput)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.commandoutput = QtWidgets.QTextEdit(self.CommandOutput)
        self.commandoutput.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.commandoutput.setObjectName("commandoutput")
        self.verticalLayout_2.addWidget(self.commandoutput)
        self.commandtab.addTab(self.CommandOutput, "")
        self.Manual = QtWidgets.QWidget()
        self.Manual.setObjectName("Manual")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Manual)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.manualpage = QtWebEngineWidgets.QWebEngineView(self.Manual)
        self.manualpage.setUrl(QtCore.QUrl("about:blank"))
        self.manualpage.setObjectName("manualpage")
        self.verticalLayout.addWidget(self.manualpage)
        self.commandtab.addTab(self.Manual, "")
        self.gridLayout.addWidget(self.commandtab, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.commandtab.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "command_name_keywords"))
        self.closecommand.setText(_translate("MainWindow", "Close"))
        self.runcommand.setText(_translate("MainWindow", "Run"))
        self.copycommand.setText(_translate("MainWindow", "Copy"))
        self.commanddescription.setText(_translate("MainWindow", "Command Description"))
        self.commandtab.setTabText(self.commandtab.indexOf(self.CommandOutput), _translate("MainWindow", "Command Output"))
        self.commandtab.setTabText(self.commandtab.indexOf(self.Manual), _translate("MainWindow", "Manual"))

from PyQt5 import QtWebEngineWidgets
import resources_rc