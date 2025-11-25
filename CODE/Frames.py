'''
 ____ ____ ____ ____ ____ ____
||B |||a |||x |||t |||e |||r ||
||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|
Version 5
last updated: 19/06/23
'''

from tkinter import *

#create Exit bar
def ExitCreate(window):
    menuBar = Menu(window)
    topBar = Menu(menuBar,tearoff=0)
    topBar.add_command(label="Exit", command=window.destroy)
    menuBar.add_cascade(label="Exit", menu=topBar)
    window.config(menu=menuBar)

    
def LoginCreate(window, plus,space):
    global frmLogin
    #create Frame
    frmLogin = Frame(window, bg="white")

    #fill the screen
    space = "       "*90 + "\n"*70
    label = Label(frmLogin, text=space)
    label.pack(side="top", fill="both", expand=True)


    # create heading
    lblLogin = Label(frmLogin,text="LOGIN")
    lblLogin.config(font=('Helvetica bold',70))
    lblLogin.place(relx=0.40, rely=0)


    # create ADD button
    btnAdd = Button(frmLogin,image=plus, command=AddAccountLoad, highlightthickness = 0, bd = 0)
    btnAdd.place(relx=0.75, rely=0.55)

    #add a label under the plus symbol
    lblAdd = Label(frmLogin, text="ADD")
    lblAdd.config(font=('Helvetica bold',30))
    lblAdd.place(relx=0.78, rely=0.76)
    return frmLogin



def LoginLoad(frmLogin):
    #forget the other screens that could be on screen

    #load the Login screen
    frmLogin.grid()


def AddAccountCreate(window,space):
    global frmAddAccount
    frmAddAccount = Frame(window)




def AddAccountLoad():
    global frmAddAccount
    global frmLogin
    #forget the other screens that could be on screen
    frmLogin.grid_forget()
    #load the Login screen
    frmAddAccount.grid()


