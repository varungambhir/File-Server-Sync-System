import smbclient
import os
import operator
import datetime
import getpass
import subprocess
import time
import re

share = """Study Material""" # # for Study Material
# share = """9913103619"""  ## for my directory

fp=open("Details.txt",'r')
data = fp.read().splitlines()
server = data[0]
username = data[1]
password = data[2]
syspass=data[3]
domain = "pdc.jiit"
user = getpass.getuser()
attach = """/home/""" + user + """/Documents"""
smb = smbclient.SambaClient(server, share, username, password, domain)
local_file = []
local_dir = []  
remote_file = []
remote_dir=[]
sorted_local_dir=[]
local_dir_dict={}

# print server,username,password
def pathtodir(path):
    if not os.path.exists(path):
        l = []
        p = "/"
        l = path.split("/")
        i = 1
        while i < len(l):
            p = p + l[i] + "/"
            i = i + 1            
            if not os.path.exists(p):                
                os.mkdir(p)

with open("/home/" + user + "/File-Server-Sync-System-/path_file.txt", "r+") as f2:
    all_paths = [line.rstrip('\n') for line in f2]

for item in all_paths:
    # print item
    if '.' in item:
        remote_dir.append( item.rsplit('/', 1)[0])
remote_dir=list(set(remote_dir))
# for i in remote_dir:
#     print i
for item in remote_dir:
	if smb.exists(item):
		local_dir.append(attach+item)
for i in local_dir:
	# print i
	local_dir_dict[i]=i.count('/')
sorted_local_dir = sorted(local_dir_dict.items(), key=operator.itemgetter(1))
local_dir = [x[0] for x in sorted_local_dir]
pathtodir(os.path.dirname(local_dir[0]))
for i in local_dir:
	# print i
	if not os.path.exists(i):                
                os.mkdir(i)
		
for item in remote_dir:
	if smb.exists(item):
		for file in smb.listdir(item):
			if smb.isfile(item+"/"+file):
				# print file
				remote_file.append(item+"/"+file)
				local_file.append(attach+item+"/"+file)
for i, j in zip(remote_file, local_file):  # HURRAY DONE !!! :D  YESSSSSSSSS!!!!!!!!
    # print i
    dict_ = smb.info(i)
    str_remote = re.sub(' +', ' ', dict_["write_time"])
    remote_last_mod = str_remote.split(" ")[3]
    f = open(j, "w+")
    str_local = re.sub(' +', ' ', time.ctime(os.path.getmtime(j)))
    local_last_mod = str_local.split(" ")[3]
    if remote_last_mod != local_last_mod:
        smb.download(i, j)
        f.close()

os.system('notify-send -i ~/File-Server-Sync-System-/sync-500x300.png "Your SM is now Synchronized with the remote server !!!" ')
f.close()
fp.close()