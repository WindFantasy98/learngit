import sys
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from playsound import playsound


# --- global variables ---
MIN0_NUMBER = 0
MIN1_NUMBER = 0
SEC0_NUMBER = 0
SEC1_NUMBER = 0
MIN0_WORK_LIMIT = 0
MIN1_WORK_LIMIT = 3
SEC0_WORK_LIMIT = 0
SEC1_WORK_LIMIT = 0
MIN0_REST_LIMIT = 5
MIN1_REST_LIMIT = 0
SEC0_REST_LIMIT = 0
SEC1_REST_LIMIT = 0
STYLE_NUMBER = 1
CLOCK_RUN_FLAG = False
CLOCK_RESET = False
CLOCK_MODE = True
CLOCK_SHAKE = False
DIRECTION_SHAKE = True

class Ui_MainWindow_Info(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(719, 361)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 681, 331))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(300, 300))
        self.label.setMaximumSize(QtCore.QSize(300, 300))
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser.setMinimumSize(QtCore.QSize(350, 300))
        self.textBrowser.setMaximumSize(QtCore.QSize(350, 300))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 719, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        context = "小番茄 V1.0 帮助文档\n\n\nI'm a happy tomato!~~≥ω≤"
        self.textBrowser.setText(context)
        self.label.setPixmap(QPixmap('fonts/tomato/tomato.png'))
        self.label.setScaledContents(True)

class Ui_MainWindow_Setting(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(576, 323)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 491, 201))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setMinimumSize(QtCore.QSize(130, 35))
        self.comboBox.setMaximumSize(QtCore.QSize(130, 35))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(45, 35))
        self.label_3.setMaximumSize(QtCore.QSize(45, 35))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(45, 35))
        self.label_5.setMaximumSize(QtCore.QSize(45, 35))
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(70, 35))
        self.label_4.setMaximumSize(QtCore.QSize(70, 35))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit.setMinimumSize(QtCore.QSize(130, 35))
        self.textEdit.setMaximumSize(QtCore.QSize(130, 35))
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setMinimumSize(QtCore.QSize(200, 35))
        self.label_7.setMaximumSize(QtCore.QSize(200, 35))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setMinimumSize(QtCore.QSize(200, 35))
        self.label_8.setMaximumSize(QtCore.QSize(200, 35))
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(70, 35))
        self.label_2.setMaximumSize(QtCore.QSize(70, 35))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_2.setMinimumSize(QtCore.QSize(130, 35))
        self.textEdit_2.setMaximumSize(QtCore.QSize(130, 35))
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout.addWidget(self.textEdit_2, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(70, 35))
        self.label.setMaximumSize(QtCore.QSize(70, 35))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 240, 110, 35))
        self.pushButton.setMinimumSize(QtCore.QSize(110, 35))
        self.pushButton.setMaximumSize(QtCore.QSize(110, 35))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 576, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "紫色星球"))
        self.comboBox.setItemText(1, _translate("MainWindow", "灰色绅士"))
        self.comboBox.setItemText(2, _translate("MainWindow", "怪兽世界"))
        self.comboBox.setItemText(3, _translate("MainWindow", "七彩气球"))
        self.label_3.setText(_translate("MainWindow", "分钟"))
        self.label_5.setText(_translate("MainWindow", "分钟"))
        self.label_4.setText(_translate("MainWindow", "休息时间"))
        self.label_2.setText(_translate("MainWindow", "学习时间"))
        self.label.setText(_translate("MainWindow", "主题选择"))
        self.pushButton.setText(_translate("MainWindow", "应用"))
        self.textEdit.setText('30')
        self.textEdit_2.setText('5')
        self.textEdit.textChanged.connect(self.check_input)
        self.textEdit_2.textChanged.connect(self.check_input_2)
        self.pushButton.clicked.connect(self.on_btn)
        self.minute_flag = True
        self.second_flag = True

    def check_input(self):
        minute_num = self.textEdit.toPlainText()
        if not minute_num.isdigit():
            self.label_7.setText('输入整数鸭！')
            self.minute_flag = False
            return
        x = eval(minute_num)
        if x > 788400:
            self.label_7.setText('好好学习！！')
        elif x > 525600:
            self.label_7.setText('功夫在平时，加油！')
        elif x > 1440:
            self.label_7.setText('小火汁你要上天嘛！')
        elif x > 60:
            self.label_7.setText('不要大跃进嗷~~！┗|｀O′|┛')
        elif x >= 50:
            self.label_7.setText('劳逸结合，张弛有度~ ●﹏●')
        elif x <= 10:
            self.label_7.setText('不要调戏茄茄!＞▂＜')
        else:
            self.label_7.setText('（●>∀<●）')
        self.minute_flag = True

    def check_input_2(self):
        second_num = self.textEdit_2.toPlainText()
        if not second_num.isdigit():
            self.label_8.setText('输入整数鸭！')
            self.second_flag = False
            return
        x = eval(second_num)
        if x <= 0:
            self.label_8.setText('会休息才会学习，嗷嗷！')
        elif x >= 24*60*365:
            self.label_8.setText('这边没彩蛋嗷 (´◔ ‸◔`)')
        elif x >= 24*60*2:
            self.label_8.setText('(´◔ ‸◔`)')
        self.second_flag = True

    def on_btn(self):
        minute_num = self.textEdit.toPlainText()
        second_num = self.textEdit_2.toPlainText()
        if not(self.minute_flag and self.second_flag):
            QMessageBox.about(self, '提示信息', '输入不合法嗷！┗|｀O′|┛ ')
            return
        else:
            QMessageBox.about(self, '提示信息', '旨意收到！ (●′ω`●) ')
        global MIN1_WORK_LIMIT, MIN0_WORK_LIMIT, MIN1_REST_LIMIT, MIN0_REST_LIMIT, STYLE_NUMBER
        MIN0_WORK_LIMIT = int(minute_num) % 10
        MIN1_WORK_LIMIT = int(minute_num) % 61 // 10
        MIN0_REST_LIMIT = int(second_num) % 10
        MIN1_REST_LIMIT = int(second_num) % 61 // 10
        STYLE_NUMBER = self.comboBox.currentIndex() + 1

