#************************************************************************************************************
# content         = ScriptTeleporter Tool.
#
# creation date   = 11/02/2023 
#
# description     = Script Teleporter Tool developed using PySide2
#
# author          = Fernando Arbelaez <fernandoa@iknowvfx.com>
# 
#************************************************************************************************************

#************************************************************************************************************
# IMPORTS
#************************************************************************************************************
# Third party API
import nuke
import PySide2.QtWidgets as QtWidgets
import PySide2.QtGui as QtGui
import PySide2.QtCore as QtCore

#************************************************************************************
# Classes
#************************************************************************************

#Button class
class CustomButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super(CustomButton, self).__init__(parent)
        self.setStyleSheet("background-color: gray;")
        self.setFixedSize(100, 50)

    # Define button color behavior when mouse hovering
    def enterEvent(self, event):
        self.setStyleSheet("background-color: lightblue;")

    def leaveEvent(self, event):
        self.setStyleSheet("background-color: gray;")

#Panel class
class CustomPanel(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(CustomPanel, self).__init__(parent)
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

#Text input class
class TextInput(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        super(TextInput, self).__init__(parent)
        self.setFixedSize(100, 50)

#Panel Assembly class
class Panel(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Panel, self).__init__(parent)
        
        # set the window flags to keep the widget on top
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)
        
        # adds horizontal layout to the panel MAYBE CHANGE NAME AND INVESTIGATE FURTHER
        self.button_text_input_layout = QtWidgets.QHBoxLayout()
        self.layout.addLayout(self.button_text_input_layout)
        
        # adds button to the panel
        self.button = CustomButton()
        self.button_text_input_layout.addWidget(self.button)
        
        # adds text input to the panel
        self.text_input = TextInput()
        self.button_text_input_layout.addWidget(self.text_input)
        
        # adds the main panel class
        self.panel = CustomPanel()
        self.layout.addWidget(self.panel)



my_panel = Panel()
my_panel.show()