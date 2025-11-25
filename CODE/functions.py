'''
 ____ ____ ____ ____ ____ ____
||B |||a |||x |||t |||e |||r ||
||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|
Version 5
last updated: 21/06/23
'''

import pandas as pd


def ScreenSpace():
    file = open("LTscreen.txt","r")
    array = []
    for line in file:
        array.append(int(line.strip("\n")))

    
    space = "       "*array[0] + "\n"*array[1]
    return space


#crate the users new account
def CreateAccount(username, password, icon):
    #crate account file with username, password, icon, personal file location
    userFile = pd.read_csv("UserFile.csv",)
    addArray = pd.DataFrame({"Username":username.get(),"Password":password.get(),"Icon":icon.get(),"File":username.get() + ".csv"},index=[username.get()])
    userFile = pd.concat([userFile,addArray])
    userFile.to_csv("UserFile.csv",index=False)
    print(userFile)
    LoginLoad()
    
    

    
