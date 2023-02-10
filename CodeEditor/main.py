from tkinter import *

def copy_text(event=None):
    text.clipboard_clear()
    text.clipboard_append(text.selection_get())

def select_text(event=None):
    text.tag_add("sel", "1.0", "end")
    return "break"

def cut_text(event=None):
    copy_text()
    text.delete("sel.first", "sel.last")

def submit_text(event=None):
    # Add your desired action for the submit button here
    pass

root = Tk()
root.geometry("350x250")
root.title("Sticky Notes")
root.minsize(height=250, width=350)
root.maxsize(height=250, width=350)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

text = Text(root, yscrollcommand=scrollbar.set)
text.pack(fill=BOTH)

text.bind("<Control-c>", copy_text)
text.bind("<Control-a>", select_text)
text.bind("<Control-x>", cut_text)

scrollbar.config(command=text.yview)

submit_button = Button(root, text="Submit", command=submit_text)
submit_button.pack()

root.mainloop()
