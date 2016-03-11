import smbclient
import os
import subprocess
import time
import re

server="fileserver2"
share="""Study Material"""
username="13103535"
password="9899496277"
domain="pdc.jiit"
attach="""/home/nirmit/Documents/"""
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


with open("path_file.txt", "r+") as f2:
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
	
for i in remote_file:
	# print "last modified at local M/C: %s" % time.ctime(os.path.getmtime(i))
	dict_=smb.info(i)
	str_=re.sub(' +',' ',dict_["change_time"])
	remote_last_mod=str_.split(" ")[3]
	print remote_last_mod
	# print "last modified at remote: %s" % smb.info(i)
	print

print "all_paths=",all_paths
print
print	
print "local_file=",local_file
print
print
print "local_dir=",local_dir

for i in local_dir:
			if not os.path.exists(i):
				os.makedirs(i)
for i,j in zip(remote_file,local_file): #HURRAY DONE !!! :D
	dict_=smb.info(i)
	str_remote=re.sub(' +',' ',dict_["change_time"])
	remote_last_mod=str_remote.split(" ")[3]
	str_local=re.sub(' +',' ',time.ctime(os.path.getmtime(j)))
	local_last_mod=str_local.split(" ")[3]
	if remote_last_mod!=local_last_mod:
		f=open(j,"w+")
		smb.download(i,j)
		f.close()
