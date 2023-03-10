
from PyQt5 import QtCore, QtGui, QtWidgets
from utils.AddMovie import Ui_enterMovieWindow
from utils.showMovies import Ui_showMovies
import time
from utils.movieDetailsTree import MovieDetailsWindowTree
import storageManager as database
class Ui_mainAppWindow(object):
    def setupUi(self, mainAppWindow):
        mainAppWindow.setObjectName("mainAppWindow")
        mainAppWindow.resize(239, 280)
        self.centralwidget = QtWidgets.QWidget(mainAppWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.createMovie = QtWidgets.QPushButton(self.centralwidget, clicked=lambda : self.onclickCreateMovie())
        self.createMovie.setGeometry(QtCore.QRect(0, 0, 241, 81))
        self.createMovie.setObjectName("createMovie")
        # self.removeMovie = QtWidgets.QPushButton(self.centralwidget)
        # self.removeMovie.setGeometry(QtCore.QRect(0, 80, 241, 91))
        # self.removeMovie.setObjectName("removeMovie")
        self.showAllMovies = QtWidgets.QPushButton(self.centralwidget, clicked=lambda : self.onclickShowAllMovies())
        self.showAllMovies.setGeometry(QtCore.QRect(0, 80, 241, 91))
        self.showAllMovies.setObjectName("showAllMovies")
        mainAppWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainAppWindow)
        self.statusbar.setObjectName("statusbar")
        mainAppWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainAppWindow)
        QtCore.QMetaObject.connectSlotsByName(mainAppWindow)

    def retranslateUi(self, mainAppWindow):
        _translate = QtCore.QCoreApplication.translate
        mainAppWindow.setWindowTitle(_translate("mainAppWindow", "MainWindow"))
        self.createMovie.setText(_translate("mainAppWindow", "Create New Movie"))
        # self.removeMovie.setText(_translate("mainAppWindow", "Remove A Movie"))
        self.showAllMovies.setText(_translate("mainAppWindow", "Show All Movies"))

    def onclickCreateMovie(self):
        self.createMovieWindow  = QtWidgets.QMainWindow()
        self.createMovieui = Ui_enterMovieWindow()
        self.createMovieui.setupUi(self.createMovieWindow)
        self.createMovieWindow.show()
        database.clearTemp()

    def onclickShowAllMovies(self):
        
        self.showAllui =  MovieDetailsWindowTree()
        self.showAllui.show()
        



        




if __name__ == "__main__":
    database.clearTemp()
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainAppWindow = QtWidgets.QMainWindow()
    ui = Ui_mainAppWindow()
    ui.setupUi(mainAppWindow)
    mainAppWindow.show()
    sys.exit(app.exec_())
