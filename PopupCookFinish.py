import sys
import mongoDBServer
import math

from bson import ObjectId
from time import sleep

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QDialog
from PyQt5.QtCore import QObject, QThread, pyqtSignal

import PopupCookFinishUI


class PopUp5Sec(QThread):
    time_popup = pyqtSignal(int)

    def __init__(self, _id, parent=None):
        super(PopUp5Sec, self).__init__(parent)
        self.time = 5
        self._id = _id
        self.currentFood = mongoDBServer.get_food(_id)['stock']

    def run(self):
        mongoDBServer.food_finish(self._id, self.currentFood)
        mongoDBServer.export_log()
        while True:
            sleep(1)
            self.time_popup.emit(self.time)
            self.time -= 1

    def stop(self):
        self.terminate()


class PopupCookFinish(QDialog, PopupCookFinishUI.Ui_Dialog_PopupCookFinish):
    def __init__(self, change, _id, parent=None):
        super(PopupCookFinish, self).__init__(parent)
        self.setupUi(self)
        self.change = change
        self._id = _id
        # var
        self.can_close = False
        print('เงินทอน : {}'.format(change))
        self.PopUp5SecThread = PopUp5Sec(self._id)
        self.PopUp5SecThread.start()
        self.PopUp5SecThread.time_popup.connect(self.time_popup)

    def time_popup(self, time):
        if time == 0:
            self.PopUp5SecThread.stop()
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = PopupCookFinish()
    form.show()
    app.exec_()
