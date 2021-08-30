import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


class Demo1(QWidget):
    def __init__(self):
        super(Demo1, self).__init__()
        self.resize(300, 300)
        self.button = QPushButton('information', self)
        # 实例化一个QPushButton并将clicked信号与自定义的show_messagebox槽函数连接起来
        self.button.clicked.connect(self.show_messagebox)

    def show_messagebox(self):
        QMessageBox.information(self, 'Title', 'Content', 
                                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)


class Demo2(QWidget):
    def __init__(self):
        super(Demo2, self).__init__()
        self.resize(300, 300)
        self.button = QPushButton('Click Me!', self)
        self.button.resize(150, 150)
        self.button.clicked.connect(self.show_messagebox)

    def show_messagebox(self):
        choice = QMessageBox.question(self, 'Change Text?', 'Would you like to change the button text?',  
                             QMessageBox.Yes | QMessageBox.No) 

        if choice == QMessageBox.Yes:
            self.button.setText('you clicked yes')
        elif choice == QMessageBox.No:
            self.button.setText('you clicked no')

def test(classname):
    app = QApplication(sys.argv)
    demo = classname()
    demo.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    test(Demo2)