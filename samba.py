import smbclient
server="fileserver2"
share="""Study Material"""
username="9913103619"
password="fghjkl"
domain="pdc.jiit"
smb = smbclient.SambaClient(server,share ,username, password, domain)
print smb.listdir(u"/")
path="""/Computer Science & IT/Even Sem 2016/BTech/III Year/Compiler Design/Notice - 21-01-2016 B4-B6.txt"""
f1 = smb.open(path)
# path="""/Even Sem 2016/B4-B6Tech/III Year/Compiler Design/Notice - 21-01-2016 B4-B6.txt"""
# path="/Computer%20Science%20&%20IT/Even%20Sem%202016/BTech/III%20Year/Compiler%20Design/Notice%20- 21-01-2016 B4-B6.txt"
# f2=smb.open(path)
data = f1.read()
# data1=f2.read()
# # smb.rename(u'/abc.txt', u'/abcd.txt')
# # smb._getfile(u"/abcd.txt",u"/new.txt")

smb.download(path,"wow.txt")
# smb.download(path,"wow.txt")
f1.close()
# f2.close()