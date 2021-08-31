import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QScrollArea, QScrollBar, \
                            QHBoxLayout, QVBoxLayout

class DemoScroll(QWidget):
    def __init__(self):
        super(DemoScroll, self).__init__()
        # 实例化一个QLabel控件用于显示大图
        # setScaledContents(True)方法可以让图片随着QLabel控件大小变化而变化
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('images/image.jpg'))
        self.label.setScaledContents(True)

        # 实例化一个QScrollArea控件
        self.scroll_area = QScrollArea(self)
        # 调用setWidget()方法将QLabel滚动区域中的控件
        self.scroll_area.setWidget(self.label)
        # 将滚动区域自带的横向滚动条给隐藏掉
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # 隐藏纵向 self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # 实例化一个横向滚动条 调用setMaximum()方法设置最大值
        self.scrollbar = QScrollBar(Qt.Horizontal, self)
        self.scrollbar.setMaximum(self.scroll_area.horizontalScrollBar().maximum())

        # 实例化两个按钮用于放大缩小QLabel控件
        self.bigger_btn = QPushButton('Zoom in', self)
        self.smaller_btn = QPushButton('Zoom out', self)

        self.bigger_btn.clicked.connect(self.bigger_func)
        self.smaller_btn.clicked.connect(self.smaller_func)
        self.scrollbar.valueChanged.connect(self.sync_func)        

        self.h_layout = QHBoxLayout()                        
        self.h_layout.addWidget(self.bigger_btn)
        self.h_layout.addWidget(self.smaller_btn)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.scroll_area)
        self.v_layout.addWidget(self.scrollbar)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)

    def bigger_func(self):
        self.label.resize(self.label.width() * 1.2, self.label.height() * 1.2)
        self.scrollbar.setMaximum(self.scroll_area.horizontalScrollBar().maximum())

    def smaller_func(self):
        self.label.resize(self.label.width() * 0.8, self.label.height() * 0.8)
        self.scrollbar.setMaximum(self.scroll_area.horizontalScrollBar().maximum())
    
    # QScrollArea横向滚动条的当前值和QScrollBar的值同步
    def sync_func(self):
        self.scroll_area.horizontalScrollBar().setValue(self.scrollbar.value())

def test(classname):
    app = QApplication(sys.argv)
    demo = classname()
    demo.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    test(DemoScroll)