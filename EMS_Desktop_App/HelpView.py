# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/HelpWindow.ui'
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

class Ui_HelpWindow(object):
    def setupUi(self, HelpWindow):
        HelpWindow.setObjectName(_fromUtf8("HelpWindow"))
        HelpWindow.resize(830, 565)
        HelpWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/favicon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HelpWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(HelpWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 61, 61))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("icons/Login-icon.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 50, 181, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 61, 61))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("icons/Logout-icon.png")))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 130, 191, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 190, 61, 61))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("icons/TG-Attendance-Welfare-300x300.png")))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(100, 210, 231, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(100, 290, 231, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 260, 81, 81))
        self.label_8.setText(_fromUtf8(""))
        self.label_8.setPixmap(QtGui.QPixmap(_fromUtf8("icons/time.png")))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(100, 360, 231, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 340, 61, 61))
        self.label_10.setText(_fromUtf8(""))
        self.label_10.setPixmap(QtGui.QPixmap(_fromUtf8("icons/helpme.png")))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(400, 110, 61, 61))
        self.label_11.setText(_fromUtf8(""))
        self.label_11.setPixmap(QtGui.QPixmap(_fromUtf8("icons/user_valid-512.png")))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(470, 130, 251, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(470, 210, 251, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(400, 190, 61, 61))
        self.label_14.setText(_fromUtf8(""))
        self.label_14.setPixmap(QtGui.QPixmap(_fromUtf8("icons/bargraph.png")))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(470, 290, 251, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(400, 270, 61, 61))
        self.label_16.setText(_fromUtf8(""))
        self.label_16.setPixmap(QtGui.QPixmap(_fromUtf8("icons/profile.png")))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(470, 370, 331, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(390, 330, 81, 81))
        self.label_18.setText(_fromUtf8(""))
        self.label_18.setPixmap(QtGui.QPixmap(_fromUtf8("icons/attendance.png")))
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(470, 450, 251, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_20 = QtGui.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(400, 430, 61, 61))
        self.label_20.setText(_fromUtf8(""))
        self.label_20.setPixmap(QtGui.QPixmap(_fromUtf8("icons/settings2.png")))
        self.label_20.setScaledContents(True)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.pushButton_reset_pass = QtGui.QPushButton(self.centralwidget)
        self.pushButton_reset_pass.setGeometry(QtCore.QRect(120, 440, 141, 35))
        self.pushButton_reset_pass.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_reset_pass.setStyleSheet(_fromUtf8("color: green;"))
        self.pushButton_reset_pass.setObjectName(_fromUtf8("pushButton_reset_pass"))
        self.label_21 = QtGui.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(30, 420, 71, 71))
        self.label_21.setText(_fromUtf8(""))
        self.label_21.setPixmap(QtGui.QPixmap(_fromUtf8("icons/reset.png")))
        self.label_21.setScaledContents(True)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.label_22 = QtGui.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(170, 520, 561, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.label_23 = QtGui.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(120, 520, 51, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet(_fromUtf8("color: orangered;"))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.label_24 = QtGui.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(400, 30, 61, 61))
        self.label_24.setText(_fromUtf8(""))
        self.label_24.setPixmap(QtGui.QPixmap(_fromUtf8("icons/rem2.png")))
        self.label_24.setScaledContents(True)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.label_25 = QtGui.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(470, 50, 251, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        HelpWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(HelpWindow)
        QtCore.QMetaObject.connectSlotsByName(HelpWindow)

    def retranslateUi(self, HelpWindow):
        HelpWindow.setWindowTitle(_translate("HelpWindow", "Help", None))
        self.label_2.setText(_translate("HelpWindow", "Sign-In    Ctrl+I", None))
        self.label_4.setText(_translate("HelpWindow", "Sign-Out    Ctrl+O", None))
        self.label_6.setText(_translate("HelpWindow", "Self Attendance Logs    Ctrl+S", None))
        self.label_7.setText(_translate("HelpWindow", "* All Attendance Logs    Ctrl+A", None))
        self.label_9.setText(_translate("HelpWindow", "Help    F1", None))
        self.label_12.setText(_translate("HelpWindow", "Clocked-In Employees    Ctrl+T", None))
        self.label_13.setText(_translate("HelpWindow", "* Graphs    Ctrl+G", None))
        self.label_15.setText(_translate("HelpWindow", "* Register Employee    Ctrl+R", None))
        self.label_17.setText(_translate("HelpWindow", "* Employees\' Information and Logs    Ctrl+Y", None))
        self.label_19.setText(_translate("HelpWindow", "* Global Configurations    Ctrl+W", None))
        self.pushButton_reset_pass.setText(_translate("HelpWindow", "Reset Password", None))
        self.label_22.setText(_translate("HelpWindow", "Commands with \'*\' prefix are only for users with administrative capability.", None))
        self.label_23.setText(_translate("HelpWindow", "Note:", None))
        self.label_25.setText(_translate("HelpWindow", "* Memo   Ctrl+M", None))

