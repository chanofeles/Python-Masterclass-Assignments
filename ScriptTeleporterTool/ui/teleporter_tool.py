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

#*******************************************************************
# VARIABLE
TITLE = os.path.splitext(os.path.basename(__file__))[0]
path_ui = ("/").join([os.path.dirname(__file__), TITLE + ".ui"])
print(path_ui)

#*******************************************************************

#*******************************************************************
# CLASS
class TeleporterTool():
    def __init__(self):
        # BUILD local ui path
        path_ui = ("/").join([os.path.dirname(__file__),TITLE + ".ui"])

        # LOAD ui with absolute path
        self.wgUtil = QtCompat.loadUi(path_ui)

        # BUTTON
        self.wgUtil.btnAdd.clicked.connect(self.press_add)
        self.wgUtil.btnGetPosition.clicked.connect(self.press_bookmark)
        self.wgUtil.btnTeleport.clicked.connect(self.press_teleport)
        self.wgUtil.btnWeb.clicked.connect(self.press_web)

        # SHOW the UI
        self.wgUtil.show()

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


class Widget(TeleporterTool):
    
    position = None
    
    def __init__(self):
        super(TeleporterTool, self).__init__()

        # Add a layout to the widget
        layout = QHBoxLayout()
        self.setLayout(layout)

        # Add a button and text input to the layout
        self.button = btnGetPosition()
        layout.addWidget(self.button)

        self.text_input = QLineEdit()
        layout.addWidget(self.text_input)

        self.btnTeleport = QPushButton()
        layout.addWidget(self.btnTeleport)




#*******************************************************************
# START
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    classVar = TeleporterTool()
    app.exec_()
