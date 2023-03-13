#******************************************************************************
# content         = Simple ui
#
# creation date   = 08/03/2023 
#
# description     = simpleUI application dev.
#
# author          = Fernando Arbelaez <fernandoa@iknowvfx.com>
# 
#******************************************************************************


import os
import sys
import webbrowser

from Qt import QtWidgets, QtGui, QtCore, QtCompat
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton


#*******************************************************************
# VARIABLE
TITLE = os.path.splitext(os.path.basename(__file__))[0]
path_ui = ("/").join([os.path.dirname(__file__), TITLE + ".ui"])
print(path_ui)


#*******************************************************************
# CLASS
class SimpleUI(QWidget):
    def __init__(self):
        # BUILD local ui path
        path_ui = ("/").join([os.path.dirname(__file__),TITLE + ".ui"])

        # LOAD ui with absolute path
        self.wgUtil = QtCompat.loadUi(path_ui)

        # BUTTON
        # self.wgUtil.btnAccept.clicked.connect(self.press_accept)
        # self.wgUtil.btnHelp.clicked.connect(self.press_help)

        # SHOW the UI
        self.wgUtil.show()


     # BUTTON
        self.wgUtil.pushButton.clicked.connect(self.add_btn)
        self.vLayout = self.findChild(QVBoxLayout,"verticalLayout")
        self.lineEdit = self.findChild(QLineEdit, "lineEdit")
    #************************************************************
    # PRESS
    def press_accept(self):
        print("You accepted this process!")

    def press_help(self):
        webbrowser.open("https://www.alexanderrichtertd.com")


        
    def add_btn(self):
        self.lineEdit = QLineEdit(self.verticalLayout)
        self.vLayout.addWidget(self.lineEdit)

    

    


#*******************************************************************
# START
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    classVar = SimpleUI()
    app.exec_()
