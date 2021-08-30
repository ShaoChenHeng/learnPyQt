import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QPushButton, QHBoxLayout, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(300, 300)
        # 实例化一个QProgressBar
        # 默认是水平的，可以通过setOrientation(Qt.Vertical)让进度条垂直显示
        self.progressbar = QProgressBar(self)
        # self.progressbar.setOrientation(Qt.Vertical) 

        # 通过setMinimum()和setMaximum()方法来设置范围
        # 也可以单单用setRange()方法来实现
        self.progressbar.setMinimum(0)
        self.progressbar.setMaximum(100)
        # self.progressbar.setRange(0, 100)

        self.step = 0
        
        # 实例化一个QTimer
        # 并将timeout信号连接到update_func()槽函数上：
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_func)

        # 实例化一个QPushButton按钮来控制QTimer的启动与停止
        self.ss_button = QPushButton('Start', self)
        self.ss_button.clicked.connect(self.start_stop_func)
        # 实例化一个QPushButton按钮来控制QTimer的重置
        self.reset_button = QPushButton('Reset', self)
        self.reset_button.clicked.connect(self.reset_func)

        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.h_layout.addWidget(self.ss_button)
        self.h_layout.addWidget(self.reset_button)
        self.v_layout.addWidget(self.progressbar)
        self.v_layout.addLayout(self.h_layout)

        self.setLayout(self.v_layout)

    def update_func(self):
        self.step += 1
        self.progressbar.setValue(self.step)

        if self.step >= 100:
            self.ss_button.setText('Start')
            self.timer.stop()
            self.step = 0

    def start_stop_func(self):
        if self.ss_button.text() == 'Start':
            self.ss_button.setText('Stop')
            self.timer.start(100)
        else:
            self.ss_button.setText('Start')
            self.timer.stop()

    def reset_func(self):
        self.progressbar.reset()
        self.ss_button.setText('Start')
        self.timer.stop()
        self.step = 0

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())