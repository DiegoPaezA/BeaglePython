# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ieb-ufsc/BeaglePython/control5Deportivo/ui/home.ui'
#
# Created: Wed May 13 15:16:46 2015
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
        MainWindow.resize(863, 712)
        MainWindow.setAutoFillBackground(False)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.layoutWidget = QtGui.QWidget(self.centralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(25, 15, 806, 681))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_6 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_6.setMargin(0)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.line_2 = QtGui.QFrame(self.layoutWidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_6.addWidget(self.line_2, 6, 0, 1, 4)
        self.line_5 = QtGui.QFrame(self.layoutWidget)
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.gridLayout_6.addWidget(self.line_5, 2, 2, 4, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Mukti Narrow"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.line = QtGui.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_3.addWidget(self.line, 2, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.Readtext = QtGui.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(12)
        self.Readtext.setFont(font)
        self.Readtext.setAlignment(QtCore.Qt.AlignCenter)
        self.Readtext.setObjectName(_fromUtf8("Readtext"))
        self.gridLayout_2.addWidget(self.Readtext, 1, 1, 1, 1)
        self.buttongo = QtGui.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(12)
        self.buttongo.setFont(font)
        self.buttongo.setObjectName(_fromUtf8("buttongo"))
        self.gridLayout_2.addWidget(self.buttongo, 1, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.line_10 = QtGui.QFrame(self.layoutWidget)
        self.line_10.setFrameShape(QtGui.QFrame.HLine)
        self.line_10.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_10.setObjectName(_fromUtf8("line_10"))
        self.gridLayout_2.addWidget(self.line_10, 0, 0, 1, 3)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_3, 0, 0, 1, 4)
        self.line_3 = QtGui.QFrame(self.layoutWidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout_6.addWidget(self.line_3, 3, 0, 1, 2)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.line_4 = QtGui.QFrame(self.layoutWidget)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout_5.addWidget(self.line_4, 1, 0, 1, 5)
        self.activarVFC = QtGui.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.activarVFC.setFont(font)
        self.activarVFC.setObjectName(_fromUtf8("activarVFC"))
        self.gridLayout_5.addWidget(self.activarVFC, 0, 2, 1, 1)
        self.activarIMUS = QtGui.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.activarIMUS.setFont(font)
        self.activarIMUS.setObjectName(_fromUtf8("activarIMUS"))
        self.gridLayout_5.addWidget(self.activarIMUS, 0, 4, 1, 1)
        self.label_11 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_5.addWidget(self.label_11, 0, 0, 1, 1)
        self.activarEMG = QtGui.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.activarEMG.setFont(font)
        self.activarEMG.setObjectName(_fromUtf8("activarEMG"))
        self.gridLayout_5.addWidget(self.activarEMG, 0, 3, 1, 1)
        self.line_9 = QtGui.QFrame(self.layoutWidget)
        self.line_9.setFrameShape(QtGui.QFrame.VLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.gridLayout_5.addWidget(self.line_9, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 1, 0, 1, 4)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.ButtonStart = QtGui.QPushButton(self.layoutWidget)
        self.ButtonStart.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(12)
        self.ButtonStart.setFont(font)
        self.ButtonStart.setObjectName(_fromUtf8("ButtonStart"))
        self.verticalLayout.addWidget(self.ButtonStart)
        self.ButtonTrigeron = QtGui.QPushButton(self.layoutWidget)
        self.ButtonTrigeron.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(12)
        self.ButtonTrigeron.setFont(font)
        self.ButtonTrigeron.setObjectName(_fromUtf8("ButtonTrigeron"))
        self.verticalLayout.addWidget(self.ButtonTrigeron)
        self.ButtonStop = QtGui.QPushButton(self.layoutWidget)
        self.ButtonStop.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(12)
        self.ButtonStop.setFont(font)
        self.ButtonStop.setObjectName(_fromUtf8("ButtonStop"))
        self.verticalLayout.addWidget(self.ButtonStop)
        self.gridLayout_6.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.resetButton = QtGui.QPushButton(self.layoutWidget)
        self.resetButton.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(12)
        self.resetButton.setFont(font)
        self.resetButton.setObjectName(_fromUtf8("resetButton"))
        self.gridLayout_4.addWidget(self.resetButton, 3, 1, 1, 1)
        self.pauseEmgButton = QtGui.QPushButton(self.layoutWidget)
        self.pauseEmgButton.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(12)
        self.pauseEmgButton.setFont(font)
        self.pauseEmgButton.setObjectName(_fromUtf8("pauseEmgButton"))
        self.gridLayout_4.addWidget(self.pauseEmgButton, 1, 1, 1, 1)
        self.line_11 = QtGui.QFrame(self.layoutWidget)
        self.line_11.setFrameShape(QtGui.QFrame.VLine)
        self.line_11.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_11.setObjectName(_fromUtf8("line_11"))
        self.gridLayout_4.addWidget(self.line_11, 0, 0, 4, 1)
        self.savePositionButton = QtGui.QPushButton(self.layoutWidget)
        self.savePositionButton.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.savePositionButton.setFont(font)
        self.savePositionButton.setObjectName(_fromUtf8("savePositionButton"))
        self.gridLayout_4.addWidget(self.savePositionButton, 2, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_4, 2, 1, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.arduinoLabel = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.arduinoLabel.setFont(font)
        self.arduinoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.arduinoLabel.setObjectName(_fromUtf8("arduinoLabel"))
        self.gridLayout.addWidget(self.arduinoLabel, 5, 0, 1, 1)
        self.labelbpsout = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(12)
        self.labelbpsout.setFont(font)
        self.labelbpsout.setAlignment(QtCore.Qt.AlignCenter)
        self.labelbpsout.setObjectName(_fromUtf8("labelbpsout"))
        self.gridLayout.addWidget(self.labelbpsout, 2, 0, 1, 1)
        self.labelintervaloRR = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(12)
        self.labelintervaloRR.setFont(font)
        self.labelintervaloRR.setAlignment(QtCore.Qt.AlignCenter)
        self.labelintervaloRR.setObjectName(_fromUtf8("labelintervaloRR"))
        self.gridLayout.addWidget(self.labelintervaloRR, 4, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout, 2, 3, 3, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_8 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout.addWidget(self.label_8)
        self.tempoProvaout = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.tempoProvaout.setFont(font)
        self.tempoProvaout.setObjectName(_fromUtf8("tempoProvaout"))
        self.horizontalLayout.addWidget(self.tempoProvaout)
        self.label_7 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout.addWidget(self.label_7)
        self.relojout = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.relojout.setFont(font)
        self.relojout.setAlignment(QtCore.Qt.AlignCenter)
        self.relojout.setObjectName(_fromUtf8("relojout"))
        self.horizontalLayout.addWidget(self.relojout)
        self.gridLayout_6.addLayout(self.horizontalLayout, 4, 0, 1, 2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_10 = QtGui.QLabel(self.layoutWidget)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_3.addWidget(self.label_10)
        self.line_8 = QtGui.QFrame(self.layoutWidget)
        self.line_8.setFrameShape(QtGui.QFrame.VLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.horizontalLayout_3.addWidget(self.line_8)
        self.plotEMG = QtGui.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.plotEMG.setFont(font)
        self.plotEMG.setObjectName(_fromUtf8("plotEMG"))
        self.horizontalLayout_3.addWidget(self.plotEMG)
        self.line_6 = QtGui.QFrame(self.layoutWidget)
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.horizontalLayout_3.addWidget(self.line_6)
        self.plotVFC = QtGui.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.plotVFC.setFont(font)
        self.plotVFC.setObjectName(_fromUtf8("plotVFC"))
        self.horizontalLayout_3.addWidget(self.plotVFC)
        self.line_7 = QtGui.QFrame(self.layoutWidget)
        self.line_7.setFrameShape(QtGui.QFrame.VLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.horizontalLayout_3.addWidget(self.line_7)
        self.plotButton = QtGui.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.plotButton.setFont(font)
        self.plotButton.setObjectName(_fromUtf8("plotButton"))
        self.horizontalLayout_3.addWidget(self.plotButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.line_12 = QtGui.QFrame(self.layoutWidget)
        self.line_12.setFrameShape(QtGui.QFrame.HLine)
        self.line_12.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_12.setObjectName(_fromUtf8("line_12"))
        self.verticalLayout_2.addWidget(self.line_12)
        self.plot = PlotWidget(self.layoutWidget)
        self.plot.setObjectName(_fromUtf8("plot"))
        self.verticalLayout_2.addWidget(self.plot)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_2.addWidget(self.label_5)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout_6.addLayout(self.verticalLayout_3, 7, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Control Interface For Developer", None))
        self.buttongo.setText(_translate("MainWindow", "GO!", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><a name=\"result_box\"/><span style=\" font-weight:600;\">T</span><span style=\" font-weight:600;\">ype the name and session number:</span></p></body></html>", None))
        self.activarVFC.setText(_translate("MainWindow", "HRV Register", None))
        self.activarIMUS.setText(_translate("MainWindow", "IMUS Register", None))
        self.label_11.setText(_translate("MainWindow", "Enable:", None))
        self.activarEMG.setText(_translate("MainWindow", "EMG Register", None))
        self.ButtonStart.setText(_translate("MainWindow", "Start Capture", None))
        self.ButtonTrigeron.setText(_translate("MainWindow", "Save Shoot Position", None))
        self.ButtonStop.setText(_translate("MainWindow", "Stop Capture", None))
        self.resetButton.setText(_translate("MainWindow", "Reset", None))
        self.pauseEmgButton.setText(_translate("MainWindow", "Pause Emg", None))
        self.savePositionButton.setText(_translate("MainWindow", "Save Position", None))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><a name=\"result_box\"/><span style=\" font-weight:600;\">C</span><span style=\" font-weight:600;\">urrent</span><span style=\" font-weight:600;\"> Variables</span></p></body></html>", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">RR Interval : </span></p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Bpm : </span></p></body></html>", None))
        self.arduinoLabel.setText(_translate("MainWindow", "--", None))
        self.labelbpsout.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">-----</span></p></body></html>", None))
        self.labelintervaloRR.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">-----</span></p></body></html>", None))
        self.label_8.setText(_translate("MainWindow", "Session Time :", None))
        self.tempoProvaout.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">00:00</span></p></body></html>", None))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Timer :</p></body></html>", None))
        self.relojout.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff0000;\">00:00</span></p></body></html>", None))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><a name=\"result_box\"/><span style=\" font-weight:600;\">S</span><span style=\" font-weight:600;\">elect Graph:</span></p></body></html>", None))
        self.plotEMG.setText(_translate("MainWindow", "EMG", None))
        self.plotVFC.setText(_translate("MainWindow", "HRV", None))
        self.plotButton.setText(_translate("MainWindow", "Plot", None))
        self.label_5.setText(_translate("MainWindow", "Develope By : Eng. Diego R. Páez Ardila, IEB-UFSC, 2015 ", None))

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

