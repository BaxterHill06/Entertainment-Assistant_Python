'''
 ____ ____ ____ ____ ____ ____
||B |||a |||x |||t |||e |||r ||
||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|
Version 5
last updated: 19/06/23
'''

from tkinter import *
from Images import *
from Frames import *
from functions import *

window = Tk()
window.attributes('-fullscreen', True)

#gather images
plus, empLogo = GetImages()

#create Exit bar
ExitCreate(window)

#collect screen size to allow for place functions
space = screenSpace()

#create screens
frmLogin = LoginCreate(window,plus,space)
frmAddAccount = AddAccountCreate(window,space)

#load screen
LoginLoad(frmLogin)



#opens the window
window.mainloop()
