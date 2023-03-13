import os

import nuke

from Qt import QtWidgets, QtGui, QtCore, QtCompat
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel

IMAGE_PATH = r"E:\PythonMasterclass\assignments\ScriptTeleporterTool\ui\img\{}" + ".png"

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        # set the window flags to keep the widget on top
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        # set the title of the widget
        self.setWindowTitle("Script Teleporter")

        # Set the window properties
        self.setWindowTitle("Teleporter Tool")
        self.setGeometry(100, 100, 300, 150)


        # Add a main widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_widget.setMaximumWidth(400)

        # Add a layout to the main widget
        layout = QVBoxLayout()
        main_widget.setLayout(layout)
        layout.setStretch(0,0)

        self.lblHeader = QLabel()
        self.lblHeader.setMaximumWidth(400)
        self.lblHeader.setPixmap(QtGui.QPixmap(IMAGE_PATH.format("header")))
        layout.addWidget(self.lblHeader)

        # Add the first button to the layout
        btnAddArea = QPushButton("Add New Area")
       
        #set the style of the button
        btnAddArea.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; font-weight: bold; }"
                      "QPushButton:hover{background-color: rgb(209, 225, 219); color: rgb(50, 52, 64);}"
                      "QPushButton:pressed{background-color: rgb(168, 162, 142); border-style: inset;}")


       
        btnAddArea.clicked.connect(lambda: self.add_widget(layout))
        layout.addWidget(btnAddArea)

        # Add the first widget to the layout
        self.add_widget(layout)
    

    def add_widget(self, layout):
        widget = Widget()
        widget.btnGetPosition.setText("Bookmark")
        widget.btnGetPosition.clicked.connect(widget.compute_position)
        widget.btnTeleport.setText("Teleport")
        widget.btnTeleport.clicked.connect(widget.set_position)
        widget.btnLock.setIcon(QtGui.QPixmap(IMAGE_PATH.format("unlock")))
        widget.btnLock.clicked.connect(widget.unlock_button)
        layout.addWidget(widget)

    def print_text_input(self, text_input):
        print(text_input.text())
    


class Widget(QWidget):
    
    position = None
    
    def __init__(self):
        super(Widget, self).__init__()

        # Add a layout to the widget
        layout = QHBoxLayout()
        self.setLayout(layout)

        # Add button lock

        self.btnLock = QPushButton()
        self.btnLock.setMaximumWidth(20)
        self.btnLock.setMaximumHeight(20)
        layout.addWidget(self.btnLock)

        self.text_input = QLineEdit()
        layout.addWidget(self.text_input)

        self.btnGetPosition = QPushButton()
        layout.addWidget(self.btnGetPosition)

        self.btnTeleport = QPushButton()
        layout.addWidget(self.btnTeleport)



    def compute_position(self):
        
        if not nuke.selectedNodes():

            nuke.message("Please select at least one node.")

        else:
        
            # Get selected nodes & store the names
            nodes = nuke.selectedNodes()
            sel_nodes = [node['name'].value() for node in nodes]
            
            # Get the amount of nodes selected
            amount = len( nodes )

            # Average of all X and Y position values of the selected nodes
            allX = sum( [ n.xpos()+n.screenWidth()/2 for n in nodes ] )
            allY = sum( [ n.ypos()+n.screenHeight()/2 for n in nodes ] )
            
            # Stores de current zoom value of the DAG (Node graph)
            zoom_value = nuke.zoom()

            # Center of selected nodes.
            centreX = allX / amount
            centreY = allY / amount

            # Stores de zoom / X / Y values of the nodes in a list
            zoom_data = [zoom_value , 
                        centreX , 
                        centreY]

            self.position = zoom_data
            self.btnGetPosition.setEnabled(False)
            self.btnLock.setIcon(QtGui.QPixmap(IMAGE_PATH.format("lock")))
            self.text_input.setEnabled(False)

    def set_position(self):

        if not self.position:
            nuke.message('Please Bookmark first.')
        else:
            # Retrieves the stored DAG zoom and position data and override the current values.      
            nuke.zoom(self.position[0],(self.position[1],self.position[2]))
            # print('will this work someday?')
        
        
    def unlock_button(self):
        self.btnGetPosition.setEnabled(True)
        self.btnLock.setIcon(QtGui.QPixmap(IMAGE_PATH.format("unlock")))

        self.text_input.setEnabled(True)
        
    


panel = Window()
panel.show()
