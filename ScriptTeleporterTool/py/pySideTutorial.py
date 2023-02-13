import nuke
from PySide2 import QtWidgets, QtCore

class TeleporterTool(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TeleporterTool, self).__init__(parent)

        # set the window flags to keep the widget on top
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        # set the title of the widget
        self.setWindowTitle("Script Teleporter")

        # create a button
        self.button = QtWidgets.QPushButton("Settings")
        self.button.clicked.connect(settings.show)

        # create a layout and add the button to it
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def show_message(self):
        nuke.message("Well done")

class SetupWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SetupWindow, self).__init__(parent)

        # set the window flags to keep the widget on top
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        # set the title of the widget
        self.setWindowTitle("Script Teleporter")

        # create a button
        self.button = QtWidgets.QPushButton("+")
        self.button.clicked.connect(self.show_message)
        self.area1 = QtWidgets.QLineEdit()
        #area1.setFont(QFont('Arial',14))
        

        # create a layout and add the button to it
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.area1)
        self.setLayout(layout)

    def show_message(self):
        nuke.message("Well done")

# create an instance of the widget and show it
settings = SetupWindow()
my_widget = TeleporterTool()
my_widget.show()