from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtCore import *
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QFileDialog
import sys
import telnetlib
import time
import MyPythonWindow


class newTelnetThread(QThread):
    finishedSignal = pyqtSignal()

    def __init__(self, telnetParams, listOfHosts):
        """
        Make a new thread instance with the specified
        telnetParams as the first argument. The telnetParams argument
        will be stored in an instance variable called telnetParams
        which then can be accessed by all other class instance functions
        :param telnetParams: A list of telnet param names
        :type telnetParams: list
        """
        QThread.__init__(self)
        self.telnetParams = telnetParams
        self.listOfHosts = listOfHosts

    def __del__(self):
        self.wait()

    def _run_telnet_connection(self):
        count = self.telnetParams[0]
        rate = self.telnetParams[1]
        port = self.telnetParams[2]
        command = self.telnetParams[3]
        print(self.telnetParams)
        for pollNum in range(1, count + 1):
            for ipHost in self.listOfHosts:
                    try:
                        telnet = telnetlib.Telnet(ipHost, port)
                        telnet.write((command + '\n').encode('UTF-8'))
                        telnet.close()
                        print(("#{0} Command {1} sent to {2}".format(pollNum, command, ipHost)))
                    except Exception as e:
                        print("HOST [{0}]: ".format(ipHost), e)
            if pollNum < count:
                pollRate = int(rate)
                print("Sleeping for {} seconds".format(pollRate))
                while pollRate > 0:
                    minutes, sec = divmod(int(pollRate), 60)
                    countdown = '{:02d}:{:02d}'.format(minutes, sec)
                    #pollLeft = count - pollNum
                    #if pollLeft > 1:
                        #self.statusBar().showMessage("{} Until next poll. {} polls left".format(countdown, pollLeft))
                        #print("{} Until next poll. {} polls left".format(countdown, pollLeft), end='\r')
                    #else:
                        #self.statusBar().showMessage("{} Until next poll. {} poll left".format(countdown, pollLeft))
                        #print("{} Until next poll. {} poll left".format(countdown, pollLeft), end='\r')
                    print(countdown, end='\r')
                    time.sleep(1)
                    pollRate -= 1

    def run(self):
        self._run_telnet_connection()
        self.finishedSignal.emit()


class MyApp(QtWidgets.QMainWindow, MyPythonWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyApp, self).__init__(parent)
        self.setupUi(self)

        # Button Functionality.
        self.buttonAddItemToList.clicked.connect(self.buttonAddClicked)
        self.buttonCancel.clicked.connect(self.buttonQuitApp)
        self.buttonRemoveItemFromList.clicked.connect(self.buttonRemoveChecked)
        self.model = QStandardItemModel(self.listView)
        self.listView.setModel(self.model)
        self.buttonStartTelnet.clicked.connect(self.startTelnetTreading)
        self.buttonStopTelnet.clicked.connect(self.stopTelnetThreading)
        self.buttonLoadFile.clicked.connect(self.openFile)
        self.checkBoxCheckAll.stateChanged.connect(self.CheckUncheckAll)

    def buttonAddClicked(self):
        # ToDo: Make key ENTER add items to the list.
        _getTextFromLineEditHost = self.lineEditHost.text()
        if _getTextFromLineEditHost:
            item = QStandardItem()
            item.setText(_getTextFromLineEditHost)
            item.setAccessibleText(_getTextFromLineEditHost)
            item.setCheckable(True)
            self.model.appendRow(item)
            self.lineEditHost.clear()
            self.statusBar().showMessage(_getTextFromLineEditHost + ' was added to the list')
            print(_getTextFromLineEditHost + ' was added to the list')
        else:
            self.statusBar().showMessage('Nothing to add')

    def CheckUncheckAll(self):
        for index in range(self.model.rowCount()):
            item = self.model.item(index)
            if self.checkBoxCheckAll.isChecked():
                item.setCheckState(QtCore.Qt.Checked)
            else:
                item.setCheckState(QtCore.Qt.Unchecked)

    def buttonRemoveChecked(self):
        try:
            for index in range(self.model.rowCount()):
                item = self.model.item(index)
                if item.checkState() == QtCore.Qt.Checked:
                    self.model.removeRow(index)
        except AttributeError as error:
            print(error)
            pass

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        print(sender.text() + ' was pressed')

    def buttonQuitApp(self):
        self.statusBar().showMessage('Aplication will now exit.')
        time.sleep(1)
        quit()

    def startTelnetTreading(self):
        _com = str(self.lineEditCommand.text())
        _port = str(self.lineEditPort.text())
        _count = int(self.countBox.text())
        _rate = float(self.frequencyBox.text())
        telnetParams_list = [_count, _rate, _port, _com]

        ipHosts_list = []
        for index in range(self.model.rowCount()):
            ipItem = self.model.item(index)
            ipItemText = ipItem.accessibleText()
            if ipItem.checkState() == QtCore.Qt.Checked:
                ipHosts_list.append(ipItemText)

        self.get_thread = newTelnetThread(telnetParams_list, ipHosts_list)
        self.get_thread.start()
        self.buttonStopTelnet.setEnabled(True)
        self.get_thread.finishedSignal.connect(self.stopTelnetThreading)
        self.buttonStopTelnet.clicked.connect(self.get_thread.terminate)
        self.buttonStartTelnet.setEnabled(False)

    def stopTelnetThreading(self):
        self.buttonStopTelnet.setEnabled(False)
        self.buttonStartTelnet.setEnabled(True)

    def openFile(self):
        fileName = QFileDialog.getOpenFileName(self, 'Load file')
        if fileName[0]:
            with open(fileName[0]) as IP_LIST:
                line = IP_LIST.read().splitlines()
                for f in line:
                    item = QStandardItem()
                    item.setText(f)
                    item.setAccessibleText(f)
                    item.setCheckable(True)
                    self.model.appendRow(item)
        self.statusBar().showMessage("{} loaded...".format(fileName[0]))


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = MyApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
