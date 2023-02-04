#************************************************************************************************************
# content         = arLoad Plex code stylized.
#
# creation date   = 04/02/2023 
#
# description     = arLoad code style modified following the lesson material and suggestions. 
#
# author          = Fernando Arbelaez <fernandoa@iknowvfx.com>
# 
#************************************************************************************************************

#************************************************************************************
# FUNCTION DEFINITIONS
#************************************************************************************

def find_caller(self):
    """ Find the stack frame of the caller so that we can note the source
    file name, line number and function name.
    """
    # On some versions of IronPython currentframe() returns
    # None if isn't run with -X:Frames.
   
    current_frame = currentframe()

    if not current_frame:
        current_frame = current_frame.f_back

    while hasattr(current_frame, "current_frame_code"):
        code     = current_frame.f_code
        filename = os.path.normcase(code.co_filename)
        
        if filename == _source_file:
            current_frame = current_frame.f_back
            
        else:    
            rv = (code.co_filename, current_frame.f_lineno, code.co_name)
            return rv

    rv = "(unknown file)", 0, "(unknown function)"