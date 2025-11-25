'''
 ____ ____ ____ ____ ____ ____
||B |||a |||x |||t |||e |||r ||
||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|
Version 17
last updated: 27/09/23
'''

# import the external libraries
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
from operator import itemgetter


def ScreenSpace(x, y):
    global array
    # open screen size file
    file = open("ScreenSize.txt", "r")
    array = []
    for line in file: # save the details
        array.append(int(line.strip("\n")))

    space = " "*(array[0]*7-x) + "\n"*(array[1]-y) # create the space acording to the scrren size. -x and -y is to remove screen space for the bar
    file.close() # close the file
    return space

def ScreenFill(frmLocal, space):
    lblAASize = Label(frmLocal, text=space) # create a label the size of the screen to allow for place
    lblAASize.pack(side="top", fill="both", expand=True)

def ChangeSize(item,font,size):
    # change font and size
    item.config(font=(font,size))


def ItemSize():
    global array
    # get the screen size of the display
    user32 = ctypes.windll.user32
    screenSize = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
    width = screenSize[0]
    height = screenSize[1]

    # get the screen decrease factor for images
    multiplier = int(round(2160/height ,0))

    # get the base size for text
    baseSize = int(30 * (height / 1080))

    # return these values
    return multiplier, baseSize, height, width

def GetTypes():
    # create a list for movies or tv shows
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

        movieScores.append([libTitle, titleVal + genreVal + typeVal + lengthVal + yearVal]) # save the score to the title to a 2-d array
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
        score += 4 # add 4 points if they are the same type("Movie", "TV-Show")

    return score

def LengthSearch(libLength, inLength):
    score = 0

    libLength = int(libLength)
    try: # turn the length to an integer
        inLength = int(inLength)
    except: # else set it to 0
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
    try: # set the year to an intager
        inYear = int(inYear)
    except: # else set it to 0
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
    # create a list of banned characters
    remove = [" ", "!", "@", "#", "$", "%", "-", "_", "(", ")"]


    df = pd.read_csv("files/Libary.csv") # create a data frame with the movies in it
    # create a file to global the cover images
    text = "from tkinter import *\ndef GlobalImageFile(selMovie):\n    global "
    for index, row in df.iterrows(): # loop through each row of the data frame
        name = row["Title"]
        for item in range(len(remove)): # remove any banned characters
            name = name.replace(remove[item], "")
        text += "img" + name + ", "
    text = text[:len(text)-2]  # remove last ","

    #initiate el
    el = ""
    for index, row in df.iterrows(): # loop through each row of the data frame
        title = row["Title"]
        file = row["File"]
        name = title
        for item in range(len(remove)):
            name = name.replace(remove[item], "") # remove any banned characters
        text += "\n    img" + name + " = PhotoImage(file='Movie Covers/" + file + "')"
    for index, row in df.iterrows(): # loop through each row of the data
        title = row["Title"]
        file = row["File"]
        name = title
        for item in range(len(remove)):
            name = name.replace(remove[item], "") # remove any banned characters
        text += "\n    " + el + "if '" + title + "' == selMovie:\n        mov = img" + name # create an if statement for the file
        el = "el"
        
    text += "\n    return mov" # add the returm mov

    file = open("imageGlobal.py", "w") # open the file
    file.write(text) # write to the file
    file.close() # close the file

