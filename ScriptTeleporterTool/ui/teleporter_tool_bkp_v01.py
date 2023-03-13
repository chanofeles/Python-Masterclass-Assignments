import sys
import os
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton,QHBoxLayout


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Load the UI file
        from PySide2.QtUiTools import QUiLoader
        TITLE = os.path.splitext(os.path.basename(__file__))[0]
        path_ui = ("/").join([os.path.dirname(__file__),TITLE + ".ui"])
        loader = QUiLoader()
        self.ui = loader.load(path_ui, self)

         # Set up the layout
        self.verticalLayout = self.ui.verticalLayout       
        self.horizontalLayout = self.ui.mainLayout
        self.btnGetPosition = self.ui.btnGetPosition
        self.btnTeleport = self.ui.btnTeleport
        self.lineEdit = self.ui.lineEdit
        self.verticalLayout.addLayout(self.horizontalLayout)

        # Connect the button
        self.ui.btnAdd.clicked.connect(self.add_widget)
    
       
    
    def add_widget(self):
        widget = NewWidget()
        verticalLayout = self.verticalLayout   
        #self.verticalLayout = self.ui.verticalLayout  
        #widget.btnGetposition.clicked.connect(widget.compute_position)
        #widget.btnTeleport.setText("Teleport")
        #widget.btnTeleport.clicked.connect(widget.set_position)
        verticalLayout.addWidget(widget)

class NewWidget(MyWidget):
    def __init__(self):
        super(NewWidget, self).__init__()

        # Add a layout to the widget
        layout = QHBoxLayout()
        self.setLayout(layout)

        # Add a button and text input to the layout
        
        line_edit = self.lineEdit
        layout.addWidget(line_edit)
        
        btnGetposition = self.btnGetPosition
        layout.addWidget(btnGetposition)
        
        btnTeleport = self.btnTeleport
        layout.addWidget(btnTeleport)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyWidget()
    window.show()

    sys.exit(app.exec_())
