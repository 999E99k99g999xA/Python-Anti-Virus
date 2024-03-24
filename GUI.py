
from tkinter import *
from AntiVirus import AntiVirus
from tkinter.filedialog import *


class AppGUI():
    def __init__(self, AntiVirus):
        self.root = Tk()
        self.root.configure(background='#3b3b3b')
        self.root.geometry("600x400")
        self.root.title("AntiVirusProgram")
        self.root.resizable(False, False)
        self.AntiVirus = AntiVirus
        self.buttons = []
        self.topframe = Frame(self.root, width=600, height=20)
        self.topframe.pack(side=TOP)
        self.leftframe = Frame(self.root, width=300, height=380)
        self.leftframe.pack(side=LEFT)
        self.rightframe = Frame(self.root, width=300, height=380)
        self.rightframe.pack(side=LEFT)
        self.rightframe.configure(background='#3b3b3b')
        self.leftframe.configure(background='#3b3b3b')

        Title = Label(self.topframe, text="Anti-Virus Program", font=('Roboto', 30), fg="#FFFFFF")
        Title.configure(background='#3b3b3b')
        Title.pack()
        

        self.addButton("Specfic Scan", self.AntiVirus.SpecificScan)
        self.addButton("Heuristic Scan", self.AntiVirus.HeuristicScan)
        self.addButton("Hard Scan", self.AntiVirus.hardscan)
        self.addButton("Delete", self.AntiVirus.historyDelete)
        
        

        self.outputText = Text(self.rightframe, height=15, width=52, font=('Roboto', 12), bg='black')
        self.outputText.pack(side=LEFT)
        self.outputText.configure(background='#adadad', borderwidth=0, border=0)
        self.outputText.config(state='disabled')
        

        

    
    def addButton(self, text, func):

        button = Button(self.leftframe, text=text, command=func, height=2, width=8, font=('Roboto', 10))
        button.configure(background='#adadad', borderwidth=0)
        button.grid(row=len(self.buttons)+1, column=1, padx=20, pady=20)
        self.buttons.append(button)

        return button
    
    def displayoutput(self, output, color=None):
        if color == None:
            self.outputText.config(fg="#000000")
        else:
            self.outputText.config(fg=color)

        self.outputText.config(state='normal')
        self.outputText.tag_configure("center", justify='center')
        self.outputText.insert(END, output)
        self.outputText.tag_add("center", "1.0", "end")
        self.outputText.config(state='disabled')

    def clearOutput(self):
        self.outputText.config(state='normal')
        self.outputText.delete("1.0", END)
        self.outputText.config(state='disabled')

    def askForFile(self):
        return askopenfilename()
    
    def askForDir(self):
        return askdirectory()

    def displayWindow(self):
        self.root.mainloop()

