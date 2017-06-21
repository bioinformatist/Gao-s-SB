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
        MainWindow.resize(800, 588)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/Radiance.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget_main = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget_main.setGeometry(QtCore.QRect(10, 10, 781, 541))
        self.stackedWidget_main.setObjectName("stackedWidget_main")
        self.page_about = QtWidgets.QWidget()
        self.page_about.setObjectName("page_about")
        self.label_about = QtWidgets.QLabel(self.page_about)
        self.label_about.setGeometry(QtCore.QRect(20, 10, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_about.setFont(font)
        self.label_about.setObjectName("label_about")
        self.label_2 = QtWidgets.QLabel(self.page_about)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 741, 421))
        self.label_2.setObjectName("label_2")
        self.stackedWidget_main.addWidget(self.page_about)
        self.page_alignQuery = QtWidgets.QWidget()
        self.page_alignQuery.setObjectName("page_alignQuery")
        self.label_subject = QtWidgets.QLabel(self.page_alignQuery)
        self.label_subject.setGeometry(QtCore.QRect(150, 0, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_subject.setFont(font)
        self.label_subject.setObjectName("label_subject")
        self.label_query = QtWidgets.QLabel(self.page_alignQuery)
        self.label_query.setGeometry(QtCore.QRect(550, -6, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_query.setFont(font)
        self.label_query.setObjectName("label_query")
        self.label = QtWidgets.QLabel(self.page_alignQuery)
        self.label.setGeometry(QtCore.QRect(560, 420, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.splitter = QtWidgets.QSplitter(self.page_alignQuery)
        self.splitter.setGeometry(QtCore.QRect(21, 51, 741, 361))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.textEdit_subject = QtWidgets.QTextEdit(self.splitter)
        self.textEdit_subject.setObjectName("textEdit_subject")
        self.textEdit_query = QtWidgets.QTextEdit(self.splitter)
        self.textEdit_query.setObjectName("textEdit_query")
        self.textBrowser_alignmentDestination = QtWidgets.QTextBrowser(self.page_alignQuery)
        self.textBrowser_alignmentDestination.setGeometry(QtCore.QRect(560, 450, 201, 31))
        self.textBrowser_alignmentDestination.setObjectName("textBrowser_alignmentDestination")
        self.layoutWidget = QtWidgets.QWidget(self.page_alignQuery)
        self.layoutWidget.setGeometry(QtCore.QRect(600, 490, 158, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_changeFileAlignment = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_changeFileAlignment.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_changeFileAlignment.setCheckable(True)
        self.pushButton_changeFileAlignment.setObjectName("pushButton_changeFileAlignment")
        self.horizontalLayout_2.addWidget(self.pushButton_changeFileAlignment)
        self.pushButton_doAligning = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_doAligning.setFont(font)
        self.pushButton_doAligning.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_doAligning.setCheckable(True)
        self.pushButton_doAligning.setObjectName("pushButton_doAligning")
        self.horizontalLayout_2.addWidget(self.pushButton_doAligning)
        self.stackedWidget_main.addWidget(self.page_alignQuery)
        self.page_downloadSeq = QtWidgets.QWidget()
        self.page_downloadSeq.setObjectName("page_downloadSeq")
        self.textEdit_accessionList = QtWidgets.QTextEdit(self.page_downloadSeq)
        self.textEdit_accessionList.setGeometry(QtCore.QRect(10, 50, 391, 481))
        self.textEdit_accessionList.setObjectName("textEdit_accessionList")
        self.label_accessionList = QtWidgets.QLabel(self.page_downloadSeq)
        self.label_accessionList.setGeometry(QtCore.QRect(10, 20, 471, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_accessionList.setFont(font)
        self.label_accessionList.setObjectName("label_accessionList")
        self.label_3 = QtWidgets.QLabel(self.page_downloadSeq)
        self.label_3.setGeometry(QtCore.QRect(410, 210, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.layoutWidget1 = QtWidgets.QWidget(self.page_downloadSeq)
        self.layoutWidget1.setGeometry(QtCore.QRect(410, 90, 333, 42))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_oneFile = QtWidgets.QCheckBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_oneFile.setFont(font)
        self.checkBox_oneFile.setObjectName("checkBox_oneFile")
        self.verticalLayout.addWidget(self.checkBox_oneFile)
        self.checkBox_removeVersion = QtWidgets.QCheckBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_removeVersion.setFont(font)
        self.checkBox_removeVersion.setObjectName("checkBox_removeVersion")
        self.verticalLayout.addWidget(self.checkBox_removeVersion)
        self.label_7 = QtWidgets.QLabel(self.page_downloadSeq)
        self.label_7.setGeometry(QtCore.QRect(410, 70, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.textBrowser_downloadSeqDestination = QtWidgets.QTextBrowser(self.page_downloadSeq)
        self.textBrowser_downloadSeqDestination.setGeometry(QtCore.QRect(410, 230, 181, 31))
        self.textBrowser_downloadSeqDestination.setObjectName("textBrowser_downloadSeqDestination")
        self.layoutWidget2 = QtWidgets.QWidget(self.page_downloadSeq)
        self.layoutWidget2.setGeometry(QtCore.QRect(594, 232, 158, 25))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_changeFileDownloadSeq = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_changeFileDownloadSeq.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_changeFileDownloadSeq.setCheckable(True)
        self.pushButton_changeFileDownloadSeq.setObjectName("pushButton_changeFileDownloadSeq")
        self.horizontalLayout.addWidget(self.pushButton_changeFileDownloadSeq)
        self.pushButton_doDownloadSeq = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_doDownloadSeq.setFont(font)
        self.pushButton_doDownloadSeq.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_doDownloadSeq.setCheckable(True)
        self.pushButton_doDownloadSeq.setObjectName("pushButton_doDownloadSeq")
        self.horizontalLayout.addWidget(self.pushButton_doDownloadSeq)
        self.stackedWidget_main.addWidget(self.page_downloadSeq)
        self.page_filtering = QtWidgets.QWidget()
        self.page_filtering.setObjectName("page_filtering")
        self.tabWidget = QtWidgets.QTabWidget(self.page_filtering)
        self.tabWidget.setGeometry(QtCore.QRect(6, -1, 781, 541))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_superUniq = QtWidgets.QWidget()
        self.tab_superUniq.setObjectName("tab_superUniq")
        self.textEdit_uniqInput = QtWidgets.QTextEdit(self.tab_superUniq)
        self.textEdit_uniqInput.setGeometry(QtCore.QRect(20, 60, 361, 441))
        self.textEdit_uniqInput.setObjectName("textEdit_uniqInput")
        self.textBrowser_uniqResult = QtWidgets.QTextBrowser(self.tab_superUniq)
        self.textBrowser_uniqResult.setGeometry(QtCore.QRect(400, 120, 361, 381))
        self.textBrowser_uniqResult.setObjectName("textBrowser_uniqResult")
        self.label_4 = QtWidgets.QLabel(self.tab_superUniq)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_superUniq)
        self.label_5.setGeometry(QtCore.QRect(400, 100, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_superUniq)
        self.label_6.setGeometry(QtCore.QRect(400, 30, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.textEdit_uniqSep = QtWidgets.QTextEdit(self.tab_superUniq)
        self.textEdit_uniqSep.setGeometry(QtCore.QRect(400, 60, 151, 31))
        self.textEdit_uniqSep.setObjectName("textEdit_uniqSep")
        self.pushButton_doSuperUniq = QtWidgets.QPushButton(self.tab_superUniq)
        self.pushButton_doSuperUniq.setGeometry(QtCore.QRect(570, 60, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_doSuperUniq.setFont(font)
        self.pushButton_doSuperUniq.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_doSuperUniq.setCheckable(True)
        self.pushButton_doSuperUniq.setObjectName("pushButton_doSuperUniq")
        self.tabWidget.addTab(self.tab_superUniq, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.stackedWidget_main.addWidget(self.page_filtering)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuSequences = QtWidgets.QMenu(self.menubar)
        self.menuSequences.setObjectName("menuSequences")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuTables = QtWidgets.QMenu(self.menubar)
        self.menuTables.setObjectName("menuTables")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_queryAligner = QtWidgets.QAction(MainWindow)
        self.action_queryAligner.setObjectName("action_queryAligner")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setIcon(icon)
        self.action_about.setObjectName("action_about")
        self.action_downloadSequence = QtWidgets.QAction(MainWindow)
        self.action_downloadSequence.setObjectName("action_downloadSequence")
        self.action_filtering = QtWidgets.QAction(MainWindow)
        self.action_filtering.setObjectName("action_filtering")
        self.action_help = QtWidgets.QAction(MainWindow)
        self.action_help.setIcon(icon)
        self.action_help.setObjectName("action_help")
        self.actionMerge_or_Spliting = QtWidgets.QAction(MainWindow)
        self.actionMerge_or_Spliting.setObjectName("actionMerge_or_Spliting")
        self.actionMerge_Split = QtWidgets.QAction(MainWindow)
        self.actionMerge_Split.setObjectName("actionMerge_Split")
        self.action_setWorkingDirectory = QtWidgets.QAction(MainWindow)
        self.action_setWorkingDirectory.setObjectName("action_setWorkingDirectory")
        self.menuSequences.addAction(self.action_queryAligner)
        self.menuSequences.addAction(self.action_downloadSequence)
        self.menuHelp.addAction(self.action_help)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.action_about)
        self.menuTables.addAction(self.action_filtering)
        self.menuSettings.addAction(self.action_setWorkingDirectory)
        self.menubar.addAction(self.menuSequences.menuAction())
        self.menubar.addAction(self.menuTables.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget_main.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gao\'s SB"))
        self.label_about.setText(_translate("MainWindow", "About"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">What you\'re using is a toolbox for</span></p><p><span style=\" font-size:18pt;\">bioinformatics works in Dr. Gao\'s lab.</span></p><p><span style=\" font-size:18pt;\">Contributors: </span><a href=\"http://icannotendure.space/\"><span style=\" font-size:22pt; font-weight:600; font-style:italic; text-decoration: underline; color:#0000ff;\">Yu Sun</span></a></p><p><span style=\" font-size:18pt;\">You can choose tools from menu.</span></p></body></html>"))
        self.label_subject.setText(_translate("MainWindow", "Subject"))
        self.label_query.setText(_translate("MainWindow", "Query"))
        self.label.setText(_translate("MainWindow", "Output file"))
        self.textBrowser_alignmentDestination.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">alignment.txt                </p></body></html>"))
        self.pushButton_changeFileAlignment.setText(_translate("MainWindow", "Change..."))
        self.pushButton_doAligning.setText(_translate("MainWindow", "Do!"))
        self.textEdit_accessionList.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#666666;\"># Whole sequence example</span><span style=\" color:#666666;\">:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#666666;\">NC_005809.1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#666666;\">NR_046235</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#666666;\"># By specific region example:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#666666;\">NC_005809.1    1655    1777</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#666666;\">NC_005809.1    1111    1234</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; color:#666666;\"><br /></p></body></html>"))
        self.label_accessionList.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Enter list:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Output file"))
        self.checkBox_oneFile.setText(_translate("MainWindow", "One file, one sequence (use ID as file name)"))
        self.checkBox_removeVersion.setText(_translate("MainWindow", "Auto remove version number"))
        self.label_7.setText(_translate("MainWindow", "Output mode"))
        self.textBrowser_downloadSeqDestination.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Downloaded sequences.txt                </p></body></html>"))
        self.pushButton_changeFileDownloadSeq.setText(_translate("MainWindow", "Change..."))
        self.pushButton_doDownloadSeq.setText(_translate("MainWindow", "Do!"))
        self.textEdit_uniqInput.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"2\" cellpadding=\"0\">\n"
"<tr>\n"
"<td width=\"280\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#666666;\"># Example:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#666666;\">J02428,FJ150422</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#666666;\">J02428,FJ150422</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#666666;\">J02428,FJ150422</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#666666;\">J02428,FJ150422</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#666666;\">J02428,FJ150422</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#666666;\">J02428,FJ150422</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#666666;\">Z30318,FJ150422</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#666666;\">Z30318,FJ150422</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#666666;\">Z30318,FJ150422</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#666666;\">Z30318,FJ150422</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#666666;\">Z30318,FJ150422</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#666666;\">Z30318,FJ150422</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#666666;\">AF014388</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#666666;\">AF014388</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#666666;\">AF014388</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#666666;\">AF014388</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#666666;\">AF014388</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#666666;\">AF014388</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#666666;\">FJ150422</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#666666;\">AY243312</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#666666;\">AY243312</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#666666;\">AY243312</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#666666;\">DQ439815</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#666666;\">DQ439815</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#666666;\">AY243312</span></p></td></tr></table></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Text to be split then apply uniq on:"))
        self.label_5.setText(_translate("MainWindow", "Result:"))
        self.label_6.setText(_translate("MainWindow", "Separator (regular expreesion):"))
        self.textEdit_uniqSep.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'inherit\'; font-size:10pt; color:#666666; background-color:#eff0f1;\">[^a-zA-Z0-9]</span></p></body></html>"))
        self.pushButton_doSuperUniq.setText(_translate("MainWindow", "Do!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_superUniq), _translate("MainWindow", "Super Uniqer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Developing..."))
        self.menuSequences.setTitle(_translate("MainWindow", "Sequences"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuTables.setTitle(_translate("MainWindow", "Tables"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.action_queryAligner.setText(_translate("MainWindow", "Align queries"))
        self.action_about.setText(_translate("MainWindow", "About"))
        self.action_downloadSequence.setText(_translate("MainWindow", "Download sequences"))
        self.action_filtering.setText(_translate("MainWindow", "Filtering"))
        self.action_help.setText(_translate("MainWindow", "Help"))
        self.actionMerge_or_Spliting.setText(_translate("MainWindow", "Merge or Spliting"))
        self.actionMerge_Split.setText(_translate("MainWindow", "Merge or split"))
        self.action_setWorkingDirectory.setText(_translate("MainWindow", "Set working directory..."))

import resources_rc
