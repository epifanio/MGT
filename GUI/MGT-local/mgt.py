import sys
import os
from PyQt5.QtWidgets import QApplication, \
                            QAction, \
                            QWidget, \
                            QAbstractItemView, \
                            QTableWidgetItem, \
                            QPushButton

from PyQt5.QtGui import QStandardItemModel, QIcon
from PyQt5 import QtCore

from mgtui import MainGui

from gcommands import get_command_list, get_command_description

from gmodules import GrassModule

from taskmanagerui import taskManagerUi

import functools



class MGT():

    def __init__(self):

        super(MGT, self).__init__()
        #
        # set the UI elements
        # MainGui() main user interface: self.ui
        # QMenuBar: self.ui.menubar
        # QMdiArea: self.ui.mdiArea
        # QDockArea: self.ui.taskmanager
        #
        self.ui = MainGui()
        #
        # taskManagerUi(): content of taskmanager QDockArea
        # lineEdit: self.takmanagerui.param
        # QTableWidget: self.takmanagerui.tasks
        # QPushButton: self.takmanagerui.runit, self.takmanagerui.clear
        #
        self.taskmanagerui = taskManagerUi()
        #
        # setup task manager elements:
        #
        self.rowcount = 0
        self.taskmodel = QStandardItemModel()
        self.commandrunning = 0
        self.mylistofprocesses = []
        #
        self.taskmanagerui.tasks.setColumnCount(6)
        self.taskmanagerui.tasks.setHorizontalHeaderLabels(
            ['Process', 'Parameter', 'STDOut', 'Status', 'Kill Switch', 'Print Output'])
        self.taskmanagerui.runit.clicked.connect(self.runcommand)
        self.taskmanagerui.clean.clicked.connect(self.cleanprocess)
        ###


        self.grassdialogs = []
        General = self.ui.menubar.addMenu('&General')
        Raster = self.ui.menubar.addMenu('&Raster')
        Vector = self.ui.menubar.addMenu('&Vector')
        Temporal = self.ui.menubar.addMenu('&Temporal')
        db = self.ui.menubar.addMenu('&db')
        Display = self.ui.menubar.addMenu('&Display')
        self.menubars={'g': General, 'r': Raster, 'v': Vector, 't': Temporal, 'db': db, 'd': Display}
        commandlist = get_command_list()
        #commandlist = get_message('g.search.modules', ip=self.serverconf['IP'], port=self.serverconf['PORT'], socket=self.socket)
        for i, name in enumerate(commandlist):
            if name.split('.')[0] in list(self.menubars.keys()):
                Action = QAction(QIcon('grass_logo.png'), name, self.ui)
                actionStatusTip = 'action %s ! ' % name
                Action.setStatusTip(actionStatusTip)
                Action.triggered.connect(functools.partial(self.opengrassdialog, name))
                self.menubars[name.split('.')[0]].addAction(Action)
        for i in self.grassdialogs:
            i.valueUpdated.connect(self.handleValueUpdated)
        self.ui.taskmanager.setWidget(self.taskmanagerui)
        #self.taskmanagerui.tasks.repaint()


        self.ui.show()


    def handleValueUpdated(self, value):
        self.taskmanagerui.param.setText(value)
        QApplication.processEvents()




    def opengrassdialog(self, name):
        self.grassdialog = GrassModule(name)
        #self.grassdialog.w.show()

        self.ui.mdiArea.addSubWindow(self.grassdialog.w)
        self.grassdialog.w.show()
        self.grassdialogs.append(self.grassdialog)
        self.grassdialog.valueUpdated.connect(self.handleValueUpdated)


    # TaskManager methods

    def cleanprocess(self):
        self.taskmanagerui.tasks.setSelectionMode(QAbstractItemView.MultiSelection)
        indextoremove=[]
        for i, v in enumerate(self.mylistofprocesses):
            if v.state() == 0:
                indextoremove.append(i)
                self.taskmanagerui.tasks.selectRow(i)
                self.rowcount=self.rowcount-1
            else:
                print(v.pid())
                #self.taskmanagerui.tasks.repaint()
        index_list = []
        for model_index in self.taskmanagerui.tasks.selectionModel().selectedRows():
            index = QtCore.QPersistentModelIndex(model_index)
            index_list.append(index)
        for index in index_list:
            self.taskmanagerui.tasks.removeRow(index.row())

        self.mylistofprocesses = [i for j, i in enumerate(self.mylistofprocesses) if j not in indextoremove]
        self.taskmanagerui.tasks.setSelectionMode(QAbstractItemView.NoSelection)
        self.taskmanagerui.tasks.repaint()

    def runcommand2(self):
        # add a record in the QTableWidget
        # updating its row number at each run
        self.taskmanagerui.tasks.repaint()
        self.stdoutput=[]
        self.rowcount = self.rowcount + 1
        self.taskmanagerui.tasks.setRowCount(self.rowcount)
        print(self.rowcount)
        # add column 0: command string
        self.c1 = QTableWidgetItem()
        self.c1.setText("%s" % os.path.join(os.getcwd(), self.taskmanagerui.param.text()))
        self.taskmanagerui.tasks.setItem(self.rowcount - 1, 0, self.c1)

        # add column 1: parameter string
        self.c2 = QTableWidgetItem()
        self.c2.setText("%s" % self.taskmanagerui.param.text())
        self.taskmanagerui.tasks.setItem(self.rowcount - 1, 1, self.c2)

        # add column 2 to store the  Process StandardOutput
        stdout_item = QTableWidgetItem()
        self.taskmanagerui.tasks.setItem(self.rowcount - 1, 2, stdout_item)

        # add column 3: index to store the process status (0: Not Running, 1: Starting, 2: Running)
        status_item = QTableWidgetItem()
        self.taskmanagerui.tasks.setItem(self.rowcount - 1, 3, status_item)

        # add column 4: kill button to kill the relative process
        killbtn = QPushButton(self.taskmanagerui.tasks)
        killbtn.setText('Kill')
        self.taskmanagerui.tasks.setCellWidget(self.rowcount - 1, 4, killbtn)

        # add column 5: print button to print the complete output of the relative process
        printbtn = QPushButton(self.taskmanagerui.tasks)
        printbtn.setText('Print')
        self.taskmanagerui.tasks.setCellWidget(self.rowcount - 1, 5, printbtn)
        # Initiate a QProcess running a system command

        # Initiate a QProcess running a system command
        ## process = QtCore.QProcess()
        process = myQprocess()
        command = 'python3' + ' ' + os.getcwd() + '/' + 'simplerun.py' + ' ' + '10'
        process.setProcessChannelMode(QtCore.QProcess.MergedChannels)
        # connect the stdout_item to the Process StandardOutput
        # it gets constantly update as the process emit std output
        ## process.readyReadStandardOutput.connect(lambda: stdout_item.setText(str(process.readAllStandardOutput().data().decode('utf-8'))))

        # connect the kill button to the process.kill method, to stop the process
        killbtn.clicked.connect(process.kill)
        killbtn.clicked.connect(lambda: killbtn.setText('Killed'))

        printbtn.clicked.connect(lambda: print(self.stdoutput))

        process.valueUpdated.connect(stdout_item.setText)
        process.valueUpdated.connect(self.stdoutput.append)
        # start the process
        process.start(command)
        # connect the kill button to the process.kill method, to stop the process
        # Connect the process to the stateChanged method, to update its status
        status = {QtCore.QProcess.NotRunning: "Not Running",
                  QtCore.QProcess.Starting: "Starting",
                  QtCore.QProcess.Running: "Running"}
        process.stateChanged.connect(lambda state: status_item.setText(status[state]))
        process.stateChanged.connect(
            lambda state: killbtn.setText('Terminated') if status[state] == "Not Running" else killbtn.setText('Kill'))
        process.stateChanged.connect(
            lambda state: killbtn.setEnabled(False) if status[state] == "Not Running" else killbtn.setText('Kill'))
        # append the process to a list so that it doesn't get destroyed at each run
        self.mylistofprocesses.append(process)
        self.taskmanagerui.tasks.repaint()
        print('runnami')

    def runcommand(self):
        # add a record in the QTableWidget
        # updating its row number at each run
        self.stdoutput = []
        self.rowcount = self.rowcount + 1
        self.taskmanagerui.tasks.setRowCount(self.rowcount)

        # add column 0: command string
        self.c1 = QTableWidgetItem()
        self.c1.setText(self.taskmanagerui.param.text())
        self.taskmanagerui.tasks.setItem(self.rowcount - 1, 0, self.c1)

        # add column 1: parameter string
        self.c2 = QTableWidgetItem()
        self.c2.setText("%s" % self.taskmanagerui.param.text().split()[1:])
        self.taskmanagerui.tasks.setItem(self.rowcount - 1, 1, self.c2)

        # add column 2 to store the  Process StandardOutput
        stdout_item = QTableWidgetItem()
        self.taskmanagerui.tasks.setItem(self.rowcount - 1, 2, stdout_item)

        # add column 3: index to store the process status (0: Not Running, 1: Starting, 2: Running)
        status_item = QTableWidgetItem()
        self.taskmanagerui.tasks.setItem(self.rowcount - 1, 3, status_item)

        # add column 4: kill button to kill the relative process
        killbtn = QPushButton(self.taskmanagerui.tasks)
        killbtn.setText('Kill')
        self.taskmanagerui.tasks.setCellWidget(self.rowcount - 1, 4, killbtn)

        # add column 5: print button to print the complete output of the relative process
        printbtn = QPushButton(self.taskmanagerui.tasks)
        printbtn.setText('Print')
        self.taskmanagerui.tasks.setCellWidget(self.rowcount - 1, 5, printbtn)

        # Initiate a QProcess running a system command
        ## process = QtCore.QProcess()
        process = myQprocess()
        print(process)
        #command = 'python3' + ' ' + os.getcwd() + '/' + self.commandlist.currentText() + ' ' + self.param.text()
        #command = 'python3.6' + ' ' + os.getcwd() + '/' + 'simplerun.py' + ' ' + '10'
        command = self.taskmanagerui.param.text()

        process.setProcessChannelMode(QtCore.QProcess.MergedChannels)
        # connect the stdout_item to the Process StandardOutput
        # it gets constantly update as the process emit std output
        ## process.readyReadStandardOutput.connect(lambda: stdout_item.setText(str(process.readAllStandardOutput().data().decode('utf-8'))))

        # connect the kill button to the process.kill method, to stop the process
        killbtn.clicked.connect(process.kill)
        killbtn.clicked.connect(lambda: killbtn.setText('Killed'))

        printbtn.clicked.connect(lambda: print(self.stdoutput))


        process.valueUpdated.connect(stdout_item.setText)
        process.valueUpdated.connect(self.stdoutput.append)
        # start the process
        #command = 'g.region -p'
        process.start(command)
        # connect the kill button to the process.kill method, to stop the process
        # Connect the process to the stateChanged method, to update its status
        status = {QtCore.QProcess.NotRunning: "Not Running",
                  QtCore.QProcess.Starting: "Starting",
                  QtCore.QProcess.Running: "Running"}
        process.stateChanged.connect(lambda state: status_item.setText(status[state]))
        process.stateChanged.connect(lambda state: killbtn.setText('Terminated') if status[state] == "Not Running" else killbtn.setText('Kill'))
        process.stateChanged.connect(lambda state: killbtn.setEnabled(False) if status[state] == "Not Running" else killbtn.setText('Kill'))
        # append the process to a list so that it doesn't get destroyed at each run
        self.mylistofprocesses.append(process)
        self.taskmanagerui.tasks.repaint()

    # MISC
    def debugfunction(self):
        print('###### DEBUG THIS ######')


class myQprocess(QtCore.QProcess):
    valueUpdated = QtCore.pyqtSignal(str)
    def __init__(self):
        super(myQprocess, self).__init__()
        self.readyReadStandardOutput.connect(self.printstdout)

    def printstdout(self):
        value = self.readAllStandardOutput().data().decode('utf-8')
        self.valueUpdated.emit(value)


def main():
    app = QApplication(sys.argv)
    ex = MGT()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
