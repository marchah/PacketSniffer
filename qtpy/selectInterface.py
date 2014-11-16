# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectInterface.ui'
#
# Created: Thu Nov  6 14:11:04 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_selectInterfaceWindow(object):
    def setupUi(self, selectInterfaceWindow):
        selectInterfaceWindow.setObjectName(_fromUtf8("selectInterfaceWindow"))
        selectInterfaceWindow.resize(419, 139)
        self.centralwidget = QtGui.QWidget(selectInterfaceWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.selectInterfaceLabel = QtGui.QLabel(self.centralwidget)
        self.selectInterfaceLabel.setGeometry(QtCore.QRect(20, 20, 191, 21))
        self.selectInterfaceLabel.setObjectName(_fromUtf8("selectInterfaceLabel"))
        self.selectInterfaceValid = QtGui.QDialogButtonBox(self.centralwidget)
        self.selectInterfaceValid.setGeometry(QtCore.QRect(220, 70, 176, 31))
        self.selectInterfaceValid.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.selectInterfaceValid.setObjectName(_fromUtf8("selectInterfaceValid"))
        self.selectInterfaceChoice = QtGui.QComboBox(self.centralwidget)
        self.selectInterfaceChoice.setGeometry(QtCore.QRect(230, 20, 85, 31))
        self.selectInterfaceChoice.setObjectName(_fromUtf8("selectInterfaceChoice"))
        selectInterfaceWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(selectInterfaceWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        selectInterfaceWindow.setStatusBar(self.statusbar)
        self.actionNew_capture = QtGui.QAction(selectInterfaceWindow)
        self.actionNew_capture.setObjectName(_fromUtf8("actionNew_capture"))
        self.actionQuit = QtGui.QAction(selectInterfaceWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))

        self.retranslateUi(selectInterfaceWindow)
        QtCore.QMetaObject.connectSlotsByName(selectInterfaceWindow)

    def retranslateUi(self, selectInterfaceWindow):
        selectInterfaceWindow.setWindowTitle(QtGui.QApplication.translate("selectInterfaceWindow", "Select Interface", None, QtGui.QApplication.UnicodeUTF8))
        self.selectInterfaceLabel.setText(QtGui.QApplication.translate("selectInterfaceWindow", "Select the network interface", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_capture.setText(QtGui.QApplication.translate("selectInterfaceWindow", "New capture", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("selectInterfaceWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))

