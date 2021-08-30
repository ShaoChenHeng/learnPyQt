import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QMessageBox, QVBoxLayout


class DemoWindowCloseEvent(QWidget):
    def __init__(self):
        super(DemoWindowCloseEvent, self).__init__()
        # is_saved变量用于记录用户是否已经进行保存
        self.is_saved = True  
        
        # 实例化一个QTextEdit控件用于文本编辑
        self.textedit = QTextEdit(self)                                 # 2
        self.textedit.textChanged.connect(self.on_textchanged_func)

        # 实例化一个按钮用于保存操作
        self.button = QPushButton('Save', self)                         # 3
        self.button.clicked.connect(self.on_clicked_func)

        self.v_layout = QVBoxLayout()   
        self.v_layout.addWidget(self.textedit)
        self.v_layout.addWidget(self.button)
        self.setLayout(self.v_layout)

    def on_textchanged_func(self):
        # 文本有变化就将is_saved设置为False 即未保存
        if self.textedit.toPlainText():
            self.is_saved = False
        else:
            self.is_saved = True
    
    def on_clicked_func(self):
        self.save_func(self.textedit.toPlainText())
        self.is_saved = True
    
    def save_func(self, text):          
        with open('saved.txt', 'w') as f:
            f.write(text)
    
    def closeEvent(self, QCloseEvent):
        if not self.is_saved:
            choice = QMessageBox.question(self, '', 'Do you want to save the text?',
                                          QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if choice == QMessageBox.Yes:
                self.save_func(self.textedit.toPlainText())
                QCloseEvent.accept()
            elif choice == QMessageBox.No:
                QCloseEvent.accept()
            else:
                QCloseEvent.ignore()

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QVBoxLayout
class DemoMouseEvent(QWidget):
    def __init__(self):
        super(DemoMouseEvent, self).__init__()
        self.resize(300, 300)
        #  button_label用来显示鼠标的点击和释放动作
        self.button_label = QLabel('No Button Pressed', self)
        # xy_label用于记录鼠标相对于QWidget窗口的坐标
        self.xy_label = QLabel('x:0, y:0', self)
        # global_xy_label用于记录鼠标相对于显示屏屏幕的坐标
        self.global_xy_label = QLabel('global x:0, global y:0', self) 

        self.button_label.setAlignment(Qt.AlignCenter)
        self.xy_label.setAlignment(Qt.AlignCenter)
        self.global_xy_label.setAlignment(Qt.AlignCenter)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.button_label)
        self.v_layout.addWidget(self.xy_label)
        self.v_layout.addWidget(self.global_xy_label)
        self.setLayout(self.v_layout)

        # setMouseTracking(True)方法可以让窗口始终追踪鼠标
        # 否则只能每次等鼠标被点击后 窗口才会开始记录鼠标的动作变化
        # 而鼠标释放后 窗口又会不进行记录了 比较麻烦
        
        self.setMouseTracking(True)

    # mouseMoveEvent()为鼠标移动时所触发的响应函数
    # 通过x()和y()方法获取鼠标相对于QWidget窗口的坐标
    # 用globalX()和globalY()方法获取鼠标相对于显示屏屏幕的坐标
    def mouseMoveEvent(self, QMouseEvent):
        x = QMouseEvent.x()
        y = QMouseEvent.y()
        global_x = QMouseEvent.globalX()
        global_y = QMouseEvent.globalY()

        self.xy_label.setText('x:{}, y:{}'.format(x, y))
        self.global_xy_label.setText('global x:{}, global y:{}'.format(global_x, global_y))

    #  mousePressEvent()为鼠标被按下时所触发的响应函数
    # 通过button()方法来确认被按下的键
    # 用button_label显示被按下的键；
    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.button_label.setText('Left Button Pressed')
        elif QMouseEvent.button() == Qt.MidButton:
            self.button_label.setText('Middle Button Pressed')
        elif QMouseEvent.button() == Qt.RightButton:
            self.button_label.setText('Right Button Pressed')

    # 类似mousePressEvent
    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.button_label.setText('Left Button Released')
        elif QMouseEvent.button() == Qt.MidButton:
            self.button_label.setText('Middle Button Released')
        elif QMouseEvent.button() == Qt.RightButton:
            self.button_label.setText('Right Button Released')

    # 鼠标双击事件
    def mouseDoubleClickEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.button_label.setText('Left Button Double Clikced')
        elif QMouseEvent.button() == Qt.MidButton:
            self.button_label.setText('Middle Button Double Clicked')
        elif QMouseEvent.button() == Qt.RightButton:
            self.button_label.setText('Right Button Double Clikced')

from PyQt5.QtGui import QPixmap

class DemoKeyboardEvent(QWidget):
    def __init__(self):
        super(DemoKeyboardEvent, self).__init__()
        # pic_label用于设置图片
        # 先将初始化的图片设为bird.png
        self.resize(300, 300)
        self.pic_label = QLabel(self)
        self.pic_label.setPixmap(QPixmap('bird.png'))
        self.pic_label.setAlignment(Qt.AlignCenter)

        # key_label用于记录按键状态
        self.key_label = QLabel('No Key Pressed', self)
        self.key_label.setAlignment(Qt.AlignCenter)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.pic_label)
        self.v_layout.addWidget(self.key_label)
        self.setLayout(self.v_layout)

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Up:
            self.pic_label.setPixmap(QPixmap('birdup.png'))
            self.key_label.setText('Key Up Pressed')
        elif QKeyEvent.key() == Qt.Key_Down:
            self.pic_label.setPixmap(QPixmap('birddown.png'))
            self.key_label.setText('Key Down Pressed')
        elif QKeyEvent.key() == Qt.Key_Left:
            self.pic_label.setPixmap(QPixmap('birdleft.png'))
            self.key_label.setText('Key Left Pressed')
        elif QKeyEvent.key() == Qt.Key_Right:
            self.pic_label.setPixmap(QPixmap('birdright.png'))
            self.key_label.setText('Key Right Pressed')

    def keyReleaseEvent(self, QKeyEvent):                               # 4
        self.pic_label.setPixmap(QPixmap('bird.png'))
        self.key_label.setText('Key Released')


def test(classname):
    app = QApplication(sys.argv)
    demo = classname()
    demo.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    test(DemoKeyboardEvent)
