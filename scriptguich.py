import tkinter as tk
from tkinter import *

class ParentWindow(Frame):
    def __init__ (self,master):
        Frame.__init__ (self)
    
        self.master = master
        self.master.resizable(width=False, height=True)
        self.master.geometry('{}x{}'.format(400, 250))
        self.master.title('Check files')
        self.master.config(bg='lightgray')

        self.btnSubmit = Button(self.master, text="Browse...", width=15, height=2, command=self.submit)
        self.btnSubmit.grid(row=0, column=0,padx=(0,90), pady=(30,0), sticky=NE)

        def submit(self):
        fn = self.varFName.get()
        ln = self.varLName.get()
        self.lblDisplay.config(text='Hello{} {}!'.format(fn,ln))







if __name__== "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
