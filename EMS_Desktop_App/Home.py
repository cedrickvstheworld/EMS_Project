# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/MainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1370, 750)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/favicon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.employeeinfo_toolbtn = QtGui.QToolButton(self.centralwidget)
        self.employeeinfo_toolbtn.setEnabled(False)
        self.employeeinfo_toolbtn.setGeometry(QtCore.QRect(1070, 10, 131, 101))
        self.employeeinfo_toolbtn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.employeeinfo_toolbtn.setStyleSheet(_fromUtf8("QToolButton{border: None;}"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/attendance.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.employeeinfo_toolbtn.setIcon(icon1)
        self.employeeinfo_toolbtn.setIconSize(QtCore.QSize(110, 110))
        self.employeeinfo_toolbtn.setObjectName(_fromUtf8("employeeinfo_toolbtn"))
        self.charts_toolbtn = QtGui.QToolButton(self.centralwidget)
        self.charts_toolbtn.setEnabled(False)
        self.charts_toolbtn.setGeometry(QtCore.QRect(770, 10, 131, 101))
        self.charts_toolbtn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.charts_toolbtn.setStyleSheet(_fromUtf8("QToolButton{border: None;}"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/bargraph.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.charts_toolbtn.setIcon(icon2)
        self.charts_toolbtn.setIconSize(QtCore.QSize(95, 95))
        self.charts_toolbtn.setObjectName(_fromUtf8("charts_toolbtn"))
        self.settings_toolbtn = QtGui.QToolButton(self.centralwidget)
        self.settings_toolbtn.setEnabled(False)
        self.settings_toolbtn.setGeometry(QtCore.QRect(1220, 10, 131, 101))
        self.settings_toolbtn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.settings_toolbtn.setStyleSheet(_fromUtf8("QToolButton{border: None;}"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("icons/settings2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_toolbtn.setIcon(icon3)
        self.settings_toolbtn.setIconSize(QtCore.QSize(85, 85))
        self.settings_toolbtn.setObjectName(_fromUtf8("settings_toolbtn"))
        self.register_toolbtn = QtGui.QToolButton(self.centralwidget)
        self.register_toolbtn.setEnabled(False)
        self.register_toolbtn.setGeometry(QtCore.QRect(920, 10, 131, 101))
        self.register_toolbtn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.register_toolbtn.setStyleSheet(_fromUtf8("QToolButton{border: None;}"))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("icons/profile.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.register_toolbtn.setIcon(icon4)
        self.register_toolbtn.setIconSize(QtCore.QSize(100, 100))
        self.register_toolbtn.setObjectName(_fromUtf8("register_toolbtn"))
        self.time_label = QtGui.QLabel(self.centralwidget)
        self.time_label.setGeometry(QtCore.QRect(30, 30, 431, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.time_label.setFont(font)
        self.time_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.time_label.setObjectName(_fromUtf8("time_label"))
        self.date_label = QtGui.QLabel(self.centralwidget)
        self.date_label.setGeometry(QtCore.QRect(30, 90, 451, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.date_label.setFont(font)
        self.date_label.setStyleSheet(_fromUtf8(""))
        self.date_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.date_label.setObjectName(_fromUtf8("date_label"))
        self.table_frame = QtGui.QFrame(self.centralwidget)
        self.table_frame.setGeometry(QtCore.QRect(490, 170, 851, 541))
        self.table_frame.setStyleSheet(_fromUtf8(""))
        self.table_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.table_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.table_frame.setObjectName(_fromUtf8("table_frame"))
        self.search_lineEdit = QtGui.QLineEdit(self.table_frame)
        self.search_lineEdit.setGeometry(QtCore.QRect(20, 20, 301, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.search_lineEdit.setFont(font)
        self.search_lineEdit.setText(_fromUtf8(""))
        self.search_lineEdit.setObjectName(_fromUtf8("search_lineEdit"))
        self.name_label = QtGui.QLabel(self.table_frame)
        self.name_label.setGeometry(QtCore.QRect(210, 500, 621, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.name_label.setFont(font)
        self.name_label.setText(_fromUtf8(""))
        self.name_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name_label.setObjectName(_fromUtf8("name_label"))
        self.attendance_view = QtGui.QTableWidget(self.table_frame)
        self.attendance_view.setGeometry(QtCore.QRect(20, 70, 811, 421))
        self.attendance_view.setObjectName(_fromUtf8("attendance_view"))
        self.attendance_view.setColumnCount(0)
        self.attendance_view.setRowCount(0)
        self.search_lineEdit_2 = QtGui.QLineEdit(self.table_frame)
        self.search_lineEdit_2.setGeometry(QtCore.QRect(20, 20, 301, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.search_lineEdit_2.setFont(font)
        self.search_lineEdit_2.setText(_fromUtf8(""))
        self.search_lineEdit_2.setObjectName(_fromUtf8("search_lineEdit_2"))
        self.label_search = QtGui.QLabel(self.table_frame)
        self.label_search.setGeometry(QtCore.QRect(320, 20, 31, 31))
        self.label_search.setText(_fromUtf8(""))
        self.label_search.setPixmap(QtGui.QPixmap(_fromUtf8("icons/search (1).png")))
        self.label_search.setScaledContents(True)
        self.label_search.setObjectName(_fromUtf8("label_search"))
        self.btn_close = QtGui.QToolButton(self.table_frame)
        self.btn_close.setGeometry(QtCore.QRect(790, 20, 41, 41))
        self.btn_close.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btn_close.setStyleSheet(_fromUtf8("QToolButton{border: None;}"))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("icons/close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon5)
        self.btn_close.setIconSize(QtCore.QSize(36, 36))
        self.btn_close.setObjectName(_fromUtf8("btn_close"))
        self.user_pass = QtGui.QLineEdit(self.centralwidget)
        self.user_pass.setGeometry(QtCore.QRect(30, 540, 381, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.user_pass.setFont(font)
        self.user_pass.setText(_fromUtf8(""))
        self.user_pass.setObjectName(_fromUtf8("user_pass"))
        self.calendarWidget = QtGui.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(30, 170, 431, 291))
        self.calendarWidget.setStyleSheet(_fromUtf8("alternate-background-color: rgb(43, 45, 49);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(77, 94, 102);"))
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.clocked_toolbtn = QtGui.QToolButton(self.centralwidget)
        self.clocked_toolbtn.setGeometry(QtCore.QRect(620, 10, 131, 101))
        self.clocked_toolbtn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.clocked_toolbtn.setStyleSheet(_fromUtf8("QToolButton{border: None;}"))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("icons/user_valid-512.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clocked_toolbtn.setIcon(icon6)
        self.clocked_toolbtn.setIconSize(QtCore.QSize(95, 95))
        self.clocked_toolbtn.setObjectName(_fromUtf8("clocked_toolbtn"))
        self.btn_signin = QtGui.QToolButton(self.centralwidget)
        self.btn_signin.setGeometry(QtCore.QRect(20, 580, 82, 100))
        self.btn_signin.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btn_signin.setStyleSheet(_fromUtf8("QToolButton{border: None;}"))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("icons/Login-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_signin.setIcon(icon7)
        self.btn_signin.setIconSize(QtCore.QSize(65, 65))
        self.btn_signin.setObjectName(_fromUtf8("btn_signin"))
        self.btn_signout = QtGui.QToolButton(self.centralwidget)
        self.btn_signout.setGeometry(QtCore.QRect(110, 580, 82, 100))
        self.btn_signout.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btn_signout.setStyleSheet(_fromUtf8("QToolButton{border: None;}"))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("icons/Logout-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_signout.setIcon(icon8)
        self.btn_signout.setIconSize(QtCore.QSize(65, 65))
        self.btn_signout.setObjectName(_fromUtf8("btn_signout"))
        self.btn_logs = QtGui.QToolButton(self.centralwidget)
        self.btn_logs.setGeometry(QtCore.QRect(200, 580, 82, 100))
        self.btn_logs.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btn_logs.setStyleSheet(_fromUtf8("QToolButton{border: None;}"))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8("icons/TG-Attendance-Welfare-300x300.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_logs.setIcon(icon9)
        self.btn_logs.setIconSize(QtCore.QSize(65, 65))
        self.btn_logs.setObjectName(_fromUtf8("btn_logs"))
        self.btn_alllogs = QtGui.QToolButton(self.centralwidget)
        self.btn_alllogs.setEnabled(False)
        self.btn_alllogs.setGeometry(QtCore.QRect(290, 580, 82, 100))
        self.btn_alllogs.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btn_alllogs.setStyleSheet(_fromUtf8("QToolButton{border: None;}"))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8("icons/time.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_alllogs.setIcon(icon10)
        self.btn_alllogs.setIconSize(QtCore.QSize(90, 90))
        self.btn_alllogs.setObjectName(_fromUtf8("btn_alllogs"))
        self.btn_help = QtGui.QToolButton(self.centralwidget)
        self.btn_help.setGeometry(QtCore.QRect(380, 580, 82, 100))
        self.btn_help.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btn_help.setStyleSheet(_fromUtf8("QToolButton{border: None;}"))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8("icons/helpme.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_help.setIcon(icon11)
        self.btn_help.setIconSize(QtCore.QSize(80, 80))
        self.btn_help.setObjectName(_fromUtf8("btn_help"))
        self.memo_toolbtn = QtGui.QToolButton(self.centralwidget)
        self.memo_toolbtn.setEnabled(False)
        self.memo_toolbtn.setGeometry(QtCore.QRect(470, 10, 131, 101))
        self.memo_toolbtn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.memo_toolbtn.setStyleSheet(_fromUtf8("QToolButton{border: None;}"))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8("icons/rem2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.memo_toolbtn.setIcon(icon12)
        self.memo_toolbtn.setIconSize(QtCore.QSize(95, 95))
        self.memo_toolbtn.setObjectName(_fromUtf8("memo_toolbtn"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(510, 120, 51, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(630, 120, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(800, 120, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(930, 120, 111, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1080, 110, 111, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1230, 120, 121, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 670, 71, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(110, 670, 91, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(220, 670, 51, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(300, 670, 61, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(400, 670, 41, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(410, 530, 61, 51))
        self.label_12.setText(_fromUtf8(""))
        self.label_12.setPixmap(QtGui.QPixmap(_fromUtf8("icons/forgot-password-icon-9.png")))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.unlock_admin_widget = QtGui.QPushButton(self.centralwidget)
        self.unlock_admin_widget.setGeometry(QtCore.QRect(30, 480, 251, 41))
        self.unlock_admin_widget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.unlock_admin_widget.setStyleSheet(_fromUtf8("color: #fff;\n"
"background-color: rgb(21, 141, 141);\n"
"font: 14px/20px \"Helvetica Neue\",Helvetica,Arial,sans-serif;"))
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8("icons/unlock.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.unlock_admin_widget.setIcon(icon13)
        self.unlock_admin_widget.setIconSize(QtCore.QSize(30, 30))
        self.unlock_admin_widget.setObjectName(_fromUtf8("unlock_admin_widget"))
        self.lock_admin_widget = QtGui.QPushButton(self.centralwidget)
        self.lock_admin_widget.setGeometry(QtCore.QRect(30, 480, 251, 41))
        self.lock_admin_widget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.lock_admin_widget.setStyleSheet(_fromUtf8("color: #fff;\n"
"background-color: rgb(0, 156, 5);\n"
"font: 14px/20px \"Helvetica Neue\",Helvetica,Arial,sans-serif;"))
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8("icons/lock.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lock_admin_widget.setIcon(icon14)
        self.lock_admin_widget.setIconSize(QtCore.QSize(30, 30))
        self.lock_admin_widget.setObjectName(_fromUtf8("lock_admin_widget"))
        self.lock_admin_widget.raise_()
        self.unlock_admin_widget.raise_()
        self.label_5.raise_()
        self.label_9.raise_()
        self.label_8.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_7.raise_()
        self.employeeinfo_toolbtn.raise_()
        self.charts_toolbtn.raise_()
        self.settings_toolbtn.raise_()
        self.register_toolbtn.raise_()
        self.time_label.raise_()
        self.date_label.raise_()
        self.table_frame.raise_()
        self.user_pass.raise_()
        self.calendarWidget.raise_()
        self.clocked_toolbtn.raise_()
        self.btn_signin.raise_()
        self.btn_signout.raise_()
        self.btn_logs.raise_()
        self.btn_alllogs.raise_()
        self.btn_help.raise_()
        self.memo_toolbtn.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_6.raise_()
        self.label_12.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.user_pass, self.btn_signin)
        MainWindow.setTabOrder(self.btn_signin, self.btn_signout)
        MainWindow.setTabOrder(self.btn_signout, self.btn_logs)
        MainWindow.setTabOrder(self.btn_logs, self.btn_alllogs)
        MainWindow.setTabOrder(self.btn_alllogs, self.btn_help)
        MainWindow.setTabOrder(self.btn_help, self.memo_toolbtn)
        MainWindow.setTabOrder(self.memo_toolbtn, self.clocked_toolbtn)
        MainWindow.setTabOrder(self.clocked_toolbtn, self.charts_toolbtn)
        MainWindow.setTabOrder(self.charts_toolbtn, self.register_toolbtn)
        MainWindow.setTabOrder(self.register_toolbtn, self.employeeinfo_toolbtn)
        MainWindow.setTabOrder(self.employeeinfo_toolbtn, self.settings_toolbtn)
        MainWindow.setTabOrder(self.settings_toolbtn, self.search_lineEdit_2)
        MainWindow.setTabOrder(self.search_lineEdit_2, self.search_lineEdit)
        MainWindow.setTabOrder(self.search_lineEdit, self.btn_close)
        MainWindow.setTabOrder(self.btn_close, self.attendance_view)
        MainWindow.setTabOrder(self.attendance_view, self.calendarWidget)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "GAPAN CITY COLLEGE Employee Managent System", None))
        self.employeeinfo_toolbtn.setToolTip(_translate("MainWindow", "employee information and logs", None))
        self.employeeinfo_toolbtn.setText(_translate("MainWindow", "...", None))
        self.charts_toolbtn.setToolTip(_translate("MainWindow", "charts", None))
        self.charts_toolbtn.setText(_translate("MainWindow", "...", None))
        self.settings_toolbtn.setToolTip(_translate("MainWindow", "configurations", None))
        self.settings_toolbtn.setText(_translate("MainWindow", "...", None))
        self.register_toolbtn.setToolTip(_translate("MainWindow", "register employee", None))
        self.register_toolbtn.setText(_translate("MainWindow", "...", None))
        self.time_label.setText(_translate("MainWindow", "07:12:00 PM", None))
        self.date_label.setText(_translate("MainWindow", "March 16, 2013", None))
        self.btn_close.setText(_translate("MainWindow", "...", None))
        self.user_pass.setPlaceholderText(_translate("MainWindow", "Password", None))
        self.clocked_toolbtn.setToolTip(_translate("MainWindow", "show clocked-in employees", None))
        self.clocked_toolbtn.setText(_translate("MainWindow", "...", None))
        self.btn_signin.setText(_translate("MainWindow", "...", None))
        self.btn_signout.setText(_translate("MainWindow", "...", None))
        self.btn_logs.setText(_translate("MainWindow", "...", None))
        self.btn_alllogs.setText(_translate("MainWindow", "...", None))
        self.btn_help.setText(_translate("MainWindow", "...", None))
        self.memo_toolbtn.setToolTip(_translate("MainWindow", "memo", None))
        self.memo_toolbtn.setText(_translate("MainWindow", "...", None))
        self.label.setText(_translate("MainWindow", "Memo", None))
        self.label_2.setText(_translate("MainWindow", "Clocked-In\n"
"Employee(s)", None))
        self.label_3.setText(_translate("MainWindow", "Graphs", None))
        self.label_4.setText(_translate("MainWindow", "Register\n"
"Employee", None))
        self.label_5.setText(_translate("MainWindow", "Employee\'s\n"
"Information\n"
"and Logs", None))
        self.label_6.setText(_translate("MainWindow", "Configurations", None))
        self.label_7.setText(_translate("MainWindow", "Clock-In", None))
        self.label_8.setText(_translate("MainWindow", "Clock-Out", None))
        self.label_9.setText(_translate("MainWindow", "User\n"
"Logs", None))
        self.label_10.setText(_translate("MainWindow", "All\n"
"Logs", None))
        self.label_11.setText(_translate("MainWindow", "Help", None))
        self.unlock_admin_widget.setText(_translate("MainWindow", "Unlock Administrative Widgets", None))
        self.lock_admin_widget.setText(_translate("MainWindow", "Lock Administrative Widgets", None))

