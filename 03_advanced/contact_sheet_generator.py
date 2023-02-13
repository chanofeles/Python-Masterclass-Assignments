# Contact_sheet_generator *********************************************************************
# content     = final assignment python masterclass 
# date        = 2022-03-08
# author      = Fernando Arbelaez fernandoa@iknowvfx.com
#******************************************************************************


#*********************************************************************
# CONTACTSHEET GENERATOR
#*********************************************************************
# Creates a contact sheet from a project folder containing the sequence shots.
# Allows the user to select which shots he wants to be added to the contactsheet.


import os
import nuke
import nukescripts


def contactsheet_gen():

    # File path search panel
    # Panel properties
    panel_1 = nuke.Panel('Contactsheet Generator files path')
    panel_1.setWidth(700)
    panel_1.addFilenameSearch('file_path', 'please select a valid project path')



    # Shows the panel 
    if panel_1.value('file_path'):
        panel_1.show()
        shot_stills_path = panel_1.value('file_path')
        references = os.listdir(shot_stills_path)
        panel = nuke.Panel('Contactsheet Generator')
        panel.setWidth(250)

        # Check if the path exist
        if os.path.exists(shot_stills_path):
            shots = []
            selected_shots = []

            # Project settings.
            nuke.root().knob('format').setValue('HD_1080')
            proj_width = int(nuke.root().knob('format').value().width())
            proj_height = int(nuke.root().knob('format').value().height())

            # Checks the amount of shots that live in the project path and creates a check box per each.
            for ref in references:
                shots.append(ref)
                panel.addBooleanCheckBox(ref, True)

            # Creates line input for the user to choose the number of Rows and Columns.
            panel.addSingleLineInput('rows', 'Enter number of columns')
            panel.addSingleLineInput('cols', 'Enter number of rows')

            # Show shot selection panel
            if shots:
                panel.show()
                
                # Check if the box is ticked or not
                for shot in shots:
                    if panel.value(shot) == True:
                        selected_shots.append(shot)

                # Validates the data entered in the input text field as numeric
                if panel.value('rows').isnumeric() and panel.value('cols').isnumeric():
                    rows = panel.value('rows')
                    cols = panel.value('cols')

                    # Check if there is more than 1 shot selected
                    if len(selected_shots) <= 1:
                        nuke.message('Select at least 2 shots')
                        
                    # Node tree creation
                    else:
                        text_nodes = [] 
                        for shot in selected_shots:

                            # Creates read node for every selected shot and set some properties
                            node = nuke.createNode('Read')
                            node['name'].setValue(shot)
                            node['file'].setValue(shot_stills_path + shot + '/' + shot + '.png')
                            text_node = nuke.createNode('Text2')
                            text_node['name'].setValue('label_' + shot)
                            text_node['message'].setValue('[full_name [topnode]]')
                            text_node['font_size'].setValue(50)
                            text_nodes.append(text_node)

                        # Create an appendclip node and connects its inputs to the respective shot
                        append_01 = nuke.createNode('AppendClip')
                        inputs = 0
                        
                        for node in text_nodes:
                            node_name = node['name'].value()
                            input_num = int(node_name[-1])-1
                            append_01.setInput(input_num,node)
                        
                        # Creates contactsheet node and set its properties
                        contact_sheet01 = nuke.createNode('ContactSheet')
                        contact_sheet01['width'].setValue(proj_width * 2)
                        contact_sheet01['height'].setValue(proj_height * 2)
                        contact_sheet01['center'].setValue(True)
                        contact_sheet01['roworder'].setValue(0)
                        contact_sheet01['rows'].setValue(int(rows))
                        contact_sheet01['columns'].setValue(int(cols))

                        # Connects contact sheet node inputs to the node tree nodes
                        for node in text_nodes:
                            node_name = node['name'].value()
                            input_num = int(node_name[-1])-1
                            contact_sheet01.setInput(input_num,node)

                        # Creates a second appendclip node and connects its inputs to the upstream nodes
                        append_02 = nuke.createNode('AppendClip')
                        append_02.setInput(0,contact_sheet01)
                        append_02.setInput(1,append_01)

                        # Creates a write node and set basic properties
                        file_output = nuke.nodes.Write(file= '../contact_sheetv01', name='Contactsheet output',file_type = 3)
                        file_output.setInput(0, append_02)

                        nuke.autoplace_all()

                else:
                    nuke.message('Please enter a valid integer')

        else:
            nuke.message('Please select a valid path containing the desired shots.')


