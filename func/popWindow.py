# -*- coding: utf-8 -*-

from ui.Ui_popwindow import Ui_notice_window
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature
from base.statusDict import NOTICE_DICT as noticeDict

class NoticeWindow(QDialog, Ui_notice_window):
    def __init__(self,intArg = 0):
        QDialog.__init__(self)
        self.setupUi(self)
        self.setFixedSize(319, 119)
        self.notice_content.setText(noticeDict[intArg])
        self.status = False

    def show(self, intArg = 0):
        self.notice_content.setText(noticeDict[intArg])
        QDialog.show(self)

    def exec_(self, intArg = 0):
        self.notice_content.setText(noticeDict[intArg])
        self.status = False
        QDialog.exec_(self)


    def Confirm(self, intArg = 0):
        self.exec_(intArg)

    @pyqtSignature("")
    def on_notice_true_btn_clicked(self):
        self.status = True
        self.close()

    @pyqtSignature("")
    def on_notice_cancel_btn_clicked(self):
        self.status = False
        self.close()
