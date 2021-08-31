import sys
import time
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.count = 0
        self.resize(300, 300)

        self.button = QPushButton('Start', self)
        self.button.clicked.connect(self.count_func)
        self.button_2 = QPushButton('Stop', self)
        self.button_2.clicked.connect(self.stop_count_func)

        self.label = QLabel('0', self)
        self.label.setAlignment(Qt.AlignCenter)

        self.my_thread = MyThread()
        self.my_thread.my_signal.connect(self.set_label_func)

        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()
        self.h_layout.addWidget(self.button)
        self.h_layout.addWidget(self.button_2)
        self.v_layout.addWidget(self.label)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)

    def count_func(self):
        self.my_thread.is_on = True
        self.my_thread.start()

    def stop_count_func(self, num):
        self.my_thread.is_on = False
        self.my_thread.count = 0

    def set_label_func(self, num):
        self.label.setText(num)


class MyThread(QThread):
    # MyThread()类中自定义一个信号
    # pyqtSignal(str)加上str就代表这个信号可以传一个字符串数值
    my_signal = pyqtSignal(str)

    def __init__(self):
        super(MyThread, self).__init__()
        self.count = 0
        self.is_on = True

    def run(self):
        while self.is_on:
            print(self.count)
            self.count += 1
            # 调用信号的emit()函数释放信号
            # 其中传入str(self.count)字符串值
            # count变量本身是int类型 而信号要传递的是字符串 所以要调用str()方法将count转为字符串
            # 每次循环都会释放信号 而该信号会同时传递count变量的字符串值
            self.my_signal.emit(str(self.count))
            self.sleep(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())