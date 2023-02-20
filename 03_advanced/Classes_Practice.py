import nuke
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        # Set the window properties
        self.setWindowTitle("PySide 2 and Nuke 13 Window")
        self.setGeometry(100, 100, 300, 150)

        # Add a main widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # Add a layout to the main widget
        layout = QVBoxLayout()
        main_widget.setLayout(layout)

        # Add the first button to the layout
        button1 = QPushButton("Add New Area")
       
        #set the style of the button
        button1.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; font-weight: bold; }")
       
        button1.clicked.connect(lambda: self.add_widget(layout))
        layout.addWidget(button1)

        # Add the first widget to the layout
        self.add_widget(layout)
    

    def add_widget(self, layout):
        widget = Widget()
        widget.button.setText("Set Area")
        widget.button.clicked.connect(lambda: self.print_text_input(widget.text_input))
        layout.addWidget(widget)

    def print_text_input(self, text_input):
        print(text_input.text())


class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()

        # Add a layout to the widget
        layout = QHBoxLayout()
        self.setLayout(layout)

        # Add a button and text input to the layout
        self.button = QPushButton()
        layout.addWidget(self.button)

        self.text_input = QLineEdit()
        layout.addWidget(self.text_input)


panel = Window()
panel.show()
