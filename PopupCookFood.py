import sys
import mongoDBServer
import math

from bson import ObjectId
from time import sleep

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QDialog
from PyQt5.QtCore import QObject, QThread, pyqtSignal

import PopupCookFoodUI
import TimerCook
import PopupCookFinish


class getTimeCook(QThread):
    time_cooking = pyqtSignal(int)

    def __init__(self, _id, parent=None):
        super(getTimeCook, self).__init__(parent)
        self.time_set = mongoDBServer.get_food_time(_id)['time']

    def run(self):
        self.time_cooking.emit(self.time_set)

    def stop(self):
        self.terminate()


class PopupCookFood(QDialog, PopupCookFoodUI.Ui_Dialog_PopupCookFood):
    def __init__(self, change, _id, parent=None):
        super(PopupCookFood, self).__init__(parent)
        self.setupUi(self)
        self.change = change
        self._id = _id
        # var
        self.can_close = False
        # print('เงินทอน : {}'.format(change))
        self.getTimeCookThread = getTimeCook(_id)
        self.getTimeCookThread.start()
        self.getTimeCookThread.time_cooking.connect(self.printTimeCook)
        self.btn_cook_no.clicked.connect(self.cook_no)
        self.btn_cook_ok.clicked.connect(self.cook_yes)

    def printTimeCook(self, time):
        self.lbl_timer.setText('{} นาที'.format(math.trunc(time / 60)))

    def cook_no(self):
        popup_cook_finish = PopupCookFinish.PopupCookFinish(self.change, self._id)
        popup_cook_finish.exec_()
        self.can_close = True
        self.close()

    def cook_yes(self):
        timer_cook_ui = TimerCook.TimerCook(self.change, self._id)
        timer_cook_ui.exec_()
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
