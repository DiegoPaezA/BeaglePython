# -*- coding: utf-8 -*-
#
# Created: Fri Nov 28 14:43:23 2014
#
# Diego R. Paez A.
# Control Deportivo, Registro VFC e EMG
#funciones de activar y desactivar registro se encuentran desactivadas, se mejoraran en la version dos



from PyQt4 import QtCore, QtGui
from ui.home import MainWindow
 
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
