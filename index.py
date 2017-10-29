import os
import smbclient
import tkMessageBox
import Tkinter
from Tkinter import *
import getpass
import subprocess
import time
import soldier
from Tkinter import Tk
from tkFileDialog import askopenfilename

user=getpass.getuser()
def_nameofserver=""
def_enroll="" 
def_pass=""
def_syspass=""

top = Tkinter.Tk()
top.wm_title("File Server Synchronization System")

path_details="""/home/"""+user+"/File-Server-Sync-System-/Details.txt"""
def hello():
   f=open(path_details,'w+')   
   f.write(str(sname.get())+'\n')
   f.write(str(uname.get())+'\n')
   f.write(str(passw.get())+'\n')
   f.write(str(sys_passw.get()))
   f.close() #
   return
def sync(): #TODO
	soldier.run("python /home/"+user+"/File-Server-Sync-System-/samba.py", sudo=def_syspass)
def select_dir():#TODO
	soldier.run("python /home/"+user+"/File-Server-Sync-System-/main.py", sudo=def_syspass)

def upload():
	fp=open(path_details,"r")	
	data = fp.read().splitlines()
	server = data[0]
	username = data[1]
	password = data[2]
	syspass=data[3]
	share=data[1]
	domain = "pdc.jiit"
	smb = smbclient.SambaClient(server, share, username, password, domain)
	Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
	path = askopenfilename() 
	filename= os.path.basename(path)	
	remote_path="""/"""+username+"""/"""
	smb.upload(path, remote_path) 
	smb.rename("""/"""+username,"""/"""+filename)

	os.system('notify-send  "File Uploaded" ')
	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % ( 1, 99999))
	fp.close()
	# print(filename)

flag=0  

try:   
	f1=open(path_details,'r')   
	def_nameofserver=f1.readline()
	def_enroll=f1.readline()
	def_pass=f1.readline()
	def_syspass=f1.readline()
except:
	flag=1 #If no details entered yet

B1 = Tkinter.Button(top, text = " Submit", command = hello,height=1)
B2 = Tkinter.Button(top, text = " Sync Manually ", command = sync)
B3 = Tkinter.Button(top, text = " Select Directories  ", command = select_dir)
B4 = Tkinter.Button(top, text = " Upload File  ", command = upload)

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
B4.pack()
top.mainloop()
#
