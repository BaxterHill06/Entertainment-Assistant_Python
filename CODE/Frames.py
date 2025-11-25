'''
 ____ ____ ____ ____ ____ ____
||B |||a |||x |||t |||e |||r ||
||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|
Version 13
last updated: 18/08/23
'''




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


def GetImages():
    global imgPlus,imgEmpLogo,imgSmurf, imgJoker, imgKyle, imgMando, imgPredator, imgR2, imgTransformer, imgYoda, imgHomer, imgHedwig, imgGrinch, imgDarthVader, imgC3PO, imgBlackPanther, imgBook, imgClock, imgExit, imgHeart, imgHouse, imgMagGlass, imgMenuPlus,imgRightArrow, imgLeftArrow, imgEmptyCover, imgDownArrow, imgUpArrow
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

    imgRightArrow = PhotoImage(file="arrow Right.png")
    imgLeftArrow = PhotoImage(file="arrow Left.png")
    imgDownArrow = PhotoImage(file="arrow Down.png")
    imgUpArrow = PhotoImage(file="arrow Up.png")

    imgEmptyCover = PhotoImage(file="Movie Covers/Empty Cover.png")


#create Exit bar
def ExitCreate(window):
    menuBar = Menu(window)
    topBar = Menu(menuBar,tearoff=0)
    topBar.add_command(label="Exit", command=window.destroy)
    menuBar.add_cascade(label="Exit", menu=topBar)
    window.config(menu=menuBar)

def InitiateFrames():
    global frmLogin, frmAccountLogin, frmMovieBox, frmAddAccount, frmSearchTop, frmSearch, frmShowInfo, frmShowInfoTop, frmHomeTop, frmHome, frmReviewTop, frmReview, frmMatchTop, frmMatch, frmWatchLaterTop, frmWatchLater, frmAddShowTop, frmAddShow
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


def ClearScreens():
    global frmLogin ,frmAccountLogin, frmSearchTop, frmSearch, frmShowInfo, frmShowInfoTop, frmHomeTop, frmHome, frmReviewTop, frmReview, frmMatchTop, frmMatch, frmWatchLaterTop, frmWatchLater, frmAddShowTop, frmAddShow
    frames = [frmLogin ,frmMovieBox, frmAccountLogin, frmAddAccount, frmSearchTop, frmSearch, frmHomeTop, frmHome, frmReviewTop, frmReview, frmMatchTop, frmMatch, frmWatchLaterTop, frmWatchLater, frmAddShowTop, frmAddShow, frmShowInfo, frmShowInfoTop]
    for frame in frames:
        try:
            frame.grid_forget()
        except:
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
    frmLogin = Frame(window, bg="white", width=width, height=height-20)


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
    LoginLoad()



def LoginIconCreate(accountUsername,accountPassword, accountIcon,element, screenPage):
    global baseSize,multiplier, imgLGLeftArrow, imgLGRightArrow, accountInfo, frmLogin, localIcon,window, space, imgSmurf, imgJoker, imgKyle, imgMando, imgPredator, imgR2, imgTransformer, imgYoda, imgHomer, imgHedwig, imgGrinch, imgDarthVader, imgC3PO, imgBlackPanther, imgRightArrow, imgLeftArrow
    if accountIcon == "Smurf": # checks what the icon selected is and save the file to a variable
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
    global frmAddAccount,imgEmpLogo, baseSize, multiplier, selAAIcon,lblAALogo, window, space, baseSize, multiplier, imgAAEmpLogo, height, width
    frmAddAccount = Frame(window, width=width-20, height=height-35)
    
    #resizing the empty icon image
    imgAAEmpLogo = imgEmpLogo.subsample(multiplier)

    # gathering the array with the icons for dropdown box
    icons = GatherIcons()
    
    
    #create logo image
    lblAALogo = Label(frmAddAccount, image=imgAAEmpLogo)
    lblAALogo.place(relx=0.42, rely=0.05)

    #add dropdown for selection icon
    selAAIcon = StringVar()
    dropAALogo = OptionMenu(frmAddAccount, selAAIcon , *icons,)
    dropAALogo.config(width=int(13/multiplier),height=int(2/multiplier))
    ChangeSize(dropAALogo,'Helvetica bold', baseSize)
    dropAALogo.place(relx=0.65, rely=0.15, anchor="center")
    

    #add a select button for the icon
    btnAASelect = Button(frmAddAccount, text="SELECT", command=IconConfigure)
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
    global window, space
    username = username.get()
    # add account info to a csv file
    userFile = pd.read_csv("UserFile.csv")
    addArray = pd.DataFrame({"Username":username,"Password":password.get(),"Icon":icon.get(),"File":username + ".csv"},index=[username])
    userFile = pd.concat([userFile,addArray])
    userFile.to_csv("UserFile.csv",index=False)
    # create a deicated file for the user to save their preferences into
    userSpecificFile = open("User Files/" + username + ".csv", "w")
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
    frmBar = Frame(window, highlightbackground="black", highlightthickness=1,) # width=width-1629, height=height-20) # create side bar frame
    print(multiplier)

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
    #  create variable with spacific size for  the top bar and main dscreent
    topHeight = (height - 20) / 11
    topWidth = ((width) / 13) * 12
    mainHeight = ((height - 20) / 12) * 11
    mainWidth = ((width) / 13) * 12

    # create the data frame with the movie data in it
    dfMovies = pd.read_csv("files/Libary.csv")
    dfUser = pd.read_csv("User Files/" + accountUsernameG + ".csv")

    # create frames
    frmHome = Frame(window, height=mainHeight, width=mainWidth)
    frmHomeTop = Frame(window, highlightbackground="black", highlightthickness=1, height=topHeight, width=topWidth)


    # create sub headings
    """
    lblHORecent = Label(frmHome, text="Recently Added")
    ChangeSize(lblHORecent, 'Helvetica bold', int(baseSize*0.33))
    lblHORecent.place(relx=0.05, rely=0,anchor="nw")

    lblHOHigh = Label(frmHome, text="Highly Rated")
    ChangeSize(lblHOHigh, 'Helvetica bold', int(baseSize*0.33))
    lblHOHigh.place(relx=0.05, rely=0.48,anchor="nw")
    """

    HomeRec(1)
    HomeHigh(1)

    HomeLoad()


