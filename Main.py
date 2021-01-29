import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow

from MainScreen import Ui_MainForm


class MainWindows(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainForm()
        self.ui.setupUi(self)
        # Event


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindows()
    form.show()
    app.exec_()
