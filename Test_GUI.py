from tkinter import *
from t_code_editor import CodeEditor
from pylint_interaction import *

def get_per_of_num(num, per, returnInt=True):
    if returnInt:
        return int((per/100) * num)
    else:
        return (per/100) * num

def onclick_btn_submit(text):
    # Get the text
    code = text.get("1.0", END)
    # Save file
    with open(filepath, 'w') as f:
        f.write(code)
    # pass file to the pylint_interaction for getting score
    ce.console['text'] = f'score : {get_score(filepath)}'
    # ce.console['text'] = get_output_lines(filepath)


filepath = 'level1_code_file.py'


root = Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))

# Header
header = Frame(root, bg="black", height=50, width=width)
header.pack()

def_label = Label(header, text="Defination", fg="gold", bg='black', font=("Monospace", 18), width=get_per_of_num(width, 7.54))
def_label.pack(padx=10, pady=10)

#  Left part for editor
left_frame = Frame(root, bg = 'red')
left_frame.pack(side='left', expand=True, fill=BOTH)
ce = CodeEditor(left_frame)
ce.load_text(filepath)

# Right part for buttons and other elements
right_frame = Frame(root, bg = 'blue')
right_frame.pack(side='left', expand=True, fill='both')

submit_btn = Button(right_frame, width=get_per_of_num(width, 2.9), height=get_per_of_num(height, .3), text='SUBMIT', font=("Arial", 18), command=lambda: onclick_btn_submit(ce.text))
submit_btn.pack(side='bottom')
submit_btn['fg']="gold"
submit_btn['bg']="black"

root.mainloop()

