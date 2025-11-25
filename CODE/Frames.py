'''
 ____ ____ ____ ____ ____ ____
||B |||a |||x |||t |||e |||r ||
||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|
Version 17
last updated: 27/09/23
'''



# import external libraries
from tkinter import *
from Images import *
from functions import *
import pandas as pd
import PIL
from PIL import Image, ImageTk
from tkinter import ttk
#from imageGlobal import *
import tensorflow as tf 
from tensorflow import keras
import numpy as np
import matplotlib as plt
import os
import datetime


def GetImages():
    global imgPlus,imgEmpLogo, imgRefresh, imgCamera, imgSmurf, imgJoker, imgKyle, imgMando, imgPredator, imgR2, imgTransformer, imgYoda, imgHomer, imgHedwig, imgGrinch, imgDarthVader, imgC3PO, imgBlackPanther, imgBook, imgClock, imgExit, imgHeart, imgHouse, imgMagGlass, imgMenuPlus,imgRightArrow, imgLeftArrow, imgEmptyCover, imgDownArrow, imgUpArrow
    # save the images to these variables to be used on screen
    imgPlus = PhotoImage(file="plus.png")
    imgEmpLogo = PhotoImage(file="empty_logo.png")

    imgSmurf = PhotoImage(file="icons/Smurf.png")
    imgJoker = PhotoImage(file="icons/Joker.png")
    imgKyle = PhotoImage(file="icons/Kyle.png")
    imgMando = PhotoImage(file="icons/Mando.png")
    imgPredator = PhotoImage(file="icons/Predator.png")
    imgR2 = PhotoImage(file="icons/R2.png")
    imgTransformer = PhotoImage(file="icons/Transformer.png")
    imgYoda = PhotoImage(file="icons/Yoda.png")
    imgHomer = PhotoImage(file="icons/Homer.png")
    imgHedwig = PhotoImage(file="icons/Hedwig.png")
    imgGrinch = PhotoImage(file="icons/Grinch.png")
    imgDarthVader = PhotoImage(file="icons/Darth Vader.png")
    imgC3PO = PhotoImage(file="icons/C-3PO.png")
    imgBlackPanther = PhotoImage(file="icons/Black Panther.png")

    imgBook = PhotoImage(file="Menu/book.png")
    imgClock = PhotoImage(file="Menu/clock.png")
    imgExit = PhotoImage(file="Menu/exit.png")
    imgHeart = PhotoImage(file="Menu/heart.png")
    imgHouse = PhotoImage(file="Menu/House.png")
    imgMagGlass = PhotoImage(file="Menu/Magnifying glass.png")
    imgMenuPlus = PhotoImage(file="Menu/Plus.png")
    imgCamera = PhotoImage(file="Menu/camera.png")

    imgRightArrow = PhotoImage(file="arrow Right.png")
    imgLeftArrow = PhotoImage(file="arrow Left.png")
    imgDownArrow = PhotoImage(file="arrow Down.png")
    imgUpArrow = PhotoImage(file="arrow Up.png")

    imgEmptyCover = PhotoImage(file="Movie Covers/Empty Cover.png")

    imgRefresh = PhotoImage(file="refresh.png")



def ExitCreate(window):
    # create Exit button
    menuBar = Menu(window)
    topBar = Menu(menuBar,tearoff=0)
    topBar.add_command(label="Exit", command=window.destroy)
    menuBar.add_cascade(label="Exit", menu=topBar)
    window.config(menu=menuBar)

def InitiateFrames():
    global frmLogin, frmMatchScroll, frmHomeRec, frmHomeHigh, frmAccountLogin, frmMovieBox, frmAddAccount, frmSearchTop, frmSearch, frmShowInfo, frmShowInfoTop, frmHomeTop, frmHome, frmReviewTop, frmReview, frmMatchTop, frmMatch, frmWatchLaterTop, frmWatchLater, frmAddShowTop, frmAddShow
    # initialize the frames
    frmLogin = ""
    frmAccountLogin = ""
    frmAddAccount = ""
    frmSearchTop = ""
    frmSearch = ""
    frmHomeTop = ""
    frmHome = ""
    frmReviewTop = ""
    frmReview = ""
    frmMatchTop = ""
    frmMatch = ""
    frmWatchLaterTop = ""
    frmWatchLater = ""
    frmAddShowTop = ""
    frmAddShow = ""
    frmShowInfo = ""
    frmShowInfoTop = ""
    frmMovieBox = ""
    frmMatchScroll = ""
    frmHomeRec = ""
    frmHomeHigh = ""


def ClearScreens():
    # try to clear all frames on screen
    global frmLogin ,frmAccountLogin,frmHomeRec, frmHomeHigh, frmMatchScroll, frmSearchTop, frmSearch, frmShowInfo, frmShowInfoTop, frmHomeTop, frmHome, frmReviewTop, frmReview, frmMatchTop, frmMatch, frmWatchLaterTop, frmWatchLater, frmAddShowTop, frmAddShow
    # place all frames into an array
    frames = [frmLogin, frmMatchScroll, frmMovieBox, frmAccountLogin, frmAddAccount, frmSearchTop, frmSearch, frmHomeTop, frmHome, frmReviewTop, frmReview, frmMatchTop, frmMatch, frmWatchLaterTop, frmWatchLater, frmAddShowTop, frmAddShow, frmShowInfo, frmShowInfoTop]
    for frame in frames: # loop through each frame
        try: # try to grid forget it
            frame.grid_forget()
        except: # if it can not then nothing happens
            pass




def LoginCreate(win,spa,screenPage):
    global frmLogin,imgPlus,window,space, multiplier, baseSize, imgLGPlus, height, width, accountInfo
    #def window and space so they can be globaled for other functions
    window = win
    space = spa

    # destroy any previous versions of the login screen
    try:
        frmLogin.destroy()
    except:
        pass

    # gather text and image size for screen
    multiplier, baseSize, height, width = ItemSize()


    #create Frame
    frmLogin = Frame(window, width=width, height=height-20)


    # create heading
    lblLGLogin = Label(frmLogin,text="LOGIN")
    ChangeSize(lblLGLogin,'Helvetica bold', baseSize*3)
    lblLGLogin.place(relx=0.5, rely=0.07, anchor="center")

    # resize image
    imgLGPlus = imgPlus.subsample(multiplier)

    # create ADD button
    btnLGAdd = Button(frmLogin,image=imgLGPlus, command=AddAccountLoad, highlightthickness = 0, bd = 0)
    btnLGAdd.place(relx=0.8, rely=0.61, anchor= "center")

    #add a label under the plus symbol
    lblLGAdd = Label(frmLogin, text="ADD")
    ChangeSize(lblLGAdd,'Helvetica bold', baseSize)
    lblLGAdd.place(relx=0.8, rely=0.82, anchor="center")

    # Open the Account file account logos
    accountFile = open("UserFile.csv","r")

    #create an array with the users infomation in form of: ["Username,Password,Icon,File","Username,Password,Icon,File"]
    #note: this is not a 2D array, just seperate stings
    accountInfo = []
    for line in accountFile: # run through the file and save to an array
        accountInfo.append(line.strip("\n"))
    print(accountInfo)
    for element in range(len(accountInfo)-1): # looping through each part of list
        #note: uses minus 1 to counter the first line with the headings
        # +1 to skip the heading
        accountElements = accountInfo[element+1].split(",")
        accountUsername = accountElements[0]
        accountPassword = accountElements[1]
        accountIcon = accountElements[2]
        LoginIconCreate(accountUsername,accountPassword,accountIcon,element, screenPage)
    # load the loading screen
    LoginLoad()



