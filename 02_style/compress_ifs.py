# STYLE ***************************************************************************
# content = assignment (Python Advanced)
#
# date    = 2022-01-07
# email   = contact@alexanderrichtertd.com
#**********************************************************************************


# COMMENT --------------------------------------------------
# Not optimal
def set_color(ctrlList=None, color=None):

    #Defines Dictionary of override values
    overrides_dict = {1:4,
                      2:13,
                      3:25,
                      4:17,
                      5:17,
                      6:15,
                      7:6,
                      8:16}

    for ctrlName in ctrlList:
        try:
            for key,value in overrides_dict.items():
                if color == key:
                    mc.setAttr(ctrlName + 'Shape.overrideColor', value)
        except:
            pass



# EXAMPLE
set_color(['circle','circle1'], 8)
            