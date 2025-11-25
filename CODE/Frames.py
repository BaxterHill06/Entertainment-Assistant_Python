'''
 ____ ____ ____ ____ ____ ____
||B |||a |||x |||t |||e |||r ||
||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|
Version 9
last updated: 04/07/23
'''


# note/ remimndering
#try manualy entering the width or height of the label or maybe the frame to see if we can bypass the "   " and \n

from tkinter import *
from Images import *
from functions import *
import pandas as pd
import PIL
from PIL import Image

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
    global frmLogin, frmAccountLogin, frmAddAccount, frmSearchTop, frmSearch, frmHomeTop, frmHome, frmReviewTop, frmReview, frmMatchTop, frmMatch, frmWatchLaterTop, frmWatchLater, frmAddShowTop, frmAddShow
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


def ClearScreens():
    global frmLogin ,frmAccountLogin, frmSearchTop, frmSearch, frmHomeTop, frmHome, frmReviewTop, frmReview, frmMatchTop, frmMatch, frmWatchLaterTop, frmWatchLater, frmAddShowTop, frmAddShow
    frames = [frmLogin ,frmAccountLogin, frmAddAccount, frmSearchTop, frmSearch, frmHomeTop, frmHome, frmReviewTop, frmReview, frmMatchTop, frmMatch, frmWatchLaterTop, frmWatchLater, frmAddShowTop, frmAddShow]
    for frame in frames:
        try:
            frame.grid_forget()
        except:
            pass




def LoginCreate(win,spa,screenPage):
    global frmLogin,imgPlus,window,space, multiplier, baseSize, imgLGPlus, height, width
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




    print("height:", height, "width:", width)
    #create Frame
    frmLogin = Frame(window, bg="white", width=width-35, height=height-20, highlightbackground="blue", highlightthickness=4)


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
    global baseSize,multiplier, imgLGLeftArrow, imgLGRightArrow, frmLogin, localIcon,window, space, imgSmurf, imgJoker, imgKyle, imgMando, imgPredator, imgR2, imgTransformer, imgYoda, imgHomer, imgHedwig, imgGrinch, imgDarthVader, imgC3PO, imgBlackPanther, imgRightArrow, imgLeftArrow
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
    #crate account file with username, password, icon, personal file location
    userFile = pd.read_csv("UserFile.csv",)
    addArray = pd.DataFrame({"Username":username.get(),"Password":password.get(),"Icon":icon.get(),"File":username.get() + ".csv"},index=[username.get()])
    userFile = pd.concat([userFile,addArray])
    userFile.to_csv("UserFile.csv",index=False)
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
    global entALPassword, lblALMessage
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

    HomeCreate()

