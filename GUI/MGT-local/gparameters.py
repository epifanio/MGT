#!/usr/bin/env python3

from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5 import QtWidgets


class GisOptionDirectoryPrompt(QtWidgets.QWidget):
    valueUpdated = pyqtSignal(str)

    def __init__(self, fl, filelist, command):
        super(GisOptionDirectoryPrompt, self).__init__()
        self.fl = fl
        self.filelist = filelist
        self.command = command
        self.param_name = self.command['name']
        self.filename = [['']]
        self.initUI()

    def initUI(self):
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        # name
        self.paramlabel = QtWidgets.QLabel()
        self.paramlabel.setObjectName("label")
        self.gridLayout.addWidget(self.paramlabel, 0, 0, 1, 1)
        if self.command['label'] != '':
            self.paramlabel.setText(self.command['label'])
        else:
            self.paramlabel.setText(self.command['description'])
        self.paramlabel.setWordWrap(True)
        # label
        self.paramname = QtWidgets.QLabel()
        self.paramname.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.paramname.setObjectName("paramname")
        self.gridLayout.addWidget(self.paramname, 0, 1, 1, 1)
        self.paramname.setText('(' + self.command['name'] + '=' + self.command['type'] + ')')
        self.paramname.setWordWrap(True)
        # filepath
        self.filepath = QtWidgets.QLineEdit()
        self.filepath.setObjectName("filepath")
        # self.filepath.setMaximumSize(QSize(290, 16777215))
        self.gridLayout.addWidget(self.filepath, 1, 0, 1, 1)
        # browse button
        self.filebrowser = QtWidgets.QPushButton()
        # self.filebrowser.setMaximumSize(QSize(24, 20))
        # icon = QIcon()
        # icon.addPixmap(QPixmap("../../grass_modules/QT/resources/arrowdown.png"), QIcon.Normal,
        #               QIcon.Off)
        # self.filebrowser.setIcon(icon)
        # self.filebrowser.setIconSize(QSize(22, 22))
        self.filebrowser.setText("Browse")
        self.filebrowser.setObjectName("filebrowser")
        self.filebrowser.clicked.connect(self.openfile)
        self.gridLayout.addWidget(self.filebrowser, 1, 1, 1, 1)

        # list all formats
        # v.in.ogr -f


        # list available layers in data source
        # v.in.ogr -f

        self.fl.addLayout(self.gridLayout)

    def openDirectory(self):
        self.filename = QtWidgets.QFileDialog.getOpenFileName(self, self.tr("Input file"), self.filepath.text())
        print(self.filename[0])
        self.filepath.setText(self.filename[0])
        status = self.command['name'] + '=' + self.filename[0]
        self.valueUpdated.emit(status)


class GisOptionFilePrompt(QtWidgets.QWidget):
    valueUpdated = pyqtSignal(str)

    def __init__(self, fl, filelist, command):
        super(GisOptionFilePrompt, self).__init__()
        self.fl = fl
        self.filelist = filelist
        self.command = command
        self.param_name = self.command['name']
        self.filename = [['']]
        self.initUI()

    def initUI(self):
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        # name
        self.paramlabel = QtWidgets.QLabel()
        self.paramlabel.setObjectName("label")
        self.gridLayout.addWidget(self.paramlabel, 0, 0, 1, 1)
        if self.command['label'] != '':
            self.paramlabel.setText(self.command['label'])
        else:
            self.paramlabel.setText(self.command['description'])
        self.paramlabel.setWordWrap(True)
        # label
        self.paramname = QtWidgets.QLabel()
        self.paramname.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.paramname.setObjectName("paramname")
        self.gridLayout.addWidget(self.paramname, 0, 1, 1, 1)
        self.paramname.setText('(' + self.command['name'] + '=' + self.command['type'] + ')')
        self.paramname.setWordWrap(True)
        # filepath
        self.filepath = QtWidgets.QLineEdit()
        self.filepath.setObjectName("filepath")
        # self.treeviewresults.setMaximumSize(QSize(290, 16777215))
        self.gridLayout.addWidget(self.filepath, 1, 0, 1, 1)
        # browse button
        self.filebrowser = QtWidgets.QPushButton()
        # self.filebrowser.setMaximumSize(QSize(24, 20))
        # icon = QIcon()
        # icon.addPixmap(QPixmap("../../grass_modules/QT/resources/arrowdown.png"), QIcon.Normal,
        #               QIcon.Off)
        # self.filebrowser.setIcon(icon)
        # self.filebrowser.setIconSize(QSize(22, 22))
        self.filebrowser.setText("Browse")
        self.filebrowser.setObjectName("filebrowser")
        self.filebrowser.clicked.connect(self.openfile)
        self.gridLayout.addWidget(self.filebrowser, 1, 1, 1, 1)
        self.fl.addLayout(self.gridLayout)

    def openfile(self):
        self.filename = QtWidgets.QFileDialog.getOpenFileName(self, self.tr("Input file"), self.filepath.text())
        print(self.filename[0])
        self.filepath.setText(self.filename[0])
        status = self.command['name'] + '=' + self.filename[0]
        self.valueUpdated.emit(status)


