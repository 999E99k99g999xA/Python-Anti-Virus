import hashlib
import glob
import os
import csv

class AntiVirus():
    def __init__(self, GUI):
        self.GUI = GUI

    def findHash(self, filename):
        h = hashlib.sha256()
        try:
            with open(filename,'rb') as file:
                chunk = 0
                while chunk != b'':
                    chunk = file.read()
                    h.update(chunk)
        except:
            pass
        return h.hexdigest()
    

    def SpecificScan(self):
        self.GUI.clearOutput()
        filename = self.GUI.askForFile()
        if filename == "": return
        try:
            Hash = self.findHash(filename)
        except:
            return
        Pancea = False
        ViralHash = None
        with open("virusTotal2.txt", "r") as file:
            NApple = file.read()
            Listo = NApple.split(",")
            for i in Listo:
                if i == Hash:
                    # print("This File Matches A Virus Hash of "+i)
                    self.GUI.displayoutput("This File Matches A Virus Hash of " + i, "#FF474C")
                    ViralHash = i
                    Pancea = True
            if Pancea == False:
                    # print("This file appears to be clean as it's current Hash of "+Hash+ " does not match any virus Hashes in the database.")
                    self.GUI.displayoutput("The File Hash:\n" + Hash + " does not match any virus Hashes in the database.\n")
                    self.GUI.displayoutput("\n##### File seems to be clean #####")
        return ViralHash
    
    def GetFileHash(self, X):

        programs = glob.glob(str(X)+"/*")
        programList = []
        for p in programs:
            programData = self.findHash(p)
            programList.append(programData)
        return programList



    def hardscan(self):
        self.GUI.clearOutput()
        Directory = self.GUI.askForDir()
        
        try:
            ProgramList = self.GetFileHash(Directory)
        except:
            return
        
        if Directory == "": return
        self.GUI.displayoutput("##### Running Hard Scan on " + str(len(ProgramList)) +" files... #####\n")

        with open("virusTotal2.txt", "r") as file:
            NApple = file.read()
            Listo = NApple.split(",")
        for i in ProgramList:
            for i2 in Listo:
                if i == i2:
                    # print("Warning: Hash" + i + " Matches with a Virus")
            
                    self.GUI.displayoutput("\nWarning: Hash" + i + " Matches with a Virus", "#FF474C")
        else:
            # print("Computer Appears to be Clean")
            self.GUI.displayoutput("\nComputer Appears to be Clean\n")
        self.GUI.displayoutput("\n##### Hardscan Complete #####")
            
    def getFileData(self, X):
        programs = glob.glob(str(X)+"/*")
        programList = []
        for p in programs:
            programSize= os.path.getsize(p)
            programModified= os.path.getmtime(p)
            programData = [p, programSize, programModified]

            programList.append(programData)
        return programList


    def WriteFileData(self, programs):
        if (os.path.exists("fileData2309092309230923.txt")):
            return
        with open("fileData2309092309230923.txt", "w") as file:
            wr = csv.writer(file)
            wr.writerows(programs)

 

    def checkForChanges(self, filedata):
        self.WriteFileData(filedata)

        with open("fileData2309092309230923.txt") as file:
            fileList=file.read().splitlines()
        originalFileList= []
        for each in fileList:
            items = each.split(",")
            originalFileList.append(items)
        currentFileList = self.getFileData(filedata)
        self.WriteFileData(currentFileList)

        Mismatch = False
        for c in currentFileList:
            for o in originalFileList:
                if ( c[0] == o[0]):
                    if (str(c[1]) != str(o[1])) or str(c[2]) != str(o[2]):
                        # print("Warning: File Mismatch:")
                        # print ("Mismatch detected in "+str(c)+", the original value is "+str(o))
                        Mismatch = True
                        self.GUI.displayoutput("\nWarning: File Mismatch:\n", "#FF474C")
                        self.GUI.displayoutput("Mismatch detected in "+str(c)+", the original value is "+str(o) + "\n", "#FF474C")
                    else:
                        self.GUI.displayoutput("\n##### Heuristic Scan End #####\n")


        # print("##### Heuristic Scan End #####")
        if not Mismatch: self.GUI.displayoutput("\n No Mismatch detected \n")    
        self.GUI.displayoutput("\n##### Heuristic Scan End #####")

    def HeuristicScan(self):
        self.GUI.clearOutput()
        Directory = self.GUI.askForDir()

        print(Directory)

        if Directory == "": return

        try:
            filedata = self.getFileData(Directory)
        except:
            return


        self.GUI.displayoutput("##### Running Heuristic Scan... #####\n")
        # self.WriteFileData(filedata)
        self.checkForChanges(filedata)

    
    def historyDelete(self):
        self.GUI.clearOutput()
        try:
            os.remove("fileData2309092309230923.txt")
        except:
            self.GUI.displayoutput("##### Heuristic History doesn't exist #####\n", "#FF474C")
            return
        self.GUI.displayoutput("##### Heuristic History deleted #####\n")