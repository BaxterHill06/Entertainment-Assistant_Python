'''
 ____ ____ ____ ____ ____ ____
||B |||a |||x |||t |||e |||r ||
||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|
Version 9
last updated: 04/07/23
'''


from tkinter import *
import ctypes

def ScreenSpace(x, y):
    global array
    file = open("ScreenSize.txt", "r")
    array = []
    for line in file:
        array.append(int(line.strip("\n")))

    space = " "*(array[0]*7-x) + "\n"*(array[1]-y) # create the space acording to the scrren size. -x and -y is to remove screen space for the bar
    print(array[1]-y)
    file.close()
    return space

def ScreenFill(frmLocal, space):
    lblAASize = Label(frmLocal, text=space) # create a label the size of the screen to allow for place
    lblAASize.pack(side="top", fill="both", expand=True)

#change font and size
def ChangeSize(item,font,size):
    item.config(font=(font,size))


def ItemSize():
    global array
    user32 = ctypes.windll.user32
    screenSize = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
    width = screenSize[0]
    height = screenSize[1]
    print(screenSize)
    multiplier = int(round(2160/height ,0))
    print(multiplier)
    baseSize = int(30 * (height / 1080))

    return multiplier, baseSize, height, width

def GetTypes():
    types = ["Movie", "Tv Show"]

    return types