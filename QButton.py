from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QWidget, QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from random import randrange


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.button = QPushButton('Test', self)
        self.label = QLabel(self)
        self.button.clicked.connect(self.handleButton)
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.button)

    def handleButton(self):
        _random_integer = randrange(0, 1000000)
        _random = str(_random_integer)
        self.label.setText(_random)

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())