def HomeRec(recLoc):
    global dfMovies, cov, frmHomeRec, mainWidth, mainHeight
    
    dfRec = ((dfMovies[len(dfMovies)-20:]).iloc[::-1]).reset_index()
    print(dfRec)
    frmHomeRec = Frame(frmHome, width=mainWidth, height= int(mainHeight/2), bg="Black")
    frmHomeRec.grid(row=1, column=1)

    for index, row in dfRec.iterrows(): # loop through each row of the data
        title = row["Title"]
        cover = (PhotoImage(file="Movie Covers/" +title + ".png"))
        HomeRecPlace(title, index, cover, recLoc)

def HomeRecPlace(title, index, cover, recLoc):
    global multiplier, frmHomeRec, cov, imgHORLeftArrow, imgLeftArrow, imgHORRightArrow, imgRightArrow
    print(index)
    page = ((index // 5) + 1)

    if page == recLoc:
        cov = cover.subsample(int(multiplier*1.7))
        btnHORImg = Button(frmHomeRec, image=cov, text="Hi")
        btnHORImg.place(relx=(0.18 * (index % 5) ) + 0.14, rely= 0.5, anchor="center")
        lblHORTitle = Label(frmHomeRec, text=title)
        ChangeSize(lblHORTitle,'Helvetica bold', int(baseSize*0.4))
        lblHORTitle.place(relx=(0.18 * (index % 5) ) + 0.14, rely= 0.9, anchor="center")
        
    imgHORLeftArrow = imgLeftArrow.subsample(multiplier)
    imgHORRightArrow = imgRightArrow.subsample(multiplier)

    if recLoc != 1:
        btnHORArrowLeft = Button(frmHomeRec, image=imgHORLeftArrow, command = lambda recLoc = recLoc: HomeRec(recLoc-1))
        btnHORArrowLeft.place(relx=0.04, rely=0.5, anchor = "center")

    if recLoc != 4:
        btnHORArrowRight = Button(frmHomeRec, image=imgHORRightArrow, command = lambda recLoc = recLoc: HomeRec(recLoc+1))
        btnHORArrowRight.place(relx=0.96, rely=0.5, anchor = "center")

def HomeHigh(highLoc):
    global dfMovies, frmHomeHigh

    GetAverageRating()

    frmHomeHigh = Frame(frmHome, width=mainWidth, height= int(mainHeight/2), bg="Black")
    frmHomeHigh.grid(row=2, column=2)


    dfHigh = dfMovies.sort_values("Rating")
    dfHigh = dfHigh[(len(dfHigh)) - 20:]
    print(dfHigh)
    for index, row in dfHigh.iterrows(): # loop through each row of the data
        title = row["Title"]
        cover = (PhotoImage(file="Movie Covers/" +title + ".png"))
        HomeRecPlace(title, index, cover, highLoc)
    

def HomeHighPlace(title, index, cover, highLoc):
    global frmHomeHigh

    if page == highLoc:
        cov = cover.subsample(int(multiplier*1.7))
        btnHOHImg = Button(frmHomeHigh, image=cov, text="Hi")
        btnHOHImg.place(relx=(0.18 * (index % 5) ) + 0.14, rely= 0.5, anchor="center")
        lblHOHTitle = Label(frmHomeHigh, text=title)
        ChangeSize(lblHOHTitle,'Helvetica bold', int(baseSize*0.4))
        lblHOHTitle.place(relx=(0.18 * (index % 5) ) + 0.14, rely= 0.9, anchor="center")
        
    imgHOHLeftArrow = imgLeftArrow.subsample(multiplier)
    imgHOHRightArrow = imgRightArrow.subsample(multiplier)

    if highLoc != 1:
        btnHOHArrowLeft = Button(frmHomeHigh, image=imgHOLeftArrow, command = lambda highLoc = recLoc: HomeHigh(highLoc-1))
        btnHOHArrowLeft.place(relx=0.04, rely=0.5, anchor = "center")

    if highLoc != 4:
        btnHOArrowRight = Button(frmHomeHigh, image=imgHORightArrow, command = lambda highLoc = recLoc: HomeHigh(highLoc+1))
        btnHOArrowRight.place(relx=0.96, rely=0.5, anchor = "center")

    


    
def GetAverageRating():
    userFile = open("UserFile.csv", "r")
    
    
    users = []
    for line in userFile:
        print(line, "line")
        line = line.split(",")
        print(line, "line2")
        users.append(line[0])
    users = users[1:]
    print(users)

    for indexMov, rowMov in dfMovies.iterrows(): # loop through each row of the data
        score = 0
        count = 0
        for name in users:
            dfAccount = pd.read_csv("User files/" + name + ".csv")
            for indexAcc, rowAcc in dfAccount.iterrows(): # loop through each row of the data
                title = rowAcc["Title"]
                rating = rowAcc["Rating"]
                if title == rowMov["Title"]:
                    score += rating
                    count += 1
        try:
            average = score/count
        except:
            average = -1
        dfMovies.at[indexMov, "Rating"] = average
        
    print(dfMovies)

    dfMovies.to_csv("Files/Libary.CSV", index=False)
        
        
        

def HomeLoad():
    global frmAccountLogin, frmBar, frmHome, multiplier, frmHomeTop
    # forget previous screens
    ClearScreens()

    # create other screens
    SearchCreate()
    ReviewCreate()
    MatchCreate()
    WatchLaterCreate()
    AddShowCreate()

    #display the side bar and home screen
    frmBar.grid(column=0,row=0,rowspan=2,sticky="NW")
    frmHome.grid(column=1,row=1,sticky="NW")
    frmHomeTop.grid(column=1,row=0,sticky="NW")


def SearchCreate():
    global window, space, frmSearch, frmSearchTop, topSpace, bottomSpace, baseSize, multiplier, topWidth, mainWidth, topHeight, mainHeight, imgMagGlass, imgDownARRow, imgSRTDownArrow, imgSRTSearch, entSRTLength, dropSRTType, entSRTYear, entSRTGenre, entSRTTitle, selSRTType, types
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


    lblSRTLength = Label(frmSearchTop, text="Length")
    ChangeSize(lblSRTLength,  'Helvetica bold', int(baseSize/1.3))
    lblSRTLength.place(relx=0.25, rely=0.01, anchor="n")

    lblSRTType = Label(frmSearchTop, text="Type")
    ChangeSize(lblSRTType,  'Helvetica bold', int(baseSize/1.3))
    lblSRTType.place(relx=0.35, rely=0.01, anchor="n")

    lblSRTYear = Label(frmSearchTop, text="Year")
    ChangeSize(lblSRTYear,  'Helvetica bold', int(baseSize/1.3))
    lblSRTYear.place(relx=0.45, rely=0.01, anchor="n")

    lblSRTGenre = Label(frmSearchTop, text="Genre")
    ChangeSize(lblSRTGenre,  'Helvetica bold', int(baseSize/1.3))
    lblSRTGenre.place(relx=0.58, rely=0.01, anchor="n")

    lblSRTTitle = Label(frmSearchTop, text="Title")
    ChangeSize(lblSRTTitle,  'Helvetica bold', int(baseSize/1.3))
    lblSRTTitle.place(relx=0.76, rely=0.01, anchor="n")

    # create entry boxes
    entSRTLength = Entry(frmSearchTop, width=int(16/multiplier))
    ChangeSize(entSRTLength, 'Helvetica bold', int(baseSize / 1.3))
    entSRTLength.place(relx=0.25, rely=0.9, anchor="s")

    dropSRTType = OptionMenu(frmSearchTop,selSRTType, *types)
    ChangeSize(dropSRTType, 'Helvetica bold', int(baseSize / 1.6))
    dropSRTType.config(compound='right', image=imgSRTDownArrow, width=baseSize * 5)
    dropSRTType.place(relx=0.35, rely=0.95, anchor="s")

    entSRTYear = Entry(frmSearchTop, width=int(16/multiplier))
    ChangeSize(entSRTYear, 'Helvetica bold', int(baseSize / 1.3))
    entSRTYear.place(relx=0.45, rely=0.9, anchor="s")

    entSRTGenre = Entry(frmSearchTop, width=int(30/multiplier))
    ChangeSize(entSRTGenre, 'Helvetica bold', int(baseSize / 1.3))
    entSRTGenre.place(relx=0.58, rely=0.9, anchor="s")

    entSRTTitle = Entry(frmSearchTop, width=int(37/multiplier))
    ChangeSize(entSRTTitle, 'Helvetica bold', int(baseSize / 1.3))
    entSRTTitle.place(relx=0.76, rely=0.9, anchor="s")



    btnSRTSearch = Button(frmSearchTop, text="SEARCH", command=SearchLibary)
    ChangeSize(btnSRTSearch, 'Helvetica bold', int(baseSize / 2))
    btnSRTSearch.place(relx=0.89, rely=0.9, anchor="s")

    btnSRTClear = Button(frmSearchTop, text="X", bg="red", command=ClearSearchTop)
    ChangeSize(btnSRTClear, 'Helvetica bold', int(baseSize / 2))
    btnSRTClear.place(relx=0.94 , rely=0.9 , anchor="s")




    lblSRTLogo = Label(frmSearchTop, image=imgSRTSearch)
    lblSRTLogo.place(relx=0.99,rely=0.5, anchor="e")



def ClearSearchTop():
    global entSRTLength, dropSRTType, entSRTYear, entSRTGenre, entSRTTitle, selSRTType, types, frmSearchTop, mainHeight
    # clear the entries
    entSRTLength.delete(0,END)
    entSRTYear.delete(0,END)
    entSRTGenre.delete(0,END)
    entSRTTitle.delete(0,END)

    dropSRTType.place_forget()
    selSRTType = StringVar()
    dropSRTType = OptionMenu(frmSearchTop, selSRTType, *types)
    ChangeSize(dropSRTType, 'Helvetica bold', int(baseSize / 1.6))
    dropSRTType.config(compound='right', image=imgSRTDownArrow, width=baseSize * 5)
    dropSRTType.place(relx=0.35, rely=0.95, anchor="s")


def SearchLibary():
    global window, frmMovieBox, scrSearch, dfMovies, imgSmurf, frmSearch, entSRTLength, entSRTYear, entSRTGenre, entSRTTitle, selSRTType, frmSearch, lblMBTitle, movImage, lblMBCover
    # get the input from the entry boxes
    
    movLength = entSRTLength.get()
    movType = selSRTType.get()
    movYear = entSRTYear.get()
    movGenre = entSRTGenre.get()
    movTitle = entSRTTitle.get()

    # clear other searches
    try:
        frmSearch.grid_forget()
    except:
        pass
    frmSearch = Frame(window, width=mainWidth, height=mainHeight) # clears old results
    
    

    # run the function to sort the movies by the criteria 
    movieSort = SearchSort(movTitle,movGenre,movType,movLength,movYear)

    # create a canvas for scroll bar
    canSearch = Canvas(frmSearch, width=int(mainWidth-30), height=mainHeight)
    canSearch.pack(side=LEFT, fill=BOTH, expand=1)

    # add scroll bar
    scrSearch = ttk.Scrollbar(frmSearch, orient=VERTICAL, command=canSearch.yview)
    scrSearch.pack(side=RIGHT, fill=Y)

    #configure the canvas
    canSearch.configure(yscrollcommand=scrSearch.set)
    canSearch.bind("<Configure>", lambda e:canSearch.configure(scrollregion=canSearch.bbox("all")))

    # create another frame inside canvas
    frmSearchScroll = Frame(canSearch, width=mainWidth-30, height=mainHeight)

    # add that new frame to a window in the canvas
    canSearch.create_window((0,0), window=frmSearchScroll, anchor="nw")

    
    frmSearch.grid()
    for loc in range(12):
        FillScreenMovies(movieSort[loc][0], frmSearchScroll)
        SearchLoad()
    


def FillScreenMovies(selMovie, frm):
    global dfMovies, multiplier, scrSearch, frmMovieBox, mov, lblMBTitle, frmSearch, imgOzTheGreatandPowerful, imgTheWizardofOz
    global baseSize,multiplier, imgLGLeftArrow, imgLGRightArrow, frmLogin, localIcon,window, space, imgSmurf, imgJoker, imgKyle, imgMando, imgPredator, imgR2, imgTransformer, imgYoda, imgHomer, imgHedwig, imgGrinch, imgDarthVader, imgC3PO, imgBlackPanther, imgRightArrow, imgLeftArrow
   
    frmMovieBox = Frame(frm, width=mainWidth, height=mainHeight/4, highlightbackground="black", highlightthickness=2)
    frmMovieBox.pack()
    RefreshImageFile()
    GlobalImageFile(selMovie)
    if 'Shrek' == selMovie:
        mov = imgShrek
    elif 'Rise Of The Guardians' == selMovie:
        mov = imgRiseOfTheGuardians
    elif 'Shrek 2' == selMovie:
        mov = imgShrek2
    elif 'Shrek the Third' == selMovie:
        mov = imgShrektheThird
    elif 'The Wizard of Oz' == selMovie:
        mov = imgTheWizardofOz
    elif 'Journey Back to Oz' == selMovie:
        mov = imgJourneyBacktoOz
    elif 'Oz The Great and Powerful' == selMovie:
        mov = imgOzTheGreatandPowerful
    elif 'Return to Oz' == selMovie:
        mov = imgReturntoOz
    elif 'Back to the Future' == selMovie:
        mov = imgBacktotheFuture
    elif 'Back to the Future Part II' == selMovie:
        mov = imgBacktotheFuturePartII
    elif 'Back to the Future Part III' == selMovie:
        mov = imgBacktotheFuturePartIII
    elif 'Journey to the Center of the Earth' == selMovie:
        mov = imgJourneytotheCenteroftheEarth
    elif 'Journey 2 The Mysterious Island' == selMovie:
        mov = imgJourney2TheMysteriousIsland
    elif 'Halloween' == selMovie:
        mov = imgHalloween
    elif 'Halloween II' == selMovie:
        mov = imgHalloweenII
    elif 'Halloween III Season of the Witch' == selMovie:
        mov = imgHalloweenIIISeasonoftheWitch
    elif 'Halloween 4 The Return of Michael Myers' == selMovie:
        mov = imgHalloween4TheReturnofMichaelMyers
    elif 'Halloween 5 The Revenge of Michael Myers' == selMovie:
        mov = imgHalloween5TheRevengeofMichaelMyers
    elif 'Halloween The Curse of Michael Myers' == selMovie:
        mov = imgHalloweenTheCurseofMichaelMyers
    elif 'Halloween H20 20 Years Later' == selMovie:
        mov = imgHalloweenH2020YearsLater
    elif 'Halloween Resurrection' == selMovie:
        mov = imgHalloweenResurrection
    elif 'Halloween(2018)' == selMovie:
        mov = imgHalloween2018
    elif 'Halloween Kills' == selMovie:
        mov = imgHalloweenKills
    elif 'Halloween Ends' == selMovie:
        mov = imgHalloweenEnds
    elif 'Spider-Man' == selMovie:
        mov = imgSpiderMan
    elif 'Spider-Man 2' == selMovie:
        mov = imgSpiderMan2
    elif 'Spider-Man 3' == selMovie:
        mov = imgSpiderMan3
    elif 'The Amazing Spider-Man' == selMovie:
        mov = imgTheAmazingSpiderMan
    elif 'The Amazing Spider-Man 2' == selMovie:
        mov = imgTheAmazingSpiderMan2
    
    
    mov = mov.subsample(multiplier*3)
    
    lblMBTitle = Label(frmMovieBox, text=selMovie)
    ChangeSize(lblMBTitle, 'Helvetica bold', int(baseSize/2))
    lblMBTitle.place(relx=0.08, rely=0.1, anchor="center")

    
    #Create the button with the logo
    lblMBCover = Label(frmMovieBox,image=mov, highlightthickness = 0, highlightbackground="black")
    lblMBCover.place(relx=0.08, rely=0.58,anchor="center") # place the button based on the section

    # Create button to view the show info
    btnMBView = Button(frmMovieBox, text="VIEW", command= lambda selMovie = selMovie :ShowInfoCreate(selMovie))
    ChangeSize(btnMBView, 'Helvetica bold', int(baseSize*2.8))
    btnMBView.place(relx=0.47, rely=0.5, anchor="center")

    # create button to add to watch later
    btnMBWatch = Button(frmMovieBox, text="Watch Later", command= lambda selMovie = selMovie :ShowInfoCreate(selMovie))
    ChangeSize(btnMBWatch, 'Helvetica bold', int(baseSize*2.8))
    btnMBWatch.place(relx=0.8, rely=0.5, anchor="center")


    
def GlobalImageFile(selMovie):
    global imgShrek, imgRiseOfTheGuardians, imgShrek2, imgShrektheThird, imgTheWizardofOz, imgJourneyBacktoOz, imgOzTheGreatandPowerful, imgReturntoOz, imgBacktotheFuture, imgBacktotheFuturePartII, imgBacktotheFuturePartIII, imgJourneytotheCenteroftheEarth, imgJourney2TheMysteriousIsland, imgHalloween, imgHalloweenII, imgHalloweenIIISeasonoftheWitch, imgHalloween4TheReturnofMichaelMyers, imgHalloween5TheRevengeofMichaelMyers, imgHalloweenTheCurseofMichaelMyers, imgHalloweenH2020YearsLater, imgHalloweenResurrection, imgHalloween2018, imgHalloweenKills, imgHalloweenEnds, imgSpiderMan, imgSpiderMan2, imgSpiderMan3, imgTheAmazingSpiderMan, imgTheAmazingSpiderMan2
    imgShrek = PhotoImage(file='Movie Covers/Shrek.png')
    imgRiseOfTheGuardians = PhotoImage(file='Movie Covers/Rise of the Guardians.png')
    imgShrek2 = PhotoImage(file='Movie Covers/Shrek 2.png')
    imgShrektheThird = PhotoImage(file='Movie Covers/Shrek the Third.png')
    imgTheWizardofOz = PhotoImage(file='Movie Covers/The Wizard of Oz.png')
    imgJourneyBacktoOz = PhotoImage(file='Movie Covers/Journey Back to Oz.png')
    imgOzTheGreatandPowerful = PhotoImage(file='Movie Covers/Oz The Great and Powerful.png')
    imgReturntoOz = PhotoImage(file='Movie Covers/Return to Oz.png')
    imgBacktotheFuture = PhotoImage(file='Movie Covers/Back to the Future.png')
    imgBacktotheFuturePartII = PhotoImage(file='Movie Covers/Back to the Future Part II.png')
    imgBacktotheFuturePartIII = PhotoImage(file='Movie Covers/Back to the Future Part III.png')
    imgJourneytotheCenteroftheEarth = PhotoImage(file='Movie Covers/Journey to the Center of the Earth.png')
    imgJourney2TheMysteriousIsland = PhotoImage(file='Movie Covers/Journey 2 The Mysterious Island.png')
    imgHalloween = PhotoImage(file='Movie Covers/Halloween.png')
    imgHalloweenII = PhotoImage(file='Movie Covers/Halloween II.png')
    imgHalloweenIIISeasonoftheWitch = PhotoImage(file='Movie Covers/Halloween III Season of the Witch.png')
    imgHalloween4TheReturnofMichaelMyers = PhotoImage(file='Movie Covers/Halloween 4 The Return of Michael Myers.png')
    imgHalloween5TheRevengeofMichaelMyers = PhotoImage(file='Movie Covers/Halloween 5 The Revenge of Michael Myers.png')
    imgHalloweenTheCurseofMichaelMyers = PhotoImage(file='Movie Covers/Halloween The Curse of Michael Myers.png')
    imgHalloweenH2020YearsLater = PhotoImage(file='Movie Covers/Halloween H20 20 Years Later.png')
    imgHalloweenResurrection = PhotoImage(file='Movie Covers/Halloween Resurrection.png')
    imgHalloween2018 = PhotoImage(file='Movie Covers/Halloween(2018).png')
    imgHalloweenKills = PhotoImage(file='Movie Covers/Halloween Kills.png')
    imgHalloweenEnds = PhotoImage(file='Movie Covers/Halloween Ends.png')
    imgSpiderMan = PhotoImage(file='Movie Covers/Spider-Man.png')
    imgSpiderMan2 = PhotoImage(file='Movie Covers/Spider-Man 2.png')
    imgSpiderMan3 = PhotoImage(file='Movie Covers/Spider-Man 3.png')
    imgTheAmazingSpiderMan = PhotoImage(file='Movie Covers/The Amazing Spider-Man.png')
    imgTheAmazingSpiderMan2 = PhotoImage(file='Movie Covers/The Amazing Spider-Man 2.png')

def ReviewCreate():
    print("hi")

def MatchCreate():
    global dfMovies, dfUser
    
    dfMovieTest = pd.read_csv("Files/dfMovieTestFrame.CSV")

    
    for indexM, rowM in dfMovies.iterrows(): # loop through each row of the data
        dfGenre = pd.read_csv("Files/Genre.CSV")
        inside = False
        for indexU, rowU in dfUser.iterrows(): # loop through each row of the data 
            if rowU["Title"] == rowM["Title"]:
                inside = True

        if inside == False:
            try:
                gen = rowM["Genre"].split("/")
            except:
                gen = [rowM["Genre"]]
            for item in gen:
                print(gen)
                print(item)
                dfGenre.at[0, item] = 1
            print(dfGenre)
            genre = (str(dfGenre.to_numpy().flatten())).strip("[").strip("]")
            print(genre, "genre")
            
            dfTemp = pd.DataFrame({"Title":rowM["Title"], "Genre":genre, "Type":rowM["Type"], "Length":rowM["Length"], "Year":rowM["Year"]}, index=[rowM["Title"]])
            dfMovieTest = pd.concat([dfMovieTest, dfTemp ])
    dfMovieTest = dfMovieTest.reset_index(drop=True)

    NeuralNetwork(dfUser, dfMovieTest)
    

    

def WatchLaterCreate():
    print("hi")

def AddShowCreate():
    global window, frmAddShowTop, frmAddShow, multiplier, baseSize, entASRating, selASType, entASTitle, entASGenre, dropASType, entASLength, entASYear, entASFile, lblASCover, imgPlus, topSpace, bottomSpace, imgASTPlus, topWidth, mainWidth, topHeight, mainHeight, imgEmptyCover, imgDownArrow, imgASDownArrow
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
    ChangeSize(lblASTHeading,'Helvetica bold', int(baseSize*1.7))
    lblASTHeading.place(relx=0.01, rely=0.06, anchor="nw")


    lblASTLogo = Label(frmAddShowTop, image=imgASTPlus)
    lblASTLogo.place(relx=0.99, rely=0.06, anchor="ne")

    # create the elements on screen
    lblASTitle = Label(frmAddShow, text="Title")
    ChangeSize(lblASTitle,'Helvetica bold', baseSize*2)
    lblASTitle.place(relx=0.5, rely=0.01, anchor="n")

    entASTitle = Entry(frmAddShow)
    ChangeSize(entASTitle,'Helvetica bold', baseSize*2)
    entASTitle.config(width=int(40/multiplier))
    entASTitle.place(relx=0.5, rely=0.1, anchor="n")

    lblASFile = Label(frmAddShow, text="Enter File Path")
    ChangeSize(lblASFile,'Helvetica bold', int(baseSize/1.5))
    lblASFile.place(relx=0.01, rely=0.2, anchor="nw")

    entASFile = Entry(frmAddShow)
    ChangeSize(entASFile,'Helvetica bold', int(baseSize/1.5))
    entASFile.place(relx=0.01, rely=0.25, anchor="nw")

    btnASLoad = Button(frmAddShow, command=AddShowConfigure, text="Load", width=int(baseSize/5))
    ChangeSize(btnASLoad,'Helvetica bold', int(baseSize/2))
    btnASLoad.place(relx=0.2, rely=0.247, anchor="nw")

    lblASCover = Label(frmAddShow, borderwidth=1, relief="solid", image=imgASEmptyCover)
    lblASCover.place(relx=0.01, rely=0.32, anchor="nw")

    lblASType = Label(frmAddShow, text="Type")
    ChangeSize(lblASType, 'Helvetica bold', int(baseSize*1.5))
    lblASType.place(relx=0.45, rely=0.25, anchor="center")

    lblASGenre = Label(frmAddShow, text="Genre")
    ChangeSize(lblASGenre, 'Helvetica bold', int(baseSize*1.5))
    lblASGenre.place(relx=0.7, rely=0.25, anchor="center")

    lblASLength = Label(frmAddShow, text="Length")
    ChangeSize(lblASLength, 'Helvetica bold', int(baseSize*1.5))
    lblASLength.place(relx=0.45, rely=0.46, anchor="center")

    lblASYear = Label(frmAddShow, text="Year")
    ChangeSize(lblASYear, 'Helvetica bold', int(baseSize*1.5))
    lblASYear.place(relx=0.7, rely=0.46, anchor="center")

    dropASType = OptionMenu(frmAddShow, selASType, *types)
    ChangeSize(dropASType, 'Helvetica bold', int(baseSize*1.5))
    dropASType.place(relx=0.45, rely=0.36, anchor="center")
    dropASType.config(compound='right', image=imgASDownArrow, width=baseSize*11)
    dropASType.image=imgASDownArrow

    entASGenre = Entry(frmAddShow,width=int(baseSize/2))
    ChangeSize(entASGenre, 'Helvetica bold', int(baseSize*1.2))
    entASGenre.place(relx=0.73, rely=0.36, anchor="center")

    entASLength = Entry(frmAddShow,width=int(baseSize/2))
    ChangeSize(entASLength, 'Helvetica bold', int(baseSize*1.2))
    entASLength.place(relx=0.45, rely=0.54, anchor="center")

    entASYear = Entry(frmAddShow,width=int(baseSize/2))
    ChangeSize(entASYear, 'Helvetica bold', int(baseSize*1.2))
    entASYear.place(relx=0.73, rely=0.54, anchor="center")

    lblASRating = Label(frmAddShow, text="Rating")
    ChangeSize(lblASRating, 'Helvetica bold', int(baseSize*1.5))
    lblASRating.place(relx=0.6, rely=0.61, anchor="center")

    entASRating = Entry(frmAddShow,width=int(baseSize/2))
    ChangeSize(entASRating, 'Helvetica bold', int(baseSize*1.2))
    entASRating.place(relx=0.6, rely=0.69, anchor="center")

    btnASAdd = Button(frmAddShow, text="ADD", width=baseSize, command=AddShow)
    ChangeSize(btnASAdd, 'Helvetica bold', int(baseSize*1.2))
    btnASAdd.place(relx=0.5, rely=0.9, anchor="center")

def AddShowConfigure():
    global entASFile, lblASCover, imgMovieCover, multiplier, imgCover
    # collects the file path and swaps any back slashes to forward slashes and removes any ""
    filePath = (entASFile.get()).replace("\\", "/").strip('"')


    # resize the image to the base size
    imgCover = Image.open(filePath)
    imgCoverResize = imgCover.resize((int(850/multiplier),int(1250/multiplier)))
    imgCover = ImageTk.PhotoImage(imgCoverResize)

    # resize the image to the screen size and configure the lbl to appear on screen
    #imgMovieCover = PhotoImage(file="Movie Covers/" + fileName)
    #imgMovieCover = imgCoverResize.subsample(multiplier)
    lblASCover.config(image=imgCover)

def AddShow():
    global entASTitle, entASFile, entASGenre, dropASType, entASLength, entASYear, selASType, accountUsername, entASRating
    # read from libary file
    libaryDataFrame = pd.read_csv("Files/Libary.CSV")


    # get the name of the image 
    fileName = "Movie Covers/" + entASTitle.get() + ".png"

    # resize the image to the base size
    imgCover = Image.open(filePath)
    imgCoverResize = imgCover.resize((800,1200))
    imgCoverResize.save("Movie Covers/" + fileName)

    # add new item to the data frame and save to file
    addDataFrame = pd.DataFrame({"Title":entASTitle.get(), "File":fileName, "Genre":entASGenre.get(), "Type":selASType.get(), "Length":entASLength.get(), "Year":entASYear.get()}, index=[entASTitle.get()])
    libaryFile = pd.concat([libaryDataFrame, addDataFrame])
    libaryFile.to_csv("Files/Libary.CSV",index=False)

    userFile = open("User Files/" + accountUsername + ".csv", "a")
    userFile.write("\n" + entASTitle.get() + "," + entASGenre.get() + "," + selASType.get() + "," + entASLength.get() + "," + entASYear.get()) 
    # return to the home screen
    
    HomeLoad()
    


    
def SearchLoad():
    global frmSearchTop, frmSearch, frmHome
    # clear previous screens
    ClearScreens()
    # load new screen
    frmSearchTop.grid(column=1,row=0,sticky="N")
    frmSearch.grid(column=1,row=1,sticky="NW")

def ReviewLoad():
    # clear previous screens
    ClearScreens()

def MatchLoad():
    # clear previous screens
    ClearScreens()

def WatchLaterLoad():
    # clear previous screens
    ClearScreens()

def AddShowLoad():
    global frmAddShow, frmAddShowTop
    # clear previous screens
    ClearScreens()

    # load new screens
    frmAddShowTop.grid(column=1,row=0,sticky="NE")
    frmAddShow.grid(column=1,row=1,sticky="NE")

def ShowInfoCreate(selMovie):
    global dfMovies, dfUser, accountUsernameG, window, entSIRating, mainHeight, mainWidth, topHeight, topWidth, frmShowInfoTop, frmShowInfo, multiplier, baseSize, imgSICover
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
    dfUser = pd.read_csv("User Files/" + accountUsernameG + ".csv")
    
    
    

    lblSITTitle = Label(frmShowInfoTop, text="SHOW INFO")
    ChangeSize(lblSITTitle, 'Helvetica bold', int(baseSize*1.5))
    lblSITTitle.place(relx=0.05, rely=0.5, anchor="w")

    lblSITIcon = Label(frmShowInfoTop, text="Add Camera icon")
    lblSITIcon.place(relx=0.95, rely=0.5, anchor="e")

    # add elements on the main part of the screen
    lblSITitle = Label(frmShowInfo, text=showTitle)
    ChangeSize(lblSITitle, 'Helvetica bold', int(baseSize*3))
    lblSITitle.place(relx=0.5, rely=0.1, anchor="center")
    
        # save image and resize
    imgSICover = (PhotoImage(file="Movie Covers/" + showFile )).subsample(int(multiplier/1.5))
    
    lblSICover = Label(frmShowInfo, image=imgSICover)
    lblSICover.place(relx=0.001, rely=0.5, anchor="w")

    # add info about movie
    lblSIYear = Label(frmShowInfo, text="   YEAR   \n\n" + showYear, borderwidth = 2, relief="solid", width=int(mainWidth/130))
    ChangeSize(lblSIYear, 'Helvetica bold', int(baseSize*1.7))
    lblSIYear.place(relx=0.55, rely=0.4, anchor="se")

    lblSILength = Label(frmShowInfo, text="LENGTH\n\n" + showLength, borderwidth = 2, relief="solid", width=int(mainWidth/130))
    ChangeSize(lblSILength, 'Helvetica bold', int(baseSize*1.7))
    lblSILength.place(relx=0.55, rely=0.4, anchor="sw")

    lblSIGenre = Label(frmShowInfo, text="  GENRE \n\n" + showGenre, borderwidth = 2, relief="solid", width=int(mainWidth/130))
    ChangeSize(lblSIGenre, 'Helvetica bold', int(baseSize*1.7))
    lblSIGenre.place(relx=0.55, rely=0.4, anchor="ne")

    lblSIType = Label(frmShowInfo, text="  TYPE   \n\n" + showType + "\n", borderwidth = 2, relief="solid", width=int(mainWidth/130))
    ChangeSize(lblSIType, 'Helvetica bold', int(baseSize*1.7))
    lblSIType.place(relx=0.55, rely=0.4, anchor="nw")

    lblSIRate = Label(frmShowInfo, text="ADD RATING")
    ChangeSize(lblSIRate,  'Helvetica bold', baseSize)
    lblSIRate.place(relx=0.9, rely=0.15, anchor="center")

    rated = False
    for index, row in dfUser.iterrows(): # loop through each row of the data 
        if row["Title"] == selMovie:
            lblSIRate.config(text="YOUR RATING")
            rated = True
    if rated == True:
        lblSIRating = Label(frmShowInfo, text=row["Rating"])
        ChangeSize(lblSIRating,  'Helvetica bold', baseSize)
        lblSIRating.place(relx=0.9, rely=0.2, anchor="center")
        print("True")
    elif rated == False:
        entSIRating = Entry(frmShowInfo, width=int(mainWidth/150))
        ChangeSize(entSIRating,  'Helvetica bold', baseSize)
        entSIRating.place(relx=0.9, rely=0.2, anchor="center")

        btnSISubmit = Button(frmShowInfo, text="SUBMIT", command=lambda selMovie=selMovie: RefreshShowInfo(selMovie))
        ChangeSize(btnSISubmit,  'Helvetica bold', baseSize)
        btnSISubmit.place(relx=0.9, rely=0.28, anchor="center")

        
        print("False")
    else:
        print("else")
        
    

    ShowInfoLoad()

def RefreshShowInfo(selMovie):
    global entSIRating, accountUsernameG, dfUser, dfMovies
    rating = entSIRating.get()

    file = open("User Files/" + accountUsernameG + ".csv", "a")
    for index, row in dfMovies.iterrows(): # loop through each row of the data
        if row["Title"] == selMovie:
            file.write("\n" + row["Title"] + "," + row["Genre"] + "," + row["Type"] + "," + str(row["Length"]) + "," + str(row["Year"]) + "," + str(rating))
        
    file.close()

    ClearScreens()
    ShowInfoCreate(selMovie)
    
    

def ShowInfoLoad():
    global frmShowInfoTop, frmShowInfo
    # clear previous screens
    ClearScreens()

    # load new screens
    frmShowInfoTop.grid(column=1,row=0,sticky="NE")
    frmShowInfo.grid(column=1,row=1,sticky="NE")
    
    
    

