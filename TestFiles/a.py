from PyQt4 import QtCore, QtGui
import sys, time




class MainWindow (QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.buttonDaemon = QtGui.QPushButton(self)
        self.layout = QtGui.QVBoxLayout(self)
        self.layout.addWidget(self.buttonDaemon)
        self.setLayout(self.layout)

        self.thread = Worker()
        self.connect(self.thread, QtCore.SIGNAL('finished()'), self.unfreezeUi)
        self.connect(self.thread, QtCore.SIGNAL('terminated()'), self.unfreezeUi)
        #self.thread.stop.connect(self.stopped) # part of proposed solution
        self.connect(self.thread, QtCore.SIGNAL('stopped(int)'), self.stopped) #adapted from proposed solution

        self.connect(self.buttonDaemon, QtCore.SIGNAL('clicked()'), self.pressDaemon)

    def unfreezeUi (self):
        self.buttonDaemon.setEnabled(True)

    # the problem begins below: I'm not using signals, or queue, or whatever, while I believe I should for StopSignal and DaemonRunning
    def pressDaemon (self):
        self.buttonDaemon.setEnabled(False)
        if self.thread.isDaemonRunning():
            self.thread.setDaemonStopSignal(True)
            self.buttonDaemon.setText('Daemon - run code every %s sec'% 1)
        else:
            self.thread.startDaemon()
            self.buttonDaemon.setText('Stop Daemon')
            self.buttonDaemon.setEnabled(True)

    # part of proposed solution
    def stopped (self, val):
        print 'stopped ' + str(val)

class Worker (QtCore.QThread):
    daemonIsRunning = False
    daemonStopSignal = False
    daemonCurrentDelay = 0

    def isDaemonRunning (self): return self.daemonIsRunning
    def setDaemonStopSignal (self, bool): self.daemonStopSignal = bool

    def __init__ (self, parent = None):
        QtCore.QThread.__init__(self, parent)
        self.exiting = False
        self.thread_to_run = None

    def __del__ (self):
        self.exiting = True
        self.thread_to_run = None
        self.wait()

    def run (self):
        if self.thread_to_run != None:
            self.thread_to_run(mode='continue')

    #stop = QtCore.pyqtSignal(int) # part of proposed solution

    def startDaemon (self, mode = 'run'):
        if mode == 'run':
            self.thread_to_run = self.startDaemon # I'd love to be able to just pass this as an argument on start() below
            return self.start() # this will begin the thread

        # this is where the thread actually begins
        self.daemonIsRunning = True
        print 'Daemon started'
        self.daemonStopSignal = False
        sleepStep = 0.1 # don't know how to interrupt while sleeping - so the less sleepStep, the faster StopSignal will work

        # begins the daemon in an "infinite" loop
        while self.daemonStopSignal == False and not self.exiting:
            print 'Daemon running'
            # here, do any kind of daemon service

            delay = 0
            while self.daemonStopSignal == False and not self.exiting and delay < 1:
                print 'Daemon sleeping'
                time.sleep(sleepStep) # delay is actually set by while, but this holds for 'sleepStep' seconds
                delay += sleepStep

        # daemon stopped, reseting everything
        self.daemonIsRunning = False
        print 'Daemon stopped'
        #self.stop.emit(self.daemonIsRunning) # part of proposed solution
        self.emit(QtCore.SIGNAL('stopped(int)'), self.daemonIsRunning) # adapted from proposed solution
        self.emit(QtCore.SIGNAL('terminated'))

def main (args):
    app = QtGui.QApplication(args)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main(sys.argv)