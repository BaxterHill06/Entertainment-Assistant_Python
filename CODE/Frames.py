'''
 ____ ____ ____ ____ ____ ____
||B |||a |||x |||t |||e |||r ||
||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|
Version 5
last updated: 20/06/23
'''

from tkinter import *
from Images import *

def GetImages():
    global plus,empLogo
    plus = PhotoImage(file="plus.png")
    empLogo = PhotoImage(file="empty_logo.png")


#change font and size
def ChangeSize(item,font,size):
    item.config(font=(font,size))



#create Exit bar
def ExitCreate(window):
    menuBar = Menu(window)
    topBar = Menu(menuBar,tearoff=0)
    topBar.add_command(label="Exit", command=window.destroy)
    menuBar.add_cascade(label="Exit", menu=topBar)
    window.config(menu=menuBar)

    
def LoginCreate(window,space):
    global frmLogin,plus
    #gather images needed
    
    #create Frame
    frmLogin = Frame(window, bg="white")

    #fill the screen
    lblLGSize = Label(frmLogin, text=space)
    lblLGSize.pack(side="top", fill="both", expand=True)


    # create heading
    lblLGLogin = Label(frmLogin,text="LOGIN")
    ChangeSize(lblLGLogin,'Helvetica bold', 70)
    lblLGLogin.place(relx=0.40, rely=0)


    # create ADD button
    btnLGAdd = Button(frmLogin,image=plus, command=AddAccountLoad, highlightthickness = 0, bd = 0)
    btnLGAdd.place(relx=0.75, rely=0.5)

    #add a label under the plus symbol
    lblLGAdd = Label(frmLogin, text="ADD")
    ChangeSize(lblLGAdd,'Helvetica bold', 30)
    lblLGAdd.place(relx=0.79, rely=0.76)
    return frmLogin



def LoginLoad(frmLogin):
    #forget the other screens that could be on screen

    #load the Login screen
    frmLogin.grid()


def AddAccountCreate(window,space):
    global frmAddAccount,empLogo, selAAIcon,lblAALogo
    frmAddAccount = Frame(window)
    
    #fill the screen
    lblAASize = Label(frmAddAccount, text=space)
    lblAASize.pack(side="top", fill="both", expand=True)
    
    #gather needed images 
    empLogo = PhotoImage(file="empty_logo.png")
    icons = GatherIcons()
    
    
    #create logo image
    lblAALogo = Label(frmAddAccount, image=empLogo)
    lblAALogo.place(relx=0.42, rely=0.05)

    #add dropdown for selection icon
    selAAIcon = StringVar()
    dropAALogo = OptionMenu(frmAddAccount, selAAIcon , *icons,)
    dropAALogo.config(width=10,height=2)
    ChangeSize(dropAALogo,'Helvetica bold', 30)
    dropAALogo.place(relx=0.65, rely=0.15)
    

    #add a select button for the icon
    btnAASelect = Button(frmAddAccount, text="SELECTING", command=IconConfigure)
    ChangeSize(btnAASelect,'Helvetica bold', 15)
    btnAASelect.place(relx=0.70, rely=0.3)


    

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


