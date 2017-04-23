# -*- coding: utf-8 -*-

"""
Module implementing testermain.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QDialog, QApplication
import sys
from ui.Ui_testermain import Ui_Dialog
from showdata import showDataWindow 

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
    
    @pyqtSignature("")
    def on_startOneTestBtn_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
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
    def on_remoteIpInput_textChanged(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("")
    def on_gapTimeEdit_editingFinished(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("QTime")
    def on_gapTimeEdit_timeChanged(self, date):
        """
        Slot documentation goes here.
        
        @param date DESCRIPTION
        @type QTime
        """
        # TODO: not implemented yet
        raise NotImplementedError

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = testermain()
    myapp.show()
    sys.exit(app.exec_())
