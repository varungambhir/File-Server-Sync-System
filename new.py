import Tix
import os
import subprocess
import glob
import Tkinter
import ttk

from Tkinter import *
import tkMessageBox
import Tkinter
	
class View(object):
    def __init__(self, root,x):
        self.root = root
        self.makeCheckList(x)
        

    def makeCheckList(self,x):
        self.cl = Tix.CheckList(self.root, browsecmd=self.selectItem)
        self.cl.pack()
   	count=1
   	self.cl.config(height=700)
   	self.cl.config(width=700)
        for i in x:
   
        	self.cl.hlist.add("CL"+str(count), text=i)	
        	self.cl.hlist.add("CL"+str(count)+".1",text="YO")
		self.cl.setstatus("CL"+str(count), "on")
		count=count+1
        '''
        self.cl.hlist.add("CL1", text="checklist1")
        self.cl.hlist.add("CL1.Item1", text="subitem1")
        self.cl.hlist.add("CL2", text="checklist2")
        self.cl.hlist.add("CL2.Item1", text="subitem1")
        self.cl.setstatus("CL2", "on")
        self.cl.setstatus("CL2.Item1", "on")
        self.cl.setstatus("CL1", "off")
        self.cl.setstatus("CL1.Item1", "off")
        self.cl.autosetmode()
	'''
    def selectItem(self, item):
        print item, self.cl.getstatus(item)

def main():
    root = Tix.Tk()
    lis=[]
    for i in os.listdir(os.getcwd()):
    	lis.append(i)
    root.geometry('{}x{}'.format(600,600))
	
    view = View(root,lis)
    root.update()
    root.mainloop()

if __name__ == '__main__':
    #print os.listdir(os.getcwd())
    #for i in os.listdir(os.getcwd()):
    #	print i


    main()
