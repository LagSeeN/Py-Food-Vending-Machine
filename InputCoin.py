import sys
import mongoDBServer
from bson import ObjectId

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QDialog
from PyQt5.QtCore import QObject, QThread, pyqtSignal

import InputCoinUI


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


class InputCoin(QDialog, InputCoinUI.Ui_Dialog):
    def __init__(self, _id, parent=None):
        super(InputCoin, self).__init__(parent)
        self.setupUi(self)
        # แปลง str เป็น ObjectId
        self._id = ObjectId(_id)
        self.getFoodThread = getFood(self._id)
        self.getFoodThread.start()
        self.getFoodThread.get_food.connect(self.foodShowInfomation)

    def foodShowInfomation(self, food, idItem):
        self.getFoodThread.stop()
        # self.foodArea.setEnabled(True)
        print('{}'.format(food[0]['product_name']))
        # if food[0]['stock'] == 0:
        #     self.btnPay.setEnabled(False)
        #     self.lblStatus.setText('หมด')
        # else:
        #     self.btnPay.setEnabled(True)
        #     self.lblStatus.setText('พร้อมจำหน่าย')
        # self.lblStock.setText('{}'.format(food[0]['stock']))
        # self.lblPrice.setText('{}'.format(food[0]['price']))
        # self.groupBoxDetailFood.setVisible(True)
        # self.currentSelect = idItem


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = InputCoin()
    form.show()
    app.exec_()