class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(586, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 40, 441, 152))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(82, 150))
        self.label_4.setMaximumSize(QtCore.QSize(82, 150))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(82, 150))
        self.label_2.setMaximumSize(QtCore.QSize(82, 150))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(60, 150))
        self.label_3.setMaximumSize(QtCore.QSize(60, 150))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(82, 150))
        self.label.setMaximumSize(QtCore.QSize(82, 150))
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(82, 150))
        self.label_5.setMaximumSize(QtCore.QSize(82, 150))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 4, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 210, 401, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(150, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(150, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton()
        self.pushButton_1.setMinimumSize(QtCore.QSize(150, 40))
        self.pushButton_1.setMaximumSize(QtCore.QSize(150, 40))
        self.pushButton_1.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton()
        self.pushButton_2.setMinimumSize(QtCore.QSize(150, 40))
        self.pushButton_2.setMaximumSize(QtCore.QSize(150, 40))
        self.pushButton_2.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton()
        self.pushButton_3.setMinimumSize(QtCore.QSize(150, 40))
        self.pushButton_3.setMaximumSize(QtCore.QSize(150, 40))
        self.pushButton_3.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton()
        self.pushButton_4.setMinimumSize(QtCore.QSize(150, 40))
        self.pushButton_4.setMaximumSize(QtCore.QSize(150, 40))
        self.pushButton_4.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 586, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actions = QtWidgets.QAction(MainWindow)
        self.actions.setObjectName("actions")
        self.actions_2 = QtWidgets.QAction(MainWindow)
        self.actions_2.setObjectName("actions_2")
        self.actions_3 = QtWidgets.QAction(MainWindow)
        self.actions_3.setObjectName("actions_3")
        self.menu.addAction(self.actions)
        # self.menu.addAction(self.actions_2)
        self.menu.addAction(self.actions_3)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "开始"))
        self.pushButton_1.setText(_translate("MainWindow", "暂停"))
        self.pushButton_2.setText(_translate("MainWindow", "重置"))
        self.pushButton_3.setText(_translate("MainWindow", "开始休息"))
        self.pushButton_4.setText(_translate("MainWindow", "开始学习"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.actions.setText(_translate("MainWindow", "设置"))
        # self.actions_2.setText(_translate("MainWindow", "导出数据"))
        self.actions_3.setText(_translate("MainWindow", "使用帮助"))
        self.label.setStyleSheet("border: 1px solid purple")
        self.label.setScaledContents(True)
        self.label_2.setStyleSheet("border: 1px solid purple")
        self.label_2.setScaledContents(True)
        self.label_3.setStyleSheet("border: 1px solid purple")
        self.label_3.setScaledContents(True)
        self.label_4.setStyleSheet("border: 1px solid purple")
        self.label_4.setScaledContents(True)
        self.label_5.setStyleSheet("border: 1px solid purple")
        self.label_5.setScaledContents(True)
        self.path_min0 = 'fonts/1-font/0.png'
        self.path_min1 = 'fonts/1-font/0.png'
        self.path_dot = 'fonts/1-font/dot.png'
        self.path_sec0 = 'fonts/1-font/0.png'
        self.path_sec1 = 'fonts/1-font/0.png'
        self.limit_work_min0 = 0
        self.limit_work_min1 = 3
        self.limit_work_sec0 = 0
        self.limit_work_sec1 = 0
        self.limit_rest_min0 = 5
        self.limit_rest_min1 = 0
        self.limit_rest_sec0 = 0
        self.limit_rest_sec1 = 0
        self.set_min0()
        self.set_min1()
        self.set_dot()
        self.set_sec0()
        self.set_sec1()
        self.thread_clock = Thread_Clock()
        self.thread_shake = Thread_Shake()
        self.pushButton.clicked.connect(self.on_start)
        self.pushButton_1.clicked.connect(self.on_pause)
        self.pushButton_2.clicked.connect(self.on_reset)
        self.actions.triggered.connect(self.trigger_setting)
        self.actions_2.triggered.connect(self.trigger_output)
        self.actions_3.triggered.connect(self.trigger_help)
        self.thread_clock.signal_show.connect(self.clock_show)
        self.thread_clock.signal_window_shake.connect(self.mode_change)
        self.pushButton_3.clicked.connect(self.shift_to_rest)
        self.pushButton_4.clicked.connect(self.shift_to_learn)
        self.thread_shake.signal_shake_pos.connect(shake_window)
        self.thread_ring = Thread_Ring()
        self.thread_clock.signal_ring.connect(self.start_ring)

        self.thread_clock.clock_set_work()
        self.clock_show()

    def num_to_path(self, num):
        if  isinstance(num, int):
            return 'fonts/' + str(STYLE_NUMBER) + '-font/' + str(num) + '.png'
        else:
            return 'fonts/' + str(STYLE_NUMBER) + '-font/dot.png'
    
    def clock_show(self):
        self.set_dot()
        self.set_min0()
        self.set_min1()
        self.set_sec0()
        self.set_sec1()
        self.label.setPixmap(QPixmap(self.path_min1))
        self.label_2.setPixmap(QPixmap(self.path_min0))
        self.label_3.setPixmap(QPixmap(self.path_dot))
        self.label_4.setPixmap(QPixmap(self.path_sec1))
        self.label_5.setPixmap(QPixmap(self.path_sec0))

    def start_ring(self):
        self.thread_ring.start()

    def set_min0(self):
        self.path_min0 = self.num_to_path(MIN0_NUMBER)

    def set_min1(self):
        self.path_min1 = self.num_to_path(MIN1_NUMBER)
    
    def set_dot(self):
        self.path_dot = self.num_to_path('dot')
    
    def set_sec0(self):
        self.path_sec0 = self.num_to_path(SEC0_NUMBER)

    def set_sec1(self):
        self.path_sec1 = self.num_to_path(SEC1_NUMBER)

    def on_start(self):
        global CLOCK_RUN_FLAG
        CLOCK_RUN_FLAG = True
        self.label.setStyleSheet("border: 1px solid white")
        self.label_2.setStyleSheet("border: 1px solid white")
        self.label_3.setStyleSheet("border: 1px solid white")
        self.label_4.setStyleSheet("border: 1px solid white")
        self.label_5.setStyleSheet("border: 1px solid white")
        self.thread_clock.clock_set_work()
        self.thread_clock.start()
        self.pushButton.setParent(None)
        self.horizontalLayout.addWidget(self.pushButton_1)
        self.horizontalLayout.addWidget(self.pushButton_2)

    def on_pause(self):
        print('pause')
        global CLOCK_RUN_FLAG
        CLOCK_RUN_FLAG = not CLOCK_RUN_FLAG
        if not CLOCK_RUN_FLAG:
            self.pushButton_1.setText('继续')
        else:
            self.pushButton_1.setText('暂停')

    def on_reset(self):
        print('reset')
        global CLOCK_RUN_FLAG, CLOCK_MODE, CLOCK_RESET
        CLOCK_RUN_FLAG = False
        CLOCK_MODE = True
        CLOCK_RESET = True
        self.pushButton_1.setText('继续')
        self.thread_clock.clock_reset()

    def mode_change(self):
        global CLOCK_RUN_FLAG, CLOCK_SHAKE
        if CLOCK_MODE:
            self.pushButton_1.setParent(None)
            self.pushButton_2.setParent(None)
            self.pushButton_4.setParent(None)
            self.horizontalLayout.addWidget(self.pushButton_3)
        else:
            self.pushButton_1.setParent(None)
            self.pushButton_2.setParent(None)
            self.pushButton_3.setParent(None)
            self.horizontalLayout.addWidget(self.pushButton_4)
        CLOCK_RUN_FLAG = False
        CLOCK_SHAKE = True
        show_Window()
        self.thread_shake.start()

    def shift_to_rest(self):
        global CLOCK_RUN_FLAG, CLOCK_MODE, CLOCK_SHAKE
        self.pushButton_3.setParent(None)
        self.horizontalLayout.addWidget(self.pushButton_1)
        self.horizontalLayout.addWidget(self.pushButton_2)
        CLOCK_RUN_FLAG = True
        CLOCK_MODE = False
        CLOCK_SHAKE = False
        shade_Window()

    def shift_to_learn(self):
        global CLOCK_RUN_FLAG, CLOCK_MODE, CLOCK_SHAKE
        self.pushButton_4.setParent(None)
        self.horizontalLayout.addWidget(self.pushButton_1)
        self.horizontalLayout.addWidget(self.pushButton_2)
        CLOCK_RUN_FLAG = True
        CLOCK_MODE = True
        CLOCK_SHAKE = False
        shade_Window()

    def trigger_setting(self):
        show_Setting()

    def trigger_help(self):
        show_Help()

    def trigger_output(self):
        print('trigger output')

class Thread_Shake(QThread):
    signal_shake_pos = pyqtSignal()

    def __init__(self):
        super(Thread_Shake, self).__init__()

    def run(self):
        print('thread shake')
        cnt = 0
        while(CLOCK_SHAKE):
            sleep(0.2)
            cnt += 1
            if cnt < 6:
                self.signal_shake_pos.emit()
            else:
                cnt = 0
                sleep(2)

class Thread_Clock(QThread):
    signal_show = pyqtSignal()
    signal_window_shake = pyqtSignal()
    signal_timetorest = pyqtSignal()
    signal_timetowork = pyqtSignal()
    signal_ring = pyqtSignal()

    def __init__(self):
        super(Thread_Clock, self).__init__()
    
    def run(self):
        # global CLOCK_MODE
        while(not CLOCK_RESET):
            self.signal_show.emit()
            sleep(1)
            if CLOCK_RUN_FLAG:
                if(self.is_timeout()):
                    if CLOCK_MODE:
                        self.signal_window_shake.emit()
                        self.clock_set_rest()
                        self.signal_ring.emit()
                    else:
                        self.signal_window_shake.emit()
                        self.clock_set_work()
                        self.signal_ring.emit()
                    # CLOCK_MODE = not CLOCK_MODE
                else:
                    self.clock_run()
        self.signal_show.emit()

    def is_timeout(self):
        return MIN1_NUMBER == 0 and MIN0_NUMBER == 0 and SEC0_NUMBER == 0 and SEC1_NUMBER == 0

    def clock_run(self):
        global MIN1_NUMBER, MIN0_NUMBER, SEC0_NUMBER, SEC1_NUMBER
        if SEC0_NUMBER > 0:
            SEC0_NUMBER -= 1
        else:
            if SEC1_NUMBER > 0:
                SEC1_NUMBER -= 1
                SEC0_NUMBER = 9
            else:
                if MIN0_NUMBER > 0:
                    MIN0_NUMBER -= 1
                    SEC0_NUMBER = 9
                    SEC1_NUMBER = 5
                else:
                    if MIN1_NUMBER > 0:
                        MIN1_NUMBER -= 1
                        MIN0_NUMBER = 9
                        SEC0_NUMBER = 9
                        SEC1_NUMBER = 5

    def clock_set_work(self):
        global MIN1_NUMBER, MIN0_NUMBER, SEC1_NUMBER, SEC0_NUMBER
        MIN1_NUMBER = MIN1_WORK_LIMIT
        MIN0_NUMBER = MIN0_WORK_LIMIT
        SEC1_NUMBER = SEC1_WORK_LIMIT
        SEC0_NUMBER = SEC0_WORK_LIMIT

    def clock_set_rest(self):
        global MIN1_NUMBER, MIN0_NUMBER, SEC1_NUMBER, SEC0_NUMBER
        MIN1_NUMBER = MIN1_REST_LIMIT
        MIN0_NUMBER = MIN0_REST_LIMIT
        SEC1_NUMBER = SEC1_REST_LIMIT
        SEC0_NUMBER = SEC0_REST_LIMIT

    def clock_reset(self):
        global CLOCK_RESET, CLOCK_MODE
        CLOCK_RESET = False
        CLOCK_MODE = True
        self.clock_set_work()
        self.signal_show.emit()

class Thread_Ring(QThread):
    def __init__(self):
        super(Thread_Ring, self).__init__()
    
    def run(self):
        playsound('fonts/audio/piano_jazz.wav')
        print('ring')

def show_Window():
    ui.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    ui.show()

def shade_Window():
    ui.setWindowFlags(QtCore.Qt.Widget)
    ui.show()

def shake_window():
    global DIRECTION_SHAKE
    d = 0
    if DIRECTION_SHAKE:
        d = 2
    else:
        d = -2
    DIRECTION_SHAKE = not DIRECTION_SHAKE
    ui.move(ui.x()+d, ui.y())

def show_Setting():
    ui_set.show()

def show_Help():
    ui_info.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui = QMainWindow()
    wds = Ui_MainWindow()
    wds.setupUi(ui)
    ui.setWindowTitle('小番茄')
    ui.setWindowIcon(QIcon('fonts/tomato/tomato.ico'))
    ui.show()

    ui_info = QMainWindow()
    wds_info = Ui_MainWindow_Info()
    wds_info.setupUi(ui_info)
    ui_info.setWindowTitle('帮助')

    ui_set = QMainWindow()
    wds_set = Ui_MainWindow_Setting()
    wds_set.setupUi(ui_set)
    ui_set.setWindowTitle('设置')

    sys.exit(app.exec_())