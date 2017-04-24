# -*- coding: utf-8 -*-

"""
Module implementing testermain.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QDialog, QApplication
import sys
from ui.Ui_testermain import Ui_Dialog
from showdata import showDataWindow
from base.statusDict import LOCAL_STATUS
from func.popWindow import NoticeWindow

class testermain(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setFixedSize(331, 229)
        self.showWindow = showDataWindow()
        self.status = LOCAL_STATUS.WAIT

    def Confirm(self, intArg):
        """
        确认窗口
        :param intArg:
        :return:确定返回True， 取消返回False
        """
        noticeWindow = NoticeWindow()
        noticeWindow.Confirm(intArg)
        return noticeWindow.status

    def verifyIp(self, ipStr):
        ip = str(ipStr).split('.')
        result =  len(ip) == 4 and len(filter(lambda x: x >= 0 and x <= 255, map(int, filter(lambda x:x.isdigit(), ip)))) == 4 and ip[0] != '0'
        if result is True:
            self.Confirm(1)
            return True
        else:
            self.Confirm(2)
            return False

    @pyqtSignature("")
    def on_startOneTestBtn_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.verifyIp(self.remoteIpInput.text())

    @pyqtSignature("")
    def on_startAutoTestBtn_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_showResultBtn_clicked(self):
        """
        Slot documentation goes here.
        """
        self.showWindow.show()


    @pyqtSignature("")
    def on_remoteIpInput_returnPressed(self):
        """
        Slot documentation goes here.
        """
        pass

    @pyqtSignature("")
    def on_gapTimeEdit_editingFinished(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        pass

    @pyqtSignature("QTime")
    def on_gapTimeEdit_timeChanged(self, date):
        """
        Slot documentation goes here.

        @param date DESCRIPTION
        @type QTime
        """
        # TODO: not implemented yet
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = testermain()
    myapp.show()
    sys.exit(app.exec_())
