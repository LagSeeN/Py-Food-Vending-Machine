# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assets\design\CoinEmulator.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CoinEmulator(object):
    def setupUi(self, CoinEmulator):
        CoinEmulator.setObjectName("CoinEmulator")
        CoinEmulator.resize(371, 238)
        self.gridLayout = QtWidgets.QGridLayout(CoinEmulator)
        self.gridLayout.setObjectName("gridLayout")
        self.coin1btn = QtWidgets.QPushButton(CoinEmulator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coin1btn.sizePolicy().hasHeightForWidth())
        self.coin1btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.coin1btn.setFont(font)
        self.coin1btn.setObjectName("coin1btn")
        self.gridLayout.addWidget(self.coin1btn, 0, 0, 1, 1)
        self.coin5btn = QtWidgets.QPushButton(CoinEmulator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coin5btn.sizePolicy().hasHeightForWidth())
        self.coin5btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.coin5btn.setFont(font)
        self.coin5btn.setObjectName("coin5btn")
        self.gridLayout.addWidget(self.coin5btn, 0, 1, 1, 1)
        self.coin10btn = QtWidgets.QPushButton(CoinEmulator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coin10btn.sizePolicy().hasHeightForWidth())
        self.coin10btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.coin10btn.setFont(font)
        self.coin10btn.setObjectName("coin10btn")
        self.gridLayout.addWidget(self.coin10btn, 0, 2, 1, 1)
        self.coin20btn = QtWidgets.QPushButton(CoinEmulator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coin20btn.sizePolicy().hasHeightForWidth())
        self.coin20btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.coin20btn.setFont(font)
        self.coin20btn.setObjectName("coin20btn")
        self.gridLayout.addWidget(self.coin20btn, 1, 0, 1, 1)
        self.coin50btn = QtWidgets.QPushButton(CoinEmulator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coin50btn.sizePolicy().hasHeightForWidth())
        self.coin50btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.coin50btn.setFont(font)
        self.coin50btn.setObjectName("coin50btn")
        self.gridLayout.addWidget(self.coin50btn, 1, 1, 1, 1)
        self.coin100btn = QtWidgets.QPushButton(CoinEmulator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coin100btn.sizePolicy().hasHeightForWidth())
        self.coin100btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.coin100btn.setFont(font)
        self.coin100btn.setObjectName("coin100btn")
        self.gridLayout.addWidget(self.coin100btn, 1, 2, 1, 1)

        self.retranslateUi(CoinEmulator)
        QtCore.QMetaObject.connectSlotsByName(CoinEmulator)

    def retranslateUi(self, CoinEmulator):
        _translate = QtCore.QCoreApplication.translate
        CoinEmulator.setWindowTitle(_translate("CoinEmulator", "Coin Emulator"))
        self.coin1btn.setText(_translate("CoinEmulator", "1"))
        self.coin5btn.setText(_translate("CoinEmulator", "5"))
        self.coin10btn.setText(_translate("CoinEmulator", "10"))
        self.coin20btn.setText(_translate("CoinEmulator", "20"))
        self.coin50btn.setText(_translate("CoinEmulator", "50"))
        self.coin100btn.setText(_translate("CoinEmulator", "100"))
