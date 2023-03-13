import sys
import os
from Qt import QtWidgets, QtGui, QtCore, QtCompat
from Qt.QtWidgets import QHBoxLayout, QVBoxLayout
from PySide2.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

#*******************************************************************
# VARIABLE
TITLE = os.path.splitext(os.path.basename(__file__))[0]
CURRENT_PATH = os.path.dirname(__file__)
IMAGE_PATH = CURRENT_PATH + "/img/{}.png"
path_ui = ("/").join([os.path.dirname(__file__), TITLE + ".ui"])


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        # LOAD ui with absolute path
        self.ui = QtCompat.loadUi(path_ui)

        # Set up the layout
        self.verticalLayout = QVBoxLayout()
        self.lblHeader = self.ui.lblHeader
        self.lblHeader.setPixmap(QtGui.QPixmap(IMAGE_PATH.format("header")))
        # Connect the button
        self.ui.btnAdd.clicked.connect(self.add_widget)
        print(self.ui.btnAdd.text())
        
        # SHOW the UI
        self.ui.show()    

        print(f"Number of items in vertical layout: {self.verticalLayout.count()}")

    def add_widget(self):
        # Define the new layout
        
        new_layout = QHBoxLayout()

        # Add the new widgets to the new layout
        new_layout.addWidget(self.ui.lineEdit)
        new_layout.addWidget(self.ui.btnGetPosition)
        new_layout.addWidget(self.ui.btnTeleport)


        # Add the new layout to the vertical layout
        #self.verticalLayout.addLayout(new_layout)
        self.verticalLayout.addLayout(new_layout)
        print(f"Number of items in new layout: {new_layout.count()}")
        print(f"Number of items in vertical layout: {self.verticalLayout.count()}")


#*******************************************************************
# START
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    classVar = MyWidget()
    app.exec_()
