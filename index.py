import os
import tkMessageBox
import Tkinter
from Tkinter import *
import getpass
import subprocess
import time
import soldier

user=getpass.getuser()
def_nameofserver=""
def_enroll="" 
def_pass=""
def_syspass=""

top = Tkinter.Tk()

def hello():
   f=open('Details.txt','w+')
   f.write(str(sname.get())+'\n')
   f.write(str(uname.get())+'\n')
   f.write(str(passw.get())+'\n')
   f.write(str(sys_passw.get()))
   return
def sync(): #TODO
	soldier.run("python /home/"+user+"/File-Server-Sync-System-/samba.py", sudo=def_syspass)
def select_dir():#TODO
	soldier.run("python /home/"+user+"/File-Server-Sync-System-/main.py", sudo=def_syspass)
flag=0  

try:   
	f1=open('Details.txt','r')   
	def_nameofserver=f1.readline()
	def_enroll=f1.readline()
	def_pass=f1.readline()
	def_syspass=f1.readline()
except:
	flag=1 #If no details entered yet

B1 = Tkinter.Button(top, text = " Submit", command = hello,height=1)
B2 = Tkinter.Button(top, text = " Sync.  ", command = sync)
B3 = Tkinter.Button(top, text = " Select Directories  ", command = select_dir)
T = Text(top, height=2, width=10)
var = StringVar()
var_sname = StringVar()

label_sname = Label( top, textvariable=var_sname, relief=RAISED ) #sname=server_name
var_sname.set("Server name:")
label_sname.pack()

sname=Entry(top,width=25)
if flag==0:
	sname.insert(END,def_nameofserver[0:len(def_nameofserver)-1]) #to prevent newline character to enter
sname.pack()

label = Label( top, textvariable=var, relief=RAISED )
var.set("Enrollment Number:")
label.pack()

uname = Entry(top, width=25)
if flag==0:
	uname.insert(END,def_enroll[0:len(def_enroll)-1])
	#uname.insert(END,def_enroll)
var1 = StringVar()
label1 = Label( top, textvariable=var1, relief=RAISED )
var1.set("Password:")
passw = Entry(top, show="*", width=25)
if flag==0:
	passw.insert(END,def_pass[0:len(def_pass)-1])

var2 = StringVar()
label2 = Label( top, textvariable=var2, relief=RAISED )
var2.set("System password:")
sys_passw = Entry(top, show="*", width=25)
if flag==0:
	sys_passw.insert(END,def_syspass)

uname.pack()
label1.pack()
passw.pack()
label2.pack()
sys_passw.pack()
B1.pack()
B2.pack()
B3.pack()
top.mainloop()