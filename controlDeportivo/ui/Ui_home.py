# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/diegopaez/PycharmProjects/controlDeportivo/ui/home.ui'
#
# Created: Fri Nov 28 14:43:23 2014
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
        MainWindow.resize(636, 544)
        MainWindow.setAutoFillBackground(False)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.layoutWidget = QtGui.QWidget(self.centralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 10, 390, 75))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setMargin(0)
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
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.Readtext = QtGui.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(12)
        self.Readtext.setFont(font)
        self.Readtext.setAlignment(QtCore.Qt.AlignCenter)
        self.Readtext.setObjectName(_fromUtf8("Readtext"))
        self.gridLayout_2.addWidget(self.Readtext, 0, 1, 1, 1)
        self.buttongo = QtGui.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(12)
        self.buttongo.setFont(font)
        self.buttongo.setObjectName(_fromUtf8("buttongo"))
        self.gridLayout_2.addWidget(self.buttongo, 0, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.layoutWidget1 = QtGui.QWidget(self.centralWidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 149, 160, 95))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.ButtonStart = QtGui.QPushButton(self.layoutWidget1)
        self.ButtonStart.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(12)
        self.ButtonStart.setFont(font)
        self.ButtonStart.setObjectName(_fromUtf8("ButtonStart"))
        self.verticalLayout.addWidget(self.ButtonStart)
        self.ButtonTrigeron = QtGui.QPushButton(self.layoutWidget1)
        self.ButtonTrigeron.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(12)
        self.ButtonTrigeron.setFont(font)
        self.ButtonTrigeron.setObjectName(_fromUtf8("ButtonTrigeron"))
        self.verticalLayout.addWidget(self.ButtonTrigeron)
        self.ButtonStop = QtGui.QPushButton(self.layoutWidget1)
        self.ButtonStop.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(12)
        self.ButtonStop.setFont(font)
        self.ButtonStop.setObjectName(_fromUtf8("ButtonStop"))
        self.verticalLayout.addWidget(self.ButtonStop)
        self.layoutWidget2 = QtGui.QWidget(self.centralWidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(420, 140, 163, 121))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget2)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.labelintervaloRR = QtGui.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(12)
        self.labelintervaloRR.setFont(font)
        self.labelintervaloRR.setAlignment(QtCore.Qt.AlignCenter)
        self.labelintervaloRR.setObjectName(_fromUtf8("labelintervaloRR"))
        self.gridLayout.addWidget(self.labelintervaloRR, 4, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.labelbpsout = QtGui.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(12)
        self.labelbpsout.setFont(font)
        self.labelbpsout.setAlignment(QtCore.Qt.AlignCenter)
        self.labelbpsout.setObjectName(_fromUtf8("labelbpsout"))
        self.gridLayout.addWidget(self.labelbpsout, 2, 0, 1, 1)
        self.layoutWidget3 = QtGui.QWidget(self.centralWidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(230, 189, 131, 22))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_7 = QtGui.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout.addWidget(self.label_7)
        self.relojout = QtGui.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.relojout.setFont(font)
        self.relojout.setAlignment(QtCore.Qt.AlignCenter)
        self.relojout.setObjectName(_fromUtf8("relojout"))
        self.horizontalLayout.addWidget(self.relojout)
        self.layoutWidget4 = QtGui.QWidget(self.centralWidget)
        self.layoutWidget4.setGeometry(QtCore.QRect(231, 149, 131, 30))
        self.layoutWidget4.setObjectName(_fromUtf8("layoutWidget4"))
        self.formLayout = QtGui.QFormLayout(self.layoutWidget4)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_5 = QtGui.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_5)
        self.readResultado = QtGui.QLineEdit(self.layoutWidget4)
        self.readResultado.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(12)
        self.readResultado.setFont(font)
        self.readResultado.setAlignment(QtCore.Qt.AlignCenter)
        self.readResultado.setObjectName(_fromUtf8("readResultado"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.readResultado)
        self.layoutWidget5 = QtGui.QWidget(self.centralWidget)
        self.layoutWidget5.setGeometry(QtCore.QRect(230, 220, 163, 21))
        self.layoutWidget5.setObjectName(_fromUtf8("layoutWidget5"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_8 = QtGui.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_2.addWidget(self.label_8)
        self.tempoProvaout = QtGui.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tempoProvaout.setFont(font)
        self.tempoProvaout.setObjectName(_fromUtf8("tempoProvaout"))
        self.horizontalLayout_2.addWidget(self.tempoProvaout)
        self.line = QtGui.QFrame(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(0, 260, 631, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralWidget)
        self.line_2.setGeometry(QtCore.QRect(0, 90, 631, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.layoutWidget6 = QtGui.QWidget(self.centralWidget)
        self.layoutWidget6.setGeometry(QtCore.QRect(40, 110, 531, 25))
        self.layoutWidget6.setObjectName(_fromUtf8("layoutWidget6"))
        self.gridLayout_6 = QtGui.QGridLayout(self.layoutWidget6)
        self.gridLayout_6.setMargin(0)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_11 = QtGui.QLabel(self.layoutWidget6)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_6.addWidget(self.label_11, 0, 0, 1, 1)
        self.activarEMG = QtGui.QCheckBox(self.layoutWidget6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.activarEMG.setFont(font)
        self.activarEMG.setObjectName(_fromUtf8("activarEMG"))
        self.gridLayout_6.addWidget(self.activarEMG, 0, 2, 1, 1)
        self.activarVFC = QtGui.QCheckBox(self.layoutWidget6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.activarVFC.setFont(font)
        self.activarVFC.setObjectName(_fromUtf8("activarVFC"))
        self.gridLayout_6.addWidget(self.activarVFC, 0, 1, 1, 1)
        self.layoutWidget7 = QtGui.QWidget(self.centralWidget)
        self.layoutWidget7.setGeometry(QtCore.QRect(7, 280, 611, 254))
        self.layoutWidget7.setObjectName(_fromUtf8("layoutWidget7"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget7)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_10 = QtGui.QLabel(self.layoutWidget7)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_3.addWidget(self.label_10)
        self.plotEMG = QtGui.QRadioButton(self.layoutWidget7)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.plotEMG.setFont(font)
        self.plotEMG.setObjectName(_fromUtf8("plotEMG"))
        self.horizontalLayout_3.addWidget(self.plotEMG)
        self.plotVFC = QtGui.QRadioButton(self.layoutWidget7)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.plotVFC.setFont(font)
        self.plotVFC.setObjectName(_fromUtf8("plotVFC"))
        self.horizontalLayout_3.addWidget(self.plotVFC)
        self.plotButton = QtGui.QPushButton(self.layoutWidget7)
        self.plotButton.setObjectName(_fromUtf8("plotButton"))
        self.horizontalLayout_3.addWidget(self.plotButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_9 = QtGui.QLabel(self.layoutWidget7)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_2.addWidget(self.label_9)
        self.plot = PlotWidget(self.layoutWidget7)
        self.plot.setObjectName(_fromUtf8("plot"))
        self.verticalLayout_2.addWidget(self.plot)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Interface de Controle", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt; font-weight:600;\">Insira o Nome e # do Teste :</span></p></body></html>", None))
        self.buttongo.setText(_translate("MainWindow", "GO!", None))
        self.ButtonStart.setText(_translate("MainWindow", "Start Capture", None))
        self.ButtonTrigeron.setText(_translate("MainWindow", "Trigger Shoot Start", None))
        self.ButtonStop.setText(_translate("MainWindow", "Stop Capture", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Intervalo RR : </span></p></body></html>", None))
        self.labelintervaloRR.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">-----</span></p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Bpm : </span></p></body></html>", None))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Variaveis Actuais </span></p></body></html>", None))
        self.labelbpsout.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">-----</span></p></body></html>", None))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Tempo :</span></p></body></html>", None))
        self.relojout.setText(_translate("MainWindow", "00:00", None))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Resultado :</span></p></body></html>", None))
        self.label_8.setText(_translate("MainWindow", "Tempo Prova :", None))
        self.tempoProvaout.setText(_translate("MainWindow", "00:00", None))
        self.label_11.setText(_translate("MainWindow", "Ativar:", None))
        self.activarEMG.setText(_translate("MainWindow", "Registro EMG", None))
        self.activarVFC.setText(_translate("MainWindow", "Registro VFC", None))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Seleccionar Grafico :</span></p></body></html>", None))
        self.plotEMG.setText(_translate("MainWindow", "EMG", None))
        self.plotVFC.setText(_translate("MainWindow", "VFC", None))
        self.plotButton.setText(_translate("MainWindow", "Plot", None))
        self.label_9.setText(_translate("MainWindow", "Resultado Captura EMG ou VFC", None))

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