def NeuralNetwork(dfUser, dfTestMovie):
    print(dfTestMovie, "test")
    # create a data frame with the movie details
    dfUser = dfUser[["Genre","Type","Length","Year","Rating"]]
    dfUser = dfUser.replace({"Type": {"Movie": 0, "Tv-Show":1}})

    # create a new data frame
    dfUserFix = pd.read_csv("Files/dfMovieTestFrame.CSV")
    dfUserFix = dfUserFix.drop(columns=["Title"])
    dfUserFix["Rating"] = ""
    
    for indexU, rowU in dfUser.iterrows(): # loop through each row of the data frame
        dfGenre = pd.read_csv("Files/Genre.CSV")

        try: # try to split the genres into an array
            gen = rowU["Genre"].split("/")
        except: # else only one genre, create an array with just the one genre
            gen = [rowU]
        for item in gen: # turn 0 to 1 for the genre in the movie
            dfGenre.at[0, item] = 1

        genre = (str(dfGenre.to_numpy().flatten()).strip("[").strip("]")) # covert to string

        # create a temporary data frame and save to file
        dfTemp = pd.DataFrame({"Genre":genre, "Type":rowU["Type"], "Length":rowU["Length"], "Year":rowU["Year"], "Rating":rowU["Rating"]}, index=["Genre"])
        dfTemp.to_csv("Files/dfTemp.CSV", quoting=csv.QUOTE_NONE, quotechar="",  escapechar=" ", index=False)
        dfTemp = pd.read_csv("Files/dfTemp.CSV")

        # concatenate the two data frames into one
        dfUserFix = pd.concat([dfUserFix, dfTemp])
    dfUserFix = dfUserFix.reset_index(drop=True) # remove the index

    # convert the data frame to a numpy array
    arTrainRating = (np.array(dfUserFix["Rating"])).flatten()

    # remove Rating
    dfUserFix = dfUserFix.drop(columns=["Rating"])

    # Extract the Genre column and convert it to a list of lists
    genre_values = dfUserFix["Genre"].apply(lambda x: list(map(int, x.split()))).tolist()

    # Convert the DataFrame to a NumPy array
    arTrainData = dfUserFix.drop("Genre", axis=1).values

    # Make sure the genre_values have the same number of columns as arTrainData
    genre_values = np.array(genre_values)

    # Insert the Genre values back into the array
    arTrainData = np.concatenate((genre_values, arTrainData), axis=1)
        
    # Convert trainData to numpy.float32
    trainData = arTrainData.astype(np.float32)

    # Convert trainRating to numpy.int32
    trainRating = arTrainRating.astype(np.int32)


    model = keras.Sequential([
    keras.layers.Input(shape=(trainData.shape[1],)),  # Input layer
    keras.layers.Dense(20, activation="relu"),       # Hidden layer 1
    keras.layers.Dropout(0.3),
    keras.layers.Dense(1, activation="linear")        # Output layer
    ])

    # create an optimizer for the neural network
    optimizer = keras.optimizers.Adam(learning_rate=0.001)

    # Compile the model with Mean Squared Error (MSE) loss
    model.compile(optimizer=optimizer, loss="mean_squared_error", metrics=["accuracy"])

    # Train the model
    try: # try to create the network
        # create the model with the training data
        model.fit(trainData, trainRating, epochs=100, batch_size=32, validation_split=0.2)


        arPrediction = NetworkPrediction(model, dfTestMovie) # input the model and test data frmae, output an array with the scores
    except: # else the predictions is set to 0
        arPrediction = 0

    # return predictions
    return arPrediction

def NetworkPrediction(model, dfTestMovie):
    # create a data frame without the title
    dfTest = dfTestMovie.drop(columns=["Title"])
    dfTest = dfTest.replace({"Type": {"Movie": 0, "Tv-Show":1}}) # replace the movie and tv-show with 0 or 1


    # Extract the Genre column and convert it to a list of lists
    genre_values = dfTest["Genre"].apply(lambda x: list(map(int, x.split()))).tolist()

    # Convert the DataFrame to a NumPy array
    arTestData = dfTest.drop("Genre", axis=1).values

    # Make sure the genre_values have the same number of columns as arTrainData
    genre_values = np.array(genre_values)

    # Insert the Genre values back into the array
    arTestData = np.concatenate((genre_values, arTestData), axis=1)
    
    # Convert trainData to numpy.float32
    testData = arTestData.astype(np.float32)

    # make a prediction for the movies using the network
    prediction = model.predict(testData)

    # covert into a list
    prediction = list(prediction)

    arPrediction = []
    for loc in range(len(prediction)): # for each prediction convert into a float
        arPrediction.append([(float(str(prediction[loc]).strip("[").strip("]"))), dfTestMovie.loc[loc,"Title"]]) # append the value from the network

    arPrediction = sorted(arPrediction, key=lambda x:x[0]) # sort the values in ascending order

    # reverse to be descending order
    arPrediction.reverse()

    return arPrediction # return the array


def LoadingScreen(window, multiplier, mainWidth, topWidth, mainHeight, topHeight):
    # create the loading screen frame
    frmLoadingScreen = Frame(window, width=mainWidth + topWidth, height=mainHeight + topHeight)

    # create and resize the image
    imgLoading = PhotoImage(file="Menu/loading.gif")
    imgLSLoading = imgLoading.subsample(multiplier)

    # create the loading label
    lblLoad = Label(frmLoadingScreen, image=imgLSLoading)
    lblLoad.place(relx=0.5, rely=0.5, anchor="center")

    # grid the frame
    frmLoadingScreen.grid()

    return frmLoadingScreen

    
    
