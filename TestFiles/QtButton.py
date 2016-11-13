import sys
import time
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonQuitApp)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        print(sender.text() + ' was pressed')

    def buttonQuitApp(self):
        sender = self.sender()
        _quit_in = 3
        while _quit_in > 0:
            self.statusBar().showMessage('Aplication will exit in {}'.format(_quit_in))
            print(sender.text() + ' was pressed')
            _quit_in -= 1
            time.sleep(1)
        quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
