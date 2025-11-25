'''
 ____ ____ ____ ____ ____ ____
||B |||a |||x |||t |||e |||r ||
||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|
Version 5
last updated: 25/06/23
'''

import pandas as pd


def ScreenSpace():
    file = open("LTscreen.txt","r")
    array = []
    for line in file:
        array.append(int(line.strip("\n")))

    
    space = "       "*array[0] + "\n"*array[1]
    return space



    
    

    
