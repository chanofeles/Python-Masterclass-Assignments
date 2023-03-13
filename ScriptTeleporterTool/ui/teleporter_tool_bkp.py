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
        #self.verticalLayout.addLayout(self.horizontalLayout)

        # Connect the button
        self.ui.btnAdd.clicked.connect(self.add_widget)
    
       
    
    def add_widget(self):
        
        newLayout = QVBoxLayout()
        widget = NewWidget()
        newLayout.addWidget(widget)

class NewWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Load the UI file
        from PySide2.QtUiTools import QUiLoader
        TITLE = os.path.splitext(os.path.basename(__file__))[0]
        path_module_ui = ("/").join([os.path.dirname(__file__),"teleporter_module.ui"])
        #path_module_ui = r"E:\PythonMasterclass\assignments\ScriptTeleporterTool\ui\teleporter_module.ui"
        loader = QUiLoader()
        self.module_ui = loader.load(path_module_ui, self)
        
        layout = QHBoxLayout()
        self.setLayout(layout)
        self.divider = self.module_ui.divider

    
        # Add a button and text input to the layout
        
        self.lineEdit = self.module_ui.lineEdit
        layout.addWidget(self.lineEdit)
        
        self.btnGetposition = self.module_ui.btnGetPosition
        layout.addWidget(self.btnGetposition)
        
        self.btnTeleport = self.module_ui.btnTeleport
        layout.addWidget(self.btnTeleport)

        
        


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyWidget()
    window.show()

    sys.exit(app.exec_())
