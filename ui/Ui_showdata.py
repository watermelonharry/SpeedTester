# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Harry\PyQtProjects\SpeedTester\ui\showdata.ui'
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

class Ui_showDataWindow(object):
    def setupUi(self, showDataWindow):
        showDataWindow.setObjectName(_fromUtf8("showDataWindow"))
        showDataWindow.resize(628, 436)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(showDataWindow.sizePolicy().hasHeightForWidth())
        showDataWindow.setSizePolicy(sizePolicy)
        showDataWindow.setSizeGripEnabled(True)
        self.webView = QtWebKit.QWebView(showDataWindow)
        self.webView.setGeometry(QtCore.QRect(0, 0, 631, 431))
        import os
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("file:///" + '/'.join(os.getcwd().split('\\')) + "/echart/show.html")))
        print("file:///" + '/'.join(os.getcwd().split('\\')) + "/echart/show.html")
        self.webView.setObjectName(_fromUtf8("webView"))

        self.retranslateUi(showDataWindow)
        QtCore.QMetaObject.connectSlotsByName(showDataWindow)

    def retranslateUi(self, showDataWindow):
        showDataWindow.setWindowTitle(_translate("showDataWindow", "查看图表", None))

from PyQt4 import QtWebKit

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    showDataWindow = QtGui.QDialog()
    ui = Ui_showDataWindow()
    ui.setupUi(showDataWindow)
    showDataWindow.show()
    sys.exit(app.exec_())

