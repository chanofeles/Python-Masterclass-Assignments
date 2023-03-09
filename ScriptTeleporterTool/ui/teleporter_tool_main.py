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

import teleporter_module

from Qt import QtWidgets, QtGui, QtCore, QtCompat
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton


#*******************************************************************
# VARIABLE
TITLE = os.path.splitext(os.path.basename(__file__))[0]
path_ui = ("/").join([os.path.dirname(__file__), TITLE + ".ui"])
print(path_ui)

#*******************************************************************

#*******************************************************************
# CLASS
class TeleporterTool(QMainWindow):
    def __init__(self):
        super(TeleporterTool, self).__init__()
        # BUILD local ui path
        path_ui = ("/").join([os.path.dirname(__file__),TITLE + ".ui"])

        # LOAD ui with absolute path
        main_widget = QtCompat.loadUi(path_ui)

        # # BUTTON
        # self.wgUtil.btnAdd.clicked.connect(self.press_add)

        # SHOW the UI
        # self.wgUtil.show()

        # Add a main widget
        # main_widget = teleporter_module.TeleporterModule()
        # self.setCentralWidget(main_widget)

        # Add a layout to the main widget
        layout = QVBoxLayout()
        main_widget.setLayout(layout)

    #************************************************************
    # PRESS
    def press_add(self):
        print("You added a new layout to this window!")

    def press_web(self):
        webbrowser.open("https://www.iknowvfx.com")


#*******************************************************************
# START
# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     classVar = TeleporterTool()
#     app.exec_()

panel = TeleporterTool()
panel.show()