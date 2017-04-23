# coding: utf-8
import sys
from PyQt4 import QtGui
from func.testermain import testermain
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = testermain()
    myapp.show()
    sys.exit(app.exec_())
    