def LoginIconCreate(accountUsername,accountPassword, accountIcon,element, screenPage):
    global baseSize,multiplier, imgLGLeftArrow, imgLGRightArrow, accountInfo, frmLogin, localIcon,window, space, imgSmurf, imgJoker, imgKyle, imgMando, imgPredator, imgR2, imgTransformer, imgYoda, imgHomer, imgHedwig, imgGrinch, imgDarthVader, imgC3PO, imgBlackPanther, imgRightArrow, imgLeftArrow
    if accountIcon == "Smurf": # checks what the icon selected is and save the image to a variable
        imageFile = imgSmurf
    elif accountIcon == "Joker":
        imageFile = imgJoker
    elif accountIcon == "Kyle":
        imageFile = imgKyle
    elif accountIcon == "Mando":
        imageFile = imgMando
    elif accountIcon == "Predator":
        imageFile = imgPredator
    elif accountIcon == "R2":
        imageFile = imgR2
    elif accountIcon == "Transformer":
        imageFile = imgTransformer
    elif accountIcon == "Yoda":
        imageFile = imgYoda
    elif accountIcon == "Homer":
        imageFile = imgHomer
    elif accountIcon == "Hedwig":
        imageFile = imgHedwig
    elif accountIcon == "Grinch":
        imageFile = imgGrinch
    elif accountIcon == "Darth Vader":
        imageFile = imgDarthVader
    elif accountIcon == "C-3PO":
        imageFile = imgC3PO
    elif accountIcon == "Black Panther":
        imageFile = imgBlackPanther
    else:
        imageFile = imgEmpLogo

    page = (element // 3) + 1 # returns the page value by determining the remainder and adding 1
    section = (element % 3) + 1 # returns the section by determining the quotient and adding 1

    # adjust the image based on the screen size
    imageFile = imageFile.subsample(multiplier)


    #Create the button with the logo
    if page == screenPage:
        btnLGAccount = Button(frmLogin,image=imageFile, highlightthickness = 0, bd = 0, command= lambda name = accountUsername, password = accountPassword,icon = imageFile:AccountLoginLoad(name,password,icon))
        btnLGAccount.place(relx=section * 0.2, rely=0.61,anchor="center") # place the button based on the section
        lblLGAccount = Label(frmLogin,text=accountUsername)# create the label wit hthe username
        ChangeSize(lblLGAccount, 'Helvetica bold', baseSize) # change the font and size
        lblLGAccount.place(relx=section * 0.2, rely=0.82,anchor="center") # place below the logo
    else:
        pass

    #resize buttons
    imgLGLeftArrow = imgLeftArrow.subsample(multiplier)
    imgLGRightArrow = imgRightArrow.subsample(multiplier)

    # create side buttons to slide through the users
    if screenPage != 1:
        btnLGLeft = Button(frmLogin,image=imgLGLeftArrow, highlightthickness = 0, bd = 0, command= lambda window=window, space=space, screenPage=screenPage + -1:LoginCreate(window,space,screenPage))
        btnLGLeft.place(relx=0.05, rely=0.61, anchor="center")
    if (((len(accountInfo)-2) // 3) +1 ) != screenPage:
        btnLGRight = Button(frmLogin,image=imgLGRightArrow, highlightthickness = 0, bd = 0, command= lambda window=window, space=space, screenPage=screenPage + 1:LoginCreate(window,space,screenPage))
        btnLGRight.place(relx=0.95, rely=0.61, anchor="center")



def LoginLoad():
    global frmAddAccount, frmBar, frmLogin, frmHome
    #forget the other screens that could be on screen
    ClearScreens()
    try: # insures the software still runs if the frame has not been created yet
        frmBar.grid_forget()
    except:
        pass

    #load the Login screen
    frmLogin.grid()


def AddAccountCreate():
    global frmAddAccount,imgEmpLogo, lblAAError, baseSize, multiplier, selAAIcon,lblAALogo, window, space, baseSize, multiplier, imgAAEmpLogo, height, width
    frmAddAccount = Frame(window, width=width-20, height=height-35)
    
    #resizing the empty icon image
    imgAAEmpLogo = imgEmpLogo.subsample(multiplier)

    # gathering the array with the icons for dropdown box
    icons = GatherIcons()
    
    
    #create logo image
    lblAALogo = Label(frmAddAccount, image=imgAAEmpLogo)
    lblAALogo.place(relx=0.42, rely=0.05)

    # create a select icon label
    lblAAicon = Label(frmAddAccount, text="SELECT ICON")
    ChangeSize(lblAAicon,'Helvetica bold', int(baseSize))
    lblAAicon.place(relx=0.65, rely=0.1, anchor="center")

    #add dropdown for selection icon
    selAAIcon = StringVar()
    dropAALogo = OptionMenu(frmAddAccount, selAAIcon , *icons,)
    dropAALogo.config(width=int(13/multiplier),height=int(2/multiplier))
    ChangeSize(dropAALogo,'Helvetica bold', baseSize)
    dropAALogo.place(relx=0.65, rely=0.15, anchor="center")
    

    # add a load button for the icon
    btnAASelect = Button(frmAddAccount, text="Load", command=IconConfigure)
    ChangeSize(btnAASelect,'Helvetica bold', int(baseSize))
    btnAASelect.place(relx=0.66, rely=0.26, anchor="center")

    #add "create username" label and entry
    lblAAUsername = Label(frmAddAccount, text="CREATE USERNAME")
    ChangeSize(lblAAUsername,'Helvetica bold', baseSize)
    lblAAUsername.place(relx=0.5,rely=0.43,anchor="center")

    entAAUsername = Entry(frmAddAccount)
    ChangeSize(entAAUsername,'Helvetica bold',baseSize)
    entAAUsername.place(relx=0.5,rely=0.5,anchor="center")



    #add "create password" label and entry
    lblAAPassword = Label(frmAddAccount, text="CREATE PASSWORD")
    ChangeSize(lblAAPassword,'Helvetica bold', baseSize)
    lblAAPassword.place(relx=0.5,rely=0.65,anchor="center")

    entAAPassword = Entry(frmAddAccount)
    ChangeSize(entAAPassword,'Helvetica bold',baseSize)
    entAAPassword.place(relx=0.5,rely=0.72,anchor="center")

    # error label
    lblAAError = Label(frmAddAccount, text="", fg="red")
    ChangeSize(lblAAError,'Helvetica bold', baseSize)
    lblAAError.place(relx=0.5,rely=0.79,anchor="center")


    #add "CREATE" button
    btnAACreate = Button(frmAddAccount,text="CREATE", command= lambda username=entAAUsername, password=entAAPassword, icon=selAAIcon : CreateAccount(username,password,icon))
    #btnAACreate.config(width=30,heigh=8)
    ChangeSize(btnAACreate, 'Helvetica bold',baseSize*2)
    btnAACreate.place(relx=0.5, rely=0.9,anchor="center")

    # create back button
    btnAABack = Button(frmAddAccount, command=LoginLoad, text="BACK")
    ChangeSize(btnAABack, 'Helvetica bold', baseSize)
    btnAABack.place(rely=0.95, relx=0.05, anchor='sw')

#crate the users new account
def CreateAccount(username, password, icon):
    global window, space, lblAAError
    username = username.get()
    password = password.get()
    icon = icon.get()

    # create a dataframe with the current account details
    userFile = pd.read_csv("UserFile.csv")

    # loop through each account to check if the account name is already in use
    same = False
    for index, row in userFile.iterrows(): # loop through each row
        if username == row["Username"]: # check if the username is the same as the useranme from that row
            same = True # if so se to true
        # repeat for all rows

    # check if all entries meet requirements:
    if icon == "": # if the icon is empty, config the following message
        lblAAError.config(text="Please select an Icon")
    elif username == "": # if the username is empty, config the following message
        lblAAError.config(text="Please enter a Username")
    elif password == "": # if the password is empty, config the following message
        lblAAError.config(text="Please enter a Password")
    elif same == True: # if the username is already in use, config the following message
        lblAAError.config(text="Please enter a Unique Username")
    else: # if non of the if statements are true, save the details
        # add account info to a csv file
        addArray = pd.DataFrame({"Username":username,"Password":password,"Icon":icon,"File":username + ".csv"},index=[username])
        userFile = pd.concat([userFile,addArray])
        userFile.to_csv("UserFile.csv",index=False)
        # create user folder
        folder = './' + 'User Files/' + username
        os.mkdir(folder)

        # create two dedicated files for the user to save their preferences into
        userSpecificFile = open("User Files/" + username + "/" + username + ".csv", "w")
        userSpecificFile.write("Title,Genre,Type,Length,Year,Rating")
        userSpecificFile = open("User Files/" + username + "/" + username + "WatchLater.csv", "w")
        userSpecificFile.write("Title,Genre,Type,Length,Year,Rating")
        userSpecificFile.close()

        LoginCreate(window,space,1)
        LoginLoad()


#change the image on screen to the icon selected by the user
def IconConfigure():
    global selAAIcon, lblAALogo,iconFile, multiplier
    # gather the name of the icon
    iconPath = "icons/" + selAAIcon.get() + ".png"
    # collect the image of the icon
    iconFile = PhotoImage(file=iconPath)
    #resize the image
    iconFile = iconFile.subsample(multiplier)
    #configure the label with the image
    lblAALogo.config(image=iconFile)


def AddAccountLoad():
    global frmAddAccount,frmLogin
    #forget the other screens that could be on screen
    ClearScreens()

    AddAccountCreate()
    #load the Login screen
    frmAddAccount.grid()


def AccountLoginCreate():
    global window, space, baseSize, imgEmpLogo, lblALMessage, frmAccountLogin, lblALLogo,lblALUsername, btnALLogin, entALPassword, height, width
    frmAccountLogin = Frame(window, height=height-20, width=width-35) # create the frame to place elements into

    # create logo label
    lblALLogo = Label(frmAccountLogin,image=imgEmpLogo)
    lblALLogo.place(relx=0.5, rely=0.15, anchor="center")

    # crate name label
    lblALUsername = Label(frmAccountLogin, text="")
    ChangeSize(lblALUsername,'Helvetica bold', baseSize)
    lblALUsername.place(relx=0.5 , rely=0.3, anchor="center")

    # create label and entry for password
    lblALPassword = Label(frmAccountLogin,text="ENTER PASSWORD:")
    ChangeSize(lblALPassword,'Helvetica bold', baseSize*2)
    lblALPassword.place(relx=0.5, rely=0.45, anchor="center")

    entALPassword = Entry(frmAccountLogin, width=25)
    ChangeSize(entALPassword, 'Helvetica bold', int(baseSize*1.666))
    entALPassword.place(relx=0.5, rely=0.58, anchor="center")

    # label to show any errors e.g. wrong password
    lblALMessage = Label(frmAccountLogin, text="", fg="red")
    ChangeSize(lblALMessage,'Helvetica bold', baseSize)
    lblALMessage.place(relx=0.5, rely=0.7, anchor="center")

    #create "LOGIN" Button
    btnALLogin = Button(frmAccountLogin,text="LOGIN", height=2, width=15)
    ChangeSize(btnALLogin, 'Helvetica bold', baseSize)
    btnALLogin.place(relx=0.5, rely=0.8, anchor="center")

    # create back button
    btnALBack = Button(frmAccountLogin, command=LoginLoad, text="BACK")
    ChangeSize(btnALBack, 'Helvetica bold', baseSize)
    btnALBack.place(rely=0.95, relx=0.05, anchor='sw')


def AccountLoginLoad(accountUsername, accountPassword, accountIcon):
    global frmAccountLogin, frmLogin,lblALLogo,lblALUsername,btnALLogin, multiplier, imgALLogo, imgSmurf, imgJoker, imgKyle, imgMando, imgPredator, imgR2, imgTransformer, imgYoda, imgHomer, imgHedwig, imgGrinch, imgDarthVader, imgC3PO, imgBlackPanther
    # forget previous frames
    ClearScreens()

    # create the account login screen
    AccountLoginCreate()

    # save the account icon to the variable imgALLogo
    imgALLogo = accountIcon

    # configure the logo with the users logo
    lblALLogo.config(image=imgALLogo)

    # configure name label
    lblALUsername.config(text=accountUsername)

    # configure button to pass through account info
    btnALLogin.config(command= lambda name = accountUsername, password = accountPassword:LoginAttempt(name, password))

    # grid new frame
    frmAccountLogin.grid()


def LoginAttempt(accountUsername,accountPassword):
    global entALPassword, lblALMessage, accountUsernameG, accountPassswordG
    # save the account details to a new variable to be made global
    accountUsernameG = accountUsername
    accountPasswordG = accountPassword
    passwordAttempt = entALPassword.get() # get the entered password
    entALPassword.delete(0,END)
    if passwordAttempt == accountPassword: # check if the entered password matches the set password
        BarCreate() # if correct opens next screen
    else: # if incorrect displays Incorrect password
        # add data validation. if empty( please enter a password)
        lblALMessage.config(text="Incorrect Password")



def BarCreate():
    global window, frmBar, multiplier, height, width, imgBook, imgClock, imgExit, imgHeart, imgHouse, imgMagGlass,imgMenuPlus, imgBRBook, imgBRClock, imgBRExit, imgBRHeart, imgBRHouse, imgBRMagGlass, imgBRPlus
    frmBar = Frame(window, highlightbackground="black", highlightthickness=1) # create side bar frame

    # adjust icon size based on screen size
    imgBRMagGlass = imgMagGlass.subsample(multiplier)
    imgBRHouse = imgHouse.subsample(multiplier)
    imgBRBook = imgBook.subsample(multiplier)
    imgBRHeart = imgHeart.subsample(multiplier)
    imgBRClock = imgClock.subsample(multiplier)
    imgBRPlus = imgMenuPlus.subsample(multiplier)
    imgBRExit = imgExit.subsample(multiplier)





    # create and pack menu buttons
    btnBRSearch = Button(frmBar, image=imgBRMagGlass,command=SearchLoad, highlightthickness = 0, bd = 0)
    btnBRSearch.pack()
    btnBRHome = Button(frmBar, image=imgBRHouse,command=HomeLoad, highlightthickness = 0, bd = 0)
    btnBRHome.pack()
    btnBRReview = Button(frmBar, image=imgBRBook, command=ReviewLoad, highlightthickness=0, bd=0)
    btnBRReview.pack()
    btnBRMatch = Button(frmBar, image=imgBRHeart, command=MatchLoad, highlightthickness=0, bd=0)
    btnBRMatch.pack()
    btnBRLater = Button(frmBar, image=imgBRClock, command=WatchLaterLoad, highlightthickness=0, bd=0)
    btnBRLater.pack()
    btnBRAdd = Button(frmBar, image=imgBRPlus, command=AddShowLoad, highlightthickness=0, bd=0)
    btnBRAdd.pack()
    btnBRExit = Button(frmBar, image=imgBRExit, command=LoginLoad, highlightthickness=0, bd=0)
    btnBRExit.pack()

    HomeCreate(1,1)

def HomeCreate(recLoc, highLoc):
    global window, frmHome, accountUsernameG, baseSize, multiplier, dfMovies, dfUser, bottomSpace, topSpace, frmHomeTop, height, width, topWidth, mainWidth, topHeight, mainHeight
    #  create variables with specific size for  the top bar and main screen
    topHeight = (height - 20) / 11
    topWidth = ((width) / 13) * 12
    mainHeight = ((height - 20) / 12) * 11
    mainWidth = ((width) / 13) * 12

    # create the data frame with the movie data in it
    dfMovies = pd.read_csv("files/Libary.csv")
    dfUser = pd.read_csv("User Files/" + accountUsernameG + "/" + accountUsernameG + ".csv")

    # create frames
    frmHome = Frame(window, height=mainHeight, width=mainWidth)
    frmHomeTop = Frame(window, highlightbackground="black", highlightthickness=1, height=topHeight, width=topWidth)

    # create heading
    lblHOTTitle = Label(frmHomeTop,text="HOME")
    ChangeSize(lblHOTTitle, 'Helvetica bold',int(baseSize*1.5))
    lblHOTTitle.place(relx=0.01, rely=0.06, anchor="nw")

    # load the recommended and high rated movies
    HomeRec(1)
    HomeHigh(1)

    # create menu items
    CreateMenus()


def HomeRec(recLoc):
    global dfMovies, cov, frmHomeRec, mainWidth, mainHeight, frmHome

    
    dfRec = ((dfMovies[len(dfMovies)-20:]).iloc[::-1]).reset_index() # get the last 20 movies added and save them to dfRec

    # create and grid the recent frame
    frmHomeRec = Frame(frmHome, width=mainWidth, height= int(mainHeight/2))
    frmHomeRec.grid(row=1, column=1)

    # create the title
    lblHORecent = Label(frmHomeRec, text="Recently Added")
    ChangeSize(lblHORecent, 'Helvetica bold', int(baseSize))
    lblHORecent.place(relx=0.05, rely=0,anchor="nw")

    for index, row in dfRec.iterrows(): # loop through each row of the data
        title = row["Title"]
        try:
            cover = (PhotoImage(file="Movie Covers/" + title + ".png")) # save the image to cover if it exists
        except:
            cover = (PhotoImage(file="Movie Covers/Empty Cover.png")) # else use empty image
        HomeRecPlace(title, index, cover, recLoc) # place the details

def HomeRecPlace(title, index, cover, recLoc):
    global multiplier, frmHomeRec, cov, imgHORLeftArrow, imgLeftArrow, imgHORRightArrow, imgRightArrow
    print(index)
    page = ((index // 5) + 1)

    if page == recLoc: # if the displayed page is equal to the page of the movie
        cov = cover.subsample(int(multiplier*1.7)) # resize the image

        # create button with the image
        btnHORImg = Button(frmHomeRec, image=cov, command= lambda selMovie = title:ShowInfoCreate(selMovie))
        btnHORImg.place(relx=(0.18 * (index % 5) ) + 0.14, rely= 0.5, anchor="center")

        # create a label with the title
        lblHORTitle = Label(frmHomeRec, text=title)
        ChangeSize(lblHORTitle,'Helvetica bold', int(baseSize*0.4))
        lblHORTitle.place(relx=(0.18 * (index % 5) ) + 0.14, rely= 0.9, anchor="center")

    # resize the arrows
    imgHORLeftArrow = imgLeftArrow.subsample(multiplier)
    imgHORRightArrow = imgRightArrow.subsample(multiplier)

    if recLoc != 1: # if the screen is not on the first page then place the left button
        btnHORArrowLeft = Button(frmHomeRec, image=imgHORLeftArrow, command = lambda recLoc = recLoc: HomeRec(recLoc-1))
        btnHORArrowLeft.place(relx=0.04, rely=0.5, anchor = "center")

    if recLoc != 4: # if the page is not on the fourth page then place the right button
        btnHORArrowRight = Button(frmHomeRec, image=imgHORRightArrow, command = lambda recLoc = recLoc: HomeRec(recLoc+1))
        btnHORArrowRight.place(relx=0.96, rely=0.5, anchor = "center")

def HomeHigh(highLoc):
    global dfMovies, frmHomeHigh, frmHome

    # save the average ratings of each movie
    GetAverageRating()

    # create the frame
    frmHomeHigh = Frame(frmHome, width=mainWidth, height= int(mainHeight/2))
    frmHomeHigh.grid(row=2, column=1)

    # # create the heading
    lblHOHigh = Label(frmHomeHigh, text="Highly Rated")
    ChangeSize(lblHOHigh, 'Helvetica bold', int(baseSize))
    lblHOHigh.place(relx=0.05, rely=0,anchor="nw")


    dfHigh = dfMovies.sort_values("Rating") # sort the dataframe by the rating
    dfHigh = dfHigh[(len(dfHigh)) - 20:] # save the last 20 movies
    for index, row in dfHigh.iterrows(): # loop through each row of the data
        title = row["Title"]
        try:
            cover = (PhotoImage(file="Movie Covers/" + title + ".png")) # save the image to cover if it exists
        except:
            cover = (PhotoImage(file="Movie Covers/Empty Cover.png")) # else use empty image
        HomeHighPlace(title, index, cover, highLoc) # place the details
    

def HomeHighPlace(title, index, cover, highLoc):
    global frmHomeHigh, imgRightArrow, imgLeftArrow, cov, imgHOHLeftArrow, imgHOHRightArrow

    page = ((index // 5) + 1)
    if page == highLoc:# if the displayed page is equal to the page of the movie
        cov = cover.subsample(int(multiplier*1.7))# resize the image

        # create button with the image
        btnHOHImg = Button(frmHomeHigh, image=cov, command= lambda selMovie = title:ShowInfoCreate(selMovie))
        btnHOHImg.place(relx=(0.18 * (index % 5) ) + 0.14, rely= 0.5, anchor="center")

        # create a label with the title
        lblHOHTitle = Label(frmHomeHigh, text=title)
        ChangeSize(lblHOHTitle,'Helvetica bold', int(baseSize*0.4))
        lblHOHTitle.place(relx=(0.18 * (index % 5) ) + 0.14, rely= 0.9, anchor="center")

    # resize the arrows
    imgHOHLeftArrow = imgLeftArrow.subsample(multiplier)
    imgHOHRightArrow = imgRightArrow.subsample(multiplier)

    if highLoc != 1: # if the screen is not on the first page then place the left button
        btnHOHArrowLeft = Button(frmHomeHigh, image=imgHOHLeftArrow, command = lambda highLoc = highLoc: HomeHigh(highLoc-1))
        btnHOHArrowLeft.place(relx=0.04, rely=0.5, anchor = "center")

    if highLoc != 4:  # if the page is not on the fourth page then place the right button
        btnHOHArrowRight = Button(frmHomeHigh, image=imgHOHRightArrow, command = lambda highLoc = highLoc: HomeHigh(highLoc+1))
        btnHOHArrowRight.place(relx=0.96, rely=0.5, anchor = "center")

    


    
def GetAverageRating():# average the ratings
    # open the user file
    userFile = open("UserFile.csv", "r")
    
    
    users = []
    for line in userFile: # create an array with the usernames
        print(line, "line")
        line = line.split(",")
        print(line, "line2")
        users.append(line[0])
    users = users[1:]
    print(users)

    for indexMov, rowMov in dfMovies.iterrows(): # loop through each row of the data frame
        score = 0
        count = 0
        for name in users:# loop through each user
            print("\n\n\n", users)
            dfAccount = pd.read_csv("User files/" + name + "/" + name + ".csv") # create a data frame with the accounts rated movies
            for indexAcc, rowAcc in dfAccount.iterrows(): # loop through each row of the data frame
                title = rowAcc["Title"] # save the title
                rating = rowAcc["Rating"] # save the rating
                if title == rowMov["Title"]: # if the title equals the current movie
                    score += rating # add the rating to the total score
                    count += 1 # add one to the count
        try: # if the score has a rating
            average = score/count # get the average
        except:
            average = -1 # otherwise score it -1
        dfMovies.at[indexMov, "Rating"] = average # save the score to the data frame

    dfMovies.to_csv("Files/Libary.CSV", index=False)  # save the data frame to the file
        
        
def CreateMenus():
    # create other screens
    DropDownGenre()
    SearchCreate()
    ReviewCreate()
    MatchCreate()
    WatchLaterCreate()
    AddShowCreate()
    HomeLoad()

def HomeLoad():
    global frmAccountLogin, frmBar, frmHome, multiplier, frmHomeTop, frmHomeRec, frmHomeHigh
    # forget previous screens
    ClearScreens()

    #display the side bar and home screen
    frmBar.grid(column=0,row=0,rowspan=2,sticky="NW")
    frmHome.grid(column=1,row=1,sticky="NW")
    frmHomeTop.grid(column=1,row=0,sticky="NW")



def SearchCreate():
    global window, space,varList, lblSRError, genreList,varAct,varAdv,varAni,varAnime,varCom,varCri,varDar,varDra,varFam,varFan,varFic,varHor,varLeg,varMus,varMys,varNar,varRom,varRomCom,varSci,varSla,varSpec,varThr,varWes, frmSearch, frmSearchTop, topSpace, bottomSpace, baseSize, multiplier, topWidth, mainWidth, topHeight, mainHeight, imgMagGlass, imgDownARRow, imgSRTDownArrow, imgSRTSearch, entSRTLength, dropSRTType, entSRTYear, menuSRTGenre, entSRTTitle, selSRTType, types
    # create frames
    frmSearchTop = Frame(window, highlightbackground="black", highlightthickness=1, width=topWidth, height=topHeight)
    frmSearch = Frame(window, width=mainWidth, height=mainHeight) # clears old results
    
    types = GetTypes()
    selSRTType = StringVar()


    # resize images to screen
    imgSRTSearch = imgMagGlass.subsample(multiplier*3)
    imgSRTDownArrow = imgDownArrow.subsample(multiplier*3)

    # create elements on screen
    lblSRTHeading = Label(frmSearchTop, text="SEARCH")
    ChangeSize(lblSRTHeading,  'Helvetica bold', int(baseSize*1.5))
    lblSRTHeading.place(relx=0.01, rely=0.1, anchor="nw")

    # create length label
    lblSRTLength = Label(frmSearchTop, text="Length")
    ChangeSize(lblSRTLength,  'Helvetica bold', int(baseSize/1.3))
    lblSRTLength.place(relx=0.25, rely=0.01, anchor="n")

    # create type label
    lblSRTType = Label(frmSearchTop, text="Type")
    ChangeSize(lblSRTType,  'Helvetica bold', int(baseSize/1.3))
    lblSRTType.place(relx=0.35, rely=0.01, anchor="n")

    # create year label
    lblSRTYear = Label(frmSearchTop, text="Year")
    ChangeSize(lblSRTYear,  'Helvetica bold', int(baseSize/1.3))
    lblSRTYear.place(relx=0.45, rely=0.01, anchor="n")

    # create genre label
    lblSRTGenre = Label(frmSearchTop, text="Genre")
    ChangeSize(lblSRTGenre,  'Helvetica bold', int(baseSize/1.3))
    lblSRTGenre.place(relx=0.58, rely=0.01, anchor="n")

    # create title label
    lblSRTTitle = Label(frmSearchTop, text="Title")
    ChangeSize(lblSRTTitle,  'Helvetica bold', int(baseSize/1.3))
    lblSRTTitle.place(relx=0.76, rely=0.01, anchor="n")

    # create entry boxes
    entSRTLength = Entry(frmSearchTop, width=int(16/multiplier))
    ChangeSize(entSRTLength, 'Helvetica bold', int(baseSize / 1.3))
    entSRTLength.place(relx=0.25, rely=0.9, anchor="s")

    # create type dropdown box
    dropSRTType = OptionMenu(frmSearchTop,selSRTType, *types)
    ChangeSize(dropSRTType, 'Helvetica bold', int(baseSize / 1.6))
    dropSRTType.config(compound='right', image=imgSRTDownArrow, width=baseSize * 5)
    dropSRTType.place(relx=0.35, rely=0.95, anchor="s")

    # create year entry box
    entSRTYear = Entry(frmSearchTop, width=int(16/multiplier))
    ChangeSize(entSRTYear, 'Helvetica bold', int(baseSize / 1.3))
    entSRTYear.place(relx=0.45, rely=0.9, anchor="s")

    # create genre menu box
    menuSRTGenre = Menubutton(frmSearchTop,text="Select Genre", relief=RAISED, width=int(30/multiplier))
    ChangeSize(menuSRTGenre, 'Helvetica bold', int(baseSize / 1.3))
    menuSRTGenre.place(relx=0.58, rely=0.9, anchor="s")

    menuSRTGenre.menu = Menu(menuSRTGenre, tearoff=0)
    menuSRTGenre["menu"] = menuSRTGenre.menu

    for loc in range(len(varList)):# loop through each genre
        menuSRTGenre.menu.add_checkbutton(label=genreList[loc], variable=varList[loc]) # add the genre to the dropdown

    # create title entry box
    entSRTTitle = Entry(frmSearchTop, width=int(37/multiplier))
    ChangeSize(entSRTTitle, 'Helvetica bold', int(baseSize / 1.3))
    entSRTTitle.place(relx=0.76, rely=0.9, anchor="s")

    # create Search button
    btnSRTSearch = Button(frmSearchTop, text="SEARCH", command=SearchLibary)
    ChangeSize(btnSRTSearch, 'Helvetica bold', int(baseSize / 2))
    btnSRTSearch.place(relx=0.89, rely=0.9, anchor="s")

    # create clear button
    btnSRTClear = Button(frmSearchTop, text="X", bg="red", command=ClearSearchTop)
    ChangeSize(btnSRTClear, 'Helvetica bold', int(baseSize / 2))
    btnSRTClear.place(relx=0.94 , rely=0.9 , anchor="s")

    # create an error label
    lblSRError = Label(frmSearch, text="", fg="red")
    ChangeSize(lblSRError,  'Helvetica bold', int(baseSize*1.5))
    lblSRError.place(relx=0.5, rely=0.5, anchor="center")


    # place logo in the top corner
    lblSRTLogo = Label(frmSearchTop, image=imgSRTSearch)
    lblSRTLogo.place(relx=0.99,rely=0.5, anchor="e")



def ClearSearchTop():
    global entSRTLength, varList, genreList,varAct,varAdv,varAni,varAnime,varCom,varCri,varDar,varDra,varFam,varFan,varFic,varHor,varLeg,varMus,varMys,varNar,varRom,varRomCom,varSci,varSla,varSpec,varThr,varWes, dropSRTType, entSRTYear, menuSRTGenre, entSRTTitle, selSRTType, types, frmSearchTop, mainHeight
    # clear the entries
    entSRTLength.delete(0,END)
    entSRTYear.delete(0,END)
    DropDownGenre()
    entSRTTitle.delete(0,END)

    # recreate the type drop down
    dropSRTType.place_forget()
    selSRTType = StringVar()
    dropSRTType = OptionMenu(frmSearchTop, selSRTType, *types)
    ChangeSize(dropSRTType, 'Helvetica bold', int(baseSize / 1.6))
    dropSRTType.config(compound='right', image=imgSRTDownArrow, width=baseSize * 5)
    dropSRTType.place(relx=0.35, rely=0.95, anchor="s")

    # recreate genre drop down
    menuSRTGenre.place_forget()
    menuSRTGenre = Menubutton(frmSearchTop,text="Select Genre", relief=RAISED, width=int(30/multiplier))
    ChangeSize(menuSRTGenre, 'Helvetica bold', int(baseSize / 1.3))
    menuSRTGenre.place(relx=0.58, rely=0.9, anchor="s")

    menuSRTGenre.menu = Menu(menuSRTGenre, tearoff=0)
    menuSRTGenre["menu"] = menuSRTGenre.menu

    for loc in range(len(varList)):
        menuSRTGenre.menu.add_checkbutton(label=genreList[loc], variable=varList[loc])




def SearchLibary():
    global window, varList, frmSearch, genreList,lblSRError,varAct,varAdv,varAni,varAnime,varCom,varCri,varDar,varDra,varFam,varFan,varFic,varHor,varLeg,varMus,varMys,varNar,varRom,varRomCom,varSci,varSla,varSpec,varThr,varWes, frmMovieBox, scrSearch, dfMovies, imgSmurf, frmSearch, entSRTLength, entSRTYear, entSRTGenre, entSRTTitle, selSRTType, frmSearch, lblMBTitle, movImage, lblMBCover
    # get the input from the entry boxes
    movLength = entSRTLength.get()
    movType = selSRTType.get()
    movYear = entSRTYear.get()
    movGenre = GetGenre()
    movTitle = entSRTTitle.get()

    today = datetime.date.today() # get the current date

    curYear = today.year # get the current year

    # try to remove the frame
    try:
        frmSearch.grid_forget()
    except:
        pass

    # recreate the frame
    frmSearch = Frame(window, width=mainWidth, height=mainHeight)  # clears old results

    # create an error label
    lblSRError = Label(frmSearch, text="", fg="red")
    ChangeSize(lblSRError, 'Helvetica bold', int(baseSize * 1.5))
    lblSRError.place(relx=0.5, rely=0.5, anchor="center")
    SearchLoad()


    try: # check if movLength is a number
        allow = False
        if movLength != "":
            if int(movLength) < 0 or int(movLength) > 5100:
                lblSRError.config(text="Please enter a valid length")
            else:
                allow = True
        else:
            allow = True
        if allow == True:
            try: # check if movYear is a number
                allow = False
                if movYear != "":
                    if int(movYear) < 1888 or int(movYear) > curYear: # ensure the year falls in a possible time frame
                        lblSRError.config(text="Please enter a valid year")
                    else:
                        allow = True
                else:
                    allow = True
                if allow == True:
                        # clear other searches
                        try:
                            frmSearch.grid_forget()
                        except:
                            pass
                        frmSearch = Frame(window, width=mainWidth, height=mainHeight)  # clears old results

                        # run the function to sort the movies by the criteria
                        movieSort = SearchSort(movTitle, movGenre, movType, movLength, movYear)

                        # create a canvas for scroll bar
                        canSearch = Canvas(frmSearch, width=int(mainWidth - 30), height=mainHeight)
                        canSearch.pack(side=LEFT, fill=BOTH, expand=1)

                        # add scroll bar
                        scrSearch = ttk.Scrollbar(frmSearch, orient=VERTICAL, command=canSearch.yview)
                        scrSearch.pack(side=RIGHT, fill=Y)

                        # configure the canvas
                        canSearch.configure(yscrollcommand=scrSearch.set)
                        canSearch.bind("<Configure>", lambda e: canSearch.configure(scrollregion=canSearch.bbox("all")))

                        # create another frame inside canvas
                        frmSearchScroll = Frame(canSearch, width=mainWidth - 30, height=mainHeight)

                        # add that new frame to a window in the canvas
                        canSearch.create_window((0, 0), window=frmSearchScroll, anchor="nw")

                        frmSearch.grid()
                        for loc in range(12):
                            FillScreenMovies(movieSort[loc][0], frmSearchScroll)
                            SearchLoad()

            except: # if movYear is not a number than display the following
                lblSRError.config(text="Please enter the length in minutes with no letters")
    except: # if movLength is not a number than display the following
        lblSRError.config(text="Please enter the year of release with no letters")

    
def GetGenre():
    global menuSRTGenre, varList, genreList,varUnc, varAct,varAdv,varAni,varAnime,varCom,varCri,varDar,varDra,varFam,varFan,varFic,varHor,varLeg,varMus,varMys,varNar,varRom,varRomCom,varSci,varSla,varSpec,varThr,varWes
    # initiate genre variable
    genre = ""

    for loc in range(len(varList)): # loop through each variable for each genre
        if varList[loc].get() == True: # if the variable is set to true
            genre += genreList[loc] + "/" # add the genre to the string

    genre = genre[:-1] # remove the last extra "/"
    return genre 

def FillScreenMovies(selMovie, frm):
    global dfMovies, multiplier, scrSearch, frmMovieBox, mov, lblMBTitle, frmSearch, imgOzTheGreatandPowerful, imgTheWizardofOz
    global baseSize,multiplier, imgLGLeftArrow, imgLGRightArrow, frmLogin, localIcon,window, space, imgSmurf, imgJoker, imgKyle, imgMando, imgPredator, imgR2, imgTransformer, imgYoda, imgHomer, imgHedwig, imgGrinch, imgDarthVader, imgC3PO, imgBlackPanther, imgRightArrow, imgLeftArrow

    # create frame
    frmMovieBox = Frame(frm, width=mainWidth, height=mainHeight/4, highlightbackground="black", highlightthickness=2)
    frmMovieBox.pack()

    # global images
    RefreshImageFile()

    try: # use the photo if its saved
        mov = PhotoImage(file="Movie Covers/"+ selMovie + ".png")
    except: # else use the empty cover image
        mov = PhotoImage(file="Movie Covers/Empty Cover.png")


    mov = mov.subsample(multiplier*3) # resize the image

    # create title label
    lblMBTitle = Label(frmMovieBox, text=selMovie)
    ChangeSize(lblMBTitle, 'Helvetica bold', int(baseSize/2))
    lblMBTitle.place(relx=0.08, rely=0.1, anchor="center")

    
    # Create the button with the logo
    lblMBCover = Label(frmMovieBox,image=mov, highlightthickness = 0, highlightbackground="black")
    lblMBCover.place(relx=0.08, rely=0.58,anchor="center") # place the button based on the section

    # Create button to view the show info
    btnMBView = Button(frmMovieBox, text="VIEW", command= lambda selMovie = selMovie :ShowInfoCreate(selMovie))
    ChangeSize(btnMBView, 'Helvetica bold', int(baseSize*2.8))
    btnMBView.place(relx=0.47, rely=0.5, anchor="center")

    # create button to add to watch later
    btnMBWatch = Button(frmMovieBox, text="Watch Later", command= lambda selMovie = selMovie :AddWatchLater(selMovie))
    ChangeSize(btnMBWatch, 'Helvetica bold', int(baseSize*2.8))
    btnMBWatch.place(relx=0.8, rely=0.5, anchor="center")



def ReviewCreate():
    global mainHeight, mainWidth, topHeight, topWidth, window, baseSize, frmReview, frmReviewTop
    # create frames
    frmReview = Frame(window, width=mainWidth, height=mainHeight)
    frmReviewTop = Frame(window, width=topWidth, height=topHeight, highlightbackground="black", highlightthickness=1)

    # create title label
    lblREVTTitle = Label(frmReviewTop, text="REVIEW ANALYSIS")
    ChangeSize(lblREVTTitle, 'Helvetica bold', int(baseSize*1.5))
    lblREVTTitle.place(relx=0.01, rely=0.06, anchor="nw")

    # warning that the feature has not been created yet, to be removed when feature added
    lblREVTitle = Label(frmReview, text="THIS FEATURE IS NOT AVAILABLE YET!")
    ChangeSize(lblREVTitle, 'Helvetica bold', baseSize*2)
    lblREVTitle.place(relx=0.5, rely=0.5, anchor="center")

def MatchCreate():
    global dfMovies, dfUser, multiplier, window, frmMatch, frmMatchTop, imgRefresh, imgMATRefresh, baseSize, imgHeart, imgMATIcon
    # create frames
    frmMatch = Frame(window, width=mainWidth, height=mainHeight)
    frmMatchTop = Frame(window, width=topWidth, height=topHeight, highlightbackground="black", highlightthickness=1)

    # split data and create and run neural network
    MatchMovies(1)

    # resize image
    imgMATRefresh = imgRefresh.subsample(multiplier)
    imgMATIcon = imgHeart.subsample(multiplier*2)

    # create title label
    lblMATTTitle = Label(frmMatchTop, text="YOUR MATCHES")
    ChangeSize(lblMATTTitle, 'Helvetica bold', int(baseSize*1.5))
    lblMATTTitle.place(relx=0.01, rely=0.06, anchor="nw")



    # create icon label
    lblMATTTitle = Label(frmMatchTop, image = imgMATIcon)
    lblMATTTitle.place(relx=0.98, rely=0.5, anchor="e")

    # create the refresh button
    btnMATRefresh = Button(frmMatchTop, image=imgMATRefresh, command=RefreshMatch)
    btnMATRefresh.place(relx=0.75, rely=0.5, anchor="center")


def RefreshMatch():
    # refesh the neral network and results
    MatchMovies(1)
    # reloads the screen
    MatchLoad()
    
def ScrollBar(frm):
    global mainWidth, mainHeight
    # create a canvas for scroll bar
    can = Canvas(frm, width=int(mainWidth-30), height=mainHeight)
    can.pack(side=LEFT, fill=BOTH, expand=1)

    # add scroll bar
    scr = ttk.Scrollbar(frm, orient=VERTICAL, command=can.yview)
    scr.pack(side=RIGHT, fill=Y)

    #configure the canvas
    can.configure(yscrollcommand=scr.set)
    can.bind("<Configure>", lambda e:can.configure(scrollregion=can.bbox("all")))

    # create another frame inside canvas
    frmScroll = Frame(can, width=mainWidth-30, height=mainHeight)

    # add that new frame to a window in the canvas
    can.create_window((0,0), window=frmScroll, anchor="nw")

    return frmScroll

    

def WatchLaterCreate():
    global mainHeight, mainWidth, topHeight, topWidth, window, baseSize, frmWatchLater, frmWatchLaterTop
    # create frames
    frmWatchLater = Frame(window, width=mainWidth, height=mainHeight)
    frmWatchLaterTop = Frame(window, width=topWidth, height=topHeight, highlightbackground="black", highlightthickness=1)

    # create title label
    lblWALTitle = Label(frmWatchLaterTop, text="WATCH LATER")
    ChangeSize(lblWALTitle, 'Helvetica bold', int(baseSize*1.5))
    lblWALTitle.place(relx=0.01, rely=0.06, anchor="nw")

    # warning that the feature has not been created yet, to be removed when feature added
    lblWALTitle = Label(frmWatchLater, text="THIS FEATURE IS NOT AVAILABLE YET!")
    ChangeSize(lblWALTitle, 'Helvetica bold', baseSize*2)
    lblWALTitle.place(relx=0.5, rely=0.5, anchor="center")


def AddWatchLater(selMovie):
    global accountUsernameG

    # create a data frame containing the watch later movies
    dfWatchLater = pd.read_csv("User Files/" + accountUsernameG + "/" + accountUsernameG + "WatchLater")
    

def AddShowCreate():
    global varList, genreList,lblASError,varAct,varAdv,varAni,varAnime,varCom,varCri,varDar,varDra,varFam,varFan,varFic,varHor,varLeg,varMus,varMys,varNar,varRom,varRomCom,varSci,varSla,varSpec,varThr,varWes,window, varList, genreList, frmAddShowTop, frmAddShow, multiplier, baseSize, entASRating, selASType, entASTitle, entASGenre, dropASType, entASLength, entASYear, entASFile, lblASCover, imgPlus, topSpace, bottomSpace, imgASTPlus, topWidth, mainWidth, topHeight, mainHeight, imgEmptyCover, imgDownArrow, imgASDownArrow
    # create the frames
    frmAddShowTop = Frame(window, highlightbackground="black", highlightthickness=1, width=topWidth, height=topHeight)
    frmAddShow = Frame(window, width=mainWidth, height=mainHeight)

    # get the array with the types e.g. Movie or tv show
    types = GetTypes()
    selASType = StringVar()

    # change size of image
    imgASDownArrow = imgDownArrow.subsample(multiplier*3)
    imgASTPlus = imgPlus.subsample(multiplier*3)
    imgASEmptyCover = imgEmptyCover.subsample(multiplier)



    #create the elements on the top bar
    lblASTHeading = Label(frmAddShowTop, text="ADD SHOW")
    ChangeSize(lblASTHeading,'Helvetica bold', int(baseSize*1.5))
    lblASTHeading.place(relx=0.01, rely=0.06, anchor="nw")

    # create a label with the icon
    lblASTLogo = Label(frmAddShowTop, image=imgASTPlus)
    lblASTLogo.place(relx=0.99, rely=0.06, anchor="ne")

    # create the title label
    lblASTitle = Label(frmAddShow, text="Title")
    ChangeSize(lblASTitle,'Helvetica bold', baseSize*2)
    lblASTitle.place(relx=0.5, rely=0.01, anchor="n")

    # create the title entry
    entASTitle = Entry(frmAddShow)
    ChangeSize(entASTitle,'Helvetica bold', baseSize*2)
    entASTitle.config(width=int(40/multiplier))
    entASTitle.place(relx=0.5, rely=0.1, anchor="n")

    # create the file label
    lblASFile = Label(frmAddShow, text="Enter File Path")
    ChangeSize(lblASFile,'Helvetica bold', int(baseSize/1.5))
    lblASFile.place(relx=0.01, rely=0.2, anchor="nw")

    # create the file entry box
    entASFile = Entry(frmAddShow)
    ChangeSize(entASFile,'Helvetica bold', int(baseSize/1.5))
    entASFile.place(relx=0.01, rely=0.25, anchor="nw")

    # create the load button
    btnASLoad = Button(frmAddShow, command=AddShowConfigure, text="Load", width=int(baseSize/5))
    ChangeSize(btnASLoad,'Helvetica bold', int(baseSize/2))
    btnASLoad.place(relx=0.2, rely=0.247, anchor="nw")

    # create cover label
    lblASCover = Label(frmAddShow, borderwidth=1, relief="solid", image=imgASEmptyCover)
    lblASCover.place(relx=0.01, rely=0.32, anchor="nw")

    # create the type label
    lblASType = Label(frmAddShow, text="Type")
    ChangeSize(lblASType, 'Helvetica bold', int(baseSize*1.5))
    lblASType.place(relx=0.45, rely=0.25, anchor="center")

    # create the genre label
    lblASGenre = Label(frmAddShow, text="Genre")
    ChangeSize(lblASGenre, 'Helvetica bold', int(baseSize*1.5))
    lblASGenre.place(relx=0.7, rely=0.25, anchor="center")

    # create the length label
    lblASLength = Label(frmAddShow, text="Length")
    ChangeSize(lblASLength, 'Helvetica bold', int(baseSize*1.5))
    lblASLength.place(relx=0.45, rely=0.46, anchor="center")

    # create the year label
    lblASYear = Label(frmAddShow, text="Year")
    ChangeSize(lblASYear, 'Helvetica bold', int(baseSize*1.5))
    lblASYear.place(relx=0.7, rely=0.46, anchor="center")

    # creat the type drop down box
    dropASType = OptionMenu(frmAddShow, selASType, *types)
    ChangeSize(dropASType, 'Helvetica bold', int(baseSize*1.5))
    dropASType.place(relx=0.45, rely=0.36, anchor="center")
    dropASType.config(compound='right', image=imgASDownArrow, width=baseSize*11)
    dropASType.image=imgASDownArrow

    # creat the genre drop down box
    menuASGenre = Menubutton(frmAddShow, text="Select Genre", relief=RAISED, width=int(baseSize/2))
    ChangeSize(menuASGenre, 'Helvetica bold', int(baseSize*1.2))
    menuASGenre.place(relx=0.73, rely=0.36, anchor="center")

    menuASGenre.menu = Menu(menuASGenre, tearoff=0)
    menuASGenre["menu"] = menuASGenre.menu

    for loc in range(len(varList)):
        menuASGenre.menu.add_checkbutton(label=genreList[loc], variable=varList[loc])

    

    # create the length entry box
    entASLength = Entry(frmAddShow,width=int(baseSize/2))
    ChangeSize(entASLength, 'Helvetica bold', int(baseSize*1.2))
    entASLength.place(relx=0.45, rely=0.54, anchor="center")

    # create the year entry box
    entASYear = Entry(frmAddShow,width=int(baseSize/2))
    ChangeSize(entASYear, 'Helvetica bold', int(baseSize*1.2))
    entASYear.place(relx=0.73, rely=0.54, anchor="center")

    # create the rating label
    lblASRating = Label(frmAddShow, text="Rating")
    ChangeSize(lblASRating, 'Helvetica bold', int(baseSize*1.5))
    lblASRating.place(relx=0.6, rely=0.61, anchor="center")

    # create the rating entry box
    entASRating = Entry(frmAddShow,width=int(baseSize/2))
    ChangeSize(entASRating, 'Helvetica bold', int(baseSize*1.2))
    entASRating.place(relx=0.6, rely=0.69, anchor="center")

    # add error label
    lblASError = Label(frmAddShow, text="", fg="red")
    ChangeSize(lblASError, 'Helvetica bold', baseSize)
    lblASError.place(relx=0.5, rely=0.8, anchor="center")

    # create the add button
    btnASAdd = Button(frmAddShow, text="ADD", width=baseSize, command=AddShow)
    ChangeSize(btnASAdd, 'Helvetica bold', int(baseSize*1.2))
    btnASAdd.place(relx=0.5, rely=0.9, anchor="center")


def DropDownGenre(): # create the elemets for the genre drop down box
    global varList, varUnc, genreList,varAct,varAdv,varAni,varBio,varCom,varCri,varDra,varDoc,varFam,varFan,varHis,varHor,varMus,varMusical,varMys,varNew,varRel,varRom,varSci,varSpo,varThr,varWar,varWes

    # create the variables for each genre
    varUnc = IntVar()
    varDoc = IntVar()
    varMus = IntVar()
    varAdv = IntVar()
    varCom = IntVar()
    varAni = IntVar()
    varFam = IntVar()
    varFan = IntVar()
    varHor = IntVar()
    varDra = IntVar()
    varSpo = IntVar()
    varRom = IntVar()
    varAct = IntVar()
    varSci = IntVar()
    varNew = IntVar()
    varHis = IntVar()
    varThr = IntVar()
    varWes = IntVar()
    varCri = IntVar()
    varMys = IntVar()
    varBio = IntVar()
    varMusical = IntVar()
    varWar = IntVar()
    varRel = IntVar()

    # create a list of the variables for each genre
    varList = [varUnc,varAct,varAdv,varAni,varBio,varCom,varCri,varDra,varDoc,varFam,varFan,varHis,varHor,varMus,varMusical,varMys,varNew,varRel,varRom,varSci,varSpo,varThr,varWar,varWes]

    # create a list of each genre
    genreList = ['Uncategorized', 'Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Drama', 'Documentary', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News', 'Reality-TV','Romance', 'Sci-Fi', 'Sport', 'Thriller', 'War', 'Western']
    

def AddShowConfigure():
    global entASFile, lblASCover, imgMovieCover, multiplier, imgCover
    # collects the file path and swaps any back slashes to forward slashes and removes any ""
    filePath = (entASFile.get()).replace("\\", "/").strip('"')


    # resize the image to the base size
    imgCover = Image.open(filePath)
    imgCoverResize = imgCover.resize((int(850/multiplier),int(1250/multiplier)))
    imgCover = ImageTk.PhotoImage(imgCoverResize)

    lblASCover.config(image=imgCover)

def AddShow():
    global entASTitle, varList, genreList, entASFile, entASGenre, dropASType, entASLength, entASYear, selASType, accountUsernameG, entASRating,lblASError
    # get the variables from the entries
    title = entASTitle.get()
    type = selASType.get()
    length = entASLength.get()
    year = entASYear.get()
    genre = GetGenre()
    # get the name of the image
    fileName = "Movie Covers/" + entASTitle.get() + ".png"

    today = datetime.date.today() # get the current date

    curYear = today.year # get the current year

    # read from libary file
    dfLibary = pd.read_csv("Files/Libary.CSV")

    try:  # check if movLength is a number
        allowLen = False
        if length != "":
            if int(length) < 0 or int(length) > 5100:
                lblASError.config(text="Please enter a valid length")
            else:
                allowLen = True
        else:
            allowLen = False
        if allowLen == True:
            try:  # check if movYear is a number
                allowYear = False
                if year != "":
                    if int(year) < 1888 or int(year) > curYear:  # ensure the year falls in a possible time frame
                        lblASError.config(text="Please enter a valid year")
                    else:
                        allowYear = True
                else:
                    allowYear = False
                if allowYear == True:
                    if genre == "": # check if a genre has been selected
                        lblASError.config(text="Please enter a genre")
                    else:
                        if title == "": # check if a title has been entered
                            lblASError.config(text="Please enter a title")
                        else:
                            if entASRating.get() == "": # check if a rating has been entered
                                lblASError.config(text="Please enter a rating")
                            else:
                                try: # checks if a number has been entered
                                    allowRat = False
                                    if int(entASRating.get()) < 0 or int(entASRating.get()) > 100: # check if the rating falls between 0-100
                                        lblASError.config(text="Please enter a rating between 0-100")
                                    else:
                                        allowRat = True
                                    if allowRat == True:
                                        if type == "": # check if a type has been selected
                                            lblASError.config(text="Please enter a type")
                                        else:
                                            same = False
                                            for index, row in dfLibary.iterrows():
                                                if title == row["Title"]:
                                                    same = True
                                            if same == True:
                                                lblASError.config(text="This "+ type +" is already in the system")
                                            else:
                                                if entASFile.get() != "":  # check if the file entry is empty
                                                    try:  # if not try to save the image
                                                        filePath = (entASFile.get()).replace("\\", "/").strip('"')

                                                        # resize the image to the base size
                                                        imgCover = Image.open(filePath)
                                                        imgCoverResize = imgCover.resize((750, 1125))
                                                        imgCoverResize.save(fileName)
                                                    except:  # if image can not be saved
                                                        lblASError.config(
                                                            text="image not found, ensure the image is a png file. you can also not include an image file")
                                                # add new item to the data frame and save to file
                                                addDataFrame = pd.DataFrame(
                                                    {"Title": title, "File": fileName, "Genre": genre, "Type": type,
                                                     "Length": length, "Year": year, "Rating":entASRating.get()}, index=[title])
                                                libaryFile = pd.concat([dfLibary, addDataFrame])
                                                libaryFile.to_csv("Files/Libary.CSV", index=False)
                                                userFile = open(
                                                    "User Files/" + accountUsernameG + "/" + accountUsernameG + ".csv", "a")
                                                userFile.write(
                                                    "\n" + entASTitle.get() + "," + genre + "," + selASType.get() + "," + entASLength.get() + "," + entASYear.get() + "," + entASRating.get())
                                                # return to the home screen
                                                HomeLoad()
                                                AddShowCreate()  # clear the details on screen

                                except: # letters are used
                                    lblASError.config(text="Please enter a rating between 0-100, only using digits")
                else: # if year is empty
                    lblASError.config(text="Please enter the release year")
            except:  # if movYear is not a number than display the following
                lblASError.config(text="Please enter the length in minutes with no letters")
        else: # if length is empty
            lblASError.config(text="Please enter the length in minutes")
    except:  # if movLength is not a number than display the following
        lblASError.config(text="Please enter the year of release with no letters")


    


    
def SearchLoad():
    global frmSearchTop, frmSearch, frmHome
    # clear previous screens
    ClearScreens()

    # load new screen
    frmSearchTop.grid(column=1,row=0,sticky="N")
    frmSearch.grid(column=1,row=1,sticky="NW")

def ReviewLoad():
    global frmReview, frmReviewTop
    # clear previous screens
    ClearScreens()

    # load new screens
    frmReview.grid(column=1, row=1, sticky="NW")
    frmReviewTop.grid(column=1,row=0,sticky="N")

def MatchLoad():
    global frmMatch, frmMatchTop, dfMovies, dfUser, window, frmMatch, frmMatchTop, frmLoadingScreen
    # clear previous screens
    ClearScreens()
    
    # load new screen
    frmMatch.grid(column=1, row=1, sticky="NW")
    frmMatchTop.grid(column=1,row=0,sticky="N")


def MatchMovies(x):
    global frmMatch, frmMatchTop, dfMovies, dfUser, window, frmMatch, frmMatchTop, frmLoadingScreen, frmMatchScroll, mainHeight, mainWidth

    try: # try to remove the match frame
        frmMatch.grid_forget()
    except: # else do nothing
        pass
    # recreate/ create the match frame
    frmMatch = Frame(window, width=mainWidth, height=mainHeight)
    
    # create a data frame with the needed headings
    dfMovieTest = pd.read_csv("Files/dfMovieTestFrame.CSV")

    for indexM, rowM in dfMovies.iterrows(): # loop through each row of the data
        dfGenre = pd.read_csv("Files/Genre.CSV") # create a data frame of the genres
        inside = False
        for indexU, rowU in dfUser.iterrows(): # loop through each row of the data 
            if rowU["Title"] == rowM["Title"]: # check if the users movie is the same as the movie data frames movie
                inside = True # if so set inside to true

        if inside == False: # if inside is equal to false
            try: # try to split the genre into a list
                gen = rowM["Genre"].split("/")
            except: # else there is only one genre, so a list with that one element is created
                gen = [rowM["Genre"]]
            for item in gen: # loop through each genre
                dfGenre.at[0, item] = 1 # set the digit in the data frame in the row of the genre
                """ data frame looks like:
                
                genre1,genre2,genre3,...
                0,0,1,...
                
                were 0 = not that genre, 1 = is that genre"""
            genre = (str(dfGenre.to_numpy().flatten())).strip("[").strip("]") # cover t the dataframe into a string

            # create a temporary data frame wit hthe info of that movie
            dfTemp = pd.DataFrame({"Title":rowM["Title"], "Genre":genre, "Type":rowM["Type"], "Length":rowM["Length"], "Year":rowM["Year"]}, index=[rowM["Title"]])
            dfMovieTest = pd.concat([dfMovieTest, dfTemp]) # combine the data frame with dfMovieTest
    dfMovieTest = dfMovieTest.reset_index(drop=True) # remove the index from the data frame

    try: # try to create and run ther neural network
        arPrediction = NeuralNetwork(dfUser, dfMovieTest) # input the two data frames and the list of movies nor rated in decending rating order outputed
        frmMatchScroll = ScrollBar(frmMatch) # add the scroll bar
        
        for loc in range(12):# loop the first 12 movies
            FillScreenMovies(arPrediction[loc][1], frmMatchScroll) # input the movie title and frame, and it is placed on screen
    except: # if the neural network errors
        # create an error label
        lblMAError = Label(frmMatch, text="PLEASE RATE MORE MOVIES FOR THIS FEATURE") # display that more movies must be rated
        ChangeSize(lblMAError, 'Helvetica bold', int(baseSize*1.5))
        lblMAError.place(relx=0.5, rely=0.5, anchor="center")


def WatchLaterLoad():
    global frmWatchLater, frmWatchLaterTop
    # clear previous screens
    ClearScreens()

    # load new screens
    frmWatchLaterTop.grid(column=1,row=0,sticky="NE")
    frmWatchLater.grid(column=1,row=1,sticky="NE")

def AddShowLoad():
    global frmAddShow, frmAddShowTop
    # clear previous screens
    ClearScreens()

    # load new screens
    frmAddShowTop.grid(column=1,row=0,sticky="NE")
    frmAddShow.grid(column=1,row=1,sticky="NE")

def ShowInfoCreate(selMovie):
    global dfMovies, dfUser, imgCamera, accountUsernameG, window, entSIRating, mainHeight, mainWidth, topHeight, topWidth, frmShowInfoTop, frmShowInfo, multiplier, baseSize, imgSICover
    # create the frames
    frmShowInfoTop = Frame(window,highlightbackground="black", highlightthickness=1, width=topWidth, height=topHeight)
    frmShowInfo = Frame(window, width=mainWidth, height=mainHeight)


    # collect the data on the movie 
    row = dfMovies.loc[lambda dfMovies: dfMovies["Title"] == selMovie]
    showTitle = row.iloc[0,0]
    showFile = row.iloc[0,1]
    showGenre = (row.iloc[0,2]).replace("/","\n")
    showType = row.iloc[0,3]
    showLength = str(row.iloc[0,4])
    showYear = str(row.iloc[0,5])

    # collect df from users account
    dfUser = pd.read_csv("User Files/" + accountUsernameG + "/" + accountUsernameG + ".csv")

    # create title label
    lblSITTitle = Label(frmShowInfoTop, text="SHOW INFO")
    ChangeSize(lblSITTitle, 'Helvetica bold', int(baseSize*1.5))
    lblSITTitle.place(relx=0.05, rely=0.5, anchor="w")

    # resize image
    imgSITCamera = imgCamera.subsample(multiplier*3)

    # create icon label
    lblSITIcon = Label(frmShowInfoTop, image=imgSITCamera)
    lblSITIcon.place(relx=0.95, rely=0.5, anchor="e")

    # add elements on the main part of the screen
    lblSITitle = Label(frmShowInfo, text=showTitle)
    ChangeSize(lblSITitle, 'Helvetica bold', int(baseSize*2.5))
    lblSITitle.place(relx=0.5, rely=0.1, anchor="center")
    
    # save image and resize
    try:
        imgSICover = (PhotoImage(file="Movie Covers/" + showFile)).subsample(int(multiplier))
    except:
        imgSICover = (PhotoImage(file="Movie Covers/Empty Cover.png")).subsample(multiplier)

    imgSICover = imgSICover.subsample(multiplier)

    # create cover label
    lblSICover = Label(frmShowInfo, image=imgSICover)
    lblSICover.place(relx=0.025, rely=0.5, anchor="w")

    # create year label
    lblSIYear = Label(frmShowInfo, text="   YEAR   \n\n" + showYear, borderwidth = 2, relief="solid", width=int(mainWidth/130))
    ChangeSize(lblSIYear, 'Helvetica bold', int(baseSize*1.7))
    lblSIYear.place(relx=0.55, rely=0.4, anchor="se")

    # create length label
    lblSILength = Label(frmShowInfo, text="LENGTH\n\n" + showLength, borderwidth = 2, relief="solid", width=int(mainWidth/130))
    ChangeSize(lblSILength, 'Helvetica bold', int(baseSize*1.7))
    lblSILength.place(relx=0.55, rely=0.4, anchor="sw")

    # create genre label
    lblSIGenre = Label(frmShowInfo, text="  GENRE \n\n" + showGenre, borderwidth = 2, relief="solid", width=int(mainWidth/130))
    ChangeSize(lblSIGenre, 'Helvetica bold', int(baseSize*1.7))
    lblSIGenre.place(relx=0.55, rely=0.4, anchor="ne")

    # create type label
    lblSIType = Label(frmShowInfo, text="  TYPE   \n\n" + showType + "\n", borderwidth = 2, relief="solid", width=int(mainWidth/130))
    ChangeSize(lblSIType, 'Helvetica bold', int(baseSize*1.7))
    lblSIType.place(relx=0.55, rely=0.4, anchor="nw")

    # create add rating label
    lblSIRate = Label(frmShowInfo, text="ADD RATING")
    ChangeSize(lblSIRate,  'Helvetica bold', baseSize)
    lblSIRate.place(relx=0.9, rely=0.18, anchor="center")

    rated = False # set rated to false
    for index, row in dfUser.iterrows(): # loop through each row of the data 
        if row["Title"] == selMovie: # if the titles match
            lblSIRate.config(text="YOUR RATING") # then the movie has been rated so "Your Rating" is displayed
            rated = True
    if rated == True: # if rated equals true then there rating is displayed
        # create rating label
        lblSIRating = Label(frmShowInfo, text=row["Rating"])
        ChangeSize(lblSIRating,  'Helvetica bold', baseSize)
        lblSIRating.place(relx=0.9, rely=0.23, anchor="center")
    elif rated == False: # otherwise create entry box to add rating
        # create rating enrty box
        entSIRating = Entry(frmShowInfo, width=int(mainWidth/150))
        ChangeSize(entSIRating,  'Helvetica bold', baseSize)
        entSIRating.place(relx=0.9, rely=0.23, anchor="center")

        # create submit button
        btnSISubmit = Button(frmShowInfo, text="SUBMIT", command=lambda selMovie=selMovie: RefreshShowInfo(selMovie))
        ChangeSize(btnSISubmit,  'Helvetica bold', baseSize)
        btnSISubmit.place(relx=0.9, rely=0.31, anchor="center")

    # reload the screen
    ShowInfoLoad()

def RefreshShowInfo(selMovie):
    global entSIRating, accountUsernameG, dfUser, dfMovies
    # get the users rating
    rating = entSIRating.get()

    # open the users file
    file = open("User Files/" + accountUsernameG + "/" + accountUsernameG + ".csv", "a")
    for index, row in dfMovies.iterrows(): # loop through each row of the data frame
        if row["Title"] == selMovie: # if the movies match
            file.write("\n" + row["Title"] + "," + row["Genre"] + "," + row["Type"] + "," + str(row["Length"]) + "," + str(row["Year"]) + "," + str(rating)) # write the details to the users file

    # close the file
    file.close()

    # clear the screen
    ClearScreens()
    # recreate the screen
    ShowInfoCreate(selMovie)

    

def ShowInfoLoad():
    global frmShowInfoTop, frmShowInfo
    # clear previous screens
    ClearScreens()

    # load new screens
    frmShowInfoTop.grid(column=1,row=0,sticky="NE")
    frmShowInfo.grid(column=1,row=1,sticky="NE")