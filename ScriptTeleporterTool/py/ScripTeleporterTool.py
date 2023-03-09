import nuke
import PySide2.QtWidgets as QtWidgets
import PySide2.QtGui as QtGui
import PySide2.QtCore as QtCore

class CustomButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super(CustomButton, self).__init__(parent)
        self.setStyleSheet("background-color: lightblue;")
        self.setFixedSize(100, 50)

    def enterEvent(self, event):
        self.setStyleSheet("background-color: yellow;")

    def leaveEvent(self, event):
        self.setStyleSheet("background-color: lightblue;")

class CustomPanel(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(CustomPanel, self).__init__(parent)
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

class TextInput(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        super(TextInput, self).__init__(parent)
        self.setFixedSize(100, 50)

class Panel(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Panel, self).__init__(parent)
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)
        
        self.button_text_input_layout = QtWidgets.QHBoxLayout()
        self.layout.addLayout(self.button_text_input_layout)
        
        self.button = CustomButton()
        self.button_text_input_layout.addWidget(self.button)
        
        self.text_input = TextInput()
        self.button_text_input_layout.addWidget(self.text_input)
        
        self.panel = CustomPanel()
        self.layout.addWidget(self.panel)



my_panel = Panel()
my_panel.show()