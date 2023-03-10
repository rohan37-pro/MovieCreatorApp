import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTreeWidget, QTreeWidgetItem
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont
import pprint
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.getcwd(), '..'))
sys.path.append(parent_dir)
import storageManager as database



class MovieDetailsWindowTree(QWidget):
    def __init__(self, parent=None):
        super( MovieDetailsWindowTree, self).__init__(parent)
        self.storage = database.get_storage()
        self.tree = QTreeWidget(self)
        self.tree.setColumnCount(3)
        self.tree.setHeaderLabels(['COLUMN 1', 'COLUMN 2', 'COLUMN 3'])
        self.tree.setGeometry(0, 0, 800, 500)
        self.tree.setColumnWidth(0, 200)
        self.tree.setColumnWidth(1, 200)
        self.tree.setColumnWidth(2, 200)
        self.add_items()

    def add_items(self):
        font = QFont()
        font.setBold(True)

        parent = QTreeWidgetItem(self.tree, ['All Movies', ''])
        header =  QTreeWidgetItem(parent,  ["MOVIE NAME" , "DURATION" ] )
        header.setFont(0, font)
        header.setFont(1, font)
        header.setFont(2, font)
        for Movie in self.storage.keys():
            child = QTreeWidgetItem(parent, [ Movie  ,  self.storage[Movie]["duration"] ])
            child.setSizeHint(0, QSize(200, 50))
            child.setSizeHint(1, QSize(200, 50))
            
            
            
            ######################       header for casts   ############################################
            #Setting the Heade
            child_header =  QTreeWidgetItem(child,  ["CAST NAME" , "CAST GENDER" , "CAST CHARACTER" ] )
            child_header.setFont(0, font)
            child_header.setFont(1, font)
            child_header.setFont(2, font)
            for CastDetails in self.storage[Movie]["casts"].keys():
                sub_child = QTreeWidgetItem(child,  [ CastDetails  , self.storage[Movie]["casts"][CastDetails]["gender"] , self.storage[Movie]["casts"][CastDetails]["character"]])
                sub_child.setSizeHint(0, QSize(200, 50))
                sub_child.setSizeHint(1, QSize(200, 50))
               

                sub_child_header = QTreeWidgetItem(sub_child,  ["DIALOGUE" , "FROM" , "TO" ] )
                sub_child_header.setFont(0, font)
                sub_child_header.setFont(1, font)
                sub_child_header.setFont(2, font)
                for Dialogues in self.storage[Movie]["casts"][CastDetails]['dialogue'].keys():
                    sub_sub_child = QTreeWidgetItem(sub_child, [Dialogues , self.storage[Movie]["casts"][CastDetails]['dialogue'][Dialogues]["from"] , self.storage[Movie]["casts"][CastDetails]['dialogue'][Dialogues]["to"] ] )
                    sub_sub_child.setSizeHint(0, QSize(200, 50))
                    sub_sub_child.setSizeHint(1, QSize(200, 50))
                    sub_sub_child.setSizeHint(1, QSize(200, 50))


        #self.tree.expandAll()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window =  MovieDetailsWindowTree()
    window.show()
    sys.exit(app.exec_())
