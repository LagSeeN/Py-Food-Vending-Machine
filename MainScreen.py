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
    update_time_clock = pyqtSignal(str)

    def __init__(self, parent=None):
        super(TimeClock, self).__init__(parent)

    def run(self):
        while True:
            sleep(1)
            time = QtCore.QTime.currentTime()
            self.update_time_clock.emit(time.toString('hh:mm:ss'))


class GetFood(QThread):
    get_food = pyqtSignal(dict, str)

    def __init__(self, item, parent=None):
        super(GetFood, self).__init__(parent)
        self.item = item

    def run(self):
        item = mongoDBServer.get_food(self.item)
        self.get_food.emit(item, str(self.item))

    def stop(self):
        self.terminate()


class LoadFoodItem(QThread):
    load_food = pyqtSignal(int, list, list)

    def __init__(self, parent=None):
        super(LoadFoodItem, self).__init__(parent)

    def run(self):
        count = mongoDBServer.count_data()
        image_item = mongoDBServer.get_all_image()
        _id = mongoDBServer.get_all_ids()
        self.load_food.emit(count, image_item, _id)

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
        self.timeThread.update_time_clock.connect(self.showtime)
        # Show Item
        self.loadFoodItemThread = LoadFoodItem()
        self.loadFoodItemThread.start()
        self.loadFoodItemThread.load_food.connect(self.load_food_item)
        # Event
        self.btnPay.clicked.connect(self.show_input_coin)

    def showtime(self, val):
        self.lblTimeClock.setText('{}'.format(val))

    def load_food_item(self, count, images, _id):
        row1 = 0
        row2 = 0
        for i in range(count):
            self.foodItem = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.foodItem.setMaximumSize(QtCore.QSize(280, 280))
            self.foodItem.setText("")
            base64_data = images[i]
            pm = QtGui.QPixmap()
            pm.loadFromData(base64.b64decode(base64_data))
            icon = QtGui.QIcon()
            icon.addPixmap(pm, QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.foodItem.setIcon(icon)
            self.foodItem.setIconSize(QtCore.QSize(280, 280))
            self.foodItem.clicked.connect(lambda ch, idItem=_id[i]: self.food_load_information(idItem))
            self.gridLayout.addWidget(self.foodItem, row1, row2, 1, 1)
            self.listbtn.append(self.foodItem)
            # print("[{} , {} , 1 , 1]".format(row1, row2))
            if row2 == 2:
                row2 = 0
                row1 += 1
            else:
                row2 += 1
        self.loadFoodItemThread.stop()

    def food_load_information(self, item_id):
        # add delay to protect spam click
        self.foodArea.setEnabled(False)
        self.getFoodThread = GetFood(item_id)
        self.getFoodThread.start()
        self.getFoodThread.get_food.connect(self.food_show_information)

    def food_show_information(self, food, item_id):
        self.getFoodThread.stop()
        self.foodArea.setEnabled(True)
        self.lblName.setText('{}'.format(food['product_name']))
        if food['stock'] == 0:
            self.btnPay.setEnabled(False)
            self.lblStatus.setText('หมด')
        else:
            self.btnPay.setEnabled(True)
            self.lblStatus.setText('พร้อมจำหน่าย')
        self.lblStock.setText('{0:g}'.format(food['stock']))
        self.lblPrice.setText('{0:,g}'.format(food['price']))
        self.groupBoxDetailFood.setVisible(True)
        self.currentSelect = item_id

    def show_input_coin(self):
        input_coin_ui = InputCoin.InputCoin(self.currentSelect, self)
        input_coin_ui.exec_()
        self.loadFoodItemThread.start()
        self.groupBoxDetailFood.setVisible(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindows()
    form.show()
    app.exec_()
