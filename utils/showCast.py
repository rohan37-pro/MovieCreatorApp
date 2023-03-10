
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.getcwd(), '..'))
sys.path.append(parent_dir)
import storageManager as database

class Ui_showCastWindow(object):

    castui = {}
    characternameUi = {}
    genderUi = {}
    showDialogueUi = {}
    storage = database.get_storage()

    def setupUi(self, showCastWindow, movie ) :
        self.storage = self.storage[movie]["casts"]
        print(self.storage)
        showCastWindow.setObjectName("showCastWindow")
        showCastWindow.resize(701, 600)
        self.centralwidget = QtWidgets.QWidget(showCastWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.movieName = QtWidgets.QLabel(self.centralwidget)
        self.movieName.setGeometry(QtCore.QRect(0, 0, 701, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.movieName.setFont(font)
        self.movieName.setAlignment(QtCore.Qt.AlignCenter)
        self.movieName.setObjectName("movieName")

        top = 80
        for casts in self.storage:
            self.castui[casts] = QtWidgets.QLabel(self.centralwidget)
            self.castui[casts].setGeometry(QtCore.QRect(20, top, 221, 41))
            self.castui[casts].setAlignment(QtCore.Qt.AlignCenter)
            self.castui[casts].setObjectName(casts)
            self.characternameUi[casts] = QtWidgets.QLabel(self.centralwidget)
            self.characternameUi[casts].setGeometry(QtCore.QRect(250, top, 211, 41))
            self.characternameUi[casts].setAlignment(QtCore.Qt.AlignCenter)
            self.characternameUi[casts].setObjectName(casts)
            self.genderUi[casts] = QtWidgets.QLabel(self.centralwidget)
            self.genderUi[casts].setGeometry(QtCore.QRect(480, top, 101, 41))
            self.genderUi[casts].setAlignment(QtCore.Qt.AlignCenter)
            self.genderUi[casts].setObjectName(casts)
            self.showDialogueUi[casts] = QtWidgets.QPushButton(self.centralwidget)
            self.showDialogueUi[casts].setGeometry(QtCore.QRect(580, top, 101, 41))
            self.showDialogueUi[casts].setObjectName(casts)
            top += 40

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(100, 50, 91, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(320, 50, 91, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(510, 50, 61, 16))
        self.label_7.setObjectName("label_7")
        showCastWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(showCastWindow)
        self.statusbar.setObjectName("statusbar")
        showCastWindow.setStatusBar(self.statusbar)

        self.retranslateUi(showCastWindow, movie)
        QtCore.QMetaObject.connectSlotsByName(showCastWindow)

    def retranslateUi(self, showCastWindow, movie):
        _translate = QtCore.QCoreApplication.translate
        showCastWindow.setWindowTitle(_translate("showCastWindow", "MainWindow"))
        self.movieName.setText(_translate("showCastWindow", movie))
        for casts in self.storage :
            self.castui[casts].setText(_translate("showCastWindow", casts))
            self.characternameUi[casts].setText(_translate("showCastWindow", self.storage[casts]["character"]))
            self.genderUi[casts].setText(_translate("showCastWindow", self.storage[casts]["gender"]))
            self.showDialogueUi[casts].setText(_translate("showCastWindow", "show Dialogue"))
        self.label_5.setText(_translate("showCastWindow", "Cast Name"))
        self.label_6.setText(_translate("showCastWindow", "Character Name"))
        self.label_7.setText(_translate("showCastWindow", "Gender"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    showCastWindow = QtWidgets.QMainWindow()
    ui = Ui_showCastWindow()
    ui.setupUi(showCastWindow)
    showCastWindow.show()
    sys.exit(app.exec_())
