'''
 ____ ____ ____ ____ ____ ____
||B |||a |||x |||t |||e |||r ||
||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|
Version 5
last updated: 20/06/23
'''
from tkinter import *

# adds variables and returns them
def GetImages():
    plus = PhotoImage(file="plus.png")
    empLogo = PhotoImage(file="empty_logo.png")
    return (plus, empLogo)

def GatherIcons():
    icons = ["Joker","Kyle","Mando","Predator","R2","Smurf","Transformer","Yoda"]


    return icons
