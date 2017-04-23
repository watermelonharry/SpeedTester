# -*- coding: utf-8 -*-

"""
Module implementing showDataWindow.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QDialog

from ui.Ui_showdata import Ui_showDataWindow


class showDataWindow(QDialog, Ui_showDataWindow):
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
        self.setFixedSize(628,436)
    
    @pyqtSignature("bool")
    def on_webView_loadFinished(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        pass
    
    @pyqtSignature("QUrl")
    def on_webView_urlChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type QUrl
        """
        # TODO: not implemented yet
        pass
