import smbclient
import os
import subprocess
import time

server="fileserver2"
share="""Study Material"""
username="9913103619"
password="fghjkl"
domain="pdc.jiit"
attach="""/home/varun/Documents/"""
smb = smbclient.SambaClient(server,share ,username, password, domain)
# path1="""/Computer Science & IT/Even Sem 2016/BTech/III Year/Compiler Design/Marks"""
# path="""/Computer Science & IT/Even Sem 2016/BTech/III Year/Compiler Design/Marks/B4-B6 T1 Marks.pdf"""
# print smb.glob(path1)
local_file=[]
local_dir=[]
remote_file=[]
with open("path_file.txt", "r+") as f2:
	all_paths = [line.rstrip('\n') for line in f2]

for item in all_paths:
	if smb.exists(item):
		if smb.isdir(item):
			local_dir.append(attach+item)
		else:
			remote_file.append(item)
			local_file.append(attach+item)
	
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
for i,j in zip(remote_file,local_file):
	f=open(j,"w+")
	smb.download(i,j)
	f.close()


# print smb.info(path)
# print smb.listdir(path1)
# f1 = smb.open(path)
# name="""B4-B6 T1 Marks.pdf"""
# print "last modified at local M/C: %s" % time.ctime(os.path.getmtime(name))

# f=open(name,"w+")
# smb.download(path,name)
# f.close()
# f1.close()

