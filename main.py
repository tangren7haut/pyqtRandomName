

# class My_UI(QMainWindow, Ui_Form):
#     def __init__(self):
#         QMainWindow.__init__(self)
#         Ui_Form.__init__(self)
#         self.setupUi(self)
from MY_UI import *
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 显示窗口
    win = MY_UI()
    win.show()
    sys.exit(app.exec_())