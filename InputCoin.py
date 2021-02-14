import sys
import mongoDBServer

from bson import ObjectId
from time import sleep

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QDialog
from PyQt5.QtCore import QObject, QThread, pyqtSignal

import InputCoinUI

import CoinEmulator
import PopupCookFood
import PopupReceiveCoin


class WaitCoinInput(QThread):
    update_Price = pyqtSignal(int)

    def __init__(self, parent=None):
        super(WaitCoinInput, self).__init__(parent)
        self.time_left = 5

    def run(self):
        while True:
            sleep(1)
            self.update_Price.emit(self.time_left)
            self.time_left -= 1

    def stop(self):
        self.terminate()


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


class InputCoin(QDialog, InputCoinUI.Ui_InputDialog):
    def __init__(self, _id, main_screen, parent=None):
        super(InputCoin, self).__init__(parent)
        self.WaitCoinInput = WaitCoinInput()
        self.CoinEmulator = CoinEmulator.CoinEmulator(self)
        self.setupUi(self)
        # var
        self.MainScreen = main_screen
        self.input_money = 0
        self.total_price = 0
        self.WaitCoinInputIsActive = False
        # แปลง str เป็น ObjectId
        self._id = ObjectId(_id)
        self.getFoodThread = GetFood(self._id)
        self.getFoodThread.start()
        self.getFoodThread.get_food.connect(self.food_show_information)

    def food_show_information(self, food, item_id):
        self.getFoodThread.stop()
        self.total_price = food['price']
        self.lbl_total_money.setText('{0:,g}'.format(self.total_price))
        self.lbl_input_money.setText('{0:,g}'.format(self.input_money))
        self.CoinEmulator.open()
        self.WaitCoinInput.start()
        self.WaitCoinInputIsActive = True
        self.WaitCoinInput.update_Price.connect(self.wait_coin_input)

    def wait_coin_input(self, time_left):
        if time_left == 60:
            self.lbl_time_left.setText('1:00')
        else:
            self.lbl_time_left.setText('0:{:02d}'.format(time_left))
        self.lbl_input_money.setText('{0:,g}'.format(self.input_money))
        if time_left == 0:
            if self.input_money != 0:
                popup_receive_coin = PopupReceiveCoin.PopupReceiveCoin(self.input_money)
                popup_receive_coin.exec_()
            self.WaitCoinInputIsActive = False
            self.WaitCoinInput.stop()
            self.CoinEmulator.close()
            self.close()
        if self.input_money >= self.total_price:
            self.WaitCoinInputIsActive = False
            self.WaitCoinInput.stop()
            self.CoinEmulator.close()
            change = 0
            if self.input_money > self.total_price:
                change = self.input_money - self.total_price
            popup_cook_food = PopupCookFood.PopupCookFood(change, self._id)
            popup_cook_food.exec_()
            self.close()

    def closeEvent(self, event):
        if self.WaitCoinInputIsActive:
            self.WaitCoinInput.stop()
        self.CoinEmulator.close()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = InputCoin()
    form.show()
    app.exec_()
