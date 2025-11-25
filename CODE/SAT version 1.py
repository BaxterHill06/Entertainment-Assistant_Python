'''
 ____ ____ ____ ____ ____ ____
||B |||a |||x |||t |||e |||r ||
||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|
Version 5
last updated: 19/6/23
'''

from tkinter import *

window = Tk()
window.geometry("800x600+20+20")

def AddScreen():
    print("hi")






#add images
plus = PhotoImage(file="plus.png")





# create heading
lblLogin = Label(window,text="LOGIN")
lblLogin.config(font=('Helvetica bold',40))
lblLogin.pack()

# create ADD button
btnAdd = Button(window,image=plus, command=AddScreen, highlightthickness = 0, bd = 0)
btnAdd.pack()

#
lblAdd = Label(window, text="ADD")
lblAdd.pack()

# run the user interface
window.mainloop()