class GisOptionDataSourcePrompt(QtWidgets.QWidget):
    valueUpdated = pyqtSignal(str)

    def __init__(self, fl, datasourcelist, command):
        super(GisOptionDataSourcePrompt, self).__init__()
        self.fl = fl
        self.datasourcelist = datasourcelist
        self.command = command
        self.param_name = self.command['name']
        self.initUI()

    def initUI(self):
        # this is tough
        # need  gropbox with radio button
        # based on the radio button selection:
        #    show/hide the correct parameter prompt
        # connect the chosen parameter with a qtable
        # in case the option datasource_layer is True
        # use gdal to check the available layers
        # and updare the table with a checkable item
        # use a model

        # desc and label:

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        # Label
        self.commandlabel = QtWidgets.QLabel()
        self.commandlabel.setObjectName("label")
        self.gridLayout.addWidget(self.commandlabel, 0, 0, 1, 1)
        if self.command['label'] != '':
            self.commandlabel.setText(self.command['label'])
        else:
            self.commandlabel.setText(self.command['description'])
        self.commandlabel.setWordWrap(True)
        # treeviewlabel
        self.paramname = QtWidgets.QLabel()
        self.paramname.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.paramname.setObjectName("paramname")
        self.gridLayout.addWidget(self.paramname, 0, 1, 1, 1)
        self.paramname.setText('(' + self.command['name'] + '=' + self.command['type'] + ')')
        self.paramname.setWordWrap(True)

        #
        #

        self.sourcetypebox = QtWidgets.QGroupBox()
        self.sourcetypebox.setObjectName("sourcetypebox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.sourcetypebox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radio_file = QtWidgets.QRadioButton(self.sourcetypebox)
        self.radio_file.setObjectName("radio_file")
        self.horizontalLayout_2.addWidget(self.radio_file)
        self.radio_directory = QtWidgets.QRadioButton(self.sourcetypebox)
        self.radio_directory.setObjectName("radio_directory")
        self.horizontalLayout_2.addWidget(self.radio_directory)
        self.radio_database = QtWidgets.QRadioButton(self.sourcetypebox)
        self.radio_database.setObjectName("radio_database")
        self.horizontalLayout_2.addWidget(self.radio_database)
        self.radio_protocol = QtWidgets.QRadioButton(self.sourcetypebox)
        self.radio_protocol.setObjectName("radio_protocol")
        self.horizontalLayout_2.addWidget(self.radio_protocol)
        self.sourcetypebox.setTitle("Source Type")
        self.radio_file.setText("File")
        self.radio_directory.setText("Directory")
        self.radio_database.setText("Database")
        self.radio_protocol.setText("Protocol")

        self.sourceinputbox = QtWidgets.QGroupBox()
        self.sourceinputbox.setObjectName("sourceinputbox")
        self.sourcetypebox.setTitle("Source Input")
        self.sourceinputboxLayout = QtWidgets.QHBoxLayout(self.sourceinputbox)

        # this will reveal if the 'radio_file' is checked
        self.fileopen = GisOptionFilePrompt(self.sourceinputboxLayout, self.datasourcelist, self.command)
        self.fileopen.setObjectName("fileopen_%s" % self.command)
        self.datasourcelist.append(self.fileopen)

        self.fl.addLayout(self.gridLayout)
        self.fl.addWidget(self.sourcetypebox)
        self.fl.addWidget(self.sourceinputbox)


class GisOptionPrompt(QtWidgets.QWidget):
    valueUpdated = pyqtSignal(str)

    def __init__(self, fl, parameterlist, command, model):
        super(GisOptionPrompt, self).__init__()
        self.fl = fl
        self.parameterlist = parameterlist
        self.command = command
        #self.commandname = command
        self.param_name = self.command['name']
        self.model=model
        self.initUI()

    def initUI(self):
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        # Label
        self.commandlabel = QtWidgets.QLabel()
        self.commandlabel.setObjectName("label")
        self.gridLayout.addWidget(self.commandlabel, 0, 0, 1, 1)
        if self.command['label'] != '':
            self.commandlabel.setText(self.command['label'])
        else:
            self.commandlabel.setText(self.command['description'])
        self.commandlabel.setWordWrap(True)
        # treeviewlabel
        self.treeviewlabel = QtWidgets.QLabel()
        self.treeviewlabel.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.treeviewlabel.setObjectName("treeviewlabel")
        self.gridLayout.addWidget(self.treeviewlabel, 0, 1, 1, 1)
        self.treeviewlabel.setText('(' + self.command['name'] + '=' + self.command['type'] + ')')
        self.treeviewlabel.setWordWrap(True)
        # treeviewresults
        self.treeviewresults = QtWidgets.QLineEdit()
        self.treeviewresults.setObjectName("treeviewresults")
        # self.treeviewresults.setMaximumSize(QSize(290, 16777215))
        self.gridLayout.addWidget(self.treeviewresults, 1, 0, 1, 1)
        # treeview button
        self.treeviewbutton = QtWidgets.QPushButton()
        self.treeviewbutton.setMaximumSize(QSize(24, 20))
        icon = QIcon()
        icon.addPixmap(QPixmap("../../grass_modules/QT/resources/arrowdown.png"), QIcon.Normal,
                       QIcon.Off)
        self.treeviewbutton.setIcon(icon)
        self.treeviewbutton.setIconSize(QSize(22, 22))
        self.treeviewbutton.setText("")
        self.treeviewbutton.setObjectName("treeviewbutton")
        self.gridLayout.addWidget(self.treeviewbutton, 1, 1, 1, 1)
        # treeview
        self.treeView = QtWidgets.QTreeView()


        #self.commandspecs = getCommand('g.region', ip='144.76.93.231', port='5556')
        self.treeView.setModel(self.get_model2(self.command['prompt'])) #())

        #self.treeView.setModel(self.get_model(self.command['prompt']))
        if self.command['multiple']:
            self.treeView.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.treeView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.treeView.setEditTriggers(self.treeView.NoEditTriggers)
        self.treeView.setAlternatingRowColors(True)
        self.treeView.setSelectionBehavior(self.treeView.SelectRows)
        self.treeView.setAllColumnsShowFocus(True)
        self.treeView.clicked.connect(self.selectitems)
        self.treeView.hide()
        self.treeView.setObjectName("treeView")
        self.gridLayout.addWidget(self.treeView, 3, 0, 1, 1)
        #
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.treeviewbutton.clicked.connect(self.showhidetree)
        # self.fl.addRow(self.gridLayout)
        self.fl.addLayout(self.gridLayout)

        self.treeviewresults.textChanged.connect(self.setoptionprompt)

    def showhidetree(self):
        if self.treeView.isVisible():
            self.treeView.hide()
        else:
            self.treeView.show()

    def list2model(self, lista):
        model = QStandardItemModel()
        model.setParent(self)
        for listitem in lista:
            parent_item = QStandardItem(str(listitem))
            parent_item.setSelectable(True)
            model.appendRow(parent_item)
        return model
        # mapsets = [i.decode() for i in script.mapsets(search_path=True)]


    def get_model2(self, gtype):
        mapsets=self.model['mapsets']
        model = QStandardItemModel()
        # model.__init__(parent=None)
        model.setParent(self)
        for mapset in mapsets:
            parent_item = QStandardItem('Mapset: ' + str(mapset))
            parent_item.setSelectable(False)
            #print(gtype)
            #if gtype=='raster':
            #    lista=self.mapsets[1]
            #if gtype=='vector':
            #    lista=self.mapsets[2]
            #else:
            #    lista=''
            #lista = script.core.list_pairs(gtype)
            lista = self.model[gtype]
            # print
            for map in lista:
                if mapset in map:
                    # print(map)
                    parent_item.appendRow(QStandardItem
                                          ('%s@%s' % (map[0], map[1])))
            model.appendRow(parent_item)

        return model

    def get_model(self, gtype):
        """
        creates the core of a tree based model to input into widget
        :param gtask: part of gtask for this widget
        :return: tree model
        """
        mapsets = [i.decode() for i in script.mapsets(search_path=True)]
        model = QStandardItemModel()
        # model.__init__(parent=None)
        model.setParent(self)
        for mapset in mapsets:
            parent_item = QStandardItem('Mapset: ' + str(mapset))
            parent_item.setSelectable(False)
            lista = script.core.list_pairs(gtype)
            # print
            for map in lista:
                if mapset in map:
                    # print(map)
                    parent_item.appendRow(QStandardItem
                                          ('%s@%s' % (map[0], map[1])))
            model.appendRow(parent_item)

        return model

    def selectitems(self):
        indexes = [i.model().itemFromIndex(i).text() for i in self.treeView.selectedIndexes()]
        maplist = ', '.join(indexes)
        self.treeviewresults.setText(maplist)
        self.parameterlist.append(maplist)

    def setoptionprompt(self):
        status = str(self.param_name) + '=' + self.treeviewresults.text()
        self.valueUpdated.emit(status)


class GisOptionFlag(QtWidgets.QWidget):
    valueUpdated = pyqtSignal(str)

    def __init__(self, fl, flaglist, flag):
        super(GisOptionFlag, self).__init__()
        self.fl = fl
        self.flaglist = flaglist
        self.flag = flag
        self.flag_name = self.flag['name']
        self.initUI()

    def initUI(self):
        # layout
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        # checkbox
        self.checkBox = QtWidgets.QCheckBox()
        self.checkBox.setText(self.flag['description'])

        self.horizontalLayout.addWidget(self.checkBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        # checkbox label
        self.checkBox_label = QtWidgets.QLabel()
        self.checkBox_label.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_label.setInputMethodHints(Qt.ImhLatinOnly)
        self.checkBox_label.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.horizontalLayout.addWidget(self.checkBox_label)
        self.checkBox_label.setText('(' + self.flag['name'] + ')')
        self.checkBox_label.setWordWrap(True)
        self.checkBox.stateChanged.connect(self.setflag)
        # append to tab layout
        # self.fl.addRow(self.horizontalLayout)
        self.fl.addLayout(self.horizontalLayout)

    def setflag(self):
        flag = 'None'
        if self.flag['name'] in ['overwrite', 'verbose', 'quiet', 'help']:
            flagger = '--'
        else:
            flagger = '-'
        if self.checkBox.isChecked():
            flag = flagger + str(self.flag['name'])
        status = str(self.flag['name']) + ':' + flag
        self.valueUpdated.emit(status)


class GisOptionString(QtWidgets.QWidget):
    valueUpdated = pyqtSignal(str)

    def __init__(self, fl, optionstringlist, option):
        super(GisOptionString, self).__init__()
        self.fl = fl
        self.optionstringlist = optionstringlist
        self.option = option
        self.optionstring_name = self.option['name']
        self.initUI()

    def initUI(self):
        # layout
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        # combobox
        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.addItems(self.option['values'])
        if self.option['default']:
            defaultindex = [i for i, x in enumerate(self.option['values']) if x == self.option['default']]
            self.comboBox.setCurrentIndex(defaultindex[0])
        self.horizontalLayout.addWidget(self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        # combobox label
        self.combobox_label = QtWidgets.QLabel()
        self.combobox_label.setLayoutDirection(Qt.LeftToRight)
        self.combobox_label.setInputMethodHints(Qt.ImhLatinOnly)
        self.combobox_label.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.horizontalLayout.addWidget(self.combobox_label)
        self.combobox_label.setText('(' + self.option['name'] + '=' + self.option['type'] + ')')
        self.combobox_label.setWordWrap(True)

        # append to tab layout
        # self.fl.addRow(self.horizontalLayout)
        self.fl.addLayout(self.horizontalLayout)
        self.comboBox.currentIndexChanged.connect(self.setoptionstring)

    def setoptionstring(self):
        status = str(self.option['name']) + '=' + self.comboBox.currentText()
        self.valueUpdated.emit(status)


class GisOptionNum(QtWidgets.QWidget):
    valueUpdated = pyqtSignal(str)

    def __init__(self, fl, optionnumlist, option):
        super(GisOptionNum, self).__init__()
        self.fl = fl
        self.optionnumlist = optionnumlist
        self.option = option
        self.optionnum_name = self.option['name']
        self.initUI()

    def initUI(self):
        # layout
        ##self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.gridLayout = QtWidgets.QGridLayout()

        # spinbox description
        self.spinBox_desc = QtWidgets.QLabel()
        # self.spinBox_desc.setLayoutDirection(Qt.LeftToRight)
        self.spinBox_desc.setInputMethodHints(Qt.ImhLatinOnly)
        # self.spinBox_desc.setAlignment(Qt.AlignLeft | Qt.AlignTrailing | Qt.AlignVCenter)
        self.spinBox_desc.setText(self.option['description'])
        self.spinBox_desc.setWordWrap(True)
        self.gridLayout.addWidget(self.spinBox_desc, 0, 0, 1, 1)

        # spinbox
        if self.option['type'] == 'float':
            self.spinBox = QtWidgets.QDoubleSpinBox()
        if self.option['type'] == 'integer':
            self.spinBox = QtWidgets.QSpinBox()
        #'''
        if self.option['values'] != []:
            minmax = self.option['values'][0].split('-')
            print('minmax: ', minmax)
            try:
                self.spinBox.setMinimum(int(minmax[0]))
                self.spinBox.setMaximum(int(minmax[1]))
            except:
                pass
        if self.option['default'] != '':
            if self.option['default'] in range(int(self.spinBox.minimum()), int(self.spinBox.maximum())):
                self.spinBox.setProperty("value", self.option['default'])
            else:
                if self.option['type'] == 'float':
                    print('default:', self.option['default'])
                    try:
                        float(self.option['default'])
                        self.spinBox.setDecimals(len(self.option['default']))
                        default = self.option['default']
                    except:
                        default = self.option['default'].split(',')
                        #self.spinBox.setDecimals(len(self.option['default'][0]))
                    if type(default) == 'list' and len(default) >=2:
                        if float(self.option['default'][0]) < self.spinBox.minimum():
                            self.spinBox.setMinimum(int(self.option['default']))
                        if float(self.option['default'][1]) > self.spinBox.maximum():
                            self.spinBox.setMaximum(int(self.option['default']))
                        self.spinBox.setProperty("value", self.option['default'][0])
                    else:
                        self.spinBox.setProperty("value", default)
        #'''
        if 'odd number only' in self.option['description']:
            self.spinBox.setSingleStep(2)
        self.spinBox.setMaximumSize(QSize(160, 16777215))

        ##self.horizontalLayout.addWidget(self.spinBox)
        self.gridLayout.addWidget(self.spinBox, 1, 0, 1, 1)

        ##spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        ##self.horizontalLayout.addItem(spacerItem)

        # spinbox label
        self.spinBox_label = QtWidgets.QLabel()
        self.spinBox_label.setLayoutDirection(Qt.LeftToRight)
        self.spinBox_label.setInputMethodHints(Qt.ImhLatinOnly)
        self.spinBox_label.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.spinBox_label.setText('(' + self.option['name'] + '=' + self.option['type'] + ')')
        self.spinBox_label.setWordWrap(True)

        ##self.horizontalLayout.addWidget(self.spinBox_label)
        self.gridLayout.addWidget(self.spinBox_label, 0, 1, 1, 1)

        # append to tab layout
        # self.fl.addRow(self.horizontalLayout)

        ##self.fl.addLayout(self.horizontalLayout)

        self.fl.addLayout(self.gridLayout)
        self.spinBox.valueChanged.connect(self.setoptionnum)

    def setoptionnum(self):
        status = str(self.option['name']) + '=' + str(self.spinBox.value())
        self.valueUpdated.emit(status)


class GisOptionText(QtWidgets.QWidget):
    valueUpdated = pyqtSignal(str)

    def __init__(self, fl, optiontextlist, option):
        super(GisOptionText, self).__init__()
        self.fl = fl
        self.optiontextlist = optiontextlist
        self.option = option
        self.optiontext_name = self.option['name']
        self.initUI()

    def initUI(self):
        # layout
        ##self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.gridLayout = QtWidgets.QGridLayout()

        # linedit description
        self.linedit_desc = QtWidgets.QLabel()
        # self.linedit_desc.setLayoutDirection(Qt.LeftToRight)
        self.linedit_desc.setInputMethodHints(Qt.ImhLatinOnly)
        # self.linedit_desc.setAlignment(Qt.AlignLeft | Qt.AlignTrailing | Qt.AlignVCenter)
        self.linedit_desc.setText(self.option['description'])
        self.linedit_desc.setWordWrap(True)
        self.gridLayout.addWidget(self.linedit_desc, 0, 0, 1, 1)

        # optiontext
        self.optiontext = QtWidgets.QLineEdit()
        if self.option['default'] != '':
            self.optiontext.setText(self.option['default'])

        self.gridLayout.addWidget(self.optiontext, 1, 0, 1, 1)

        ##spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        ##self.horizontalLayout.addItem(spacerItem)

        # spinbox label
        self.optiontext_label = QtWidgets.QLabel()
        self.optiontext_label.setLayoutDirection(Qt.LeftToRight)
        self.optiontext_label.setInputMethodHints(Qt.ImhLatinOnly)
        self.optiontext_label.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.optiontext_label.setText('(' + self.option['name'] + '=' + self.option['type'] + ')')
        self.optiontext_label.setWordWrap(True)

        ##self.horizontalLayout.addWidget(self.spinBox_label)
        self.gridLayout.addWidget(self.optiontext_label, 0, 1, 1, 1)

        # append to tab layout
        # self.fl.addRow(self.horizontalLayout)

        ##self.fl.addLayout(self.horizontalLayout)

        self.fl.addLayout(self.gridLayout)
        self.optiontext.textChanged.connect(self.setoptiontext)

    def setoptiontext(self):
        status = str(self.option['name']) + '=' + str(self.optiontext.text())
        self.valueUpdated.emit(status)


class GisOptionMultiString(QtWidgets.QWidget):
    valueUpdated = pyqtSignal(str)

    def __init__(self, fl, optionmultistringlist, option):
        super(GisOptionMultiString, self).__init__()
        self.fl = fl
        self.optionmultistringlist = optionmultistringlist
        self.option = option
        self.optionmultistring_name = self.option['name']
        self.initUI()

    def initUI(self):
        self.checkboxes = {}
        self.groupBox = QtWidgets.QGroupBox()
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setTitle(self.option['description'])
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        for i, v in enumerate(self.option['values']):
            checkBox = QtWidgets.QCheckBox(self.groupBox)
            checkBox.setObjectName(v)
            self.gridLayout.addWidget(checkBox, i, 0, 1, 1)
            checkBox.setText(v)
            checkBox.stateChanged.connect(self.setoptionlist)
            self.checkboxes[v] = checkBox
        self.fl.addWidget(self.groupBox)

    def setoptionlist(self):
        options = []
        for i in self.checkboxes.keys():
            if self.checkboxes[i].isChecked():
                options.append(i)
        status = ','.join(options)
        status = self.option['name'] + '=' + status
        self.valueUpdated.emit(status)
