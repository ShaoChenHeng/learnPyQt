import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

# 该类继承QWidget
class Demo1(QWidget):
    def __init__(self):
        super(Demo1, self).__init__()
        # 实例化一个QPushButton
        self.button = QPushButton('Start', self)

        # 连接信号与槽函数
        # self.button就是一个控件
        # clicked(按钮被点击)是该控件的一个信号
        # connect()即连接
        # self.change_text即下方定义的函数(我们称之为槽函数)
        # 所以通用的公式可以是：widget.signal.connect(slot)；
        self.button.clicked.connect(self.change_text)

    def change_text(self):
        print('change text')
        # 将按钮文本从‘Start’改成‘Stop’
        self.button.setText('stop')
        # 信号和槽解绑
        # 解绑后再按按钮你会发现控制台不会再输出‘change text’，如果把这行解绑的代码注释掉
        # 你会发现每按一次按钮 控制台都会输出一次‘change text’；
        self.button.clicked.disconnect(self.change_text)

class Demo2(QWidget):
    def __init__(self):
        super(Demo2, self).__init__()
        self.button = QPushButton('Start', self)
        # 将pressed和released信号连接搭配change_text()槽函数上
        self.button.pressed.connect(self.change_text)
        self.button.released.connect(self.change_text)

    def change_text(self):
        if self.button.text() == 'Start':
            self.button.setText('Stop')
        else:
            self.button.setText('Start')
    
class Demo3(QWidget):
    def __init__(self):
        super(Demo3, self).__init__()
        self.button = QPushButton('Start', self)
        # 效果同Demo2
        self.button.pressed.connect(self.button.released)
        self.button.released.connect(self.change_text)

    def change_text(self):
        if self.button.text() == 'Start':
            self.button.setText('Stop')
        else:
            self.button.setText('Start')

class Demo4(QWidget):
    def __init__(self):
        super(Demo4, self).__init__()
        self.resize(300, 300)
        self.setWindowTitle('demo')
        self.button = QPushButton('Start', self)
        self.button.clicked.connect(self.change_text)
        # 修改窗口大小
        self.button.clicked.connect(self.change_window_size)
        # 修改窗口名称
        self.button.clicked.connect(self.change_window_title)

    def change_text(self):
        print('change_text')
        self.button.setText('Stop')
        self.button.clicked.disconnect(self.change_text)

    def change_window_size(self):
        print('change window size')
        self.resize(800, 800)
        self.button.clicked.disconnect(self.change_window_size)
    
    def change_window_title(self):
        print('change window title')
        self.setWindowTitle('window title changed')
        self.button.clicked.disconnect(self.change_window_title)

class Demo5(QWidget):
    # 实例化一个自定义的信号
    my_signal = pyqtSignal()

    def __init__(self):
        super(Demo5, self).__init__()
        self.resize(300, 300)
        self.label = QLabel('Hello World', self)
        # 将自定义的信号连接到自定义的槽函数上
        self.my_signal.connect(self.change_text)
    
    def change_text(self):
        if self.label.text() == 'Hello World':
            self.label.setText('Hello PyQt5')
        else:
            self.label.setText('Hello World')
    
    # mousePressEvent()方法是许多控件自带的
    # 这里来自于QWidget 该方法用来监测鼠标是否有按下
    # 现在鼠标若被按下 则会发出自定义的信号
    def mousePressEvent(self, QMouseEvent):
        self.my_signal.emit()

def test(classname):
    app = QApplication(sys.argv)
    demo = classname()
    demo.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    test(Demo3)