from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class Login_Page(QWidget):
    switch_window_to_main = QtCore.pyqtSignal()

    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.resize(614, 436)

        self.LoginButton = QtWidgets.QPushButton(LoginForm)
        self.LoginButton.setEnabled(True)
        self.LoginButton.setGeometry(QtCore.QRect(430, 320, 151, 81))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.LoginButton.setFont(font)
        self.LoginButton.setObjectName("LoginButton")
        self.LoginButton.clicked.connect(self.switch_login_page)

        self.lineEdit_SID = QtWidgets.QLineEdit(LoginForm)
        self.lineEdit_SID.setEnabled(True)
        self.lineEdit_SID.setGeometry(QtCore.QRect(100, 320, 311, 31))
        self.lineEdit_SID.setText("")
        self.lineEdit_SID.setObjectName("lineEdit_SID")

        self.lineEdit_Name = QtWidgets.QLineEdit(LoginForm)
        self.lineEdit_Name.setEnabled(True)
        self.lineEdit_Name.setGeometry(QtCore.QRect(100, 370, 311, 31))
        self.lineEdit_Name.setText("")
        self.lineEdit_Name.setObjectName("lineEdit_Name")

        self.SIDLabel = QtWidgets.QLabel(LoginForm)
        self.SIDLabel.setEnabled(True)
        self.SIDLabel.setGeometry(QtCore.QRect(30, 320, 54, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.SIDLabel.setFont(font)
        self.SIDLabel.setObjectName("SIDLabel")

        self.NameLabel = QtWidgets.QLabel(LoginForm)
        self.NameLabel.setEnabled(True)
        self.NameLabel.setGeometry(QtCore.QRect(30, 370, 54, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.NameLabel.setFont(font)
        self.NameLabel.setObjectName("NameLabel")

        self.label = QtWidgets.QLabel(LoginForm)
        self.label.setGeometry(QtCore.QRect(0, 0, 621, 441))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("UIsource/loginpage.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.label.raise_()
        self.LoginButton.raise_()
        self.lineEdit_SID.raise_()
        self.lineEdit_Name.raise_()
        self.SIDLabel.raise_()
        self.NameLabel.raise_()

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)

    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "LoginPage"))
        LoginForm.setWindowIcon(QIcon("UIsource/img-symbol.png"))
        self.LoginButton.setText(_translate("LoginForm", "Login"))
        self.SIDLabel.setText(_translate("LoginForm", "학번"))
        self.NameLabel.setText(_translate("LoginForm", "이름"))



    # SID,Name 다음 Mainpage에 Label로 표시해야됨
    def switch_login_page(self):
        SID = self.lineEdit_SID.text()
        Name = self.lineEdit_Name.text()
        self.switch_window_to_main.emit()



