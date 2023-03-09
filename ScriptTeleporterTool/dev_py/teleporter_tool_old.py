import nuke
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        # Set the window properties
        self.setWindowTitle("Teleporter Tool")
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
        widget.button.clicked.connect(widget.compute_position)
        widget.btnTeleport.setText("Teleport")
        widget.btnTeleport.clicked.connect(widget.set_position)
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

        # Add a button and text input to the layout
        self.button = QPushButton()
        layout.addWidget(self.button)

        self.text_input = QLineEdit()
        layout.addWidget(self.text_input)

        self.btnTeleport = QPushButton()
        layout.addWidget(self.btnTeleport)

    def compute_position(self):
        
        
        # Get selected nodes & store the names
        nodes = nuke.selectedNodes()

        if not nodes:
            nuke.message('seleccione nodos')
        else: 
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
            # print(zoom_data)
            # return zoom_data
    
    def set_position(self):

        # Retrieves the stored DAG zoom and position data and override the current values.      
        #position = self.get_position()
        #print(position)
        nuke.zoom(self.position[0],(self.position[1],self.position[2]))
        # print('will this work someday?')
        
    


panel = Window()
panel.show()
