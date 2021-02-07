import sys
import mongoDBServer
import base64

from time import sleep

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtCore import QObject, QThread, pyqtSignal

import MainScreenUI
import InputCoin


class TimeClock(QThread):
    update_timeclock = pyqtSignal(str)

    def __init__(self, parent=None):
        super(TimeClock, self).__init__(parent)

    def run(self):
        while True:
            sleep(1)
            time = QtCore.QTime.currentTime()
            self.update_timeclock.emit(time.toString('hh:mm:ss'))


class getFood(QThread):
    get_food = pyqtSignal(list, str)

    def __init__(self, item, parent=None):
        super(getFood, self).__init__(parent)
        self.item = item

    def run(self):
        item = mongoDBServer.getFood(self.item)
        self.get_food.emit(item, str(self.item))

    def stop(self):
        self.terminate()


class loadFoodItem(QThread):
    load_food = pyqtSignal(int, list, list)

    def __init__(self, parent=None):
        super(loadFoodItem, self).__init__(parent)

    def run(self):
        count = mongoDBServer.countData()
        imageItem = mongoDBServer.getAllImage()
        _id = mongoDBServer.getAll_Id()
        self.load_food.emit(count, imageItem, _id)

    def stop(self):
        self.terminate()


class MainWindows(QMainWindow, MainScreenUI.Ui_MainForm):
    def __init__(self, parent=None):
        super(MainWindows, self).__init__(parent)
        self.setupUi(self)
        self.btnPay.setEnabled(False)
        self.groupBoxDetailFood.setVisible(False)
        # Var
        self.listbtn = []
        self.currentSelect = ""
        # Clock
        self.timeThread = TimeClock()
        self.timeThread.start()
        self.timeThread.update_timeclock.connect(self.showTime)
        # Show Item
        self.loadFoodItemThread = loadFoodItem()
        self.loadFoodItemThread.start()
        self.loadFoodItemThread.load_food.connect(self.loadFoodItem)
        # Event
        self.btnPay.clicked.connect(self.showInputCoin)

    def showTime(self, val):
        self.lblTimeClock.setText('{}'.format(val))

    def loadFoodItem(self, count, imageItem, _id):
        row1 = 0
        row2 = 0
        for i in range(count):
            self.foodItem = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.foodItem.setMaximumSize(QtCore.QSize(280, 280))
            self.foodItem.setText("")
            base64_data = imageItem[i]
            pm = QtGui.QPixmap()
            pm.loadFromData(base64.b64decode(base64_data))
            icon = QtGui.QIcon()
            icon.addPixmap(pm, QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.foodItem.setIcon(icon)
            self.foodItem.setIconSize(QtCore.QSize(280, 280))
            self.foodItem.clicked.connect(lambda ch, idItem=_id[i]: self.foodLoadInfomation(idItem))
            self.gridLayout.addWidget(self.foodItem, row1, row2, 1, 1)
            self.listbtn.append(self.foodItem)
            # print("[{} , {} , 1 , 1]".format(row1, row2))
            if row2 == 2:
                row2 = 0
                row1 += 1
            else:
                row2 += 1
        self.loadFoodItemThread.stop()

    def foodLoadInfomation(self, idItem):
        # add delay to protect spam click
        self.foodArea.setEnabled(False)
        self.getFoodThread = getFood(idItem)
        self.getFoodThread.start()
        self.getFoodThread.get_food.connect(self.foodShowInfomation)

    def foodShowInfomation(self, food, idItem):
        self.getFoodThread.stop()
        self.foodArea.setEnabled(True)
        self.lblName.setText('{}'.format(food[0]['product_name']))
        if food[0]['stock'] == 0:
            self.btnPay.setEnabled(False)
            self.lblStatus.setText('หมด')
        else:
            self.btnPay.setEnabled(True)
            self.lblStatus.setText('พร้อมจำหน่าย')
        self.lblStock.setText('{}'.format(food[0]['stock']))
        self.lblPrice.setText('{}'.format(food[0]['price']))
        self.groupBoxDetailFood.setVisible(True)
        self.currentSelect = idItem

    def showInputCoin(self):
        self.w = InputCoin.InputCoin(self.currentSelect)
        self.w.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindows()
    form.show()
    app.exec_()
