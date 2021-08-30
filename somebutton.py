import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolButton, QCheckBox,QVBoxLayout


class DemoQPushButton(QWidget):
    def __init__(self):
        super(DemoQPushButton, self).__init__()
        self.resize(300, 300)
        self.test_button = QPushButton('Test', self)
        # 标记按钮 True False 状态不同显示的样子不同
        # True 为可标记的按钮 False 为不可标记的按钮
        # 可以通过isCheckable()方法来判断该按钮是否是可标记的
        self.test_button.setCheckable(True)
        # 通过setIcon()方法给按钮设置一个图标
        # 传入的参数为QIcon()
        self.test_button.setIcon(QIcon('bird.png'))
        # toggled信号是专门用来配合按钮标记状态变化的
        # 也就是说按钮标记状态发生变化就会发出toggled信号
        self.test_button.toggled.connect(self.button_state_func)

    def button_state_func(self):
        print(self.test_button.isChecked())

class DemoQToolButton(QWidget):
    def __init__(self):
        super(DemoQToolButton, self).__init__()
        self.resize(300, 300)
        self.test_button = QToolButton(self)
        self.test_button.setCheckable(True)
        self.test_button.setIcon(QIcon('bird.png'))
        self.test_button.toggled.connect(self.button_state_func)
        self.test_button.isCheckable()
    
    def button_state_func(self):
        print(self.test_button.isChecked())

class DemoQCheckBox(QWidget):
    def __init__(self):
        super(DemoQCheckBox, self).__init__()
        self.resize(300, 300)
        self.checkbox1 = QCheckBox('Checkbox 1', self)
        self.checkbox2 = QCheckBox('Checkbox 2', self)
        self.checkbox3 = QCheckBox('Checkbox 3', self)

        self.v_layout = QVBoxLayout()

        self.checkbox_init()
        self.layout_init()

    def layout_init(self):
        self.v_layout.addWidget(self.checkbox1)
        self.v_layout.addWidget(self.checkbox2)
        self.v_layout.addWidget(self.checkbox3)

        self.setLayout(self.v_layout)

    def checkbox_init(self):
        self.checkbox1.setChecked(True)
        # self.checkbox1.setCheckState(Qt.Checked)

        #stateChanged信号会在复选框状态发生改变的时候发出
        # 这里我们发现槽函数是带参数的 可以通过lambda表达式来将参数传入槽函数
        # 若单纯使用self.on_state_change_func(self.checkbox2)则会报错
        self.checkbox1.stateChanged.connect(lambda: self.on_state_change_func(self.checkbox1))

        self.checkbox2.setChecked(False)
        # self.checkbox2.setCheckState(Qt.Unchecked)
        self.checkbox2.stateChanged.connect(lambda: self.on_state_change_func(self.checkbox2))

        self.checkbox3.setTristate(True)
        self.checkbox3.setCheckState(Qt.PartiallyChecked)
        self.checkbox3.stateChanged.connect(lambda: self.on_state_change_func(self.checkbox3))      

    def on_state_change_func(self, checkbox):
        # checkState()方法可以获取当前复选框的状态
        # 返回值为int类型 0为无选中状态 1为半选中状态 2为选中状态。
        print('{} was clicked, and its current state is {}'.format(checkbox.text(), checkbox.checkState()))

def test(classname):
    app = QApplication(sys.argv)
    demo = classname()
    demo.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    test(DemoQCheckBox)