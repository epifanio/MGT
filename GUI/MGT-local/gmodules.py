#!/usr/bin/env python3

from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from grassui import MainGui
from remote import get_message, get_conf

from gcommands import get_command_description

from gparameters import (GisOptionPrompt,
                         GisOptionFlag,
                         GisOptionString,
                         GisOptionNum,
                         GisOptionText,
                         GisOptionMultiString,
                         GisOptionFilePrompt,
                         GisOptionDataSourcePrompt)

import zmq

class GrassModule(QtWidgets.QWidget):
    valueUpdated = pyqtSignal(str)

    def __init__(self, command=None, parent=None):
        super(GrassModule, self).__init__(parent)
        #
        self.prompts = []
        self.datasurcesprompts = []
        self.filesprompts = []
        self.gflags = []
        self.goptionsstring = []
        self.goptionsmultistring = []
        self.goptionsnum = []
        self.goptionstext = []
        #
        self.parameters=[]
        self.datasurceprompt = []
        self.fileprompt = []
        self.flags=[]
        self.stringoption = []
        self.multistringoption = []
        self.numoption = []
        self.textoption = []
        #
        print(command)
        if command != None:
            self.commandname = command
        else:
            self.commandname = 'g.list'
        #
        self.message = ''
        #self.gsec = gcommand(self.commandname)
        #self.commandspecs = gtask.command_info(self.commandname)
        #context = zmq.Context()
        #self.socket = context.socket(zmq.REQ)
        self.gsec = get_command_description(self.commandname)
        #self.gsec = get_message(self.commandname, ip=self.serverconf['IP'], port=self.serverconf['PORT'], socket=self.socket)
        self.setupui()

    def setupui(self):
        self.w = MainGui()
        self.w.commanddescription.setText(self.gsec['description'])
        self.w.commanddescription.setWordWrap(True)
        keywords = ', '.join(self.gsec['keywords'])
        title = str(self.commandname) + " [" + keywords + "]"
        #title = str(self.commandname)+" "+str(gsec['keywords'])
        self.w.setWindowTitle(title)
        for i in self.gsec['parameters'].keys():
            tab = QtWidgets.QScrollArea()
            tab.setWidget(QtWidgets.QWidget())
            fl = QtWidgets.QVBoxLayout(tab.widget())
            tab.setWidgetResizable(True)
            tab.setObjectName(i)
            self.w.commandtab.addTab(tab, i)
            for j in self.gsec['flags'][i].index.values:
                flag = self.gsec['flags'][i].iloc[j]
                gflag = GisOptionFlag(fl, self.flags, flag)
                self.gflags.append(gflag)
            for j in self.gsec['parameters'][i].index.values:
                command = self.gsec['parameters'][i].iloc[j]
                if command['gisprompt']: # and command['age'] == 'old':
                    if command['prompt'] in ['raster', 'raster_3d', 'vector', 'label', 'region', 'group', 'all']:
                        print(command['prompt'])
                        fileopen = GisOptionPrompt(fl, self.parameters, command, self.gsec['model'])
                        fileopen.setObjectName("fileopen_%s" % i)
                        self.prompts.append(fileopen)

                # TODO: handle here the datasource prompt
                #
                    if command['gisprompt'] and command['prompt'] == 'datasource':
                        fileopen = GisOptionDataSourcePrompt(fl, self.datasurceprompt, command)
                        fileopen.setObjectName("fileopen_%s" % i)
                        self.datasurcesprompts.append(fileopen)


                # TODO: handle here the file prompt
                #
                    if command['gisprompt'] and command['prompt'] == 'file':
                        fileopen = GisOptionFilePrompt(fl, self.fileprompt, command)
                        fileopen.setObjectName("fileopen_%s" % i)
                        self.filesprompts.append(fileopen)

            #for j in gsec['parameters'][i].index.values:
            #    command = gsec['parameters'][i].iloc[j]
                if command['type'] == 'string' and command['values'] != [] and not command['multiple']:
                    opt = GisOptionString(fl, self.stringoption, command)
                    opt.setObjectName("opt_%s" % i)
                    self.goptionsstring.append(opt)
            # TODO: handle multicheckbox here
                if command['type'] == 'string' and command['values'] != [] and command['multiple']:
                    opt = GisOptionMultiString(fl, self.multistringoption, command)
                    opt.setObjectName("opt_%s" % i)
                    self.goptionsmultistring.append(opt)

            #for j in gsec['parameters'][i].index.values:
            #    command = gsec['parameters'][i].iloc[j]
                if command['type'] == 'integer' or command['type'] == 'float' and not command['multiple']:
                    opt = GisOptionNum(fl, self.numoption, command)
                    opt.setObjectName("opt_%s" % i)
                    self.goptionsnum.append(opt)
                if command['type'] == 'integer' or command['type'] == 'float' and command['multiple']:
                    opt = GisOptionText(fl, self.textoption, command)
                    opt.setObjectName("opt_%s" % i)
                    self.goptionstext.append(opt)
            spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            fl.addItem(spacerItem4)
        #doclink = os.path.join(grassenv['GISBASE'], 'docs/html', self.commandname)
        doclink = 'https://grass.osgeo.org/grass73/manuals/%s' % self.commandname
        #self.w.manualpage.load(QUrl('file://%s.html' % doclink))
        self.w.manualpage.load(QUrl(doclink))
        #self.w.runcommand.clicked.connect(self.getParam)
        self.w.copycommand.clicked.connect(self.messagecopy)

        # this doesn't work when in mdi mode ...
        #self.w.closecommand.clicked.connect(self.w.close)
        self.w.closecommand.hide()

        for i in self.gflags:
            i.valueUpdated.connect(self.handleValueUpdated)
        for i in self.goptionsstring:
            i.valueUpdated.connect(self.handleValueUpdated)
        for i in self.goptionsmultistring:
            i.valueUpdated.connect(self.handleValueUpdated)
        for i in self.goptionstext:
            i.valueUpdated.connect(self.handleValueUpdated)
        for i in self.goptionsnum:
            i.valueUpdated.connect(self.handleValueUpdated)
        for i in self.prompts:
            i.valueUpdated.connect(self.handleValueUpdated)
        for i in self.filesprompts:
            i.valueUpdated.connect(self.handleValueUpdated)
        for i in self.datasurcesprompts:
            i.valueUpdated.connect(self.handleValueUpdated)

        self.status = {}
        self.status['flags'] = []
        for i in range(self.w.commandtab.count()):
            #print(i, self.w.commandtab.widget(i).objectName())
            if self.w.commandtab.widget(i).objectName() == 'Required':
                self.w.commandtab.tabBar().moveTab(i, 0)
            if self.w.commandtab.widget(i).objectName() == 'CommandOutput':
                self.w.commandtab.tabBar().moveTab(i, self.w.commandtab.count() - 2)
            if self.w.commandtab.widget(i).objectName() == 'Manual':
                self.w.commandtab.tabBar().moveTab(i, self.w.commandtab.count() - 1)
        print(self.w.commandtab.count())
        self.w.commandtab.setCurrentIndex(0)
        #self.w.show()


    def handleValueUpdated(self, value):
        if len(value.split('=')) > 1:
            self.status[value.split('=')[0]] = value.split('=')[1]
        if len(value.split(':')) > 1:
            if value.split(':')[1] != 'None':
                self.status['flags'].append(value.split(':')[1])
            else:
                self.status['flags'] = [i for i in self.status['flags'] if value.split(':')[0] not in i]
        paramstatus = ' '.join(['{}={}'.format(k, v) for k, v in self.status.items() if k != 'flags'])
        flagstatus = ' '.join(self.status['flags'])
        self.message = self.commandname+' '+paramstatus+' '+flagstatus
        #self.w.statusbar.showMessage(self.message)
        self.w.status.setText(self.message)
        QtWidgets.QApplication.processEvents()

    def messagecopy(self):
        cb = QtWidgets.QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(self.message, mode=cb.Clipboard)
        #print(self.w.commandtab.widget(0).objectName())
        self.valueUpdated.emit(self.message)


'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ss = None
    arg1 = ''
    if len(sys.argv) > 1:
        arg1 = sys.argv[1]
    app.processEvents()
    p = GrassModule()
    #p.init()
    sys.exit(app.exec_())
'''