import sys
import mongoDBServer
import base64

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow

from MainScreen import Ui_MainForm


class MainWindows(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainForm()
        self.ui.setupUi(self)
        # Event
        self.loadFoodItem()

    def loadFoodItem(self):
        row1 = 0
        row2 = 0
        count = mongoDBServer.countData()
        imageItem = mongoDBServer.getAllImage()
        _id = mongoDBServer.getAll_Id()
        for i in range(count):
            self.foodItem = QtWidgets.QPushButton(self.ui.scrollAreaWidgetContents)
            self.foodItem.setMaximumSize(QtCore.QSize(280, 280))
            self.foodItem.setText("")
            base64_data = imageItem[i]
            pm = QtGui.QPixmap()
            pm.loadFromData(base64.b64decode(base64_data))
            icon = QtGui.QIcon()
            icon.addPixmap(pm, QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.foodItem.setIcon(icon)
            self.foodItem.setIconSize(QtCore.QSize(280, 280))
            self.foodItem.clicked.connect(lambda ch, idItem=_id[i]: self.foodSelect(idItem))
            self.ui.gridLayout.addWidget(self.foodItem, row1, row2, 1, 1)
            # print("[{} , {} , 1 , 1]".format(row1, row2))
            if row2 == 2:
                row2 = 0
                row1 += 1
            else:
                row2 += 1

    def foodSelect(self, idItem):
        print('{}'.format(idItem))
        self.ui.label.setText('{}'.format(mongoDBServer.getFood(idItem)[0]['product_name']))
        self.ui.label_7.setText('{}'.format(mongoDBServer.getFood(idItem)[0]['stock']))
        self.ui.label_5.setText('{}'.format(mongoDBServer.getFood(idItem)[0]['price']))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindows()
    form.show()
    app.exec_()
