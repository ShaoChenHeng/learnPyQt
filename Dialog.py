import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QColorDialog, QFontDialog, QPushButton, \
                            QHBoxLayout, QVBoxLayout

class DemoDialog(QWidget):
    def __init__(self):
        super(DemoDialog, self).__init__()
        # QTextEdit控件用于显示文本颜色和字体变化
        self.text_edit = QTextEdit(self)

        # 实例化两个按钮分别用于打开颜色对话框和字体对话框
        self.color_btn = QPushButton('Color', self)
        self.font_btn = QPushButton('Font', self)
        self.color_btn.clicked.connect(lambda: self.open_dialog_func(self.color_btn))
        self.font_btn.clicked.connect(lambda: self.open_dialog_func(self.font_btn))

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.color_btn)
        self.h_layout.addWidget(self.font_btn)
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.text_edit)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)

    def open_dialog_func(self, btn):
        if btn == self.color_btn:
            color = QColorDialog.getColor()
            if color.isValid():
                self.text_edit.setTextColor(color)
        else:
            font, ok = QFontDialog.getFont()
            if ok:
                self.text_edit.setFont(font)

def test(classname):
    app = QApplication(sys.argv)
    demo = classname()
    demo.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    test(DemoDialog)