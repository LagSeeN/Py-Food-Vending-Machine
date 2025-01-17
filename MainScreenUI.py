# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assets\design\MainScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(1220, 769)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainForm.sizePolicy().hasHeightForWidth())
        MainForm.setSizePolicy(sizePolicy)
        MainForm.setMinimumSize(QtCore.QSize(1220, 769))
        MainForm.setMaximumSize(QtCore.QSize(1220, 769))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/vending-machine.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainForm.setWindowIcon(icon)
        self.lblHeader = QtWidgets.QLabel(MainForm)
        self.lblHeader.setGeometry(QtCore.QRect(20, 10, 711, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.lblHeader.setFont(font)
        self.lblHeader.setObjectName("lblHeader")
        self.foodArea = QtWidgets.QScrollArea(MainForm)
        self.foodArea.setGeometry(QtCore.QRect(10, 130, 901, 591))
        self.foodArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.foodArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.foodArea.setWidgetResizable(True)
        self.foodArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.foodArea.setObjectName("foodArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 882, 589))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName("gridLayout")
        self.foodArea.setWidget(self.scrollAreaWidgetContents)
        self.lblTimeClock = QtWidgets.QLabel(MainForm)
        self.lblTimeClock.setGeometry(QtCore.QRect(750, 10, 451, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.lblTimeClock.setFont(font)
        self.lblTimeClock.setText("")
        self.lblTimeClock.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblTimeClock.setObjectName("lblTimeClock")
        self.groupBoxDetailFood = QtWidgets.QGroupBox(MainForm)
        self.groupBoxDetailFood.setGeometry(QtCore.QRect(930, 130, 271, 601))
        self.groupBoxDetailFood.setTitle("")
        self.groupBoxDetailFood.setFlat(True)
        self.groupBoxDetailFood.setObjectName("groupBoxDetailFood")
        self.lblName = QtWidgets.QLabel(self.groupBoxDetailFood)
        self.lblName.setGeometry(QtCore.QRect(10, 10, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblName.setFont(font)
        self.lblName.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblName.setObjectName("lblName")
        self.label_2 = QtWidgets.QLabel(self.groupBoxDetailFood)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.lblStatus = QtWidgets.QLabel(self.groupBoxDetailFood)
        self.lblStatus.setGeometry(QtCore.QRect(90, 90, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblStatus.setFont(font)
        self.lblStatus.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblStatus.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblStatus.setObjectName("lblStatus")
        self.label_6 = QtWidgets.QLabel(self.groupBoxDetailFood)
        self.label_6.setGeometry(QtCore.QRect(10, 170, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.lblStock = QtWidgets.QLabel(self.groupBoxDetailFood)
        self.lblStock.setGeometry(QtCore.QRect(90, 170, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblStock.setFont(font)
        self.lblStock.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblStock.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblStock.setObjectName("lblStock")
        self.label_3 = QtWidgets.QLabel(self.groupBoxDetailFood)
        self.label_3.setGeometry(QtCore.QRect(20, 250, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.lblPrice = QtWidgets.QLabel(self.groupBoxDetailFood)
        self.lblPrice.setGeometry(QtCore.QRect(90, 250, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblPrice.setFont(font)
        self.lblPrice.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblPrice.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblPrice.setObjectName("lblPrice")
        self.btnPay = QtWidgets.QPushButton(self.groupBoxDetailFood)
        self.btnPay.setGeometry(QtCore.QRect(20, 510, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnPay.setFont(font)
        self.btnPay.setObjectName("btnPay")
        self.groupBoxDetailFood.raise_()
        self.foodArea.raise_()
        self.lblHeader.raise_()
        self.lblTimeClock.raise_()

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "Main Screen - Food Vending Machine"))
        self.lblHeader.setText(_translate("MainForm", "Food Vending Machine"))
        self.lblName.setText(_translate("MainForm", "ชื่ออาหาร"))
        self.label_2.setText(_translate("MainForm", "สถานะ"))
        self.lblStatus.setText(_translate("MainForm", "หมด"))
        self.label_6.setText(_translate("MainForm", "จำนวน"))
        self.lblStock.setText(_translate("MainForm", "0"))
        self.label_3.setText(_translate("MainForm", "ราคา"))
        self.lblPrice.setText(_translate("MainForm", "40"))
        self.btnPay.setText(_translate("MainForm", "ชำระเงิน"))
import icon_rc
