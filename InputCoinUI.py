# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assets\design\InputCoin.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setModal(False)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lblTotalMoney = QtWidgets.QLabel(Dialog)
        self.lblTotalMoney.setGeometry(QtCore.QRect(200, 20, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblTotalMoney.setFont(font)
        self.lblTotalMoney.setObjectName("lblTotalMoney")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(310, 20, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(310, 90, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lblInputMoney = QtWidgets.QLabel(Dialog)
        self.lblInputMoney.setGeometry(QtCore.QRect(200, 90, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblInputMoney.setFont(font)
        self.lblInputMoney.setObjectName("lblInputMoney")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "ราคา"))
        self.lblTotalMoney.setText(_translate("Dialog", "10"))
        self.label_3.setText(_translate("Dialog", "บาท"))
        self.label_4.setText(_translate("Dialog", "ยอดเงินที่ใส่ตอนนี้"))
        self.label_5.setText(_translate("Dialog", "บาท"))
        self.lblInputMoney.setText(_translate("Dialog", "10"))