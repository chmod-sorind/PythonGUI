# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyPythonWindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

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
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        MainWindow.setFont(font)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Back-upFiles/UI/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
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
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.centralwidget.setFont(font)
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
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.rightTopLayout = QtWidgets.QVBoxLayout()
        self.rightTopLayout.setSpacing(5)
        self.rightTopLayout.setObjectName("rightTopLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEditHost = QtWidgets.QLineEdit(self.tabSetup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditHost.sizePolicy().hasHeightForWidth())
        self.lineEditHost.setSizePolicy(sizePolicy)
        self.lineEditHost.setMinimumSize(QtCore.QSize(263, 27))
        self.lineEditHost.setMaximumSize(QtCore.QSize(263, 27))
        self.lineEditHost.setToolTip("")
        self.lineEditHost.setStatusTip("")
        self.lineEditHost.setWhatsThis("")
        self.lineEditHost.setAccessibleName("")
        self.lineEditHost.setAccessibleDescription("")
        self.lineEditHost.setText("")
        self.lineEditHost.setObjectName("lineEditHost")
        self.horizontalLayout_3.addWidget(self.lineEditHost)
        self.lineEditAddPort = QtWidgets.QLineEdit(self.tabSetup)
        self.lineEditAddPort.setMinimumSize(QtCore.QSize(40, 27))
        self.lineEditAddPort.setMaximumSize(QtCore.QSize(40, 27))
        self.lineEditAddPort.setObjectName("lineEditAddPort")
        self.horizontalLayout_3.addWidget(self.lineEditAddPort)
        self.rightTopLayout.addLayout(self.horizontalLayout_3)
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
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.rightTopLayout.addItem(spacerItem1)
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
        self.buttonStopTelnet.setEnabled(False)
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
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.treeView = QtWidgets.QTreeView(self.tabSetup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy)
        self.treeView.setMinimumSize(QtCore.QSize(315, 300))
        self.treeView.setMaximumSize(QtCore.QSize(315, 300))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.treeView.setFont(font)
        self.treeView.setWhatsThis("")
        self.treeView.setInputMethodHints(QtCore.Qt.ImhNone)
        self.treeView.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.treeView.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.treeView.setLineWidth(2)
        self.treeView.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.treeView.setProperty("showDropIndicator", True)
        self.treeView.setDragEnabled(True)
        self.treeView.setDragDropOverwriteMode(False)
        self.treeView.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.treeView.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.treeView.setAlternatingRowColors(True)
        self.treeView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.treeView.setSortingEnabled(True)
        self.treeView.setAnimated(True)
        self.treeView.setAllColumnsShowFocus(True)
        self.treeView.setObjectName("treeView")
        self.verticalLayout_6.addWidget(self.treeView)
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
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 3, 1, 1, 1)
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
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonLoadConigFile = QtWidgets.QPushButton(self.tabSetup)
        self.buttonLoadConigFile.setMinimumSize(QtCore.QSize(0, 27))
        self.buttonLoadConigFile.setMaximumSize(QtCore.QSize(16777215, 27))
        self.buttonLoadConigFile.setObjectName("buttonLoadConigFile")
        self.horizontalLayout.addWidget(self.buttonLoadConigFile)
        self.buttonSaveConfigToFile = QtWidgets.QPushButton(self.tabSetup)
        self.buttonSaveConfigToFile.setMinimumSize(QtCore.QSize(0, 27))
        self.buttonSaveConfigToFile.setMaximumSize(QtCore.QSize(16777215, 27))
        self.buttonSaveConfigToFile.setObjectName("buttonSaveConfigToFile")
        self.horizontalLayout.addWidget(self.buttonSaveConfigToFile)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
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
        self.lineEditHost.setToolTip('what is this <b>***** !</b>')
        self.lineEditAddPort.setPlaceholderText(_translate("MainWindow", "port"))
        self.buttonAddItemToList.setText(_translate("MainWindow", "Add Host"))
        self.buttonRemoveItemFromList.setText(_translate("MainWindow", "Remove Host"))
        self.labelCount.setText(_translate("MainWindow", "Poll Count"))
        self.labelFrequency.setText(_translate("MainWindow", "Poll Rate"))
        self.lineEditPort.setPlaceholderText(_translate("MainWindow", "Targe Port"))
        self.lineEditCommand.setPlaceholderText(_translate("MainWindow", "Telnet Command"))
        self.buttonStartTelnet.setText(_translate("MainWindow", "Send Command"))
        self.buttonStopTelnet.setText(_translate("MainWindow", "Stop Execution"))
        self.checkBoxCheckAll.setText(_translate("MainWindow", "Check/Uncheck All"))
        self.checkBoxDoNothing.setText(_translate("MainWindow", "Check Box"))
        self.buttonCancel.setText(_translate("MainWindow", "Exit Application"))
        self.buttonLoadConigFile.setText(_translate("MainWindow", "Load Configuration"))
        self.buttonSaveConfigToFile.setText(_translate("MainWindow", "Save Configuration"))
        self.tabS.setTabText(self.tabS.indexOf(self.tabSetup), _translate("MainWindow", "Setup"))
        self.logsBox.setDocumentTitle(_translate("MainWindow", "Telnet Logs"))
        self.tabS.setTabText(self.tabS.indexOf(self.tabLogs), _translate("MainWindow", "Logs"))

