import os
from tkinter import *
from PIL import ImageTk,Image  

global cwd
cwd = os.getcwd()

root = Tk() 

hu_img = ImageTk.PhotoImage(Image.open(cwd + "\\spin_ranges\\headsup.png"))
pushfold_img = ImageTk.PhotoImage(Image.open(cwd + "\\spin_ranges\\pushfold.png"))
BTN_open11_15_img = ImageTk.PhotoImage(Image.open(cwd + "\\spin_ranges\\BTN_open11_15.png"))
BTN_open17_img = ImageTk.PhotoImage(Image.open(cwd + "\\spin_ranges\\BTN_open17.png"))

# A Radiobutton to toggle between images
position = IntVar()
bigblinds = IntVar()
action = IntVar()

def call():
    canvas.delete(ALL)
    if bigblinds.get() == 10:
        canvas.create_image((2, 2), image=pushfold_img, anchor=NW)
        Label(root, text ="LB=push/call  Y=push/fold").grid(row=0, column=0, columnspan=5, sticky=S)
    else: 
        if position.get() == 4:
            canvas.create_image((2, 2), image=hu_img, anchor=NW)
            Label(root, text ="R=raise  G=call  B=fold").grid(row=0, column=0, columnspan=5, sticky=S)
        elif position.get() == 1:
            if bigblinds.get() == 11:
                canvas.create_image((2, 2), image=BTN_open11_15_img, anchor=NW)
                Label(root, text ="R=raise  G=call  B=fold").grid(row=0, column=0, columnspan=5, sticky=S)
            elif bigblinds.get() == 17:
                canvas.create_image((2, 2), image=BTN_open17_img, anchor=NW)
                Label(root, text ="R=raise  G=call  B=fold").grid(row=0, column=0, columnspan=5, sticky=S)
            else:
                canvas.create_image((2, 2), image=pushfold_img, anchor=NW)
                Label(root, text ="LB=push/call  Y=push/fold").grid(row=0, column=0, columnspan=5, sticky=S)

#Description
Label(root, text ="R=raise  G=call  B=fold").grid(row=0, column=0, columnspan=5, sticky=S)

#Position selection
R1=Radiobutton(root, text="BTN", variable=position, value=1, command=call)
R1.grid(row=6, column=0, sticky=N+E)
R2=Radiobutton(root, text="SB", variable=position, value=2, command=call)
R2.grid(row=6, column=1, sticky=N+E)
R3=Radiobutton(root, text="BB", variable=position, value=3, command=call)
R3.grid(row=6, column=2, sticky=N+E)
R3=Radiobutton(root, text="HU", variable=position, value=4, command=call)
R3.grid(row=6, column=3, sticky=N+E)
R3.select()

#Big blinds selection
R4=Radiobutton(root, text="10", variable=bigblinds, value=10, command=call)
R4.grid(row=7, column=0, sticky=N+E)
R5=Radiobutton(root, text="11-16", variable=bigblinds, value=11, command=call)
R5.grid(row=7, column=1, sticky=N+E)
R6=Radiobutton(root, text="17+", variable=bigblinds, value=17, command=call)
R6.grid(row=7, column=2, sticky=N+E)
R6.select()

#Action selection
R7=Radiobutton(root, text="btn & sb limp", variable=action, value=1, command=call)
R7.grid(row=8, column=0, sticky=N+E)
R8=Radiobutton(root, text="btn or sb open", variable=action, value=2, command=call)
R8.grid(row=9, column=0, sticky=N+E)
R9=Radiobutton(root, text="sb limp", variable=action, value=3, command=call)
R9.grid(row=10, column=0, sticky=N+E)
R10=Radiobutton(root, text="sb open", variable=action, value=4, command=call)
R10.grid(row=11, column=0, sticky=N+E)
R11=Radiobutton(root, text="btn folds", variable=action, value=5, command=call)
R11.grid(row=12, column=0, sticky=N+E)
R12=Radiobutton(root, text="btn limp", variable=action, value=6, command=call)
R12.grid(row=13, column=0, sticky=N+E)
R13=Radiobutton(root, text="btn open", variable=action, value=7, command=call)
R13.grid(row=14, column=0, sticky=N+E)

# A canvas for mouse events and image drawing
canvas = Canvas(root, height=500, width=500,)
canvas.grid(column=5, row=0, rowspan=6, sticky=W)
canvas.create_image((2, 2), image=hu_img, anchor=NW)

# Enter event loop
root.mainloop()