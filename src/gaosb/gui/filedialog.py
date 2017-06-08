from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QWidget
import sys

class FileDialog(QWidget):
    def __init__(self):
        super(FileDialog, self).__init__()

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.btn = QtWidgets.QPushButton("QFileDialog static method demo")
        self.btn.clicked.connect(self.getfile)

        self.verticalLayout.addWidget(self.btn)
        self.le = QtWidgets.QLabel("Hello")

        self.verticalLayout.addWidget(self.le)
        self.btn1 = QtWidgets.QPushButton("QFileDialog object")
        self.btn1.clicked.connect(self.getfiles)
        self.verticalLayout.addWidget(self.btn1)

        self.contents = QtWidgets.QTextEdit()
        self.verticalLayout.addWidget(self.contents)
        self.setLayout(self.verticalLayout)
        self.setWindowTitle("File Dialog demo")

    def getfile(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file',
                                            'c:\\', "Image files (*.jpg *.gif)")
        self.le.setPixmap(QtGui.QPixmap(fname))

    def getfiles(self):
        dlg = QtWidgets.QFileDialog()
        dlg.setFileMode(QtWidgets.QFileDialog.AnyFile)
        dlg.setFilter("Text files (*.txt)")
        # filenames = []

        if dlg.exec_():
            filenames = dlg.selectedFiles()
            f = open(filenames[0], 'r')

            with f:
                data = f.read()
                self.contents.setText(data)


def main():
    app = QApplication(sys.argv)
    ex = FileDialog()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()