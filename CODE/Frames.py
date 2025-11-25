'''
 ____ ____ ____ ____ ____ ____
||B |||a |||x |||t |||e |||r ||
||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|
Version 6
last updated: 25/06/23
'''


from tkinter import *
from Images import *
from functions import *
import pandas as pd

def GetImages():
    global imgPlus,imgEmpLogo,imgSmurf, imgJoker, imgKyle, imgMando, imgPredator, imgR2, imgTransformer, imgYoda, imgHomer, imgHedwig, imgGrinch, imgDarthVader, imgC3PO, imgBlackPanther, imgBook, imgClock, imgExit, imgHeart, imgHouse, imgMagGlass, imgMenuPlus
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


#create Exit bar
def ExitCreate(window):
    menuBar = Menu(window)
    topBar = Menu(menuBar,tearoff=0)
    topBar.add_command(label="Exit", command=window.destroy)
    menuBar.add_cascade(label="Exit", menu=topBar)
    window.config(menu=menuBar)

    
def LoginCreate(win,spa):
    global frmLogin,imgPlus,window,space
    #def window and space so they can be globaled for other functions
    window = win
    space = spa


    #create Frame
    frmLogin = Frame(window, bg="white")

    #fill the screen
    ScreenFill(frmLogin,space)


    # create heading
    lblLGLogin = Label(frmLogin,text="LOGIN")
    ChangeSize(lblLGLogin,'Helvetica bold', 90)
    lblLGLogin.place(relx=0.5, rely=0.05, anchor="center")


    # create ADD button
    btnLGAdd = Button(frmLogin,image=imgPlus, command=AddAccountLoad, highlightthickness = 0, bd = 0)
    btnLGAdd.place(relx=0.8, rely=0.61, anchor= "center")

    #add a label under the plus symbol
    lblLGAdd = Label(frmLogin, text="ADD")
    ChangeSize(lblLGAdd,'Helvetica bold', 30)
    lblLGAdd.place(relx=0.8, rely=0.77, anchor="center")

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
        LoginIconCreate(accountUsername,accountPassword,accountIcon,element)



