import logging
import sys
import traceback

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMessageBox

from gaosb.core.app import Application


def exception_handler(*exc_info):
    logging.error("An unhandled exception occurred",
                  exc_info=exc_info)
    exception_message(["An unhandled exception occurred"], exc_info)


def exception_message(log_lines, exc_info):
    stacktrace = traceback.format_exception(*exc_info) if exc_info else ""
    message = """
    {log_lines}

    ----
    {stacktrace}
    """.format(log_lines='\n'.join(log_lines), stacktrace='\n'.join(stacktrace))
    mb = QMessageBox()
    mb.setIcon(QMessageBox.Critical)
    mb.setWindowTitle("DUANG!!!")
    mb.setText('A critical error occurred. Select the details to display it.')
    mb.setInformativeText("Please report it to "
                          "<a href=https://github.com/bioinformatist/Gao-s-SB/issues/new>the owner's GitHub</a>")
    mb.setTextFormat(Qt.RichText)
    mb.setDetailedText(message)

    mb.setTextInteractionFlags(Qt.TextSelectableByMouse)
    mb.exec()


if __name__ == '__main__':
    gao_sb = QApplication(sys.argv)
    sys.excepthook = exception_handler

    gao_sb.setStyle('Fusion')
    widget = Application()
    widget.show()
    sys.exit(gao_sb.exec_())
