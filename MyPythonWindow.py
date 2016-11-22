from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(680, 482)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(680, 482))
        MainWindow.setMaximumSize(QtCore.QSize(680, 482))
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(670, 460))
        self.centralwidget.setMaximumSize(QtCore.QSize(670, 460))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabS = QtWidgets.QTabWidget(self.centralwidget)
        self.tabS.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabS.sizePolicy().hasHeightForWidth())
        self.tabS.setSizePolicy(sizePolicy)
        self.tabS.setMinimumSize(QtCore.QSize(660, 420))
        self.tabS.setMaximumSize(QtCore.QSize(660, 420))
        self.tabS.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabS.setObjectName("tabS")
        self.tabSetup = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabSetup.sizePolicy().hasHeightForWidth())
        self.tabSetup.setSizePolicy(sizePolicy)
        self.tabSetup.setMinimumSize(QtCore.QSize(650, 0))
        self.tabSetup.setMaximumSize(QtCore.QSize(660, 420))
        self.tabSetup.setObjectName("tabSetup")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tabSetup)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.rightTopLayout = QtWidgets.QVBoxLayout()
        self.rightTopLayout.setSpacing(5)
        self.rightTopLayout.setObjectName("rightTopLayout")
        self.lineEditHost = QtWidgets.QLineEdit(self.tabSetup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditHost.sizePolicy().hasHeightForWidth())
        self.lineEditHost.setSizePolicy(sizePolicy)
        self.lineEditHost.setMinimumSize(QtCore.QSize(313, 27))
        self.lineEditHost.setMaximumSize(QtCore.QSize(313, 27))
        self.lineEditHost.setText("")
        self.lineEditHost.setObjectName("lineEditHost")
        self.rightTopLayout.addWidget(self.lineEditHost)
        self.buttonAddItemToList = QtWidgets.QPushButton(self.tabSetup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonAddItemToList.sizePolicy().hasHeightForWidth())
        self.buttonAddItemToList.setSizePolicy(sizePolicy)
        self.buttonAddItemToList.setMinimumSize(QtCore.QSize(313, 27))
        self.buttonAddItemToList.setMaximumSize(QtCore.QSize(313, 27))
        self.buttonAddItemToList.setObjectName("buttonAddItemToList")
        self.rightTopLayout.addWidget(self.buttonAddItemToList)
        self.buttonRemoveItemFromList = QtWidgets.QPushButton(self.tabSetup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonRemoveItemFromList.sizePolicy().hasHeightForWidth())
        self.buttonRemoveItemFromList.setSizePolicy(sizePolicy)
        self.buttonRemoveItemFromList.setMinimumSize(QtCore.QSize(313, 27))
        self.buttonRemoveItemFromList.setMaximumSize(QtCore.QSize(313, 27))
        self.buttonRemoveItemFromList.setObjectName("buttonRemoveItemFromList")
        self.rightTopLayout.addWidget(self.buttonRemoveItemFromList)
        self.rightMiddleLayout = QtWidgets.QFormLayout()
        self.rightMiddleLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.rightMiddleLayout.setObjectName("rightMiddleLayout")
        self.checkBoxesLayout = QtWidgets.QVBoxLayout()
        self.checkBoxesLayout.setObjectName("checkBoxesLayout")
        self.countBox = QtWidgets.QSpinBox(self.tabSetup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.countBox.sizePolicy().hasHeightForWidth())
        self.countBox.setSizePolicy(sizePolicy)
        self.countBox.setMinimumSize(QtCore.QSize(93, 27))
        self.countBox.setMaximum(9999)
        self.countBox.setObjectName("countBox")
        self.checkBoxesLayout.addWidget(self.countBox)
        self.frequencyBox = QtWidgets.QDoubleSpinBox(self.tabSetup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frequencyBox.sizePolicy().hasHeightForWidth())
        self.frequencyBox.setSizePolicy(sizePolicy)
        self.frequencyBox.setMinimumSize(QtCore.QSize(93, 27))
        self.frequencyBox.setSpecialValueText("")
        self.frequencyBox.setMaximum(10000.0)
        self.frequencyBox.setSingleStep(1.0)
        self.frequencyBox.setObjectName("frequencyBox")
        self.checkBoxesLayout.addWidget(self.frequencyBox)
        self.rightMiddleLayout.setLayout(2, QtWidgets.QFormLayout.LabelRole, self.checkBoxesLayout)
        self.labelLayout = QtWidgets.QVBoxLayout()
        self.labelLayout.setObjectName("labelLayout")
        self.labelCount = QtWidgets.QLabel(self.tabSetup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelCount.sizePolicy().hasHeightForWidth())
        self.labelCount.setSizePolicy(sizePolicy)
        self.labelCount.setObjectName("labelCount")
        self.labelLayout.addWidget(self.labelCount)
        self.labelFrequency = QtWidgets.QLabel(self.tabSetup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelFrequency.sizePolicy().hasHeightForWidth())
        self.labelFrequency.setSizePolicy(sizePolicy)
        self.labelFrequency.setObjectName("labelFrequency")
        self.labelLayout.addWidget(self.labelFrequency)
        self.rightMiddleLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.labelLayout)
        self.rightTopLayout.addLayout(self.rightMiddleLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.rightTopLayout.addItem(spacerItem)
        self.lineEditPort = QtWidgets.QLineEdit(self.tabSetup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditPort.sizePolicy().hasHeightForWidth())
        self.lineEditPort.setSizePolicy(sizePolicy)
        self.lineEditPort.setMinimumSize(QtCore.QSize(313, 27))
        self.lineEditPort.setMaximumSize(QtCore.QSize(313, 27))
        self.lineEditPort.setObjectName("lineEditPort")
        self.rightTopLayout.addWidget(self.lineEditPort)
        self.lineEditCommand = QtWidgets.QLineEdit(self.tabSetup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditCommand.sizePolicy().hasHeightForWidth())
        self.lineEditCommand.setSizePolicy(sizePolicy)
        self.lineEditCommand.setMinimumSize(QtCore.QSize(313, 27))
        self.lineEditCommand.setMaximumSize(QtCore.QSize(313, 27))
        self.lineEditCommand.setObjectName("lineEditCommand")
        self.rightTopLayout.addWidget(self.lineEditCommand)
        self.buttonStartTelnet = QtWidgets.QPushButton(self.tabSetup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonStartTelnet.sizePolicy().hasHeightForWidth())
        self.buttonStartTelnet.setSizePolicy(sizePolicy)
        self.buttonStartTelnet.setMinimumSize(QtCore.QSize(313, 27))
        self.buttonStartTelnet.setMaximumSize(QtCore.QSize(313, 27))
        self.buttonStartTelnet.setObjectName("buttonStartTelnet")
        self.rightTopLayout.addWidget(self.buttonStartTelnet)
        self.buttonStopTelnet = QtWidgets.QPushButton(self.tabSetup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonStopTelnet.sizePolicy().hasHeightForWidth())
        self.buttonStopTelnet.setSizePolicy(sizePolicy)
        self.buttonStopTelnet.setMinimumSize(QtCore.QSize(313, 27))
        self.buttonStopTelnet.setMaximumSize(QtCore.QSize(313, 27))
        self.buttonStopTelnet.setObjectName("buttonStopTelnet")
        self.rightTopLayout.addWidget(self.buttonStopTelnet)
        self.gridLayout.addLayout(self.rightTopLayout, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonSaveToFile = QtWidgets.QPushButton(self.tabSetup)
        self.buttonSaveToFile.setObjectName("buttonSaveToFile")
        self.horizontalLayout.addWidget(self.buttonSaveToFile)
        self.buttonLoadFile = QtWidgets.QPushButton(self.tabSetup)
        self.buttonLoadFile.setObjectName("buttonLoadFile")
        self.horizontalLayout.addWidget(self.buttonLoadFile)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 1)
        self.buttonCancel = QtWidgets.QPushButton(self.tabSetup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonCancel.sizePolicy().hasHeightForWidth())
        self.buttonCancel.setSizePolicy(sizePolicy)
        self.buttonCancel.setMinimumSize(QtCore.QSize(313, 27))
        self.buttonCancel.setMaximumSize(QtCore.QSize(313, 27))
        self.buttonCancel.setObjectName("buttonCancel")
        self.gridLayout.addWidget(self.buttonCancel, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.listView = QtWidgets.QListView(self.tabSetup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy)
        self.listView.setMinimumSize(QtCore.QSize(315, 300))
        self.listView.setMaximumSize(QtCore.QSize(315, 300))
        self.listView.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.listView.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listView.setLineWidth(2)
        self.listView.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.listView.setProperty("showDropIndicator", True)
        self.listView.setDragEnabled(True)
        self.listView.setDragDropOverwriteMode(False)
        self.listView.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.listView.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.listView.setAlternatingRowColors(True)
        self.listView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.listView.setObjectName("listView")
        self.verticalLayout_6.addWidget(self.listView)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBoxCheckAll = QtWidgets.QCheckBox(self.tabSetup)
        self.checkBoxCheckAll.setObjectName("checkBoxCheckAll")
        self.horizontalLayout_2.addWidget(self.checkBoxCheckAll)
        self.checkBoxDoNothing = QtWidgets.QCheckBox(self.tabSetup)
        self.checkBoxDoNothing.setObjectName("checkBoxDoNothing")
        self.horizontalLayout_2.addWidget(self.checkBoxDoNothing)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_6, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.tabS.addTab(self.tabSetup, "")
        self.tabLogs = QtWidgets.QWidget()
        self.tabLogs.setObjectName("tabLogs")
        self.logsBox = QtWidgets.QTextEdit(self.tabLogs)
        self.logsBox.setGeometry(QtCore.QRect(10, 10, 640, 371))
        self.logsBox.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.logsBox.setAutoFillBackground(True)
        self.logsBox.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.logsBox.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.logsBox.setObjectName("logsBox")
        self.tabS.addTab(self.tabLogs, "")
        self.verticalLayout_2.addWidget(self.tabS)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabS.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Telnet Tools"))
        self.lineEditHost.setPlaceholderText(_translate("MainWindow", "hostname"))
        self.lineEditHost
        self.buttonAddItemToList.setText(_translate("MainWindow", "Add Host"))
        self.buttonRemoveItemFromList.setText(_translate("MainWindow", "Remove Host"))
        self.labelCount.setText(_translate("MainWindow", "Poll Count"))
        self.labelFrequency.setText(_translate("MainWindow", "Poll Rate"))
        self.lineEditPort.setPlaceholderText(_translate("MainWindow", "Targe Port"))
        self.lineEditCommand.setPlaceholderText(_translate("MainWindow", "Telnet Command"))
        self.buttonStartTelnet.setText(_translate("MainWindow", "Send Command"))
        self.buttonStopTelnet.setText(_translate("MainWindow", "Stop Execution"))
        self.buttonStopTelnet.setEnabled(False)
        self.buttonSaveToFile.setText(_translate("MainWindow", "Save list to file"))
        self.buttonLoadFile.setText(_translate("MainWindow", "Load File"))
        self.buttonCancel.setText(_translate("MainWindow", "Exit Application"))
        self.checkBoxCheckAll.setText(_translate("MainWindow", "Check/Uncheck All"))
        self.checkBoxDoNothing.setText(_translate("MainWindow", "Check Box"))
        self.tabS.setTabText(self.tabS.indexOf(self.tabSetup), _translate("MainWindow", "Setup"))
        self.logsBox.setDocumentTitle(_translate("MainWindow", "Telnet Logs"))
        self.tabS.setTabText(self.tabS.indexOf(self.tabLogs), _translate("MainWindow", "Logs"))

