import os
import wx
import wx.lib.agw.hypertreelist as HTL

class MyFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, pos = (0,0), size=(700, 900), title= "HyperTreeList Demo")


        # ------------------------------------------
        # Algo for creating Files' List Starts here
        # ------------------------------------------
        allFiles = []       
        for root, dirs, files in os.walk("/", topdown = True):  
            for name in files:  
                location = os.path.join(root, name)                 
                allFiles.append(location)       

        treeList= HTL.HyperTreeList(self, agwStyle= wx.TR_DEFAULT_STYLE| 0x4000 )
        treeList.AddColumn("List View")
        treeList.SetColumnWidth(0, 600)

        TLRoot = treeList.AddRoot ("D:", ct_type= 1)
        allDirs = []
        allDirsItem = []
        allDirs.append ("D:")
        allDirsItem.append(TLRoot)


        # --------------------------------------
        # Algo for filling Tree List Starts here
        # --------------------------------------
        for eachName in allFiles:
            nameSplit = eachName.split(os.sep)
            matchingDirFound = 0

            lenNS= len(nameSplit)    
            i=lenNS -1
            for eachNameSplit in reversed(nameSplit):       
                for eachDoneDir in reversed(allDirs):
                    if eachNameSplit == eachDoneDir:
                        matchingDirFound = 1
                        break     

                if matchingDirFound == 1: 
                    break   
                i= i-1              

            if matchingDirFound ==1:
                for k in range(i, lenNS-1):
                    allDirsItem.append([])
                    allDirsItem[k+1] = treeList.AppendItem (allDirsItem[k], nameSplit[k+1], ct_type= 1)

                    if len(allDirs)> k+1:
                        allDirs[k+1] = nameSplit[k+1]
                    else:
                        allDirs.append (nameSplit[k+1])