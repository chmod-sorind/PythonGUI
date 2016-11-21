from sys import argv, exit
from PyQt4 import QtCore, QtGui, uic
import PyQt4
import time


class MainWindow (QtGui.QWidget):
    # this is just a reference and not really relevant to the question
    def __init__ (self, args):
        self.app = MainApp(args)
        QtGui.QWidget.__init__(self)
        self.buttonDaemon = QtGui.QPushButton(self)
        self.buttonConvert = QtGui.QPushButton(self)
        self.layout = QtGui.QVBoxLayout(self)
        self.layout.addWidget(self.buttonDaemon)
        self.layout.addWidget(self.buttonConvert)
        self.setLayout(self.layout)

        self.thread = Worker() # this does not begin a thread - look at "Worker.run" for mor details
        self.connect(self.thread, QtCore.SIGNAL('finished()'), self.unfreezeUi)
        self.connect(self.thread, QtCore.SIGNAL('terminated()'), self.unfreezeUi)
        self.thread.stop.connect(self.stopped)

        self.connect(self.buttonDaemon, QtCore.SIGNAL('clicked()'), self.pressDaemon)

    # the problem begins below: I'm not using signals, or queue, or whatever, while I believe I should
    def pressDaemon (self):
        self.buttonDaemon.setEnabled(False)
        if self.thread.isDaemonRunning():
            self.thread.setDaemonStopSignal(True)
            self.buttonDaemon.setText('Daemon - converts every %s sec'% 1)
        else:
            self.buttonConvert.setEnabled(False)
            self.thread.startDaemon()
            self.buttonDaemon.setText('Stop Daemon')
            self.buttonDaemon.setEnabled(True)

    def unfreezeUi(self):
        print '!!'

    def stopped(self, val):
        print 'stopped ' + str(val)

# this whole class is just another reference
class Worker (QtCore.QThread):
    daemonIsRunning = False
    daemonStopSignal = False
    daemonCurrentDelay = 0

    def isDaemonRunning (self): return self.daemonIsRunning
    def setDaemonStopSignal (self, bool): self.daemonStopSignal = bool

    def __init__ (self, parent = None):
        QtCore.QThread.__init__(self, parent)
        self.exiting = False
        self.thread_to_run = None  # which def will be running

    def __del__ (self):
        self.exiting = True
        self.thread_to_run = None
        self.wait()

    def run (self):
        if self.thread_to_run != None:
            self.thread_to_run(mode='continue')

    stop = QtCore.pyqtSignal(int)

    def startDaemon (self, mode = 'run'):
        if mode == 'run':
            self.thread_to_run = self.startDaemon # I'd love to be able to just pass this as an argument on start() below
            return self.start() # this will begin the thread

        # this is where the thread actually begins
        self.daemonIsRunning = True
        self.daemonStopSignal = False
        sleepStep = 0.1 # don't know how to interrupt while sleeping - so the less sleepStep, the faster StopSignal will work

        # begins the daemon in an "infinite" loop
        while self.daemonStopSignal == False and not self.exiting:
            # here, do any kind of daemon service

            delay = 0
            while self.daemonStopSignal == False and not self.exiting and delay < 1:
                time.sleep(sleepStep) # delay is actually set by while, but this holds for N second
                delay += sleepStep

        # daemon stopped, reseting everything
        self.daemonIsRunning = False
        self.stop.emit(self.daemonIsRunning)
        self.emit(QtCore.SIGNAL('terminated'))

class MainApp(QtGui.QApplication):
    def __init__(self, args):
        QtGui.QApplication.__init__(self, args)

if __name__ == "__main__":
    main = MainWindow(argv)
    main.show()
    exit(main.app.exec_())