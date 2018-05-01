# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'taskManager_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.2.dev1804051511
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_taskmanager(object):
    def setupUi(self, taskmanager):
        taskmanager.setObjectName("taskmanager")
        taskmanager.resize(378, 272)
        self.verticalLayout = QtWidgets.QVBoxLayout(taskmanager)
        self.verticalLayout.setObjectName("verticalLayout")
        self.param = QtWidgets.QLineEdit(taskmanager)
        self.param.setObjectName("param")
        self.verticalLayout.addWidget(self.param)
        self.tasks = QtWidgets.QTableWidget(taskmanager)
        self.tasks.setObjectName("tasks")
        self.tasks.setColumnCount(0)
        self.tasks.setRowCount(0)
        self.verticalLayout.addWidget(self.tasks)
        self.groupBox = QtWidgets.QGroupBox(taskmanager)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.runit = QtWidgets.QPushButton(self.groupBox)
        self.runit.setObjectName("runit")
        self.horizontalLayout.addWidget(self.runit)
        self.clean = QtWidgets.QPushButton(self.groupBox)
        self.clean.setObjectName("clean")
        self.horizontalLayout.addWidget(self.clean)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(taskmanager)
        QtCore.QMetaObject.connectSlotsByName(taskmanager)

    def retranslateUi(self, taskmanager):
        _translate = QtCore.QCoreApplication.translate
        taskmanager.setWindowTitle(_translate("taskmanager", "Task Manager"))
        self.runit.setText(_translate("taskmanager", "Run"))
        self.clean.setText(_translate("taskmanager", "Clear"))

