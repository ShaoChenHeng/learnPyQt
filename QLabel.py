import sys
from PyQt5.QtWidgets import QApplication, QLabel

if __name__ == '__main__':
    app = QApplication(sys.argv)
    label = QLabel()
    # 加上 html 代码可以修改文本样式
    label.setText('<font color="red">Hello</font> <h1>World</h1>')
    # label.setText('Hello World!')

    # show()方法使控件可见(默认是隐藏)
    label.show()

    # app.exec_()是执行应用 
    # 让应用开始运转循环
    # 直到窗口关闭返回0给sys.exit()
    sys.exit(app.exec_())