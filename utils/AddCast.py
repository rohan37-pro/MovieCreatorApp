
'''
Store = {"movie" : {
                "duration" : 0,
                "casts" : { 
                    "riddhi" : {
                        "gender" : "male",
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
from utils.DialogAdd import Ui_MainWindow
from utils.EmptyInputPopUp import Ui_Dialog
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.getcwd(), '..'))
sys.path.append(parent_dir)
import storageManager as database


class Ui_AddCastWindow(object):

    storage = {}

    def setupUi(self, AddCastWindow):
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
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.saveExit(AddCastWindow))
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

        def openDialogueWin(self):
            self.dialogwindow = QtWidgets.QMainWindow()
            self.DialogueUi = Ui_MainWindow()
            self.DialogueUi.setupUi(self.dialogwindow)
            self.dialogwindow.show()

        storage = database.get_cast_json()
        self.cast_name_ = self.CastNameInput.text().strip()
        self.cast_character_ = self.CastCharacterInput.text().strip()
        self.cast_gender_ = self.CastGenderInput.text().strip()

        if  (self.cast_name_ not in storage) and self.cast_name_ != "" and self.cast_character_ != "" and self.cast_gender_ != "":
            self.storage[self.cast_name_] = {}
            self.storage[self.cast_name_]["gender"] = self.cast_gender_
            self.storage[self.cast_name_]["character"] = self.cast_character_
            self.storage[self.cast_name_]["dialogue"] = {}
            database.dump_cast(self.storage)
            database.clear_dialogue_store()
            openDialogueWin(self)

        elif self.cast_name_ != "" and self.cast_character_ != "" and self.cast_gender_ != "" :
            database.append_dialogue_to_cast(self.cast_name_)
            database.clear_dialogue_store()
            openDialogueWin(self)
        
        else :
            self.window = QtWidgets.QMainWindow()
            self.errorUi = Ui_Dialog()
            self.errorUi.setupUi(self.window)
            self.window.show()

        

    def saveExit(self, Mainwindow):
        storage = database.get_cast_json()
        self.cast_name_ = self.CastNameInput.text().strip()
        self.cast_character_ = self.CastCharacterInput.text().strip()
        self.cast_gender_ = self.CastGenderInput.text().strip()
        if (self.cast_name_ not in storage) and self.cast_name_ != "" and self.cast_character_ != "" and self.cast_gender_ != "":
            self.storage[self.cast_name_] = {}
            self.storage[self.cast_name_]["gender"] = self.cast_gender_
            self.storage[self.cast_name_]["character"] = self.cast_character_
            self.storage[self.cast_name_]["dialogue"] = {}
            database.dump_cast(self.storage)
            database.clear_dialogue_store()
            self.storage.clear()
            Mainwindow.close()
        
        elif self.cast_name_ != "" and self.cast_character_ != "" and self.cast_gender_ != "" :
            database.append_dialogue_to_cast(self.cast_name_)
            database.clear_dialogue_store()
            self.storage.clear()
            Mainwindow.close()

        else :
            self.window = QtWidgets.QMainWindow()
            self.errorUi = Ui_Dialog()
            self.errorUi.setupUi(self.window)
            self.window.show()


        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddCastWindow = QtWidgets.QMainWindow()
    ui = Ui_AddCastWindow()
    ui.setupUi(AddCastWindow)
    AddCastWindow.show()
    sys.exit(app.exec_())
