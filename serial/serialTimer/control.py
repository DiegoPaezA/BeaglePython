from PyQt4 import QtCore, QtGui
from ui.home import MainWindow
 

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())


