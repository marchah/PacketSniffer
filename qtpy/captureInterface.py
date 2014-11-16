# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'captureInterface.ui'
#
# Created: Thu Nov  6 14:11:18 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_captureWindow(object):
    def setupUi(self, captureWindow):
        captureWindow.setObjectName(_fromUtf8("captureWindow"))
        captureWindow.resize(1298, 754)
        self.centralwidget = QtGui.QWidget(captureWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.trafficScroll = QtGui.QScrollArea(self.centralwidget)
        self.trafficScroll.setGeometry(QtCore.QRect(190, 100, 941, 551))
        self.trafficScroll.setWidgetResizable(True)
        self.trafficScroll.setObjectName(_fromUtf8("trafficScroll"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 939, 549))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.trafficTable = QtGui.QTableView(self.scrollAreaWidgetContents)
        self.trafficTable.setGeometry(QtCore.QRect(20, 20, 901, 521))
        self.trafficTable.setObjectName(_fromUtf8("trafficTable"))
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(340, 0, 101, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(220, 0, 67, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setGeometry(QtCore.QRect(80, 0, 67, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setGeometry(QtCore.QRect(570, 0, 67, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.trafficScroll.setWidget(self.scrollAreaWidgetContents)
        captureWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(captureWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1298, 29))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        captureWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(captureWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        captureWindow.setStatusBar(self.statusbar)
        self.actionNew_capture = QtGui.QAction(captureWindow)
        self.actionNew_capture.setObjectName(_fromUtf8("actionNew_capture"))
        self.actionQuit = QtGui.QAction(captureWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFile.addAction(self.actionNew_capture)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(captureWindow)
        QtCore.QMetaObject.connectSlotsByName(captureWindow)

    def retranslateUi(self, captureWindow):
        captureWindow.setWindowTitle(QtGui.QApplication.translate("captureWindow", "PonyShark capture", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("captureWindow", "Destination IP", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("captureWindow", "Source IP", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("captureWindow", "Protocol", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("captureWindow", "Packet", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("captureWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_capture.setText(QtGui.QApplication.translate("captureWindow", "New capture", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("captureWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))

