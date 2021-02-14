# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assets\design\InputCoin.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InputDialog(object):
    def setupUi(self, InputDialog):
        InputDialog.setObjectName("InputDialog")
        InputDialog.resize(400, 300)
        InputDialog.setMinimumSize(QtCore.QSize(400, 300))
        InputDialog.setMaximumSize(QtCore.QSize(400, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/vending-machine.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        InputDialog.setWindowIcon(icon)
        InputDialog.setModal(False)
        self.lbl_txt_price = QtWidgets.QLabel(InputDialog)
        self.lbl_txt_price.setGeometry(QtCore.QRect(20, 20, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_txt_price.setFont(font)
        self.lbl_txt_price.setObjectName("lbl_txt_price")
        self.lbl_total_money = QtWidgets.QLabel(InputDialog)
        self.lbl_total_money.setGeometry(QtCore.QRect(200, 20, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_total_money.setFont(font)
        self.lbl_total_money.setText("")
        self.lbl_total_money.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_total_money.setObjectName("lbl_total_money")
        self.lbl_bath_1 = QtWidgets.QLabel(InputDialog)
        self.lbl_bath_1.setGeometry(QtCore.QRect(310, 20, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_bath_1.setFont(font)
        self.lbl_bath_1.setObjectName("lbl_bath_1")
        self.lbl_txt_coin_input = QtWidgets.QLabel(InputDialog)
        self.lbl_txt_coin_input.setGeometry(QtCore.QRect(20, 90, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_txt_coin_input.setFont(font)
        self.lbl_txt_coin_input.setObjectName("lbl_txt_coin_input")
        self.lbl_bath_2 = QtWidgets.QLabel(InputDialog)
        self.lbl_bath_2.setGeometry(QtCore.QRect(310, 90, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_bath_2.setFont(font)
        self.lbl_bath_2.setObjectName("lbl_bath_2")
        self.lbl_input_money = QtWidgets.QLabel(InputDialog)
        self.lbl_input_money.setGeometry(QtCore.QRect(200, 90, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_input_money.setFont(font)
        self.lbl_input_money.setText("")
        self.lbl_input_money.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_input_money.setObjectName("lbl_input_money")
        self.lbl_time_left = QtWidgets.QLabel(InputDialog)
        self.lbl_time_left.setGeometry(QtCore.QRect(10, 240, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_time_left.setFont(font)
        self.lbl_time_left.setText("")
        self.lbl_time_left.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_time_left.setObjectName("lbl_time_left")

        self.retranslateUi(InputDialog)
        QtCore.QMetaObject.connectSlotsByName(InputDialog)

    def retranslateUi(self, InputDialog):
        _translate = QtCore.QCoreApplication.translate
        InputDialog.setWindowTitle(_translate("InputDialog", "Input Coin - Food Vending Machine"))
        self.lbl_txt_price.setText(_translate("InputDialog", "ราคา"))
        self.lbl_bath_1.setText(_translate("InputDialog", "บาท"))
        self.lbl_txt_coin_input.setText(_translate("InputDialog", "ยอดเงินที่ใส่ตอนนี้"))
        self.lbl_bath_2.setText(_translate("InputDialog", "บาท"))
import icon_rc
