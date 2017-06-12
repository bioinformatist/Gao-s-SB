# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chooseWorkingDir.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_chooseWorkingDir(object):
    def setupUi(self, Dialog_chooseWorkingDir):
        Dialog_chooseWorkingDir.setObjectName("Dialog_chooseWorkingDir")
        Dialog_chooseWorkingDir.resize(603, 55)
        self.pushButton_chooseWorkingDir = QtWidgets.QPushButton(Dialog_chooseWorkingDir)
        self.pushButton_chooseWorkingDir.setGeometry(QtCore.QRect(490, 20, 75, 23))
        self.pushButton_chooseWorkingDir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_chooseWorkingDir.setCheckable(True)
        self.pushButton_chooseWorkingDir.setObjectName("pushButton_chooseWorkingDir")
        self.label = QtWidgets.QLabel(Dialog_chooseWorkingDir)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 16))
        self.label.setObjectName("label")
        self.textBrowser_workingDir = QtWidgets.QTextBrowser(Dialog_chooseWorkingDir)
        self.textBrowser_workingDir.setGeometry(QtCore.QRect(138, 14, 341, 31))
        self.textBrowser_workingDir.setObjectName("textBrowser_workingDir")

        self.retranslateUi(Dialog_chooseWorkingDir)
        QtCore.QMetaObject.connectSlotsByName(Dialog_chooseWorkingDir)

    def retranslateUi(self, Dialog_chooseWorkingDir):
        _translate = QtCore.QCoreApplication.translate
        Dialog_chooseWorkingDir.setWindowTitle(_translate("Dialog_chooseWorkingDir", "Set working directory"))
        self.pushButton_chooseWorkingDir.setText(_translate("Dialog_chooseWorkingDir", "Choose..."))
        self.label.setText(_translate("Dialog_chooseWorkingDir", "Working directory:"))
