#************************************************************************************************************
# content         = Shift context function.
#
# creation date   = 04/02/2023 
#
# description     = Stylized version of the file my_code_original.py that you can find in this repository. 
#
# author          = Fernando Arbelaez <fernandoa@iknowvfx.com>
# 
#************************************************************************************************************

#************************************************************************************************************
# IMPORTS
#************************************************************************************************************

# Third party API
import nuke
import nukescripts

#************************************************************************************
# VARIABLES
#************************************************************************************

node = nuke.selectedNode()
file_path = node['file'].value().split('/')
current_path = '/'.join(file_path)
plates_path = '/'.join(file_path[:6])  + '/'

shots = get_path()
node = nuke.selectedNode()
p = ShiftContext(node)

#************************************************************************************
# FUNCTION DEFINITIONS
#************************************************************************************

def get_path():
    # GETS THE FOLDER PATH CONTAINING THE DIFFERENT PLATES FOR ALL 
    # SHOTS IN A SEQUENCE AND RETURNS A LIST.
    # -------------------------------
    plates = os.listdir(plates_path)
    plates.sort()
    
    return plates

def show_panel():
    # SHOWS PANEL FOR PLATE SELECTION 
    # -------------------------------
    p.showModalDialog()
    new_context = p.typeKnob.value()
    nuke.message("You have switched your context to: {}.".format(new_context))


#************************************************************************************
# Classes
#************************************************************************************

class ShiftContext(nukescripts.PythonPanel):
    def __init__(self, node):
        nukescripts.PythonPanel.__init__(self, 'Shift Context')
        self.sl_node = node
        self.typeKnob = nuke.Enumeration_Knob('shots', 'Shot', shots)
        nukescripts.PythonPanel.addKnob(self, self.typeKnob)


show_panel()






