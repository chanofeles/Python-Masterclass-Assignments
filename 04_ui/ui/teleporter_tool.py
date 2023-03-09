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
        #self.wgUtil.btnAccept.clicked.connect(self.press_accept)
        #self.wgUtil.btnHelp.clicked.connect(self.press_help)

        # SHOW the UI
        self.wgUtil.show()

#*******************************************************************
# START
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    classVar = TeleporterTool()
    app.exec_()
