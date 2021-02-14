import sys
import mongoDBServer
import math

from bson import ObjectId
from time import sleep

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QDialog
from PyQt5.QtCore import QObject, QThread, pyqtSignal

import PopupReceiveCoinUI


class PopUp5Sec(QThread):
    time_popup = pyqtSignal(int)

    def __init__(self, parent=None):
        super(PopUp5Sec, self).__init__(parent)
        self.time = 5

    def run(self):
        while True:
            sleep(1)
            self.time_popup.emit(self.time)
            self.time -= 1

    def stop(self):
        self.terminate()


class PopupReceiveCoin(QDialog, PopupReceiveCoinUI.Ui_Dialog_PopupReciveCoin):
    def __init__(self, change, parent=None):
        super(PopupReceiveCoin, self).__init__(parent)
        self.setupUi(self)
        self.change = change
        # var
        self.can_close = False
        print('เงินทอน : {}'.format(change))
        self.PopUp5SecThread = PopUp5Sec()
        self.PopUp5SecThread.start()
        self.PopUp5SecThread.time_popup.connect(self.time_popup)

    def time_popup(self, time):
        if time == 0:
            self.PopUp5SecThread.stop()
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = PopupReceiveCoin()
    form.show()
    app.exec_()
