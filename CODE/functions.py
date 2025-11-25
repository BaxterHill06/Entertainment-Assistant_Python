'''
 ____ ____ ____ ____ ____ ____
||B |||a |||x |||t |||e |||r ||
||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|
Version 13
last updated: 18/08/23
'''


from tkinter import *
import pandas as pd 
import ctypes
import tensorflow as tf 
import keras
import numpy as np
import matplotlib as plt
from keras import layers
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import csv


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
        # score the data for each set of data
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
    libGenreSplit = libGenre.split("/") # split the genre into two if there are 2
    inGenreSplit = inGenre.split("/") # split the genre into two if there are 2

    score = 0 # set score to 0 

    for inMovie in inGenreSplit: # loop through the genres entered
        for libMovie in libGenreSplit: # loop through the genres of the movie
            if inMovie.lower() == libMovie.lower():
                score += 2 # add two points if the genre is the same
            
    return score

def TypeSearch(libType, inType):
    score = 0
    if libType == inType:
        score += 4 # add 4 points if they arethe same type("Movie", "TV-Show")

    return score

def LengthSearch(libLength, inLength):
    score = 0

    libLength = int(libLength)
    try:
        inLength = int(inLength)
    except:
        inLength = 0
    
    if inLength == libLength:
        score += 10 # add 10 points if the lenth is exactly correct
    elif inLength * 0.9 <= libLength and inLength * 1.1 >= libLength: 
        score += 5 # add 5 points if the length is within 10%
    elif inLength * 0.8 <= libLength and inLength * 1.2 >= libLength:
        score += 4 # add 4 points if the length is within 20%
    elif inLength * 0.6 <= libLength and inLength * 1.4 >= libLength:
        score += 3 # add 5 points if the length is within 40%

    return score

def YearSearch(libYear, inYear):
    libYear = int(libYear)
    try:
        inYear = int(inYear)
    except:
        inYear = 0

    score = 0
    
    if inYear == libYear:
        score = 7 # add 7 points if it is the same year
    elif inYear + 5 <= libYear and inYear - 5 >= libYear:
        score = 6 # add 6 pointsx if it is within 5 years
    elif inYear + 10 <= libYear and inYear - 10 >= libYear:
        score = 5 # add 5 pointsx if it is within 10 years
    elif inYear + 20 <= libYear and inYear - 20 >= libYear:
        score = 4 # add 4 pointsx if it is within 20 years

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

def NeuralNetwork(dfUser, dfTestMovie):
    print(dfTestMovie, "test")
    dfUser = dfUser[["Genre","Type","Length","Year","Rating"]]
    dfUser = dfUser.replace({"Type": {"Movie": 0, "Tv-Show":1}})

    dfUserFix = pd.read_csv("Files/dfMovieTestFrame.CSV")
    dfUserFix = dfUserFix.drop(columns=["Title"])
    dfUserFix["Rating"] = ""
    
    for indexU, rowU in dfUser.iterrows(): # loop through each row of the data
        dfGenre = pd.read_csv("Files/Genre.CSV")

        try:
            gen = rowU["Genre"].split("/")
        except:
            gen = [rowU]
        for item in gen:
            dfGenre.at[0, item] = 1
        genre = (str(dfGenre.to_numpy().flatten()).strip("[").strip("]"))
        dfTemp = pd.DataFrame({"Genre":genre, "Type":rowU["Type"], "Length":rowU["Length"], "Year":rowU["Year"], "Rating":rowU["Rating"]}, index=["Genre"])
        dfTemp.to_csv("Files/dfTemp.CSV", quoting=csv.QUOTE_NONE, quotechar="",  escapechar=" ", index=False)
        dfTemp = pd.read_csv("Files/dfTemp.CSV")
        
        dfUserFix = pd.concat([dfUserFix, dfTemp])
    dfUserFix = dfUserFix.reset_index(drop=True)
    dfUserFix.to_csv("Files/dfTemp.CSV", index=False)

    print(dfUserFix, "df")


    # Extract the Genre column and convert it to a list of lists
    genre_values = dfUserFix["Genre"].apply(lambda x: list(map(int, x.split()))).tolist()

    # Convert the DataFrame to a NumPy array
    arTrainData = dfUserFix.drop("Genre", axis=1).values

    # Make sure the genre_values have the same number of columns as arTrainData
    genre_values = np.array(genre_values)

    # Insert the Genre values back into the array
    arTrainData = np.concatenate((genre_values, arTrainData), axis=1)

    
    arTrainRating = (np.array(dfUserFix["Rating"])).flatten()

    print(np.shape(arTrainData))
    print(np.shape(arTrainRating))

    print(arTrainData)
    print(arTrainRating)

    trainData, testData, trainRating, testRating = sklearn.model_selection.train_test_split(arTrainData, arTrainRating, test_size=0.1)

    #trainRating = trainRating.flatten()

    
    

    """
    linear = linear_model.LinearRegression()


    print(trainData)
    linear.fit(trainData, trainRating)
    acc = linear.score(testData, testRating)
    print(acc)
    """
    
    print("\n\n\n\n\n" , trainData)
        
    # Convert trainData to numpy.float32
    trainData = trainData.astype(np.float32)

    # Convert trainRating to numpy.int32
    trainRating = trainRating.astype(np.int32)

    # Convert trainData to numpy.float32
    testData = testData.astype(np.float32)

    # Convert trainRating to numpy.int32
    testRating = testRating.astype(np.int32)

    model = keras.Sequential([
    keras.layers.Input(shape=(trainData.shape[1],)),  # Input layer
    keras.layers.Dense(2000, activation="relu"),       # Hidden layer 1
    keras.layers.Dropout(0.3),
    keras.layers.Dense(1, activation="linear")        # Output layer
    ])

    optimizer = keras.optimizers.Adam(learning_rate=0.001)

    # Compile the model with Mean Squared Error (MSE) loss
    model.compile(optimizer=optimizer, loss="mean_squared_error", metrics=["accuracy"])

    # Train the model
    model.fit(trainData, trainRating, epochs=100, batch_size=32, validation_split=0.2)

    prediction = model.predict(testData)
    print(prediction)
    
    for i in range(len(prediction)):
        print(testRating[i], prediction[i-1])
    
    
    
    






    
    
