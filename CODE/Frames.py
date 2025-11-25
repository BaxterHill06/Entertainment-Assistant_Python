'''
 ____ ____ ____ ____ ____ ____ 
||B |||a |||x |||t |||e |||r ||
||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|
Version 5
last updated: 25/06/23
'''


from tkinter import *
from Images import *
from functions import *

def GetImages():
    global imgPlus,empLogo,imgSmurf, imgJoker, imgKyle, imgMando, imgPredator, imgR2, imgTransformer, imgYoda, imgHomer, imgHedwig, imgGrinch, imgDarthVader, imgC3PO, imgBlackPanther
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

#change font and size
def ChangeSize(item,font,size):
    item.config(font=(font,size))

def ScreenFill(frmLocal):
    global space
    lblAASize = Label(frmLocal, text=space) # create a label the size of the screen to allow for place
    lblAASize.pack(side="top", fill="both", expand=True)



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
    ScreenFill(frmLogin)


    # create heading
    lblLGLogin = Label(frmLogin,text="LOGIN")
    ChangeSize(lblLGLogin,'Helvetica bold', 70)
    lblLGLogin.place(relx=0.40, rely=0)


    # create ADD button
    btnLGAdd = Button(frmLogin,image=imgPlus, command=AddAccountLoad, highlightthickness = 0, bd = 0)
    btnLGAdd.place(relx=0.75, rely=0.5)

    #add a label under the plus symbol
    lblLGAdd = Label(frmLogin, text="ADD")
    ChangeSize(lblLGAdd,'Helvetica bold', 30)
    lblLGAdd.place(relx=0.79, rely=0.76)

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
    lblLGAccount.place(relx=section * 0.2, rely=0.8,anchor="center") # place below the logo



def LoginLoad():
    #forget the other screens that could be on screen
    frmAddAccount.grid_forget()
    #load the Login screen
    frmLogin.grid()


def AddAccountCreate():
    global frmAddAccount,imgEmpLogo, selAAIcon,lblAALogo, window, space
    frmAddAccount = Frame(window)
    
    #fill the screen
    ScreenFill(frmAddAccount)
    
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
    

#crate the users new account
def CreateAccount(username, password, icon):
    global window, space
    #crate account file with username, password, icon, personal file location
    userFile = pd.read_csv("UserFile.csv",)
    addArray = pd.DataFrame({"Username":username.get(),"Password":password.get(),"Icon":icon.get(),"File":username.get() + ".csv"},index=[username.get()])
    userFile = pd.concat([userFile,addArray])
    userFile.to_csv("UserFile.csv",index=False)
    print(userFile)
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
    global window, space,imgEmpLogo, frmAccountLogin, lblALLogo
    frmAccountLogin = Frame(window) # create the frame to place elements into

    #fill the screen
    ScreenFill(frmAccountLogin)


    lblALLogo = Label(frmAccountLogin,image=imgEmpLogo)
    lblALLogo.place(relx=0.5, rely=0.2, anchor="center")





def AccountLoginLoad(accountUsername, accountPassword, accountIcon):
    global frmAccountLogin, frmLogin,lblALLogo, imgSmurf, imgJoker, imgKyle, imgMando, imgPredator, imgR2, imgTransformer, imgYoda, imgHomer, imgHedwig, imgGrinch, imgDarthVader, imgC3PO, imgBlackPanther
    # forget previous frames
    frmLogin.grid_forget()

    # configure the logo with the users logo
    lblALLogo.config(image=accountIcon)




    # grid new frame
    frmAccountLogin.grid()


