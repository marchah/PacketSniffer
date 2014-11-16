# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ponyShark1.ui'
#
# Created: Thu Nov  6 13:45:59 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(1296, 751)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.titleLabel = QtGui.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(50, 30, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))
        self.descriptionLabel = QtGui.QLabel(self.centralwidget)
        self.descriptionLabel.setGeometry(QtCore.QRect(110, 100, 591, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.descriptionLabel.setFont(font)
        self.descriptionLabel.setObjectName(_fromUtf8("descriptionLabel"))
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(280, 340, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.startButton.setFont(font)
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.QuitButton = QtGui.QPushButton(self.centralwidget)
        self.QuitButton.setGeometry(QtCore.QRect(800, 340, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.QuitButton.setFont(font)
        self.QuitButton.setObjectName(_fromUtf8("QuitButton"))
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1296, 29))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(mainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionNew_capture_2 = QtGui.QAction(mainWindow)
        self.actionNew_capture_2.setObjectName(_fromUtf8("actionNew_capture_2"))
        self.actionQuit_2 = QtGui.QAction(mainWindow)
        self.actionQuit_2.setObjectName(_fromUtf8("actionQuit_2"))
        self.menuFile.addAction(self.actionNew_capture_2)
        self.menuFile.addAction(self.actionQuit_2)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "PonyShark", None, QtGui.QApplication.UnicodeUTF8))
        self.titleLabel.setText(QtGui.QApplication.translate("mainWindow", "Welcome to PonyShark", None, QtGui.QApplication.UnicodeUTF8))
        self.descriptionLabel.setText(QtGui.QApplication.translate("mainWindow", "A new way to check your network traffic, and altering packets", None, QtGui.QApplication.UnicodeUTF8))
        self.startButton.setText(QtGui.QApplication.translate("mainWindow", "Start a capture", None, QtGui.QApplication.UnicodeUTF8))
        self.QuitButton.setText(QtGui.QApplication.translate("mainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("mainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("mainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_capture_2.setText(QtGui.QApplication.translate("mainWindow", "New capture", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit_2.setText(QtGui.QApplication.translate("mainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))

