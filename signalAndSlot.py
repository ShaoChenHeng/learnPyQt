import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

# 该类继承QWidget
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
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

def test1():
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    test1()