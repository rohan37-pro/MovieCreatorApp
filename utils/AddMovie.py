
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
from utils.AddCast import Ui_AddCastWindow
from utils.EmptyInputPopUp import Ui_Dialog
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.getcwd(), '..'))
sys.path.append(parent_dir)
import storageManager as database



class Ui_enterMovieWindow(object):
    storage = {}
    
    def setupUi(self, enterMovieWindow):
        enterMovieWindow.setObjectName("enterMovieWindow")
        enterMovieWindow.resize(441, 223)
        self.centralwidget = QtWidgets.QWidget(enterMovieWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.movieName = QtWidgets.QLabel(self.centralwidget)
        self.movieName.setGeometry(QtCore.QRect(30, 0, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.movieName.setFont(font)
        self.movieName.setObjectName("movieName")
        self.movieNameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.movieNameInput.setGeometry(QtCore.QRect(30, 30, 221, 21))
        self.movieNameInput.setObjectName("movieNameInput")
        self.AddCast = QtWidgets.QPushButton(self.centralwidget , clicked = lambda:self.onClickAddCast())
        self.AddCast.setGeometry(QtCore.QRect(30, 70, 391, 51))
        self.AddCast.setObjectName("AddCast")
        self.SaveData = QtWidgets.QPushButton(self.centralwidget , clicked = lambda:self.saveExit(enterMovieWindow) )
        self.SaveData.setGeometry(QtCore.QRect(30, 140, 101, 31))
        self.SaveData.setObjectName("SaveData")
        self.MovieDurationLabel = QtWidgets.QLabel(self.centralwidget)
        self.MovieDurationLabel.setGeometry(QtCore.QRect(300, 10, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MovieDurationLabel.setFont(font)
        self.MovieDurationLabel.setObjectName("MovieDurationLabel")
        self.MovieDurationInput = QtWidgets.QTimeEdit(self.centralwidget)
        self.MovieDurationInput.setGeometry(QtCore.QRect(300, 30, 118, 22))
        self.MovieDurationInput.setObjectName("MovieDurationInput")
        enterMovieWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(enterMovieWindow)
        self.statusbar.setObjectName("statusbar")
        enterMovieWindow.setStatusBar(self.statusbar)

        self.retranslateUi(enterMovieWindow)
        QtCore.QMetaObject.connectSlotsByName(enterMovieWindow)

        

    def retranslateUi(self, enterMovieWindow):
        _translate = QtCore.QCoreApplication.translate
        enterMovieWindow.setWindowTitle(_translate("enterMovieWindow", "MainWindow"))
        self.movieName.setText(_translate("enterMovieWindow", "Enter Movie Name"))
        self.AddCast.setText(_translate("enterMovieWindow", "Add Cast"))
        self.SaveData.setText(_translate("enterMovieWindow", "Save and Exit"))
        self.MovieDurationLabel.setText(_translate("enterMovieWindow", "Movie Duration"))
        self.MovieDurationInput.setDisplayFormat(_translate("enterMovieWindow", "HH:mm:ss"))

    def onClickAddCast(self):
        print("movie storage --> ",self.storage)
        def openCastWin(self):
            self.window = QtWidgets.QMainWindow()
            self.addCastUi = Ui_AddCastWindow()
            self.addCastUi.setupUi(self.window)
            self.window.show()

        storage = database.get_movie_json()
        self.movie_name_ = self.movieNameInput.text().strip()
        self.duration_ = self.MovieDurationInput.text().strip()
        if (self.movie_name_ not in storage) and self.movie_name_ != "" and self.duration_ != "":
            self.storage[self.movie_name_] = {}
            self.storage[self.movie_name_]["duration"] = self.duration_
            self.storage[self.movie_name_]["casts"] = {}
            database.dump_movie(self.storage)
            database.clear_cast_store()
            openCastWin(self)
        
        elif self.movie_name_ != "" and self.duration_ != "":
            database.append_cast_to_movie(self.movie_name_)
            database.clear_cast_store()
            openCastWin(self)

        else :
            self.window = QtWidgets.QMainWindow()
            self.errorUi = Ui_Dialog()
            self.errorUi.setupUi(self.window)
            self.window.show()
    
    def saveExit(self, MainWindow):
        print("movie storage --> ",self.storage)
        storage = database.get_movie_json()
        self.duration_ = self.MovieDurationInput.text().strip()
        self.movie_name_ = self.movieNameInput.text().strip()
        if self.movie_name_ != "" and storage =={} :
            self.storage[self.movie_name_] = {}
            self.storage[self.movie_name_]["duration"] = self.duration_
            self.storage[self.movie_name_]["casts"] = {}
            database.dump_movie(self.storage)
        if self.movie_name_ in storage:
            database.append_cast_to_movie(self.movie_name_)
        database.dump_storage()
        self.storage.clear()
        
        MainWindow.close()
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    enterMovieWindow = QtWidgets.QMainWindow()
    ui = Ui_enterMovieWindow()
    ui.setupUi(enterMovieWindow)
    enterMovieWindow.show()
    sys.exit(app.exec_())
