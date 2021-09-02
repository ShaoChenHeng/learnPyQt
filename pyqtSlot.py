import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class Ui_Calc(object):
    def setupUi(self, Form):
        self.inputSpinBox1 = QtWidgets.QSpinBox(Form)
        self.inputSpinBox1.setGeometry(QtCore.QRect(1, 26, 46, 25))
        self.inputSpinBox1.setObjectName("inputSpinBox1")

        self.inputSpinBox2 = QtWidgets.QSpinBox(Form)
        self.inputSpinBox2.setGeometry(QtCore.QRect(70, 26, 46, 25))
        self.inputSpinBox2.setObjectName("inputSpinBox2")

        self.outputWideget = QLabel(Form)
        self.outputWideget.setGeometry(QtCore.QRect(140, 24, 36, 27))
        self.outputWideget.setObjectName("outputWidget")

        QtCore.QMetaObject.connectSlotsByName(Form)

class MyCalc(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_Calc()
        self.ui.setupUi(self)

    @pyqtSlot(int)
    def on_inputSpinBox1_valueChanged(self, value):
        self.ui.outputWideget.setText(str(value + self.ui.inputSpinBox2.value()))
    
    @pyqtSlot(int)
    def on_inputSpinBox2_valueChanged(self, value):
        message = str(value + self.ui.inputSpinBox1.value())
        self.ui.outputWideget.setText(message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyCalc()
    win.show()
    sys.exit(app.exec_())

'''
@PyQt5.QtCore.pyqtSlot(...)
def on_发送者对象名称_发射信号名称(self, 参数):
    pass
'''