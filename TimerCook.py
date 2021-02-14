import sys
import mongoDBServer
import math

from bson import ObjectId
from time import sleep

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QDialog
from PyQt5.QtCore import QObject, QThread, pyqtSignal

import TimerCookUI
import PopupCookFinish


class TimerCooking(QThread):
    time_cooking = pyqtSignal(int, int)

    def __init__(self, _id, parent=None):
        super(TimerCooking, self).__init__(parent)
        time_set = mongoDBServer.get_food_time(_id)['time']
        self.time_set = time_set
        self.current_time = time_set

    def run(self):
        while True:
            sleep(1)
            progress_bar = 100 - ((self.current_time / self.time_set) * 100)
            self.time_cooking.emit(self.current_time, progress_bar)
            self.current_time -= 1

    def stop(self):
        self.terminate()


class TimerCook(QDialog, TimerCookUI.Ui_Dialog_TimerCook):
    def __init__(self, change, _id, parent=None):
        super(TimerCook, self).__init__(parent)
        self.setupUi(self)
        self.change = change
        self._id = _id
        # var
        self.can_close = False
        # print('เงินทอน : {}'.format(change))
        self.TimerCookingThread = TimerCooking(_id)
        self.TimerCookingThread.start()
        self.TimerCookingThread.time_cooking.connect(self.printTimeCook)

    def printTimeCook(self, current_time, progress_bar):
        min = current_time / 60
        sec = current_time % 60
        self.lblTimer.setText('{:02d}:{:02d}'.format(math.trunc(min), sec))
        self.progressBar.setValue(progress_bar)
        if current_time == 0:
            self.TimerCookingThread.stop()
            popup_cook_finish = PopupCookFinish.PopupCookFinish(self.change, self._id)
            popup_cook_finish.exec_()
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = TimerCook()
    form.show()
    app.exec_()
