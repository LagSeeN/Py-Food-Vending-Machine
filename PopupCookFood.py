import sys
import mongoDBServer

from bson import ObjectId
from time import sleep

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QDialog
from PyQt5.QtCore import QObject, QThread, pyqtSignal

import PopupCookFoodUI


class PopupCookFood(QDialog, PopupCookFoodUI.Ui_Dialog_PopupCookFood):
    def __init__(self, change, parent=None):
        super(PopupCookFood, self).__init__(parent)
        self.setupUi(self)
        # var
        self.can_close = False
        print('เงินทอน : {}'.format(change))
        self.btn_cook_no.clicked.connect(self.cook_no)

    def cook_no(self):
        self.can_close = True
        self.close()

    def closeEvent(self, event):
        if self.can_close:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = PopupCookFood()
    form.show()
    app.exec_()
