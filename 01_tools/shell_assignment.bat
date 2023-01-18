#******************************************************************************
# content         = Shell commands
#
# creation date   = 18/01/2023 
#
# description     = Advanced tools Shell assignment No.1
#
# author          = Fernando Arbelaez <fernandoa@iknowvfx.com>
# 
#******************************************************************************

:: a) Create the directory "shell_test" (and changing directory)
cd C:\Users\Keyframe\Desktop
md 01_assignment_shell
cd 01_assignment_shell

:: b) Create the file "shell_print.py" with a simple print into the directory
echo print('This will get difficult for sure!') > shell_print.py

:: c) Rename the file to "new_shell_print.py"
ren shell_print.py new_shell_print.py

:: d) List what is in the directory "shell_test" including their file permissions
dir 
icacls new_shell_print.py

:: e) Execute the Python file and call the simple print
python new_shell_print.py

:: f) Remove the directory "shell_test" with its content
cd ..
rmdir /s 01_assignment_shell


