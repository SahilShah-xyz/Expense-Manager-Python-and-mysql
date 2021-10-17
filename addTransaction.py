import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import databaseFunctions

class addNewTransaction(object):
        def setupUi(self, addTransaction):
                addTransaction.setObjectName("addTransaction")
                addTransaction.resize(550, 466)
                self.choicesAdd = QtWidgets.QComboBox(addTransaction)
                self.choicesAdd.setGeometry(QtCore.QRect(170, 230, 200, 31))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.choicesAdd.setFont(font)
                self.choicesAdd.setObjectName("choicesAdd")
                self.choicesAdd.addItem("")
                self.choicesAdd.addItem("")
                self.choicesAdd.addItem("")
                self.choicesAdd.addItem("")
                self.choicesAdd.addItem("")
                self.topAdd = QtWidgets.QLabel(addTransaction)
                self.topAdd.setGeometry(QtCore.QRect(0, 0, 551, 71))
                self.topAdd.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 98, 112, 255), stop:1 rgba(255, 107, 107, 255));\n"
        "\n"
        "")
                self.topAdd.setText("")
                self.topAdd.setObjectName("topAdd")
                self.bottomAdd = QtWidgets.QLabel(addTransaction)
                self.bottomAdd.setGeometry(QtCore.QRect(0, 0, 551, 451))
                self.bottomAdd.setStyleSheet("background-color:rgba(255,255,255);\n"
        "")
                self.bottomAdd.setText("")
                self.bottomAdd.setObjectName("bottomAdd")
                self.enterAdd = QtWidgets.QLabel(addTransaction)
                self.enterAdd.setGeometry(QtCore.QRect(80, 80, 421, 31))
                font = QtGui.QFont()
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(75)
                self.enterAdd.setFont(font)
                self.enterAdd.setStyleSheet("color:rgba(0,0,0,200);")
                self.enterAdd.setObjectName("enterAdd")
                self.valueEntryAdd = QtWidgets.QLineEdit(addTransaction)
                self.valueEntryAdd.setGeometry(QtCore.QRect(170, 130, 200, 31))
                font = QtGui.QFont()
                font.setPointSize(12)
                self.valueEntryAdd.setFont(font)
                self.valueEntryAdd.setStyleSheet("background-color:rgba(0,0,0,0);\n"
        "border: 2px solid rgba(0,0,0,0);\n"
        "border-bottom-color:rgba(46,82,101,200);\n"
        "color:rgba(0,0,0);\n"
        "padding-bottom:7px;")
                self.valueEntryAdd.setObjectName("valueEntryAdd")
                self.enterChoiceAdd = QtWidgets.QLabel(addTransaction)
                self.enterChoiceAdd.setGeometry(QtCore.QRect(80, 180, 421, 31))
                font = QtGui.QFont()
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(75)
                self.enterChoiceAdd.setFont(font)
                self.enterChoiceAdd.setStyleSheet("color:rgba(0,0,0,200);")
                self.enterChoiceAdd.setObjectName("enterChoiceAdd")
                self.submitButtonAdd = QtWidgets.QPushButton(addTransaction)
                self.submitButtonAdd.setGeometry(QtCore.QRect(220, 410, 90, 30))
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.submitButtonAdd.setFont(font)
                self.submitButtonAdd.setStyleSheet("QPushButton#submitButtonAdd{\n"
        "background-color:rgba(85,98,112,255);\n"
        "color:rgba(255,255,255,200);\n"
        "border-radius:5px;\n"
        "}\n"
        "QPushButton#submitButtonAdd:pressed{\n"
        "padding-left:5px;\n"
        "padding-top:5px;\n"
        "background-color:rgba(255,107,107,255);\n"
        "background-position:calc(100% - 10px)center;\n"
        "}\n"
        "\n"
        "QPushButton#submitButtonAdd:hover{\n"
        "background-color:rgba(255,107,107,255);\n"
        "}")
                self.submitButtonAdd.setObjectName("submitButtonAdd")
                self.bottomStripAdd = QtWidgets.QLabel(addTransaction)
                self.bottomStripAdd.setGeometry(QtCore.QRect(0, 450, 551, 21))
                self.bottomStripAdd.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 98, 112, 255), stop:1 rgba(255, 107, 107, 255));\n"
        "\n"
        "")
                self.bottomStripAdd.setText("")
                self.bottomStripAdd.setObjectName("bottomStripAdd")
                self.enterDescriptionAdd = QtWidgets.QLabel(addTransaction)
                self.enterDescriptionAdd.setGeometry(QtCore.QRect(140, 270, 291, 31))
                font = QtGui.QFont()
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(75)
                self.enterDescriptionAdd.setFont(font)
                self.enterDescriptionAdd.setStyleSheet("color:rgba(0,0,0,200);")
                self.enterDescriptionAdd.setObjectName("enterDescriptionAdd")
                self.descriptionAdd = QtWidgets.QLineEdit(addTransaction)
                self.descriptionAdd.setGeometry(QtCore.QRect(90, 299, 371, 101))
                self.descriptionAdd.setStyleSheet("background-color:rgba(0,0,0,0);\n"
        "border: 2px solid rgba(0,0,0,0);\n"
        "border-color:rgba(46,82,101,200);\n"
        "color:rgba(0,0,0);\n"
        "padding-bottom:7px;\nfont-size:14px")
                self.descriptionAdd.setObjectName("descriptionAdd")
                self.bottomAdd.raise_()
                self.choicesAdd.raise_()
                self.topAdd.raise_()
                self.enterAdd.raise_()
                self.valueEntryAdd.raise_()
                self.enterChoiceAdd.raise_()
                self.submitButtonAdd.raise_()
                self.bottomStripAdd.raise_()
                self.enterDescriptionAdd.raise_()
                self.descriptionAdd.raise_()

                self.submitButtonAdd.clicked.connect(self.submitAdd)

                self.retranslateUi(addTransaction)
                QtCore.QMetaObject.connectSlotsByName(addTransaction)
        
        def submitAdd(self):
                try:
                        self.tran = int(self.valueEntryAdd.text())
                except ValueError:
                        self.valueEntryAdd.clear()
                        self.hs = QtWidgets.QMessageBox()
                        self.hs.setWindowTitle("Warning!")
                        self.hs.setText("Only Numbers Allowed!")
                        self.hs.exec_()
                else:
                        
                        f = open("currentSessionUser.txt","r")
                        email = f.read()
                        email = str(email)
                        f.close()

                        self.date = datetime.datetime.now()
                        self.dateExp = str(self.date.strftime("%d-%m-%Y"))
                        if self.choicesAdd.currentText() == 'Money Received':
                                databaseFunctions.addExpense(self.dateExp, email,(0 - abs(int(self.valueEntryAdd.text()))),self.choicesAdd.currentText(),self.descriptionAdd.text())
                        else:
                                databaseFunctions.addExpense(self.dateExp, email,abs(int(self.valueEntryAdd.text())),self.choicesAdd.currentText(),self.descriptionAdd.text())
                        self.descriptionAdd.clear()
                        self.valueEntryAdd.clear()
                        self.hs = QtWidgets.QMessageBox()
                        self.hs.setWindowTitle("Success!")
                        self.hs.setText("Transaction added successfully!")
                        self.hs.exec_()
                        

        def retranslateUi(self, addTransaction):
                _translate = QtCore.QCoreApplication.translate
                addTransaction.setWindowTitle(_translate("addTransaction", "Add Transaction"))
                self.choicesAdd.setItemText(0, _translate("addTransaction", "Necessity"))
                self.choicesAdd.setItemText(1, _translate("addTransaction", "Medical"))
                self.choicesAdd.setItemText(2, _translate("addTransaction", "Entertainment/Outing"))
                self.choicesAdd.setItemText(3, _translate("addTransaction", "Others"))
                self.choicesAdd.setItemText(4, _translate("addTransaction", "Money Received"))
                self.enterAdd.setText(_translate("addTransaction", "Enter the Value of Transaction"))
                self.valueEntryAdd.setPlaceholderText(_translate("addTransaction", "Value"))
                self.enterChoiceAdd.setText(_translate("addTransaction", "Enter the Value of Transaction"))
                self.submitButtonAdd.setText(_translate("addTransaction", "Submit"))
                self.enterDescriptionAdd.setText(_translate("addTransaction", "Enter the Description"))
