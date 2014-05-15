# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ieb-ufsc/PycharmProjects/rrinterface/ui/home.ui'
#
# Created: Tue Feb 24 16:54:53 2015
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(631, 570)
        MainWindow.setAutoFillBackground(False)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.line_2 = QtGui.QFrame(self.centralWidget)
        self.line_2.setGeometry(QtCore.QRect(0, 90, 631, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(41, 11, 215, 37))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Mukti Narrow"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.ButtonStart = QtGui.QPushButton(self.centralWidget)
        self.ButtonStart.setEnabled(True)
        self.ButtonStart.setGeometry(QtCore.QRect(40, 130, 111, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(12)
        self.ButtonStart.setFont(font)
        self.ButtonStart.setObjectName(_fromUtf8("ButtonStart"))
        self.ButtonStop = QtGui.QPushButton(self.centralWidget)
        self.ButtonStop.setEnabled(True)
        self.ButtonStop.setGeometry(QtCore.QRect(170, 130, 111, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(12)
        self.ButtonStop.setFont(font)
        self.ButtonStop.setObjectName(_fromUtf8("ButtonStop"))
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(210, 230, 111, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(40, 230, 52, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_6 = QtGui.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(40, 200, 161, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.labelintervaloRR = QtGui.QLabel(self.centralWidget)
        self.labelintervaloRR.setGeometry(QtCore.QRect(340, 230, 28, 18))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(12)
        self.labelintervaloRR.setFont(font)
        self.labelintervaloRR.setAlignment(QtCore.Qt.AlignCenter)
        self.labelintervaloRR.setObjectName(_fromUtf8("labelintervaloRR"))
        self.labelbpsout = QtGui.QLabel(self.centralWidget)
        self.labelbpsout.setGeometry(QtCore.QRect(110, 230, 28, 18))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(12)
        self.labelbpsout.setFont(font)
        self.labelbpsout.setAlignment(QtCore.Qt.AlignCenter)
        self.labelbpsout.setObjectName(_fromUtf8("labelbpsout"))
        self.plotButton = QtGui.QPushButton(self.centralWidget)
        self.plotButton.setGeometry(QtCore.QRect(310, 130, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.plotButton.setFont(font)
        self.plotButton.setObjectName(_fromUtf8("plotButton"))
        self.plot = PlotWidget(self.centralWidget)
        self.plot.setGeometry(QtCore.QRect(10, 310, 601, 241))
        self.plot.setObjectName(_fromUtf8("plot"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "VFC INTERFACE", None))
        self.ButtonStart.setText(_translate("MainWindow", "Start Capture", None))
        self.ButtonStop.setText(_translate("MainWindow", "Stop Capture", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Intervalo RR : </span></p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Bpm : </span></p></body></html>", None))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Variaveis Actuais </span></p></body></html>", None))
        self.labelintervaloRR.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">-----</span></p></body></html>", None))
        self.labelbpsout.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">-----</span></p></body></html>", None))
        self.plotButton.setText(_translate("MainWindow", "Plot", None))

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

