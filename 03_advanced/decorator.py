#************************************************************************************************************
# content         = Decorator Practice
#
# creation date   = 12/02/2023 
#
# description     = Using decorator to print Start and End along with the processing time of 3 different functions. 
#
# author          = Fernando Arbelaez <fernandoa@iknowvfx.com>
# 
#************************************************************************************************************


"""
0. CONNECT the decorator "print_process" with all sleeping functions.
   Print START and END before and after.

   START *******
   main_function
   END *********


1. Print the processing time of all sleeping functions.
END - 00:00:00


2. PRINT the name of the sleeping function in the decorator.
   How can you get the information inside it?

START - long_sleeping

"""


import time


#*********************************************************************
# DECORATOR
def print_process(func):
    #def wrapper(*args, **kwargs):
    def wrapper(*args, **kwargs):
        print('START *******')
        start_time = time.time()
        func(*args)                  # main_function
        
        #Prints the name of func.
        print('Function: ' + func.__name__)
        end_time = time.time()
        
        #Calculate the processing time of func()
        processing_time = end_time - start_time
        print(f'END ********* {processing_time}')
    return wrapper


#*********************************************************************
# FUNC

@print_process
def short_sleeping(name):
    time.sleep(.1)
    print(name)

@print_process
def mid_sleeping():
    time.sleep(2)

@print_process
def long_sleeping():
    time.sleep(4)

short_sleeping("so sleepy")

mid_sleeping()

long_sleeping()
