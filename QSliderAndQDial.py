import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QLabel, QVBoxLayout, QHBoxLayout, QDial


class DemoQSlider(QWidget):
    def __init__(self):
        super(DemoQSlider, self).__init__()
        self.resize(300, 300)
        # 通过传入Qt.Hrizontal可以实例化一个水平的滑动条
        # 传入Qt.Vertical的话可以实例化一个垂直的滑动条
        self.slider_1 = QSlider(Qt.Horizontal, self)
        # 通过setRange()方法可以设置滑动条的范围
        self.slider_1.setRange(0, 100)
        # 当滑动时，数值发生改变，触发valueChanged信号
        self.slider_1.valueChanged.connect(lambda: self.on_change_func(self.slider_1))

        # 垂直的滑动条
        self.slider_2 = QSlider(Qt.Vertical, self)
        # 除了setRange()方法 还可以使用setMinimum()和setMaximum()方法来设置最小值和最大值
        self.slider_2.setMinimum(0)
        self.slider_2.setMaximum(100)
        self.slider_2.valueChanged.connect(lambda: self.on_change_func(self.slider_2))

        # 显示QSlider当前的数值
        self.label = QLabel('0', self)
        self.label.setFont(QFont('Arial Black', 20))

        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.h_layout.addWidget(self.slider_2)
        self.h_layout.addStretch(1)
        self.h_layout.addWidget(self.label)
        self.h_layout.addStretch(1)

        self.v_layout.addWidget(self.slider_1)
        self.v_layout.addLayout(self.h_layout)
        
        self.setLayout(self.v_layout)

        # 在自定义的槽函数中
        # 将两个滑动条的数值同步
        # 然后用QLabel显示出当前数值。
    def on_change_func(self, slider):
        if slider == self.slider_1:
            self.slider_2.setValue(self.slider_1.value())
            self.label.setText(str(self.slider_1.value()))
        else:
            self.slider_1.setValue(self.slider_2.value())
            self.label.setText(str(self.slider_2.value()))

class DemoQDial(QWidget):
    def __init__(self):
        super(DemoQDial, self).__init__()
        self.resize(300, 300)

        # 设置窗口标题
        self.setWindowTitle('QDial')

        self.dial = QDial(self)
        # 通过setFixedSize()方法来固定QDial的大小
        self.dial.setFixedSize(100, 100)
        # 使用setRange()方法来设置表盘数值范围
        # 也可以使用setMinimum()和setMaximum()方法
        self.dial.setRange(0, 100)
        # setNotchesVisible(True)可以显示刻度
        # 刻度会根据我们设置的数值自动调整；
        self.dial.setNotchesVisible(True)
        self.dial.valueChanged.connect(self.on_change_func)

        self.label = QLabel('0', self)
        self.label.setFont(QFont('Arial Black', 20))

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.dial)
        self.h_layout.addWidget(self.label)

        self.setLayout(self.h_layout)

    def on_change_func(self):
        self.label.setText(str(self.dial.value()))

def test(classname):
    app = QApplication(sys.argv)
    demo = classname()  
    demo.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    test(DemoQDial)