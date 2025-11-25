'''
 ____ ____ ____ ____ ____ ____
||B |||a |||x |||t |||e |||r ||
||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|
Version 7
last updated: 27/06/23
'''

from tkinter import *
from Images import *
from Frames import *


window = Tk()
#change if on different screen
#use _____x____+_____+____
window.attributes('-fullscreen', True)

def RunSoftware():
    #gather images
    GetImages()
    InitiateFrames()

    #create Exit bar
    ExitCreate(window)

    #collect screen size to allow for place functions
    space = ScreenSpace(0,0)

    #create screens
    LoginCreate(window,space,1)
    AddAccountCreate()
    AccountLoginCreate()


RunSoftware()

#opens the window
window.mainloop()
