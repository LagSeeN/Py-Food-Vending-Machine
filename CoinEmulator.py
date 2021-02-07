import sys
import mongoDBServer
from bson import ObjectId

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QDialog
from PyQt5.QtCore import QObject, QThread, pyqtSignal

import CoinEmulatorUI


class CoinEmulator(QDialog, CoinEmulatorUI.Ui_CoinEmulator):
    def __init__(self, InputCoin, parent=None):
        super(CoinEmulator, self).__init__(parent)
        self.setupUi(self)
        self.InputCoin = InputCoin
        # var
        # event
        self.coin1btn.clicked.connect(lambda: self.click_btn(1))
        self.coin5btn.clicked.connect(lambda: self.click_btn(5))
        self.coin10btn.clicked.connect(lambda: self.click_btn(10))
        self.coin20btn.clicked.connect(lambda: self.click_btn(20))
        self.coin50btn.clicked.connect(lambda: self.click_btn(50))
        self.coin100btn.clicked.connect(lambda: self.click_btn(100))

    def click_btn(self, coin):
        self.InputCoin.input_money += coin


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = CoinEmulator()
    form.show()
    app.exec_()
