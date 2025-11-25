'''
 ____ ____ ____ ____ ____ ____
||B |||a |||x |||t |||e |||r ||
||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|
Version 5
last updated: 20/06/23
'''

from tkinter import *
from Images import *
from Frames import *
from functions import *

window = Tk()
#change if on different screen
#use _____x____+_____+____
window.attributes('-fullscreen', True)

#gather images
GetImages()


#create Exit bar
ExitCreate(window)

#collect screen size to allow for place functions
space = screenSpace()


#create screens
frmLogin = LoginCreate(window,space)
AddAccountCreate(window,space)

#load screen
LoginLoad(frmLogin)



#opens the window
window.mainloop()
