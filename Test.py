from tkinter import *

root = Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))

frame = Frame(root, width=200, height=200)
frame.pack()

block = Label(frame, bg='red', width=50, height=50)
block.pack()

root.mainloop()
