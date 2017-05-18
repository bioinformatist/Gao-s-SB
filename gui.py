# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gao's SB.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_subject = QtWidgets.QLabel(self.centralwidget)
        self.label_subject.setGeometry(QtCore.QRect(30, 40, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_subject.setFont(font)
        self.label_subject.setObjectName("label_subject")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(390, 30, 20, 381))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_query = QtWidgets.QLabel(self.centralwidget)
        self.label_query.setGeometry(QtCore.QRect(440, 30, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_query.setFont(font)
        self.label_query.setObjectName("label_query")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 460, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 460, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.textEdit_subject = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_subject.setGeometry(QtCore.QRect(23, 90, 351, 281))
        self.textEdit_subject.setObjectName("textEdit_subject")
        self.textEdit_query = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_query.setGeometry(QtCore.QRect(430, 90, 351, 281))
        self.textEdit_query.setObjectName("textEdit_query")
        self.textEdit_destination = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_destination.setGeometry(QtCore.QRect(140, 450, 241, 31))
        self.textEdit_destination.setObjectName("textEdit_destination")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.align_query)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_subject.setText(_translate("MainWindow", "Subject:"))
        self.label_query.setText(_translate("MainWindow", "Query:"))
        self.label.setText(_translate("MainWindow", "Output file:"))
        self.pushButton.setText(_translate("MainWindow", "Do!"))

