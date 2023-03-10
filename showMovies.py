# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showMovies.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import storageManager as database
from showCast import Ui_showCastWindow
import pprint

class Ui_showMovies(object):
 
   
    def __init__(self):
        self.moviesui = {}
        self.durationui = {}
        self.storage = database.get_storage()

        pprint.pprint(self.storage)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(528, 451)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 0, 91, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(410, 10, 61, 21))
        self.label_2.setObjectName("label_2")
        

        top= 40
        for movies in self.storage:
            self.moviesui[movies] = {}
            self.moviesui[movies][2] = movies
            self.moviesui[movies][1] = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clickedonMovie(self.moviesui[movies][2]))
            self.moviesui[movies][1].setGeometry(QtCore.QRect(10, top, 381, 41))
            self.moviesui[movies][1].setObjectName("name"+movies)
            self.durationui[movies] = QtWidgets.QLabel(self.centralwidget)
            self.durationui[movies].setGeometry(QtCore.QRect(410, top+10, 81, 21))
            self.durationui[movies].setObjectName("duration"+movies)
            top += 45
        print(self.moviesui)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(510, 0, 20, 431))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "Movie Name"))
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        for  movies in self.storage:
            self.moviesui[movies][1].setText(_translate("MainWindow", movies))
            self.durationui[movies].setText(_translate("MainWindow", self.storage[movies]["duration"]))
        self.label_2.setText(_translate("MainWindow", "Duration"))

    def clickedonMovie(self, movie):
        print(f"Movie clicked --> {movie}")
        self.allCastWindow = QtWidgets.QMainWindow()
        self.showAllui = Ui_showCastWindow()
        self.showAllui.setupUi(self.allCastWindow, movie)
        self.allCastWindow.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_showMovies()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
