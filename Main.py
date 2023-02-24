#region Modules
from tkinter import *
from code_editor import *
from pylint_interaction import *
from prefabs import *
#endregion

#region UDF
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

    # update WarningPrefab
    update_wp()

    global cp
    global ep
    if get_score(filepath) == 10.0 and len(wp) == 0:
        cp = CompletedPrefab(inner_frame)
        del ep

    elif cp is not None:
        del cp

    if get_score(filepath) == None:
        ep = ErrorPrefab(inner_frame)

    elif get_score(filepath) != None:
        del ep


def update_wp():
    if len(wp) >= 1:
        del wp[:]
        update_wp()
    else:
        for a in get_output_warnings(filepath):
            wp.append(WarningPrefab(inner_frame, a))
            
#endregion

#region Variables
filepath = 'level1_code_file.py'
global wp
wp = []
cp = None
ep = None
#endregion

#region Main
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

# Right part for buttons and warnings
right_frame = Frame(root, bg='blue')
right_frame.pack(side='left', expand=True, fill='both')

# Create a container frame for the warnings prefabs
warnings_frame = Frame(right_frame, bg='grey')
warnings_frame.pack(side='top', fill='both', expand=True)

# Add a scrollbar to the warnings frame
scrollbar = Scrollbar(warnings_frame)
scrollbar.pack(side='right', fill='y')

# Create a canvas to hold the warnings prefabs
canvas = Canvas(warnings_frame, bg='grey', yscrollcommand=scrollbar.set)
canvas.pack(side='left', fill='both', expand=True)

# Configure the scrollbar to scroll the canvas
scrollbar.config(command=canvas.yview)

# Create a frame to hold the warnings prefabs inside the canvas
inner_frame = Frame(canvas, bg='grey')
inner_frame.pack(side='top', fill='both', expand=True)

# Set the size of the canvas and configure it to hold the inner frame
canvas.create_window((0, 0), window=inner_frame, anchor='nw', tags='inner_frame')
canvas.config(scrollregion=canvas.bbox('all'))

# Update the warnings prefabs to the inner frame
update_wp()

# Configure the canvas to resize with the window
def resize_canvas(event):
    canvas.config(scrollregion=canvas.bbox('all'))
canvas.bind('<Configure>', resize_canvas)

# Add the submit button to the bottom of the right frame
submit_btn = Button(right_frame, height=get_per_of_num(height, .3), text='SUBMIT', font=('Arial', 18), command=lambda: onclick_btn_submit(ce.text))
submit_btn.pack(pady=(10, 10), padx=(10, 10), fill='both', side='bottom')
submit_btn['fg'] = 'gold'
submit_btn['bg'] = 'black'

root.mainloop()
#endregion
