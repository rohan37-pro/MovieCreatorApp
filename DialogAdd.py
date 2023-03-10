# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogAdd.ui'
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
from AddCast import Ui_AddCastWindow 



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(605, 307)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.EnterDialoguelabel = QtWidgets.QLabel(self.centralwidget)
        self.EnterDialoguelabel.setGeometry(QtCore.QRect(30, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.EnterDialoguelabel.setFont(font)
        self.EnterDialoguelabel.setObjectName("EnterDialoguelabel")
        self.dialogueinput = QtWidgets.QTextEdit(self.centralwidget)
        self.dialogueinput.setGeometry(QtCore.QRect(30, 50, 561, 81))
        self.dialogueinput.setObjectName("dialogueinput")
        self.fromLabel = QtWidgets.QLabel(self.centralwidget)
        self.fromLabel.setGeometry(QtCore.QRect(30, 150, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.fromLabel.setFont(font)
        self.fromLabel.setObjectName("fromLabel")
        self.toLabel = QtWidgets.QLabel(self.centralwidget)
        self.toLabel.setGeometry(QtCore.QRect(190, 150, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.toLabel.setFont(font)
        self.toLabel.setObjectName("toLabel")
        self.fromtimeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.fromtimeEdit.setGeometry(QtCore.QRect(30, 170, 118, 22))
        font = QtGui.QFont()
        font.setKerning(True)
        self.fromtimeEdit.setFont(font)
        self.fromtimeEdit.setWrapping(True)
        self.fromtimeEdit.setFrame(False)
        self.fromtimeEdit.setCalendarPopup(False)
        self.fromtimeEdit.setObjectName("fromtimeEdit")
        self.totimeEdit_2 = QtWidgets.QTimeEdit(self.centralwidget)
        self.totimeEdit_2.setGeometry(QtCore.QRect(190, 170, 118, 22))
        self.totimeEdit_2.setObjectName("totimeEdit_2")
        self.save_dialogButton = QtWidgets.QPushButton(self.centralwidget)
        self.save_dialogButton.setGeometry(QtCore.QRect(190, 210, 201, 41))
        self.save_dialogButton.setObjectName("save_dialogButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.EnterDialoguelabel.setText(_translate("MainWindow", "Enter Dialogue "))
        self.fromLabel.setText(_translate("MainWindow", "From"))
        self.toLabel.setText(_translate("MainWindow", "To"))
        self.fromtimeEdit.setDisplayFormat(_translate("MainWindow", "HH:mm:ss"))
        self.totimeEdit_2.setDisplayFormat(_translate("MainWindow", "HH:mm:ss"))
        self.save_dialogButton.setText(_translate("MainWindow", "Save Dialogue"))


    def saveExit(self):
        obj = Ui_AddCastWindow()
        storage = {}
        dialogue = self.dialogueinput.text()
        from_ = self.fromtimeEdit.specialValueText()
        to_ = self.totimeEdit_2.specialValueText()

        storage[dialogue] = {}
        storage[dialogue]["from"] = from_
        storage[dialogue]["to"] = to_
        self.storage = storage
        obj.handleData(storage)
        print(f"dialogue storage --> {storage}")
        self.exit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())