#******************************************************************************
# content         = KnobScripter MockUp
#
# creation date   = 13/03/2023 
#
# description     = simpleUI application dev.
#
# author          = Fernando Arbelaez <fernandoa@iknowvfx.com>
# 
#******************************************************************************

import os
import sys
import webbrowser
import subprocess

from Qt import QtWidgets, QtGui, QtCore, QtCompat
from PySide2.QtWidgets import QColorDialog, QMessageBox


#*******************************************************************
# VARIABLE
TITLE = os.path.splitext(os.path.basename(__file__))[0]
CURRENT_PATH = os.path.dirname(__file__)
IMAGE_PATH = CURRENT_PATH + "/icons/{}.png"


#*******************************************************************
# CLASS
class SimpleUI():
    def __init__(self):
        # BUILD local ui path
        path_ui = ("/").join([os.path.dirname(__file__),TITLE + ".ui"])

        # LOAD ui with absolute path
        self.uiRef = QtCompat.loadUi(path_ui)

        # BUTTON
        self.uiRef.btnPicker.clicked.connect(self.pick_color)
        self.uiRef.btnPicker.setIcon(QtGui.QPixmap(IMAGE_PATH.format("icon_pick")))

        self.uiRef.btnRefresh.clicked.connect(self.set_text)
        self.uiRef.btnRefresh.setIcon(QtGui.QPixmap(IMAGE_PATH.format("refresh")))

        self.uiRef.btnImport.clicked.connect(self.first_warning_msg)
        self.uiRef.btnImport.setIcon(QtGui.QPixmap(IMAGE_PATH.format("download")))

        self.uiRef.btnSave.clicked.connect(self.third_warning_msg)
        self.uiRef.btnSave.setIcon(QtGui.QPixmap(IMAGE_PATH.format("icon_save")))

        self.uiRef.btnConsole.clicked.connect(self.console_print)
        self.uiRef.btnConsole.setIcon(QtGui.QPixmap(IMAGE_PATH.format("run")))

        self.uiRef.btnClear.clicked.connect(self.clear_text)
        self.uiRef.btnClear.setIcon(QtGui.QPixmap(IMAGE_PATH.format("clear_console")))

        self.uiRef.btnReturn.clicked.connect(self.second_warning_msg)
        self.uiRef.btnReturn.setIcon(QtGui.QPixmap(IMAGE_PATH.format("enter")))

        self.uiRef.btnSearch.clicked.connect(self.fourth_warning_msg)
        self.uiRef.btnSearch.setIcon(QtGui.QPixmap(IMAGE_PATH.format("icon_search")))


        # SHOW the UI
        self.uiRef.show()



    #************************************************************
    # PRESS
    def press_accept(self):
        print("You accepted this process!")

    def press_help(self):
        webbrowser.open("https://www.alexanderrichtertd.com")

    def pick_color(self):
    # show the color dialog and get the selected color
        color = QColorDialog.getColor()
        if color.isValid():
            # if a valid color was selected, set the line edit font color to that color
            self.uiRef.txtInput.setStyleSheet(f"color: {color.name()};")

    def first_warning_msg(self):
        msg_window = QMessageBox()
        msg_window.setIcon(QMessageBox.Warning)
        msg_window.setText("This just to warn you that none of this buttons actually work")
        msg_window.setWindowTitle("Last warning!")
        msg_window.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        # Show the warning message box and handle the user's response
        response = msg_window.exec_()
        if response == QMessageBox.Ok:
            pass
        else:
            pass

    def second_warning_msg(self):
        msg_window = QMessageBox()
        msg_window.setText("Told you nothing works here")
        msg_window.setWindowTitle("Believe me")
        # Show the warning message box and handle the user's response
        response = msg_window.exec_()
        if response == QMessageBox.Ok:
            print("Awesome!")

    def third_warning_msg(self):
        msg_window = QMessageBox()
        msg_window.setIcon(QMessageBox.Warning)
        msg_window.setText("OK, Why not, lets save nothing right?")
        msg_window.setWindowTitle("Lets save nothing!")
        msg_window.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        # Show the warning message box and handle the user's response
        response = msg_window.exec_()
        if response == QMessageBox.Ok:
            pass
        else:
            pass

    def fourth_warning_msg(self):
        msg_window = QMessageBox()
        msg_window.setIcon(QMessageBox.Warning)
        msg_window.setText("What are you looking for?")
        msg_window.setWindowTitle("Search")
        msg_window.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        # Show the warning message box and handle the user's response
        response = msg_window.exec_()
        if response == QMessageBox.Ok:
            pass
        else:
            pass

    def console_print(self):
        subprocess.Popen(["cmd.exe", "/k", "echo Here is nothing, you are welcome!"])

    def clear_text(self):
        self.uiRef.txtInput.clear()       

    def set_text(self):
        self.uiRef.txtInput.clear()        
        # Get the directory of the current script
        dir_path = os.path.dirname(os.path.realpath(__file__))
        
        # Open the file using a relative path
        with open(os.path.join(dir_path, "text_test.txt"), "r") as file:
            lines = file.readlines()
            joined_lines = ''.join(lines)
            file.close()
        self.uiRef.txtInput.insertPlainText(joined_lines)
        
#*******************************************************************
# START
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    classVar = SimpleUI()
    app.exec_()
