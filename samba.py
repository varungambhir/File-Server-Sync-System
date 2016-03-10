import smbclient
import os
import subprocess
import time

server="fileserver2"
share="""Study Material"""
username="9913103619"
password="fghjkl"
domain="pdc.jiit"
smb = smbclient.SambaClient(server,share ,username, password, domain)
# print smb.listdir(u"/")
path1="""/Computer Science & IT/Even Sem 2016/BTech/III Year/Compiler Design/Marks"""
path="""/Computer Science & IT/Even Sem 2016/BTech/III Year/Compiler Design/Marks/B4-B6 T1 Marks.pdf"""
# print smb.lsdir("/")
# print smb.glob(path1)
print smb.isdir(path1)
print smb.isdir(path)

print smb.info(path)
print smb.listdir(path1)
f1 = smb.open(path)
name="""B4-B6 T1 Marks.pdf"""
print "last modified at local M/C: %s" % time.ctime(os.path.getmtime(name))

f=open(name,"w+")
smb.download(path,name)
f.close()
f1.close()
