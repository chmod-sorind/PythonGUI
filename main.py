from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtGui import QStandardItem, QStandardItemModel
import sys
import telnetlib
import time
import MyPythonWindow
import threading


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
        self.buttonSendCommand.clicked.connect(self.startTreading())
        #self.buttonStopTelnet.clicked.connect(self.startTreading)

    def buttonAddClicked(self):
        # ToDo: If self.lineEditCommand.text() is empty string don't add it to the list.
        # ToDo: Add some sort of feedback to let the user know that the lineEditCommand is empty.
        # ToDo: Make key ENTER add items to the list.
        _getTextFromLineEditHost = self.lineEditHost.text()
        item = QStandardItem()
        item.setText(_getTextFromLineEditHost)
        item.setAccessibleText(_getTextFromLineEditHost)
        item.setCheckable(True)
        self.model.appendRow(item)
        self.statusBar().showMessage(_getTextFromLineEditHost + ' was added to the list')
        print(_getTextFromLineEditHost + ' was added to the list')

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

    def run_telnet_connection(self):
        _getTextFromLineEditCommand = self.lineEditCommand.text()
        _getTextFromLineEditPort = self.lineEditPort.text()
        _getTextFromCountBox = int(self.countBox.text())
        _getTextFromFrequencyBox = float(self.frequencyBox.text())
        for pollNum in range(1, _getTextFromCountBox + 1):
            for index in range(self.model.rowCount()):
                ipItem = self.model.item(index)
                ipItemText = ipItem.accessibleText()
                if ipItem.checkState() == QtCore.Qt.Checked:
                    try:
                        telnet = telnetlib.Telnet(ipItemText, _getTextFromLineEditPort)
                        telnet.write((_getTextFromLineEditCommand + '\n').encode('UTF-8'))
                        telnet.close()
                        print("#{0} Command {1} sent to {2}".format(pollNum, _getTextFromLineEditCommand, ipItemText))
                    except Exception as e:
                        print(e)
            if pollNum < _getTextFromCountBox:
                pollRate = int(_getTextFromFrequencyBox)
                print("Sleeping for {} seconds".format(pollRate))
                while pollRate > 0:
                    minutes, sec = divmod(int(pollRate), 60)
                    countdown = '{:02d}:{:02d}'.format(minutes, sec)
                    pollLeft = _getTextFromCountBox - pollNum
                    if pollLeft > 1:
                        self.statusBar().showMessage("{} Until next poll. {} polls left".format(countdown, pollLeft))
                    else:
                        self.statusBar().showMessage("{} Until next poll. {} poll left".format(countdown, pollLeft))
                    print(countdown, end='\r')
                    time.sleep(1)
                    pollRate -= 1
        self.statusBar().showMessage("Done!")
        return 0

    def startThreading(self):
        telnetThread = threading.Thread(target=self.run_telnet_connection,)
        telnetThread.start()

    def buttonQuitApp(self):
        self.statusBar().showMessage('Aplication will now exit.')
        time.sleep(1)
        quit()


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = MyApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
