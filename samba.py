import smbclient
import os
import datetime
import getpass
import subprocess
import time
import re


server="fileserver2"
share="""Study Material"""
username="13103535"
password="9899496277"
domain="pdc.jiit"
user=getpass.getuser()
attach= """/home/"""+user+"""/Documents"""

smb = smbclient.SambaClient(server,share ,username, password, domain)
local_file=[]
local_dir=[]#waste
remote_file=[]

def pathtodir(path):
	if not os.path.exists(path):
	    l=[]
	    p = "/"
	    l = path.split("/")
	    i = 1
	    while i < len(l):
	        p = p + l[i] + "/"
	        i = i + 1
	        if not os.path.exists(p):
	            os.mkdir(p)


with open("/home/"+user+"/File-Server-Sync-System-/path_file.txt", "r+") as f2:
	all_paths = [line.rstrip('\n') for line in f2]

for item in all_paths:
	if smb.exists(item):
		if smb.isdir(item):
			local_dir.append(attach+item)#waste
		else:
			remote_file.append(item)
			local_file.append(attach+item)
for i in local_file:
	pathtodir(os.path.dirname(i))
	
# print "all_paths=",all_paths
# print
# print	
# print "local_file=",local_file

for i,j in zip(remote_file,local_file): #HURRAY DONE !!! :D  YESSSSSSSSS!!!!!!!!
	dict_=smb.info(i)
	str_remote=re.sub(' +',' ',dict_["write_time"])
	remote_last_mod=str_remote.split(" ")[3]
	f=open(j,"w+")
	str_local=re.sub(' +',' ',time.ctime(os.path.getmtime(j)))
	local_last_mod=str_local.split(" ")[3]
	if remote_last_mod!=local_last_mod:
		smb.download(i,j)
		f.close()

os.system('notify-send "Your SM is now Synchronized with the remote server !!!" ' )
