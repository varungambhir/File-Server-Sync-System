import Tix
import os
import subprocess
import glob
import Tkinter
import ttk
import tkMessageBox
import getpass

lis = []
minn = 100000000
user=getpass.getuser()
local_path = """/home/"""+user+"""/Desktop"""
const = """/Computer Science & IT/Even Sem 2016/BTech/III Year"""

pathsave = ""  # path of checkboxes that are checked

printhash = {}

dictall = {}  # stores all checkboxes
dicti = {}

# entirepath={}
flist = []  # MAIN
file_p = None

def Finallist():  # FINAL WORK
    # print 'yo'
    file_p = open("/home/"+user+"/File-Server-Sync-System-/path_file.txt", "a+")
    for path in flist:
        path = path.replace(local_path, "")
        path = const + path
        if path in printhash:
            continue
        printhash[path] = 1
        # print path
        file_p.write("%s\n" % path)
    file_p.close()

def RunSample(w):

    top = Tix.Label(w, padx=20, pady=10, bd=1, relief=Tix.RAISED,
                    anchor=Tix.CENTER, text='Select directories you wish to update\n')
    box = Tix.ButtonBox(w, orientation=Tix.HORIZONTAL)
    box.add('ok', text='OK', underline=0, width=5,
            command=lambda w=w: Finallist())
    box.add('close', text='Finish', underline=0, width=5,
            command=lambda w=w: w.destroy())
    box.pack(side=Tix.BOTTOM, fill=Tix.X)
    top.pack(side=Tix.TOP, fill=Tix.BOTH, expand=1)


def doit():
    global minn
    minn = 100000000
    for root, dirs, files in os.walk(local_path):
        path = root.split('/')
        for i in range(len(files)):
            what = str(root) + '/' + str(files[i])
            # entirepath[files[i]]=what    #dikkat problem gadbad
        for i in range(len(dirs)):
            whatn = str(root) + '/' + str(dirs[i])
            # entirepath[dirs[i]]=whatn #dikkat problem gadbad
            # print str(root)+str(dirs[i])
        minn = min(minn, len(path) - 1)
        y = (len(path) - 1 - minn) * '-' + '/' + os.path.basename(root)
        if y != '.':
            # print y
            lis.append(y)
        for file in files:
            x = (len(path) - minn) * '-' + root + '/' + file
            if x != '.':
                # print x
                lis.append(x)

class View(object):
    def dashcount(self, x):
        count = 0
        for i in range(0, len(x)):
            if x[i] != '-':
                break
            else:
                count = count + 1
        return count
    def removedash(s):
        ind = 0
        while s[ind] == '-':
            ind = ind + 1
        ret = s[ind:len(s) - 1]
        return ret
    def __init__(self, root):
        RunSample(root)
        self.root = root
        self.makeCheckList()
    def makeCheckList(self):
        self.cl = Tix.CheckList(self.root, browsecmd=self.selectItem)
        self.cl.pack()
        count = 1
        self.cl.config(height=900)
        self.cl.config(width=1500)
        for i in lis:
            cn = self.dashcount(i)
            if cn in dicti:
                dicti[cn] = dicti[cn] + 1
            else:
                dicti[cn] = 1
            self.cl.hlist
            if 1 in dicti:
                s = "CL" + str(dicti[1])
                for j in range(cn - 1):
                    if j + 2 in dicti:
                        s = s + "." + str(dicti[j + 2])
                # print s
                dictall[s] = i
                foo = str(i)
                foo = foo.lstrip('-')
                self.cl.hlist.add(s, text=foo)
                self.cl.setstatus(s, "off")
                self.cl.autosetmode()
        # print dicti
    def selectItem(self, item):
        # print item, self.cl.getstatus(item)
        what = item
        lenn = len(what)
        for i in dictall:
            if i[0:lenn] == what:
                self.cl.setstatus(i, self.cl.getstatus(item))
                # print i, self.cl.getstatus(i)
                till = dictall[i]
                till = till.lstrip('-')
                # print pathsave+"/"+str(till)
                if self.cl.getstatus(i) == "on":
                    # flist.append(entirepath[till])
                    flist.append(str(till))
                elif self.cl.getstatus(i) == "off":
                    # flist.remove(entirepath[till])
                    flist.remove(till)

def main():
    root = Tix.Tk()
    root.geometry('{}x{}'.format(2000, 2000))
    view = View(root)
    root.update()
    root.mainloop()

if __name__ == '__main__':
    unmount = """sudo umount -f -a -t cifs -l"""
    mount = """sudo mount -t cifs //fileserver2/Study\ Material/Computer\ Science\ \&\ IT/Even\ Sem\ 2016/BTech/III\ Year """ + \
        local_path + """ -o user=13103535,password=9899496277,workgroup=workgroup,ip=172.16.68.30"""
    c = subprocess.check_output(unmount, shell=True)
    b = subprocess.check_output(mount, shell=True)
    doit()
    main()