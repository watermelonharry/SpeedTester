# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Harry\PyQtProjects\SpeedTester\ui\testermain.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(331, 229)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setSizeGripEnabled(True)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 30, 81, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 82, 81, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(220, 82, 51, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.startOneTestBtn = QtGui.QPushButton(Dialog)
        self.startOneTestBtn.setGeometry(QtCore.QRect(50, 130, 111, 31))
        self.startOneTestBtn.setObjectName(_fromUtf8("startOneTestBtn"))
        self.startAutoTestBtn = QtGui.QPushButton(Dialog)
        self.startAutoTestBtn.setGeometry(QtCore.QRect(170, 130, 111, 31))
        self.startAutoTestBtn.setObjectName(_fromUtf8("startAutoTestBtn"))
        self.showResultBtn = QtGui.QPushButton(Dialog)
        self.showResultBtn.setGeometry(QtCore.QRect(170, 170, 111, 31))
        self.showResultBtn.setObjectName(_fromUtf8("showResultBtn"))
        self.gapTimeEdit = QtGui.QTimeEdit(Dialog)
        self.gapTimeEdit.setGeometry(QtCore.QRect(140, 80, 71, 22))
        self.gapTimeEdit.setMinimumTime(QtCore.QTime(0, 1, 0))
        self.gapTimeEdit.setObjectName(_fromUtf8("gapTimeEdit"))
        self.remoteIpInput = QtGui.QLineEdit(Dialog)
        self.remoteIpInput.setGeometry(QtCore.QRect(140, 30, 113, 20))
        self.remoteIpInput.setMaxLength(15)
        self.remoteIpInput.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.remoteIpInput.setObjectName(_fromUtf8("remoteIpInput"))
        self.clearResultBtn = QtGui.QPushButton(Dialog)
        self.clearResultBtn.setGeometry(QtCore.QRect(50, 170, 111, 31))
        self.clearResultBtn.setObjectName(_fromUtf8("clearResultBtn"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "网速测试", None))
        self.label.setText(_translate("Dialog", "Remote IP:", None))
        self.label_2.setText(_translate("Dialog", "定时间隔:", None))
        self.label_4.setText(_translate("Dialog", "HH/mm/SS", None))
        self.startOneTestBtn.setText(_translate("Dialog", "开始单次测试", None))
        self.startAutoTestBtn.setText(_translate("Dialog", "开始定时测试", None))
        self.showResultBtn.setText(_translate("Dialog", "定时测试结果", None))
        self.remoteIpInput.setText(_translate("Dialog", "192.168.1.137", None))
        self.clearResultBtn.setText(_translate("Dialog", "清除测试记录", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

