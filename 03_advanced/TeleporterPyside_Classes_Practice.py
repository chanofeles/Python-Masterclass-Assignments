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

''' Disclamimer: This is what I got so far, I've tried to use classes as a mean of simplification, since it is
    only made by buttons and text input fields. There is no current action on the buttons and I am struggling 
    to make the new instances of the main class to appear below the original instead of to the side, any 
    any suggestion will be appreciated'''

#************************************************************************************************************
# IMPORTS
#************************************************************************************************************
# Third party API

import nuke
from PySide2 import QtGui, QtCore, QtWidgets


#************************************************************************************
# Classes
#************************************************************************************

# Button class
class Button(QtWidgets.QPushButton):
    def __init__(self, text, parent=None):
        super(Button, self).__init__(text, parent)
        #set the style of the button
        self.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; font-weight: bold; }")


# Text input class
class AreaName(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        super(AreaName, self).__init__(parent)
        self.setPlaceholderText('Enter Area name here...')


# Window class
class AreaWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(AreaWindow, self).__init__(parent)
        self.initUI()

    # Assembly of all classes in a single horizontal layout 

    def initUI(self):
        # Create + button that adds a new AreaWindow instance
        self.button1 = Button('+', self)
        self.button1.setFixedSize(25,25)
        self.button1.clicked.connect(self.createNewLine)

        # Create text input
        self.text_input = AreaName(self)

        # Create button 2
        self.button2 = Button('Set Area', self)

        # Add widgets to horizontal layout
        self.hbox = QtWidgets.QHBoxLayout()
        self.hbox.addWidget(self.button1)
        self.hbox.addWidget(self.text_input)
        self.hbox.addWidget(self.button2)

        # Add the layout to the window
        self.setLayout(self.hbox)

    def createNewLine(self):
        # Creates a new array of the Area window elements (buttons and text)
        sub_window = AreaWindow(parent=self)
        self.hbox.addWidget(sub_window)



# Panel class
class SettingsPanel(QtWidgets.QDockWidget):
    def __init__(self):
        super(SettingsPanel, self).__init__()
        self.setWindowTitle('My Panel')
        self.setFeatures(QtWidgets.QDockWidget.DockWidgetClosable | QtWidgets.QDockWidget.DockWidgetFloatable)
        self.setWidget(AreaWindow())

        # Set vertical layout
        self.setLayout(QtWidgets.QVBoxLayout())
    

        # set the window flags to keep the widget on top
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        
# Create the panel
def createPanel():
    panel = SettingsPanel()
    return panel

# Show panel
panel = createPanel()
panel.show()
