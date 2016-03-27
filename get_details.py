
#To save user's enrollment number and password in a text file named 'Details.txt'

import os
import tkMessageBox
import Tkinter
from Tkinter import *
top = Tkinter.Tk()



def hello():
   f=open('Details.txt','w')
   print uname.get() #Final username
   print passw.get() #Final password
   f.write(str(uname.get())+'\n')
   f.write(str(passw.get()))
   return
   
B1 = Tkinter.Button(top, text = "SUBMIT", command = hello)
T = Text(top, height=2, width=10)
var = StringVar()
label = Label( top, textvariable=var, relief=RAISED )
var.set("Enrollment Number:")
label.pack()
uname = Entry(top, width=25)
var1 = StringVar()
label1 = Label( top, textvariable=var1, relief=RAISED )
var1.set("Password:")
passw = Entry(top, show="*", width=25)
uname.pack()
label1.pack()
passw.pack()
B1.pack()
top.mainloop()

