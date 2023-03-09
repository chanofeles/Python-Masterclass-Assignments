c = nuke.center()#Current x,y position of the DAG
z = nuke.zoom()# DAG zoom % value

print(c,z)

nuke.zoom(1,(-438, -1451))#Adding  parameters to the zoom method overrides its value.



## using average 
nodes = nuke.selectedNodes()    # GET SELECTED NODES
amount = len( nodes )    # GET NUMBER OF SELECTED NODES

allX = sum( [ n.xpos()+n.screenWidth()/2 for n in nodes ] )  # SUM OF ALL X VALUES
allY = sum( [ n.ypos()+n.screenHeight()/2 for n in nodes ] ) # SUM OF ALL Y VALUES

# CENTER OF SELECTED NODES
centreX = allX / amount
centreY = allY / amount
print(centreX, centreY)

nuke.zoom(1,(centreX,centreY))


