#************************************************************************************************************
# content         = Cube class.
#
# creation date   = 11/02/2023 
#
# description     = Use of Python Classes practice. 
#
# author          = Fernando Arbelaez <fernandoa@iknowvfx.com>
# 
#************************************************************************************************************

"""
CUBE CLASS

1. CREATE an abstract class "Cube" with the functions:
   translate(x, y, z), rotate(x, y, z), scale(x, y, z) and color(R, G, B)
   All functions store and print out the data in the cube (translate, rotate, scale and color).

2. ADD an __init__(name) and create 3 cube objects.

3. ADD the function print_status() which prints all the variables nicely formatted.

4. ADD the function update_transform(ttype, value).
   "ttype" can be "translate", "rotate" and "scale" while "value" is a list of 3 floats.
   This function should trigger either the translate, rotate or scale function.

   BONUS: Can you do it without using ifs?

5. CREATE a parent class "Object" which has a name, translate, rotate and scale.
   Use Object as the parent for your Cube class.()
   Update the Cube class to not repeat the content of Object.

"""
class Object():
   def __init__(self,name):
      '''Initialize cube attributes'''
      self.name = name
      self.translate_value = [0, 0, 0]
      self.rotate_value = [0, 0, 0]
      self.scale_value = [1, 1, 1]
      self.color_value = [250, 250, 250]

class Cube(Object):

   """Initialization of the Object properties."""

   def translate(self,x,y,z):
      self.translate_value = [x,y,z]
      print(f'Translate values {self.translate_value}')

   def rotate(self,x,y,z):
      self.rotate_value = [x,y,z]
      print(f'Rotation values {self.rotate_value}')

   def scale(self,x,y,z):
      self.scale_value = [x,y,z]
      print(f'Scale values {self.scale_value}')

   def color(self,r,g,b):
      self.color_value = [r ,g ,b]
      print(f'Scale values {self.color_value}')

   def print_status(self):

      '''Prints Object properties values'''

      print(f'Object name {self.name}')
      print(f'RGB values {self.color_value}')
      print(f'Translation values {self.translate_value}')
      print(f'Rotation values {self.rotate_value}')
      print(f'Scale values {self.scale_value}')

   def update_transform(self,ttype,value = []):

      '''Update transformation values of the object'''

      if ttype == 'translate':
         self.translate_value = value
      elif ttype == 'rotate':
         self.rotate_value = value
      elif ttype == 'scale':
         self.scale_value = value
      else:
         self.color_value = value


##Create 3 different Cube objects
cube_01 = Cube('Cube_01')
cube_02 = Cube('Cube_02')
cube_03 = Cube('Cube_03')

## Updates color of cube_01 and print status
cube_01.update_transform('color',[20,20,20])
cube_01.print_status()

## Updates color of cube_01 and print status
cube_02.update_transform('translate',[200,180,-90])
cube_02.print_status()