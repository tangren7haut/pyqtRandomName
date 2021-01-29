from PyQt5.QtWidgets import QApplication, QMainWindow
from mainWindow import Ui_Form
import sys
from MWindow import Ui_MainWindow
from PyQt5.QtCore import QTimer,Qt
from gl import *
import random
import xlrd
class MY_UI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # self.showMaximized()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.draw)
        self.pushButton.clicked.connect(self.start)
        self.pushButton_2.clicked.connect(self.stop)

        self.initdata()
    def initdata(self):
        #self.data=loadJsonFile('data.json')
        xlsdata = xlrd.open_workbook("d:\\123.xls")
       # 查看所有sheet列表
       # print('All sheets: %s' % data.sheet_names())
        print(xlsdata.sheets()[0].name)
       # 获得第一个工作表
        self.table= xlsdata.sheet_by_name(xlsdata.sheets()[0].name)
        # self.data=table.col_values(1)
        # print(self.data)
        self.rows=self.table.nrows
        print(self.table.cell(0,0).value)#读取的excel行列索引从0开始
        print(self.table.cell(0,1).value)
        print(self.rows)

    def draw(self):
        # lst=self.data.copy()
        # tmp = random.choice(lst)#随机选择一个
        # self.labName.setText(tmp)
        #得到总行数
        randomRow=random.randint(1,self.rows-1)
        #得到学号
        stuno=self.table.cell(randomRow,0).value
        #得到姓名
        stuname=self.table.cell(randomRow,1).value
        self.labName.setText(stuname)
        self.labName_2.setText(str(stuno).split('.')[0])
    def start(self):
        self.timer.start(50)
    def stop(self):
        self.timer.stop()
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Return or e.key() == Qt.Key_Space:
            if self.timer.isActive():
                self.stop()
            else:
                self.start()