from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
import sys
import MyPythonWindow


class MyApp(QtWidgets.QMainWindow, MyPythonWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyApp, self).__init__(parent)
        self.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = MyApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
