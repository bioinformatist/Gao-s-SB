from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget

from gaosb.gui.Dialog_chooseWorkingDir import Ui_Dialog_chooseWorkingDir


class SetWorkingDir(QWidget, Ui_Dialog_chooseWorkingDir):
    def __init__(self):
        super(SetWorkingDir, self).__init__()
        self.setupUi(self)
        self.working_directory = 'fuck'
        self.pushButton_chooseWorkingDir.clicked.connect(self.get_directory)

    def get_directory(self):
        dlg = QtWidgets.QFileDialog(self, 'fuck', '.')
        dlg.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)
        if dlg.exec_() == QtWidgets.QDialog.Accepted:
            self.working_directory = dlg.selectedFiles()[0]
