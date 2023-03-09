#******************************************************************************
# content         = Teleporter tool v02
#
# creation date   = 08/03/2023 
#
# description     = Overhaul of previous Teleporter tool version
#
# author          = Fernando Arbelaez <fernandoa@iknowvfx.com>
# 
#******************************************************************************


import os
import sys
import webbrowser

from Qt import QtWidgets, QtGui, QtCore, QtCompat
from PySide2.QtWidgets import QWidget, QMainWindow

#*******************************************************************
# VARIABLE
TITLE = os.path.splitext(os.path.basename(__file__))[0]
path_ui = ("/").join([os.path.dirname(__file__), TITLE + ".ui"])
print(path_ui)

#*******************************************************************

#*******************************************************************
# CLASS
class TeleporterModule(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        path_ui = ("/").join([os.path.dirname(__file__),TITLE + ".ui"])

        # LOAD ui with absolute path
        self.wgUtil = QtCompat.loadUi(path_ui)

        # BUTTON
        self.wgUtil.btnGetPosition.clicked.connect(self.press_bookmark)
        self.wgUtil.btnTeleport.clicked.connect(self.press_teleport)

        # Add a layout to the widget
        layout = self.wgUtil.mainLayout
        self.setLayout(layout)

        # Add a button and text input to the layout
        self.button = self.wgUtil.btnGetPosition
        layout.addWidget(self.button)

        self.text_input = self.wgUtil.QLineEdit
        layout.addWidget(self.text_input)

        self.btnTeleport = self.wgUtil.btnTeleport
        layout.addWidget(self.btnTeleport)
        # # SHOW the UI
        #self.wgUtil.show()

    #************************************************************
    # PRESS
    def press_add(self):
        print("You added a new layout to this window!")

    def press_teleport(self):
        print("Voila, you have teleported to another dimension.")
        
    def press_bookmark(self):
        print("You have bookmarked this thing.")

    def press_web(self):
        webbrowser.open("https://www.iknowvfx.com")



#*******************************************************************
# START
# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     classVar = TeleporterModule()
#     app.exec_()
