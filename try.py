import smbclient
from smb.SMBConnection import SMBConnection
from smb import smb_structs
smb_structs.SUPPORT_SMB2 = False
fp=open("Details.txt","r")	
data = fp.read().splitlines()
server = data[0]
username = data[1]
password = data[2]
syspass=data[3]
share=data[1]
domain = "pdc.jiit"
smb = smbclient.SambaClient(server, share, username, password, domain)
# conn = SMBConnection(username, password, "nirmit-Vostro-2520", server, use_ntlm_v2 = True)
# assert conn.connect("172.16.68.30", 139)

# conn.storeFile(service_name, path, file_obj, timeout=30)
# conn.storeFile("/"+username, "/9913103619/Details.txt", fp, timeout=30)

f_remote=smb.open(u"/sssssss.py", mode='w+')	
print f_remote
