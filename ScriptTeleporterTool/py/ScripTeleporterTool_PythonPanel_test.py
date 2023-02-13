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


def show_panel():
    # SHOWS PANEL FOR PLATE SELECTION 
    # -------------------------------
    p.showModalDialog()
    new_context = p.typeKnob.value()


class TeleporterTool(nukescripts.PythonPanel):
    def __init__(self, ):
        nukescripts.PythonPanel.__init__(self, 'Shift Context')
        self.settings = nuke.PyScript_Knob('settings', 'Settings')
        self.addKnob(self.settings)

p = TeleporterTool()

show_panel()
