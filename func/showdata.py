# -*- coding: utf-8 -*-

"""
Module implementing showDataWindow.
"""

from PyQt4.QtCore import pyqtSignature,QUrl,QString
from PyQt4.QtGui import QDialog
import os

from ui.Ui_showdata import Ui_showDataWindow
try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

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
        self.setFixedSize(700,450)
        self.webView.setUrl(
            QUrl(_fromUtf8("file:///" + '/'.join(os.getcwd().split('\\')) + "/echart/show.html")))
    
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
