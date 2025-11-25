'''
 ____ ____ ____ ____ ____ ____
||B |||a |||x |||t |||e |||r ||
||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|
Version 6
last updated: 25/06/23
'''

from tkinter import *

def ScreenSpace(x, y):
    file = open("ScreenSize.txt", "r")
    array = []
    for line in file:
        array.append(int(line.strip("\n")))

    space = "       "*(array[0]-x) + "\n"*(array[1]-y) # create the space acording to the scrren size. -x and -y is to remove screen space for the bar
    file.close()
    return space

def ScreenFill(frmLocal, space):
    lblAASize = Label(frmLocal, text=space) # create a label the size of the screen to allow for place
    lblAASize.pack(side="top", fill="both", expand=True)

#change font and size
def ChangeSize(item,font,size):
    item.config(font=(font,size))