from datetime import datetime
import sys
import addTransaction
import regexFunctions
import databaseFunctions
from PyQt5 import QtCore, QtGui, QtWidgets
from calendar import monthrange

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import colors, style
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as figureCanvas

from PyQt5 import QtCore, QtGui, QtWidgets


class homePage(object):
        def setupUi(self, MainGUI):
                MainGUI.setObjectName("MainGUI")
                MainGUI.resize(1366, 881)
                MainGUI.setFixedSize(1366, 881)
                self.stackedWidget = QtWidgets.QStackedWidget(MainGUI)
                self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1366, 881))
                self.stackedWidget.setObjectName("stackedWidget")
                self.main = QtWidgets.QWidget()
                self.main.setObjectName("main")
                self.main.setWindowTitle("Home")
                self.topBar = QtWidgets.QLabel(self.main)
                self.topBar.setGeometry(QtCore.QRect(0, -20, 1366, 141))
                self.topBar.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 98, 112, 255), stop:1 rgba(255, 107, 107, 255));\n"
        "\n"
        "")
                self.topBar.setText("")
                self.topBar.setObjectName("topBar")
                self.bottomBar = QtWidgets.QLabel(self.main)
                self.bottomBar.setGeometry(QtCore.QRect(0, 102, 1366, 881))
                self.bottomBar.setStyleSheet("background-color:rgba(255,255,255);\n"
        "")
                self.bottomBar.setText("")
                self.bottomBar.setObjectName("bottomBar")
                self.welcome = QtWidgets.QLabel(self.main)
                self.welcome.setGeometry(QtCore.QRect(6, 12, 291, 31))
                font = QtGui.QFont()
                font.setPointSize(25)
                self.welcome.setFont(font)
                self.welcome.setStyleSheet("color:rgba(255,255,255,220);")
                self.welcome.setObjectName("welcome")
                self.logOutButton = QtWidgets.QPushButton(self.main)
                self.logOutButton.setGeometry(QtCore.QRect(1030, 20, 311, 61))
                font = QtGui.QFont()
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.logOutButton.setFont(font)
                self.logOutButton.setStyleSheet("QPushButton#logOutButton{\n"
        "background-color:rgba(85,98,112,255);\n"
        "color:rgba(255,255,255,200);\n"
        "border-radius:5px;\n"
        "}\n"
        "QPushButton#logOutButton:pressed{\n"
        "padding-left:5px;\n"
        "padding-top:5px;\n"
        "background-color:rgba(255,107,107,255);\n"
        "background-position:calc(100% - 10px)center;\n"
        "}\n"
        "\n"
        "QPushButton#logOutButton:hover{\n"
        "background-color:rgba(255,107,107,255);\n"
        "}")
                self.logOutButton.setObjectName("logOutButton")
                self.search = QtWidgets.QFrame(self.main)
                self.search.setGeometry(QtCore.QRect(20, 350, 331, 511))
                self.search.setStyleSheet("background-color:rgba(255,255,255);\n"
        "")
                self.search.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.search.setFrameShadow(QtWidgets.QFrame.Raised)
                self.search.setObjectName("search")
                self.searchArea = QtWidgets.QLabel(self.search)
                self.searchArea.setGeometry(QtCore.QRect(-4, 2, 341, 511))
                self.searchArea.setStyleSheet("background-color:rgb(220,220,220);\n"
        "border-radius:30px;\n"
        "border-color:black;\n"
        "")
                self.searchArea.setText("")
                self.searchArea.setObjectName("searchArea")
                self.searchChoices = QtWidgets.QComboBox(self.search)
                self.searchChoices.setGeometry(QtCore.QRect(28, 151, 261, 51))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.searchChoices.setFont(font)
                self.searchChoices.setObjectName("searchChoices")
                self.searchChoices.addItem("")
                self.searchChoices.addItem("")
                self.searchChoices.addItem("")
                self.searchChoices.addItem("")
                self.searchChoices.addItem("")
                self.searchButton = QtWidgets.QPushButton(self.search)
                self.searchButton.setGeometry(QtCore.QRect(10, 370, 311, 61))
                font = QtGui.QFont()
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.searchButton.setFont(font)
                self.searchButton.setStyleSheet("QPushButton{\n"
        "background-color:rgba(85,98,112,255);\n"
        "color:rgba(255,255,255,200);\n"
        "border-radius:5px;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "padding-left:5px;\n"
        "padding-top:5px;\n"
        "background-color:rgba(255,107,107,255);\n"
        "background-position:calc(100% - 10px)center;\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color:rgba(255,107,107,255);\n"
        "}")
                self.searchButton.setObjectName("searchButton")
                self.dateSearch = QtWidgets.QLineEdit(self.search)
                self.dateSearch.setGeometry(QtCore.QRect(30, 270, 261, 51))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.dateSearch.setFont(font)
                self.dateSearch.setText("")
                self.dateSearch.setObjectName("dateSearch")
                self.addNew = QtWidgets.QPushButton(self.main)
                self.addNew.setGeometry(QtCore.QRect(1080, 670, 171, 61))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.addNew.setFont(font)
                self.addNew.setStyleSheet("QPushButton{\n"
        "background-color:rgba(85,98,112,255);\n"
        "color:rgba(255,255,255,200);\n"
        "border-radius:5px;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "padding-left:5px;\n"
        "padding-top:5px;\n"
        "background-color:rgba(255,107,107,255);\n"
        "background-position:calc(100% - 10px)center;\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color:rgba(255,107,107,255);\n"
        "}")
                self.addNew.setObjectName("addNew")
                self.recents = QtWidgets.QFrame(self.main)
                self.recents.setGeometry(QtCore.QRect(400, 350, 541, 511))
                self.recents.setStyleSheet("")
                self.recents.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.recents.setFrameShadow(QtWidgets.QFrame.Raised)
                self.recents.setObjectName("recents")
                self.recentDisp = QtWidgets.QTableWidget(self.recents)
                self.recentDisp.setGeometry(QtCore.QRect(0, 0, 541, 511))
                self.recentDisp.setStyleSheet("")
                self.recentDisp.setRowCount(20)
                self.recentDisp.setColumnCount(5)
                self.recentDisp.setObjectName("recentDisp")
                item = QtWidgets.QTableWidgetItem()
                self.recentDisp.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.recentDisp.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.recentDisp.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.recentDisp.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.recentDisp.setHorizontalHeaderItem(4, item)
                self.barGraphLayout = QtWidgets.QWidget(self.main)
                '''Important Stuff - former name verticalLayoutWidget'''
                self.barGraphLayout.setGeometry(QtCore.QRect(-180, 100, 1600, 250))
                self.barGraphLayout.setObjectName("verticalLayoutWidget")
                self.barGraphSpace = QtWidgets.QVBoxLayout(self.barGraphLayout)
                self.barGraphSpace.setContentsMargins(0, 0, 0, 0)
                self.barGraphSpace.setSpacing(0)
                self.barGraphSpace.setObjectName("barGraphSpace")
                self.refreshButton = QtWidgets.QPushButton(self.main)
                self.refreshButton.setGeometry(QtCore.QRect(1270, 132, 71, 211))
                font = QtGui.QFont()
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.refreshButton.setFont(font)
                self.refreshButton.setStyleSheet("QPushButton{\n"
        "background-color:rgba(85,98,112,255);\n"
        "color:rgba(255,255,255,200);\n"
        "border-radius:5px;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "padding-left:5px;\n"
        "padding-top:5px;\n"
        "background-color:rgba(255,107,107,255);\n"
        "background-position:calc(100% - 10px)center;\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color:rgba(255,107,107,255);\n"
        "}")
                self.refreshButton.setObjectName("refreshButton")
                self.developedBy = QtWidgets.QLabel(self.main)
                self.developedBy.setGeometry(QtCore.QRect(986, 752, 361, 111))
                font = QtGui.QFont()
                font.setPointSize(13)
                font.setBold(True)
                font.setWeight(75)
                self.developedBy.setFont(font)
                self.developedBy.setObjectName("developedBy")
                self.userName = QtWidgets.QLabel(self.main)
                self.userName.setGeometry(QtCore.QRect(6, 50, 400, 31))
                font = QtGui.QFont()
                font.setPointSize(19)
                self.userName.setFont(font)
                self.userName.setStyleSheet("color:rgba(255,255,255,220);")
                self.userName.setObjectName("userName")
                self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.main)
                self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(949, 339, 440, 330))
                self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
                self.verticalLayout.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout.setObjectName("verticalLayout")
                self.searchTitle = QtWidgets.QLabel(self.main)
                self.searchTitle.setGeometry(QtCore.QRect(140, 360, 91, 31))
                font = QtGui.QFont()
                font.setPointSize(19)
                font.setBold(True)
                font.setWeight(75)
                self.searchTitle.setFont(font)
                self.searchTitle.setStyleSheet("color:rgba(85,98,112,255);")
                self.searchTitle.setObjectName("searchTitle")
                self.searchType = QtWidgets.QLabel(self.main)
                self.searchType.setGeometry(QtCore.QRect(50, 440, 91, 31))
                font = QtGui.QFont()
                font.setPointSize(19)
                font.setBold(True)
                font.setWeight(75)
                self.searchType.setFont(font)
                self.searchType.setStyleSheet("color:rgba(85,98,112,255);")
                self.searchType.setObjectName("searchType")
                self.searchType_2 = QtWidgets.QLabel(self.main)
                self.searchType_2.setGeometry(QtCore.QRect(50, 570, 261, 31))
                font = QtGui.QFont()
                font.setPointSize(19)
                font.setBold(True)
                font.setWeight(75)
                self.searchType_2.setFont(font)
                self.searchType_2.setStyleSheet("color:rgba(85,98,112,255);")
                self.searchType_2.setObjectName("searchType_2")
                self.bottomBar.raise_()
                self.topBar.raise_()
                self.welcome.raise_()
                self.logOutButton.raise_()
                self.search.raise_()
                self.addNew.raise_()
                self.recents.raise_()
                self.barGraphLayout.raise_()
                self.refreshButton.raise_()
                self.developedBy.raise_()
                self.userName.raise_()
                self.verticalLayoutWidget_2.raise_()
                self.searchTitle.raise_()
                self.searchType.raise_()
                self.searchType_2.raise_()
                self.login = QtWidgets.QWidget()
                self.login.setObjectName("login")
                self.stackedWidget.addWidget(self.login)
                self.stackedWidget.addWidget(self.main)
                self.emailEntry = QtWidgets.QLineEdit(self.login)
                self.emailEntry.setGeometry(QtCore.QRect(730, 190, 400, 50))
                font = QtGui.QFont()
                font.setPointSize(20)
                self.emailEntry.setFont(font)
                self.emailEntry.setStyleSheet("background-color:rgba(0,0,0,0);\n"
        "border: 2px solid rgba(0,0,0,0);\n"
        "border-bottom-color:rgba(46,82,101,200);\n"
        "color:rgba(0,0,0);\n"
        "padding-bottom:7px;")
                self.emailEntry.setObjectName("emailEntry")
                self.passwordEntry = QtWidgets.QLineEdit(self.login)
                self.passwordEntry.setGeometry(QtCore.QRect(730, 340, 400, 50))
                font = QtGui.QFont()
                font.setPointSize(20)
                self.passwordEntry.setFont(font)
                self.passwordEntry.setStyleSheet("background-color:rgba(0,0,0,0);\n"
        "border: 2px solid rgba(0,0,0,0);\n"
        "border-bottom-color:rgba(46,82,101,200);\n"
        "color:rgba(0,0,0);\n"
        "padding-bottom:7px;")
                self.passwordEntry.setObjectName("passwordEntry")
                self.partition = QtWidgets.QWidget(self.login)
                self.partition.setGeometry(QtCore.QRect(0, 0, 691, 881))
                self.partition.setStyleSheet("color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 98, 112, 255), stop:1 rgba(255, 107, 107, 255));")
                self.partition.setObjectName("partition")
                self.bookLogo = QtWidgets.QLabel(self.partition)
                self.bookLogo.setGeometry(QtCore.QRect(0, 370, 681, 501))
                font = QtGui.QFont()
                font.setFamily("SLBookArts")
                font.setPointSize(400)
                self.bookLogo.setFont(font)
                self.bookLogo.setObjectName("bookLogo")
                self.leftPart = QtWidgets.QLabel(self.partition)
                self.leftPart.setGeometry(QtCore.QRect(0, 0, 741, 881))
                self.leftPart.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 98, 112, 255), stop:1 rgba(255, 107, 107, 255));\n"
        "")
                self.leftPart.setText("")
                self.leftPart.setObjectName("leftPart")
                self.pageTitle = QtWidgets.QLabel(self.partition)
                self.pageTitle.setGeometry(QtCore.QRect(10, 10, 521, 31))
                font = QtGui.QFont()
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(75)
                self.pageTitle.setFont(font)
                self.pageTitle.setStyleSheet("color:rgba(255,255,255,220);")
                self.pageTitle.setObjectName("pageTitle")
                self.leftPart.raise_()
                self.pageTitle.raise_()
                self.bookLogo.raise_()
                self.rightPart = QtWidgets.QLabel(self.login)
                self.rightPart.setGeometry(QtCore.QRect(691, 0, 681, 881))
                self.rightPart.setStyleSheet("background-color:rgba(255,255,255);\n"
        "")
                self.rightPart.setText("")
                self.rightPart.setObjectName("rightPart")
                self.signUpButton = QtWidgets.QPushButton(self.login)
                self.signUpButton.setGeometry(QtCore.QRect(730, 660, 311, 61))
                font = QtGui.QFont()
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.signUpButton.setFont(font)
                self.signUpButton.setStyleSheet("QPushButton#signUpButton{\n"
        "background-color:rgba(85,98,112,255);\n"
        "color:rgba(255,255,255,200);\n"
        "border-radius:5px;\n"
        "}\n"
        "QPushButton#signUpButton:pressed{\n"
        "padding-left:5px;\n"
        "padding-top:5px;\n"
        "background-color:rgba(255,107,107,255);\n"
        "background-position:calc(100% - 10px)center;\n"
        "}\n"
        "\n"
        "QPushButton#signUpButton:hover{\n"
        "background-color:rgba(255,107,107,255);\n"
        "}")
                self.signUpButton.setObjectName("signUpButton")
                self.signUpText = QtWidgets.QLabel(self.login)
                self.signUpText.setGeometry(QtCore.QRect(730, 570, 411, 51))
                font = QtGui.QFont()
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(75)
                self.signUpText.setFont(font)
                self.signUpText.setObjectName("signUpText")
                self.submitButton = QtWidgets.QPushButton(self.login)
                self.submitButton.setGeometry(QtCore.QRect(730, 450, 311, 61))
                font = QtGui.QFont()
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.submitButton.setFont(font)
                self.submitButton.setStyleSheet("QPushButton#submitButton{\n"
        "background-color:rgba(85,98,112,255);\n"
        "color:rgba(255,255,255,200);\n"
        "border-radius:5px;\n"
        "}\n"
        "QPushButton#submitButton:pressed{\n"
        "padding-left:5px;\n"
        "padding-top:5px;\n"
        "background-color:rgba(255,107,107,255);\n"
        "background-position:calc(100% - 10px)center;\n"
        "}\n"
        "\n"
        "QPushButton#submitButton:hover{\n"
        "background-color:rgba(255,107,107,255);\n"
        "}")
                self.submitButton.setObjectName("submitButton")
                self.loginText = QtWidgets.QLabel(self.login)
                self.loginText.setGeometry(QtCore.QRect(730, 10, 341, 71))
                font = QtGui.QFont()
                font.setPointSize(40)
                font.setBold(True)
                font.setWeight(75)
                self.loginText.setFont(font)
                self.loginText.setStyleSheet("color:rgba(0,0,0,200);")
                self.loginText.setObjectName("loginText")
                self.rightPart.raise_()
                self.emailEntry.raise_()
                self.passwordEntry.raise_()
                self.partition.raise_()
                self.signUpButton.raise_()
                self.signUpText.raise_()
                self.submitButton.raise_()
                self.loginText.raise_()
                self.signUp = QtWidgets.QWidget()
                self.signUp.setObjectName("signUp")
                self.emailEntryS = QtWidgets.QLineEdit(self.signUp)
                self.emailEntryS.setGeometry(QtCore.QRect(730, 520, 400, 50))
                font = QtGui.QFont()
                font.setPointSize(20)
                self.emailEntryS.setFont(font)
                self.emailEntryS.setStyleSheet("background-color:rgba(0,0,0,0);\n"
        "border: 2px solid rgba(0,0,0,0);\n"
        "border-bottom-color:rgba(46,82,101,200);\n"
        "color:rgba(0,0,0);\n"
        "padding-bottom:7px;")
                self.emailEntryS.setObjectName("emailEntryS")
                self.firstEntryS = QtWidgets.QLineEdit(self.signUp)
                self.firstEntryS.setGeometry(QtCore.QRect(730, 120, 400, 50))
                font = QtGui.QFont()
                font.setPointSize(20)
                self.firstEntryS.setFont(font)
                self.firstEntryS.setStyleSheet("background-color:rgba(0,0,0,0);\n"
        "border: 2px solid rgba(0,0,0,0);\n"
        "border-bottom-color:rgba(46,82,101,200);\n"
        "color:rgba(0,0,0);\n"
        "padding-bottom:7px;")
                self.firstEntryS.setObjectName("firstEntryS")
                self.lastEntryS = QtWidgets.QLineEdit(self.signUp)
                self.lastEntryS.setGeometry(QtCore.QRect(730, 220, 400, 50))
                font = QtGui.QFont()
                font.setPointSize(20)
                self.lastEntryS.setFont(font)
                self.lastEntryS.setStyleSheet("background-color:rgba(0,0,0,0);\n"
        "border: 2px solid rgba(0,0,0,0);\n"
        "border-bottom-color:rgba(46,82,101,200);\n"
        "color:rgba(0,0,0);\n"
        "padding-bottom:7px;")
                self.lastEntryS.setObjectName("lastEntryS")
                self.passwordEntryS = QtWidgets.QLineEdit(self.signUp)
                self.passwordEntryS.setGeometry(QtCore.QRect(730, 320, 400, 50))
                font = QtGui.QFont()
                font.setPointSize(20)
                self.passwordEntryS.setFont(font)
                self.passwordEntryS.setStyleSheet("background-color:rgba(0,0,0,0);\n"
        "border: 2px solid rgba(0,0,0,0);\n"
        "border-bottom-color:rgba(46,82,101,200);\n"
        "color:rgba(0,0,0);\n"
        "padding-bottom:7px;")
                self.passwordEntryS.setObjectName("passwordEntryS")
                self.repasswordEntryS = QtWidgets.QLineEdit(self.signUp)
                self.repasswordEntryS.setGeometry(QtCore.QRect(730, 420, 400, 50))
                font = QtGui.QFont()
                font.setPointSize(20)
                self.repasswordEntryS.setFont(font)
                self.repasswordEntryS.setStyleSheet("background-color:rgba(0,0,0,0);\n"
        "border: 2px solid rgba(0,0,0,0);\n"
        "border-bottom-color:rgba(46,82,101,200);\n"
        "color:rgba(0,0,0);\n"
        "padding-bottom:7px;")
                self.repasswordEntryS.setObjectName("repasswordEntryS")
                self.loginButtonS = QtWidgets.QPushButton(self.signUp)
                self.loginButtonS.setGeometry(QtCore.QRect(730, 760, 311, 61))
                font = QtGui.QFont()
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.loginButtonS.setFont(font)
                self.loginButtonS.setStyleSheet("QPushButton#loginButtonS{\n"
        "background-color:rgba(85,98,112,255);\n"
        "color:rgba(255,255,255,200);\n"
        "border-radius:5px;\n"
        "}\n"
        "QPushButton#loginButtonS:pressed{\n"
        "padding-left:5px;\n"
        "padding-top:5px;\n"
        "background-color:rgba(255,107,107,255);\n"
        "background-position:calc(100% - 10px)center;\n"
        "}\n"
        "\n"
        "QPushButton#loginButtonS:hover{\n"
        "background-color:rgba(255,107,107,255);\n"
        "}")
                self.loginButtonS.setObjectName("loginButtonS")
                self.loginTextS = QtWidgets.QLabel(self.signUp)
                self.loginTextS.setGeometry(QtCore.QRect(730, 690, 341, 71))
                font = QtGui.QFont()
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(75)
                self.loginTextS.setFont(font)
                self.loginTextS.setStyleSheet("color:rgba(0,0,0,200);")
                self.loginTextS.setObjectName("loginTextS")
                self.submitButtonS = QtWidgets.QPushButton(self.signUp)
                self.submitButtonS.setGeometry(QtCore.QRect(730, 620, 311, 61))
                font = QtGui.QFont()
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.submitButtonS.setFont(font)
                self.submitButtonS.setStyleSheet("QPushButton#submitButtonS{\n"
        "background-color:rgba(85,98,112,255);\n"
        "color:rgba(255,255,255,200);\n"
        "border-radius:5px;\n"
        "}\n"
        "QPushButton#submitButtonS:pressed{\n"
        "padding-left:5px;\n"
        "padding-top:5px;\n"
        "background-color:rgba(255,107,107,255);\n"
        "background-position:calc(100% - 10px)center;\n"
        "}\n"
        "\n"
        "QPushButton#submitButtonS:hover{\n"
        "background-color:rgba(255,107,107,255);\n"
        "}")
                self.submitButtonS.setObjectName("submitButtonS")
                self.partitionS = QtWidgets.QWidget(self.signUp)
                self.partitionS.setGeometry(QtCore.QRect(0, 0, 691, 881))
                self.partitionS.setStyleSheet("color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 98, 112, 255), stop:1 rgba(255, 107, 107, 255));")
                self.partitionS.setObjectName("partitionS")
                self.bookLogoS = QtWidgets.QLabel(self.partitionS)
                self.bookLogoS.setGeometry(QtCore.QRect(0, 370, 681, 501))
                font = QtGui.QFont()
                font.setFamily("SLBookArts")
                font.setPointSize(400)
                self.bookLogoS.setFont(font)
                self.bookLogoS.setStyleSheet("color:rgba(255,107,107,255)")
                self.bookLogoS.setObjectName("bookLogoS")
                self.leftPartS = QtWidgets.QLabel(self.partitionS)
                self.leftPartS.setGeometry(QtCore.QRect(0, 0, 741, 881))
                self.leftPartS.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 98, 112, 255), stop:1 rgba(255, 107, 107, 255));\n"
        "")
                self.leftPartS.setText("")
                self.leftPartS.setObjectName("leftPartS")
                self.pageTitleS = QtWidgets.QLabel(self.partitionS)
                self.pageTitleS.setGeometry(QtCore.QRect(10, 10, 521, 31))
                font = QtGui.QFont()
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(75)
                self.pageTitleS.setFont(font)
                self.pageTitleS.setStyleSheet("color:rgba(255,255,255,220);")
                self.pageTitleS.setObjectName("pageTitleS")
                self.leftPartS.raise_()
                self.bookLogoS.raise_()
                self.pageTitleS.raise_()
                self.rightPartS = QtWidgets.QLabel(self.signUp)
                self.rightPartS.setGeometry(QtCore.QRect(691, 0, 1366, 881))
                self.rightPartS.setStyleSheet("background-color:rgba(255,255,255);\n"
        "\n"
        "")
                self.rightPartS.setText("")
                self.rightPartS.setObjectName("rightPartS")
                self.signUpTextS = QtWidgets.QLabel(self.signUp)
                self.signUpTextS.setGeometry(QtCore.QRect(730, 10, 341, 71))
                font = QtGui.QFont()
                font.setPointSize(40)
                font.setBold(True)
                font.setWeight(75)
                self.signUpTextS.setFont(font)
                self.signUpTextS.setObjectName("signUpTextS")
                self.salaryEntryS = QtWidgets.QLineEdit(self.signUp)
                self.salaryEntryS.setGeometry(QtCore.QRect(1150, 520, 161, 50))
                font = QtGui.QFont()
                font.setPointSize(20)
                self.salaryEntryS.setFont(font)
                self.salaryEntryS.setStyleSheet("background-color:rgba(0,0,0,0);\n"
        "border: 2px solid rgba(0,0,0,0);\n"
        "border-bottom-color:rgba(46,82,101,200);\n"
        "color:rgba(0,0,0);\n"
        "padding-bottom:7px;")
                self.salaryEntryS.setObjectName("salaryEntryS")
                self.rightPartS.raise_()
                self.emailEntryS.raise_()
                self.firstEntryS.raise_()
                self.lastEntryS.raise_()
                self.passwordEntryS.raise_()
                self.repasswordEntryS.raise_()
                self.loginButtonS.raise_()
                self.loginTextS.raise_()
                self.submitButtonS.raise_()
                self.partitionS.raise_()
                self.signUpTextS.raise_()
                self.salaryEntryS.raise_()
                self.stackedWidget.addWidget(self.signUp)

                self.retranslateUi(MainGUI)
                self.stackedWidget.setCurrentIndex(1)
                QtCore.QMetaObject.connectSlotsByName(MainGUI)

                self.canvas = figureCanvas(plt.figure(figsize=(30,30)))
                self.PieChartCanvas = figureCanvas(plt.figure(figsize=(30,30)))
                self.month = datetime.today().strftime('%m')
                self.year = datetime.today().strftime('%Y')
                self.day = datetime.today().strftime("%d")
                self.logOutButton.clicked.connect(self.logout)
                self.loginButtonS.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.login))
                self.signUpButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.signUp))
                self.submitButton.clicked.connect(self.loginSubmit)
                self.submitButtonS.clicked.connect(self.signUpSubmit)
                self.passwordEntryS.setEchoMode(QtWidgets.QLineEdit.Password)
                self.repasswordEntryS.setEchoMode(QtWidgets.QLineEdit.Password)
                self.passwordEntry.setEchoMode(QtWidgets.QLineEdit.Password)
                self.addNew.clicked.connect(self.callAdd)
                self.refreshButton.clicked.connect(self.updateChart)
                self.today = datetime.today().strftime("-%m-%Y")
                self.searchButton.clicked.connect(self.fillTable)

                self.retranslateUi(MainGUI)
                self.stackedWidget.setCurrentIndex(0)
                QtCore.QMetaObject.connectSlotsByName(MainGUI)

        def fillTable(self):
                if (self.searchChoices.currentText() == 'All' and self.dateSearch.text() == ''):
                        record = databaseFunctions.returnAll(sessionEmail)
                elif (self.searchChoices.currentText() == 'All' and self.dateSearch.text() != ''):
                        record = databaseFunctions.returnAllDate(sessionEmail, self.dateSearch.text())
                elif(self.searchChoices.currentText() != 'All' and self.dateSearch.text() == ''):
                        record = databaseFunctions.returnAllType(sessionEmail, self.searchChoices.currentText())
                else:
                        record = databaseFunctions.returnDateType(sessionEmail, self.searchChoices.currentText(), self.dateSearch.text())
                self.recentDisp.setRowCount(0)
                for row_number, row_data in enumerate(record):
                        self.recentDisp.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                                self.recentDisp.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        def clearTable(self):
               self.recentDisp.setRowCount(0)
               self.searchChoices.setCurrentIndex(0)

        def insetAx(self):
                style.use("bmh")
                self.ax = self.canvas.figure.subplots()
                self.currentDaily = databaseFunctions.returnDaily(sessionEmail)
                self.ax.set_ylim([(0 - self.currentDaily[0] * 3),(self.currentDaily[0] * 3)])
                self.ax.tick_params(axis='y', colors='white')
                self.ax.spines['bottom'].set_color('black')
                self.ax.spines['top'].set_color('black')
                self.ax.spines['left'].set_color('black')
                self.ax.spines['right'].set_color('black')
                self.numDays = monthrange(int(self.year), int(self.month))[1]
                self.ax.set_xlim([0,(self.numDays+1)])
                self.bar = None

        def updateChart(self):
                self.pieUpdate()
                self.ax.remove()
                self.insetAx()
                GraphDataExpenses = databaseFunctions.returnExpenses(email=sessionEmail)
                self.dailyAllowance = databaseFunctions.returnDaily(sessionEmail)
                self.li = []
                self.dayList = [0] * self.numDays
                self.xs = []
                self.ys = []
                for i in range(0,self.numDays):
                        self.summation = 0
                        self.temp = databaseFunctions.returnExpensesPerDay(sessionEmail, (str((i+1))+self.today))
                        if self.temp != []:
                                for j in self.temp:
                                        self.summation += j[0]
                                self.dayList[i] = int(self.dailyAllowance[0]) - self.summation

                for i in range(0,self.numDays):
                        self.xs.append(i+1)
                        self.ys.append(self.dayList[i])

                if self.bar:
                        self.bar.remove()
                self.ax.set_xticks(self.xs, minor=True)
                self.bar = self.ax.bar(self.xs, self.ys, edgecolor="black", color='orange', width=0.6)
                for i in self.bar:
                        self.barHeight = i.get_height()
                        if self.barHeight > 0:
                                if self.barHeight > self.dailyAllowance[0] * 3:
                                        self.ax.annotate('{}'.format(str(self.barHeight)+"\nINR"), xy = (i.get_x()+i.get_width()/2,0), xytext=(0,-26), textcoords="offset points", ha='center', va='bottom')
                                else:
                                        self.ax.annotate('{}'.format(str(self.barHeight)+"\nINR"), xy = (i.get_x()+i.get_width()/2,self.barHeight), xytext=(0,0), textcoords="offset points", ha='center', va='bottom')
                                i.set_color('g')
                        else:
                                if self.barHeight < 0 - self.dailyAllowance[0] * 3:
                                        self.ax.annotate('{}'.format(str(self.barHeight)+"\nINR"), xy = (i.get_x()+i.get_width()/2,0), xytext=(0,0), textcoords="offset points", ha='center', va='bottom')
                                else:
                                        self.ax.annotate('{}'.format(str(self.barHeight)+"\nINR"), xy = (i.get_x()+i.get_width()/2,self.barHeight), xytext=(0,-26), textcoords="offset points", ha='center', va='bottom')
                                i.set_color('r')
                self.canvas.draw()
        
        def insetAy(self):
                self.ay = self.PieChartCanvas.figure.subplots()
                self.ay.spines['bottom'].set_color('black')
                self.ay.spines['top'].set_color('black')
                self.ay.spines['left'].set_color('black')
                self.ay.spines['right'].set_color('black')
                self.PieCha = None

        def pieUpdate(self):

                self.ay.remove()
                self.insetAy()
                self.labels = ['Necessity', 'Medical', 'Entertainment/Outing', 'Others']
                self.slices = []
                for i in self.labels:
                        self.pieSum = 0
                        self.pieValues = databaseFunctions.returnExpensesType(sessionEmail, i)
                        if self.pieValues == []:
                                self.pieSum = 1
                        else:
                                for j in self.pieValues:
                                        self.pieSum += j[0]
                        self.slices.append(self.pieSum) 
                self.explode = [0, 0, 0, 0]
                self.colors = ['#F66D44', '#FEAE65', '#E6F69D', '#AADEA7']
                self.PieCha = self.ay.pie(self.slices, explode=self.explode, colors=self.colors,
                        autopct='%1.1f%%', startangle=90, wedgeprops={'edgecolor': 'black'})
                self.ay.legend(self.labels, loc=2, prop={'size': 6})
                self.PieChartCanvas.draw()

        def signUpSubmit(self):
                if not regexFunctions.validateEmail(self.emailEntryS.text()):
                        self.emailEntryS.clear()
                        self.error = QtWidgets.QMessageBox()
                        self.error.setWindowTitle("Invalid Email!")
                        self.error.setText("Please enter a valid email.")
                        self.error.exec_()
                elif not regexFunctions.validateName(self.firstEntryS.text()):
                        self.firstEntryS.clear()
                        self.error = QtWidgets.QMessageBox()
                        self.error.setWindowTitle("Invalid First Name!")
                        self.error.setText("Please enter a name without digits or special characters.")
                        self.error.exec_()
                elif not regexFunctions.validateName(self.lastEntryS.text()):
                        self.lastEntryS.clear()
                        self.error = QtWidgets.QMessageBox()
                        self.error.setWindowTitle("Invalid Last Name!")
                        self.error.setText("Please enter a name without digits or special characters.")
                        self.error.exec_()
                elif regexFunctions.validatePassword(self.passwordEntryS.text()) != 'Valid':
                        self.error = QtWidgets.QMessageBox()
                        self.error.setWindowTitle("Invalid Password!")
                        self.error.setText(regexFunctions.validatePassword(self.passwordEntryS.text()))
                        self.passwordEntryS.clear()
                        self.error.exec_()
                elif self.passwordEntryS.text() != self.repasswordEntryS.text():
                        self.passwordEntryS.clear()
                        self.repasswordEntryS.clear()
                        self.error = QtWidgets.QMessageBox()
                        self.error.setWindowTitle("Invalid Entry!")
                        self.error.setText("Re - entered password does not match.")
                        self.error.exec_()
                elif not regexFunctions.validateSalary(self.salaryEntryS.text()):
                        self.salaryEntryS.clear()
                        self.error = QtWidgets.QMessageBox()
                        self.error.setWindowTitle("Invalid Salary!")
                        self.error.setText("Salary can only have digits.")
                        self.error.exec_()

                elif int((self.salaryEntryS.text())) < 0:
                        self.salaryEntryS.clear()
                        self.error = QtWidgets.QMessageBox()
                        self.error.setWindowTitle("Invalid Salary!")
                        self.error.setText("Salary cannot be negative.")
                        self.error.exec_()

                else:
                        self.numDays = monthrange(int(self.year), int(self.month))[1]
                        self.daily = int(self.salaryEntryS.text())//self.numDays
                        databaseFunctions.addClient(self.emailEntryS.text().lower(), self.passwordEntryS.text(), self.firstEntryS.text(), self.lastEntryS.text(), int(self.salaryEntryS.text()), int(self.daily))
                        self.firstEntryS.clear()
                        self.lastEntryS.clear()
                        self.emailEntryS.clear()
                        self.passwordEntryS.clear()
                        self.repasswordEntryS.clear()
                        self.stackedWidget.setCurrentWidget(self.login)

        def logout(self):
                self.ax.remove()
                self.stackedWidget.setCurrentWidget(self.login)
                self.clearTable()

        def loginSubmit(self):
                global sessionEmail
                sessionEmail = self.emailEntry.text()
                self.sessionFirstName = databaseFunctions.returnName(sessionEmail)
                if self.sessionFirstName == None:
                        self.emailEntry.clear()
                        self.passwordEntry.clear()
                        self.error = QtWidgets.QMessageBox()
                        self.error.setWindowTitle("Invalid Email or Password!")
                        self.error.setText("Entered account details invalid.")
                        self.error.exec_()
                elif databaseFunctions.returnPassword(sessionEmail)[0] != self.passwordEntry.text():
                        self.emailEntry.clear()
                        self.passwordEntry.clear()
                        self.error = QtWidgets.QMessageBox()
                        self.error.setWindowTitle("Invalid Emaile!")
                        self.error.setText("Entered account details invalid .")
                        self.error.exec_()
                else:
                        self.recentDisp.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
                        self.userName.setText(str(self.sessionFirstName[0]+", Daily allowance: "+str(databaseFunctions.returnDaily(sessionEmail)[0])+" INR"))
                        self.emailEntry.clear()
                        self.passwordEntry.clear()
                        self.stackedWidget.setCurrentWidget(self.main)
                        self.clearTable()
                        writeSessionEmail()
                        self.barGraphSpace.addWidget(self.canvas)
                        self.verticalLayout.addWidget(self.PieChartCanvas)
                        self.insetAx()
                        self.insetAy()
                        self.updateChart()

        def callAdd(self):
                self.add = addTransaction.addNewTransaction()
                self.win = QtWidgets.QDialog()
                self.add.setupUi(self.win)
                self.win.show()


        #change


        def retranslateUi(self, MainGUI):
                _translate = QtCore.QCoreApplication.translate
                MainGUI.setWindowTitle(_translate("MainGUI", "Expense Manager"))
                self.welcome.setText(_translate("MainGUI", "Welcome Back"))
                self.logOutButton.setText(_translate("MainGUI", "Logout"))
                self.searchChoices.setItemText(0, _translate("MainGUI", "All"))
                self.searchChoices.setItemText(1, _translate("MainGUI", "Necessity"))
                self.searchChoices.setItemText(2, _translate("MainGUI", "Medical"))
                self.searchChoices.setItemText(3, _translate("MainGUI", "Entertainment/Outing"))
                self.searchChoices.setItemText(4, _translate("MainGUI", "Others"))
                self.searchChoices.setItemText(5, _translate("MainGUI", "Money Received"))
                self.searchButton.setText(_translate("MainGUI", "Search"))
                self.addNew.setText(_translate("MainGUI", "Add Transaction"))
                item = self.recentDisp.horizontalHeaderItem(0)
                item.setText(_translate("MainGUI", "Date"))
                item = self.recentDisp.horizontalHeaderItem(1)
                item.setText(_translate("MainGUI", "Email"))
                item = self.recentDisp.horizontalHeaderItem(2)
                item.setText(_translate("MainGUI", "Cost"))
                item = self.recentDisp.horizontalHeaderItem(3)
                item.setText(_translate("MainGUI", "Type"))
                item = self.recentDisp.horizontalHeaderItem(4)
                item.setText(_translate("MainGUI", "Desc"))
                self.refreshButton.setText(_translate("MainGUI", "R\n"
        "e\n"
        "f\n"
        "r\n"
        "e\n"
        "s\n"
        "h"))
                self.developedBy.setText(_translate("MainGUI", "Developed by : \n"
        "C093 - Vansh Shah\n"
        "C095 - Sahil Shah\n"
        "C106 - Rohit Sonawane\n"
        "C107 - Shubh Sonparote"))
                self.userName.setText(_translate("MainGUI", "User"))
                self.searchTitle.setText(_translate("MainGUI", "Search"))
                self.searchType.setText(_translate("MainGUI", "Type :-"))
                self.searchType_2.setText(_translate("MainGUI", "Date : DD-MM-YYYY :-"))
                self.emailEntry.setPlaceholderText(_translate("MainGUI", "Email"))
                self.passwordEntry.setPlaceholderText(_translate("MainGUI", "Password"))
                self.bookLogo.setText(_translate("MainGUI", "c"))
                self.pageTitle.setText(_translate("MainGUI", "Expense Manager"))
                self.signUpButton.setText(_translate("MainGUI", "Sign Up"))
                self.signUpText.setText(_translate("MainGUI", "Not A Member? Sign Up Now!"))
                self.submitButton.setText(_translate("MainGUI", "Submit"))
                self.loginText.setText(_translate("MainGUI", "Login"))
                self.emailEntryS.setPlaceholderText(_translate("MainGUI", "Email"))
                self.firstEntryS.setPlaceholderText(_translate("MainGUI", "First Name"))
                self.lastEntryS.setPlaceholderText(_translate("MainGUI", "Last Name"))
                self.passwordEntryS.setPlaceholderText(_translate("MainGUI", "Password"))
                self.repasswordEntryS.setPlaceholderText(_translate("MainGUI", "Re-Enter Password"))
                self.loginButtonS.setText(_translate("MainGUI", "Login"))
                self.loginTextS.setText(_translate("MainGUI", "Already a member?"))
                self.submitButtonS.setText(_translate("MainGUI", "Submit"))
                self.bookLogoS.setText(_translate("MainGUI", "c"))
                self.pageTitleS.setText(_translate("MainGUI", "Expense Manager"))
                self.signUpTextS.setText(_translate("MainGUI", "Sign Up"))
                self.salaryEntryS.setPlaceholderText(_translate("MainGUI", "Salary"))

def writeSessionEmail():
        f = open("currentSessionUser.txt","w")
        f.write(str(sessionEmail))
        f.close()


        

def main():
        databaseFunctions.initialize()
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = homePage()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec())

main()