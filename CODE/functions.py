'''
 ____ ____ ____ ____ ____ ____
||B |||a |||x |||t |||e |||r ||
||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|
Version 12
last updated: 26/07/23
'''


from tkinter import *
import pandas as pd 
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


def SearchSort(inTitle,inGenre,inType,inLength,inYear):
    # collect the data from all the movies as a datafrmae
    dfMovies = pd.read_csv("files/Libary.csv")

    # create a 2-D array
    movieScores = []

    for index, row in dfMovies.iterrows(): # loop through each row of the data 
        libTitle = row["Title"]
        titleVal = TitleSearch(libTitle, inTitle)

        libGenre = row["Genre"]
        genreVal = GenreSearch(libGenre, inGenre)


        libType = row["Type"]
        typeVal = TypeSearch(libType, inType)

        libLength = row["Length"]
        lengthVal = LengthSearch(libLength, inLength)

        libYear = row["Year"]
        yearVal = YearSearch(libYear, inYear)

        movieScores.append([libTitle, titleVal + genreVal + typeVal + lengthVal + yearVal])
    movieScores.sort(key=lambda x: x[1], reverse=True) # sort by the score

    return movieScores



def TitleSearch(libTitle, inTitle):
    # split thee title into a list with the different words
    inTitleSplit = inTitle.split(" ")
    libTitleSplit = libTitle.split(" ")
    


    # create score variable
    score = 0

    
    for locIn in range(len(inTitleSplit)): # loop through each word from the input title
        partInTitle = inTitleSplit[locIn].lower()
        for locLib in range(len(libTitleSplit)): # loop through each word in the libary title
            partLibTitle = libTitleSplit[locLib].lower()
            if partLibTitle == partInTitle:
                if locIn == locLib: # if the word is in the same position give 2 points
                    score += 2
                else: # if the word is in a different position give 1 point
                    score += 1
            
    for locIn in range(len(inTitleSplit)): # loop through each word from the input title
        partInTitle = inTitleSplit[locIn].lower()
        if libTitle.lower().find(partInTitle) > -1:
            score += 1
    
    if inTitle == "": # remove free point from matching "" 
        score -= 1

    return score/1.7 # add scaling 


def GenreSearch(libGenre, inGenre):
    libGenreSplit = libGenre.split("/")
    inGenreSplit = inGenre.split("/")

    score = 0

    for inMovie in inGenreSplit:
        for libMovie in libGenreSplit:
            if inMovie.lower() == libMovie.lower():
                score += 2
            
    return score

def TypeSearch(libType, inType):
    score = 0
    if libType == inType:
        score += 4

    return score

def LengthSearch(libLength, inLength):
    libLengthSplit = str(libLength).split(".")
    inLengthSplit = str(inLength).split(".")

    libLengthMin = (int(libLengthSplit[0]) * 60) + int(libLengthSplit[1])
    try:
        inLengthMin = (int(inLengthSplit[0]) * 60) + int(inLengthSplit[1])
    except:
        inLengthMin = 0

    # note. float removes last decimal so 2.10 becomes 2 and 1 ( 120 + 1)
    # use if statment to check length of split[1] and times by 10

    score = 0
    
    if inLengthMin == libLengthMin:
        score += 10
    elif inLengthMin * 0.9 <= libLengthMin and inLengthMin * 1.1 >= libLengthMin:
        score += 5
    elif inLengthMin * 0.8 <= libLengthMin and inLengthMin * 1.2 >= libLengthMin:
        score += 4
    elif inLengthMin * 0.6 <= libLengthMin and inLengthMin * 1.4 >= libLengthMin:
        score += 3

    return score

def YearSearch(libYear, inYear):
    libYear = int(libYear)
    try:
        inYear = int(inYear)
    except:
        inYear = 0

    score = 0
    
    if inYear == libYear:
        score = 7
    elif inYear + 5 <= libYear and inYear - 5 >= libYear:
        score = 6
    elif inYear + 10 <= libYear and inYear - 10 >= libYear:
        score = 5
    elif inYear + 20 <= libYear and inYear - 20 >= libYear:
        score = 4

    return score
    

def RefreshImageFile():
    remove = [" ", "!", "@", "#", "$", "%", "-", "_", "(", ")"]

    
    df = pd.read_csv("files/Libary.csv")
    text = "from tkinter import *\ndef GlobalImageFile(selMovie):\n    global "
    for index, row in df.iterrows(): # loop through each row of the data
        name = row["Title"]
        for item in range(len(remove)):
            name = name.replace(remove[item], "")
        text += "img" + name + ", "
    text = text[:len(text)-2]


    # note. pass file name not title to ensure propper name used
    
    el = ""
    for index, row in df.iterrows(): # loop through each row of the data
        title = row["Title"]
        file = row["File"]
        name = title
        for item in range(len(remove)):
            name = name.replace(remove[item], "")
        text += "\n    img" + name + " = PhotoImage(file='Movie Covers/" + file + "')"
    for index, row in df.iterrows(): # loop through each row of the data
        title = row["Title"]
        file = row["File"]
        name = title
        for item in range(len(remove)):
            name = name.replace(remove[item], "")
        text += "\n    " + el + "if '" + title + "' == selMovie:\n        mov = img" + name
        el = "el"
        
    text += "\n    return mov"

    file = open("imageGlobal.py", "w")
    file.write(text)

         






    
    
