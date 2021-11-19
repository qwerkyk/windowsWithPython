import sys
from PyQt5.QtWidgets import*

class text1(QWidget):
    def __int__(self):
        super().__init__()
        self.title='测试代码1号'
        self.initUI()
    def initUI(self):
        self.setWindowTitle(self.title)
        bt1=QPushButton("整数输入")
        bt2=QPushButton("浮点数输入")
        bt3=QPushButton("字符串输入")
        bt4=QPushButton("下拉列表对话框")
        vlayout.addWidget(bt1)
if __name__ == '__main__':
	app = QApplication(sys.argv)
	mainWindows = QMainWindow()
	ui = Ui_MainWindow()
	# 向主窗口上添加控件
	ui.setupUi(mainWindows)
	mainWindows.show()
	sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

