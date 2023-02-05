import nuke
import nukescripts

node = nuke.selectedNode()
file_path = node['file'].value().split('/')
current_path = '/'.join(file_path)
plates_path = '/'.join(file_path[:6])  + '/'
def get_path():
    plates = os.listdir(plates_path)
    plates.sort()
    
    return plates

class ShiftContext(nukescripts.PythonPanel):
    def __init__(self, node):
        nukescripts.PythonPanel.__init__(self, 'Shift Context')
        self.sl_node = node
        self.typeKnob = nuke.Enumeration_Knob('shots', 'Shot', shots)
        nukescripts.PythonPanel.addKnob(self, self.typeKnob)


shots = get_path()
node = nuke.selectedNode()
p = ShiftContext(node)
p.showModalDialog()
new_context = p.typeKnob.value()
print("You have switched your context to: {}.".format(new_context))

new_context = plates_path + '/' + new_context + '/' +  file_path[7] + '/'
folders = os.listdir(new_context)
nuke.
print(folders)