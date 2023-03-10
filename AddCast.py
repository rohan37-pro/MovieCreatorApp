# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddCast.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

'''
Store = {"movie" : {
                "duration" : 0,
                "casts" : { 
                    "riddhi" : {
                        "gender" : "male",
                        "NAME" : "",
                        "character" :"" 
                        "dialog" : {
                            'fuck yoou' : { "from" : 0 , "to" : 0}
                            ''
                        }
                    }
                }
        }
}
'''


from PyQt5 import QtCore, QtGui, QtWidgets
from DialogAdd import Ui_MainWindow
stiragte["sot"] = {}
class Ui_AddCastWindow(object):
    def setupUi(self, AddCastWindow):
        if self.storage == None:
            self.storage = {}
        AddCastWindow.setObjectName("AddCastWindow")
        AddCastWindow.resize(489, 214)
        self.centralwidget = QtWidgets.QWidget(AddCastWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CastNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.CastNameLabel.setGeometry(QtCore.QRect(20, 10, 91, 41))
        self.CastNameLabel.setObjectName("CastNameLabel")
        self.CastCharacterLabel = QtWidgets.QLabel(self.centralwidget)
        self.CastCharacterLabel.setGeometry(QtCore.QRect(180, 20, 91, 21))
        self.CastCharacterLabel.setObjectName("CastCharacterLabel")
        self.castGenderLabel = QtWidgets.QLabel(self.centralwidget)
        self.castGenderLabel.setGeometry(QtCore.QRect(340, 20, 91, 21))
        self.castGenderLabel.setObjectName("castGenderLabel")
        self.CastNameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.CastNameInput.setGeometry(QtCore.QRect(20, 50, 113, 20))
        self.CastNameInput.setObjectName("CastNameInput")
        self.CastCharacterInput = QtWidgets.QLineEdit(self.centralwidget)
        self.CastCharacterInput.setGeometry(QtCore.QRect(180, 50, 113, 20))
        self.CastCharacterInput.setObjectName("CastCharacterInput")
        self.CastGenderInput = QtWidgets.QLineEdit(self.centralwidget)
        self.CastGenderInput.setGeometry(QtCore.QRect(340, 50, 113, 20))
        self.CastGenderInput.setObjectName("CastGenderInput")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget , clicked = lambda: self.onClickAddDialogue())
        self.pushButton.setGeometry(QtCore.QRect(20, 90, 451, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 140, 181, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        AddCastWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AddCastWindow)
        self.statusbar.setObjectName("statusbar")
        AddCastWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AddCastWindow)
        QtCore.QMetaObject.connectSlotsByName(AddCastWindow)

    def retranslateUi(self, AddCastWindow):
        _translate = QtCore.QCoreApplication.translate
        AddCastWindow.setWindowTitle(_translate("AddCastWindow", "MainWindow"))
        self.CastNameLabel.setText(_translate("AddCastWindow", "Cast Name"))
        self.CastCharacterLabel.setText(_translate("AddCastWindow", "Cast Character"))
        self.castGenderLabel.setText(_translate("AddCastWindow", "Cast Gender"))
        self.CastGenderInput.setPlaceholderText(_translate("AddCastWindow", "Male / Female"))
        self.pushButton.setText(_translate("AddCastWindow", "Add Dialogue +"))
        self.pushButton_2.setText(_translate("AddCastWindow", "Save Cast / Dialogue Data"))

    def onClickAddDialogue(self):
        self.dialogwindow = QtWidgets.QMainWindow()
        self.DialogueUi = Ui_MainWindow()
        self.DialogueUi.setupUi(self.dialogwindow)
        self.dialogwindow.show()

    def handleData(self, storage):
        print(f"dialogue --> {storage}")
        cast_name = self.CastNameInput.text()
        cast_character = self.CastCharacterInput.text()
        cast_gender = self.CastGenderInput.text()
        if cast_name not in self.storage.keys() :
            self.storage[cast_name] = {}
        self.storage[cast_name]["gender"] =cast_gender
        self.storage[cast_name]["character"] =  cast_character
        if self.storage[cast_name]["dialogue"] == None:
            self.storage[cast_name]["dialogue"] = {}
        prev_dialogues = self.storage[cast_name]["dialogue"]
        self.storage[cast_name]["dialogue"] = {**prev_dialogues, **storage}
        print("cast storage --> " ,self.storage)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddCastWindow = QtWidgets.QMainWindow()
    ui = Ui_AddCastWindow()
    ui.setupUi(AddCastWindow)
    AddCastWindow.show()
    sys.exit(app.exec_())