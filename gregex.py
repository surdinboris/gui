from tkinter import  Tk, Label, Frame, Button, Entry, Text
import fnmatch

class Reggui:
    def __init__(self, master):
        self.master = master
        master.title('Gregex')
        self.label = Label(master, text = "Regex generator")
        self.label.pack()
        self.req = Entry(master)
        self.req.pack()
        self.outp = Text(master, height=1, width=20)
        self.outp.pack()
        self.sbutton= Button(master,text = "Calcularte", command=self.calc)
        self.sbutton.pack()
    def calc(self):
        val=self.req.get()
        regval=fnmatch.translate(val)
        self.outp.insert(1.0, regval)
        return regval

root = Tk()
reggui = Reggui(root)
root.mainloop()
