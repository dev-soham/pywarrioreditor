""" PREFAB OF WARNING FRAME """
from tkinter import *


class WarningPrefab:
    """ a prefab that will appears with all the warnings """

    def __init__(self, parent, text):
        self.parent = parent

        # create frame
        self.frm = Frame(parent, bg='red', width=512)
        self.frm.pack(expand=True, fill=BOTH, padx=(10, 10), pady=(10, 10))

        label = Label(self.frm, text=text, fg='black', bg='orange')
        label.config(width=62, wraplength=500)
        label.grid(row=0, column=0, sticky=NSEW)

        self.frm.columnconfigure(0, weight=1)
        self.frm.rowconfigure(0, weight=1)


    def __del__(self):
        if self.frm.winfo_exists():
            self.frm.destroy()



class CompletedPrefab:
    """ a prefab that will appears when user solved all the warnings """
    def __init__(self, parent):
        # create frame
        self.cpfrm = Frame(parent, bg='red', width=512)
        self.cpfrm.pack(expand=True, fill=BOTH, padx=(10, 10), pady=(10, 10))
        label = Label(self.cpfrm, text='Congratulations, You have solved all the warnings.', fg='white', bg='green')
        label.config(width=62, wraplength=500)
        label.grid(row=0, column=0, sticky=NSEW)
        self.cpfrm.columnconfigure(0, weight=1)
        self.cpfrm.rowconfigure(0, weight=1)
    
    def __del__(self):
        if self.cpfrm.winfo_exists():
            self.cpfrm.destroy()


class ErrorPrefab:
    """ a prefab that will appears when user's code get some error """
    def __init__(self, parent):
        # create frame
        self.erfrm = Frame(parent, bg='red', width=512)
        self.erfrm.pack(expand=True, fill=BOTH, padx=(10, 10), pady=(10, 10))
        label = Label(self.erfrm, text='You code have some errors.', fg='black', bg='red')
        label.config(width=62, wraplength=500)
        label.grid(row=0, column=0, sticky=NSEW)
        self.erfrm.columnconfigure(0, weight=1)
        self.erfrm.rowconfigure(0, weight=1)
    
    def __del__(self):
        if self.erfrm.winfo_exists():
            self.erfrm.destroy()