def HomeCreate():
    global window, frmHome, baseSize, multiplier, bottomSpace, topSpace, frmHomeTop, height, width, topWidth, mainWidth, topHeight, mainHeight
    #  create variable with spacific size for  the top bar and main dscreent
    topHeight = (height - 20) / 11
    topWidth = ((width - 35) / 13) * 12
    mainHeight = ((height - 20) / 12) * 11
    mainWidth = ((width - 35) / 13) * 12

    # create frames
    frmHome = Frame(window, height=mainHeight, width=mainWidth)
    frmHomeTop = Frame(window, highlightbackground="black", highlightthickness=1, height=topHeight, width=topWidth)


    # create sub headings
    lblHORecent = Label(frmHome, text="Recently Added")
    ChangeSize(lblHORecent, 'Helvetica bold', int(baseSize*0.33))
    lblHORecent.place(relx=0.05, rely=0,anchor="nw")

    lblHOHigh = Label(frmHome, text="Highly Rated")
    ChangeSize(lblHOHigh, 'Helvetica bold', int(baseSize*0.33))
    lblHOHigh.place(relx=0.05, rely=0.48,anchor="nw")


    HomeLoad()

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
    global window, space, frmSearch, frmSearchTop, topSpace, bottomSpace, baseSize, multiplier, topWidth, mainWidth, topHeight, mainHeight
    # create frames
    frmSearchTop = Frame(window, highlightbackground="black", highlightthickness=1, width=topWidth, height=topHeight)
    frmSearch = Frame(window, width=mainWidth, height=mainHeight)


    # create elements on screen
    lblSRTHeading = Label(frmSearchTop, text="SEARCH")
    ChangeSize(lblSRTHeading,  'Helvetica bold', int(baseSize))
    lblSRTHeading.place(relx=0.01, rely=0.1, anchor="nw")


    lblSRTLength = Label(frmSearchTop, text="Length")
    lblSRTLength.place(relx=0.01, rely=0.01, anchor="nw")

    lblSRTType = Label(frmSearchTop, text="Type")
    lblSRTType.place(relx=0.01, rely=0.01, anchor="nw")

    lblSRTYear = Label(frmSearchTop, text="Year")
    lblSRTYear.place(relx=0.01, rely=0.01, anchor="nw")

    lblSRTGenre = Label(frmSearchTop, text="Genre")
    lblSRTGenre.place(relx=0.01, rely=0.01, anchor="nw")

    lblSRTTitle = Label(frmSearchTop, text="Title")
    lblSRTTitle.place(relx=0.01, rely=0.01, anchor="nw")









def ReviewCreate():
    print("hi")

def MatchCreate():
    print("hi")

def WatchLaterCreate():
    print("hi")

def AddShowCreate():
    global window, frmAddShowTop, frmAddShow, multiplier, baseSize, entASFile, lblASCover, imgPlus, topSpace, bottomSpace, imgASTPlus, topWidth, mainWidth, topHeight, mainHeight, imgEmptyCover, imgDownArrow, imgASDownArrow
    # create the frames
    frmAddShowTop = Frame(window, highlightbackground="black", highlightthickness=1, width=topWidth, height=topHeight)
    frmAddShow = Frame(window, width=mainWidth, height=mainHeight)

    # get the array with the types e.g. Movie or tv show
    types = GetTypes()
    selASType = StringVar()

    # change size of image
    imgASDownArrow = imgDownArrow.subsample(multiplier*3)



    #create the elements on the top bar
    lblASTHeading = Label(frmAddShowTop, text="ADD SHOW")
    ChangeSize(lblASTHeading,'Helvetica bold', int(baseSize*1.7))
    lblASTHeading.place(relx=0.01, rely=0.06, anchor="nw")

    # change size of image
    imgASTPlus = imgPlus.subsample(int(13 / multiplier))
    imgASEmptyCover = imgEmptyCover.subsample(multiplier)

    lblASTLogo = Label(frmAddShowTop, image=imgASTPlus)
    lblASTLogo.place(relx=0.95, rely=0.06, anchor="ne")

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
    dropASType.config(compound='right', image=imgASDownArrow, width=baseSize*11) #width=int(baseSize/3)) #, image=imgASArrowDown)
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
    global entASFile, lblASCover, imgMovieCover, multiplier
    filePath = (entASFile.get()).replace("\\", "/").strip('"')
    fileName = (filePath.split("/"))
    fileName = fileName[len(fileName)-1]
    imgCover = Image.open(filePath)
    print(imgCover.height)
    imgCoverResize = imgCover.resize((800,1200))
    imgCoverResize.save("Movie Covers/" + fileName)


    imgMovieCover = PhotoImage(file="Movie Covers/" + fileName)
    imgMovieCover = imgMovieCover.subsample(multiplier)
    lblASCover.config(image=imgMovieCover)

def AddShow():
    pass

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
    global frmSearchTop, frmSearch, frmHome, frmAddShow, frmAddShowTop, frmHomeTop
    # clear previous screens
    ClearScreens()

    # load new screen
    frmAddShowTop.grid(column=1,row=0,sticky="NE")
    frmAddShow.grid(column=1,row=1,sticky="NE")