def LoginIconCreate(accountUsername,accountPassword, accountIcon,element):
    global frmLogin, localIcon, imgSmurf, imgJoker, imgKyle, imgMando, imgPredator, imgR2, imgTransformer, imgYoda, imgHomer, imgHedwig, imgGrinch, imgDarthVader, imgC3PO, imgBlackPanther
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

    page = (element // 3) + 1 # returns the page value by determining the remainder and adding 1
    section = (element % 3) + 1 # returns the section by determining the quotient and adding 1

    #Create the button with the logo
    btnLGAccount = Button(frmLogin,image=imageFile, highlightthickness = 0, bd = 0, command= lambda name = accountUsername, password = accountPassword,icon = imageFile:AccountLoginLoad(name,password,icon))
    btnLGAccount.place(relx=section * 0.2, rely=0.61,anchor="center") # place the button based on the section
    lblLGAccount = Label(frmLogin,text=accountUsername)# create the label wit hthe username
    ChangeSize(lblLGAccount, 'Helvetica bold', 30) # change the font and size
    lblLGAccount.place(relx=section * 0.2, rely=0.77,anchor="center") # place below the logo



def LoginLoad():
    global frmAddAccount, frmBar, frmLogin, frmHome
    #forget the other screens that could be on screen
    frmAddAccount.grid_forget()
    frmAccountLogin.grid_forget()
    try: # insures the software still runs if the frame has not been created yet
        frmBar.grid_forget()
        print("in2")
    except:
        pass
    try:
        frmHome.grid_forget()
        print("inside")
    except:
        pass
    #load the Login screen
    frmLogin.grid()
    print("run")


def AddAccountCreate():
    global frmAddAccount,imgEmpLogo, selAAIcon,lblAALogo, window, space
    frmAddAccount = Frame(window)
    
    #fill the screen
    ScreenFill(frmAddAccount,space)
    
    #gather needed images 
    imgEmpLogo = PhotoImage(file="empty_logo.png")
    icons = GatherIcons()
    
    
    #create logo image
    lblAALogo = Label(frmAddAccount, image=imgEmpLogo)
    lblAALogo.place(relx=0.42, rely=0.05)

    #add dropdown for selection icon
    selAAIcon = StringVar()
    dropAALogo = OptionMenu(frmAddAccount, selAAIcon , *icons,)
    dropAALogo.config(width=13,height=2)
    ChangeSize(dropAALogo,'Helvetica bold', 30)
    dropAALogo.place(relx=0.65, rely=0.15)
    

    #add a select button for the icon
    btnAASelect = Button(frmAddAccount, text="SELECT", command=IconConfigure)
    ChangeSize(btnAASelect,'Helvetica bold', 15)
    btnAASelect.place(relx=0.70, rely=0.3)

    #add "create username" label and entry
    lblAAUsername = Label(frmAddAccount, text="CREATE USERNAME")
    ChangeSize(lblAAUsername,'Helvetica bold', 30)
    lblAAUsername.place(relx=0.5,rely=0.43,anchor="center")

    entAAUsername = Entry(frmAddAccount)
    entAAUsername.config(width=40)
    ChangeSize(entAAUsername,'Helvetica bold',30)
    entAAUsername.place(relx=0.5,rely=0.5,anchor="center")



    #add "create password" label and entry
    lblAAPassword = Label(frmAddAccount, text="CREATE PASSWORD")
    ChangeSize(lblAAPassword,'Helvetica bold', 30)
    lblAAPassword.place(relx=0.5,rely=0.65,anchor="center")

    entAAPassword = Entry(frmAddAccount)
    entAAPassword.config(width=40)
    ChangeSize(entAAPassword,'Helvetica bold',30)
    entAAPassword.place(relx=0.5,rely=0.72,anchor="center")


    #add "CREATE" button
    btnAACreate = Button(frmAddAccount,text="CREATE", command= lambda username=entAAUsername, password=entAAPassword, icon=selAAIcon : CreateAccount(username,password,icon))
    btnAACreate.config(width=30,heigh=8)
    btnAACreate.place(relx=0.5, rely=0.9,anchor="center")

    # create back button
    btnAABack = Button(frmAddAccount, command=LoginLoad, text="BACK")
    ChangeSize(btnAABack, 'Helvetica bold', 30)
    btnAABack.place(rely=0.95, relx=0.05, anchor='sw')

#crate the users new account
def CreateAccount(username, password, icon):
    global window, space
    #crate account file with username, password, icon, personal file location
    userFile = pd.read_csv("UserFile.csv",)
    addArray = pd.DataFrame({"Username":username.get(),"Password":password.get(),"Icon":icon.get(),"File":username.get() + ".csv"},index=[username.get()])
    userFile = pd.concat([userFile,addArray])
    userFile.to_csv("UserFile.csv",index=False)
    LoginCreate(window,space)
    LoginLoad()


#change the image on screen to the icon selected by the user
def IconConfigure():
    global selAAIcon, lblAALogo,iconFile
    iconPath = "icons/" + selAAIcon.get() + ".png"
    iconFile = PhotoImage(file=iconPath)
    lblAALogo.config(image=iconFile)


def AddAccountLoad():
    global frmAddAccount,frmLogin
    #forget the other screens that could be on screen
    frmLogin.grid_forget()
    #load the Login screen
    frmAddAccount.grid()


def AccountLoginCreate():
    global window, space,imgEmpLogo, lblALMessage, frmAccountLogin, lblALLogo,lblALUsername, btnALLogin, entALPassword
    frmAccountLogin = Frame(window) # create the frame to place elements into

    #fill the screen
    ScreenFill(frmAccountLogin,space)

    # create logo label
    lblALLogo = Label(frmAccountLogin,image=imgEmpLogo)
    lblALLogo.place(relx=0.5, rely=0.15, anchor="center")

    # crate name label
    lblALUsername = Label(frmAccountLogin, text="")
    ChangeSize(lblALUsername,'Helvetica bold', 30)
    lblALUsername.place(relx=0.5 , rely=0.3, anchor="center")

    # create label and entry for password
    lblALPassword = Label(frmAccountLogin,text="ENTER PASSWORD:")
    ChangeSize(lblALPassword,'Helvetica bold', 60)
    lblALPassword.place(relx=0.5, rely=0.45, anchor="center")

    entALPassword = Entry(frmAccountLogin, width=25)
    ChangeSize(entALPassword, 'Helvetica bold', 50)
    entALPassword.place(relx=0.5, rely=0.58, anchor="center")

    # label to show any errors e.g. wrong password
    lblALMessage = Label(frmAccountLogin, text="", fg="red")
    ChangeSize(lblALMessage,'Helvetica bold', 30)
    lblALMessage.place(relx=0.5, rely=0.7, anchor="center")

    #create "LOGIN" Button
    btnALLogin = Button(frmAccountLogin,text="LOGIN", height=2, width=15)
    ChangeSize(btnALLogin, 'Helvetica bold', 30)
    btnALLogin.place(relx=0.5, rely=0.8, anchor="center")

    # create back button
    btnALBack = Button(frmAccountLogin, command=LoginLoad, text="BACK")
    ChangeSize(btnALBack, 'Helvetica bold', 30)
    btnALBack.place(rely=0.95, relx=0.05, anchor='sw')


def AccountLoginLoad(accountUsername, accountPassword, accountIcon):
    global frmAccountLogin, frmLogin,lblALLogo,lblALUsername,btnALLogin, imgSmurf, imgJoker, imgKyle, imgMando, imgPredator, imgR2, imgTransformer, imgYoda, imgHomer, imgHedwig, imgGrinch, imgDarthVader, imgC3PO, imgBlackPanther
    # forget previous frames
    frmLogin.grid_forget()

    # configure the logo with the users logo
    lblALLogo.config(image=accountIcon)

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
    global window, frmBar, imgBook, imgClock, imgExit, imgHeart, imgHouse, imgMagGlass
    frmBar = Frame(window,height=400, width = 400) # create side bar frame

    # create and pack menu buttons
    btnBRSearch = Button(frmBar, image=imgMagGlass,command=SearchLoad, highlightthickness = 0, bd = 0)
    btnBRSearch.pack()
    btnBRHome = Button(frmBar, image=imgHouse,command=HomeLoad, highlightthickness = 0, bd = 0)
    btnBRHome.pack()
    btnBRReview = Button(frmBar, image=imgBook, command=ReviewLoad, highlightthickness=0, bd=0)
    btnBRReview.pack()
    btnBRMatch = Button(frmBar, image=imgHeart, command=MatchLoad, highlightthickness=0, bd=0)
    btnBRMatch.pack()
    btnBRLater = Button(frmBar, image=imgClock, command=WatchLaterLoad, highlightthickness=0, bd=0)
    btnBRLater.pack()
    btnBRAdd = Button(frmBar, image=imgMenuPlus, command=AddShowLoad, highlightthickness=0, bd=0)
    btnBRAdd.pack()
    btnBRExit = Button(frmBar, image=imgExit, command=LoginLoad, highlightthickness=0, bd=0)
    btnBRExit.pack(pady=30)

    HomeCreate()

def HomeCreate():
    global window, frmHome
    frmHome = Frame(window, width = 500, height=500)
    barSpace = ScreenSpace(5,1)
    ScreenFill(frmHome,barSpace)



    HomeLoad()

def HomeLoad():
    global frmAccountLogin, frmBar, frmHome
    # forget previous screens
    frmAccountLogin.grid_forget()

    # create other screens
    SearchCreate()
    ReviewCreate()
    MatchCreate()
    WatchLaterCreate()
    AddShowCreate()



    #display the side bar and home screen
    frmBar.grid(column=0,row=0,sticky="NW")
    frmHome.grid(column=1,row=0)


def SearchCreate():
    print("hi")

def ReviewCreate():
    print("hi")

def MatchCreate():
    print("hi")

def WatchLaterCreate():
    print("hi")

def AddShowCreate():
    print("hi")




def SearchLoad():
    print("hi")

def ReviewLoad():
    print("hi")

def MatchLoad():
    print("hi")

def WatchLaterLoad():
    print("hi")

def AddShowLoad():
    print("hi")

