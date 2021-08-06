import os
from tkinter import *
from PIL import ImageTk,Image  

global cwd
cwd = os.getcwd()

root = Tk() 

hu_img                      = ImageTk.PhotoImage(Image.open(cwd + "\\spin_ranges\\headsup.png"))
pushfold_img                = ImageTk.PhotoImage(Image.open(cwd + "\\spin_ranges\\pushfold.png"))
notsupported_img            = ImageTk.PhotoImage(Image.open(cwd + "\\spin_ranges\\range_not_supported.png"))
BTN_open11_15_img           = ImageTk.PhotoImage(Image.open(cwd + "\\spin_ranges\\BTN_open11_15.png"))
BTN_open17_img              = ImageTk.PhotoImage(Image.open(cwd + "\\spin_ranges\\BTN_open17.png"))
BTN_open10_img              = ImageTk.PhotoImage(Image.open(cwd + "\\spin_ranges\\BTN_open10.png"))
SB_btn_folds11_16_img       = ImageTk.PhotoImage(Image.open(cwd + "\\spin_ranges\\SB_btn_folds11_16.png"))
SB_btn_folds17_img          = ImageTk.PhotoImage(Image.open(cwd + "\\spin_ranges\\SB_btn_folds17.png"))
SB_btn_limp11_16_img        = ImageTk.PhotoImage(Image.open(cwd + "\\spin_ranges\\SB_btn_limp11_16.png"))
SB_btn_limp17_25_img        = ImageTk.PhotoImage(Image.open(cwd + "\\spin_ranges\\SB_btn_limp17_25.png"))
SB_btn_open10_img           = ImageTk.PhotoImage(Image.open(cwd + "\\spin_ranges\\SB_btn_open10.png"))
SB_btn_open11_16_img        = ImageTk.PhotoImage(Image.open(cwd + "\\spin_ranges\\SB_btn_open11_16.png"))
SB_btn_open17_img           = ImageTk.PhotoImage(Image.open(cwd + "\\spin_ranges\\SB_btn_open17.png"))
BB_btn_and_sb_limp11_16_img = ImageTk.PhotoImage(Image.open(cwd + "\\spin_ranges\\BB_btn_and_sb_limp11_16.png"))
BB_btn_and_sb_limp17_img    = ImageTk.PhotoImage(Image.open(cwd + "\\spin_ranges\\BB_btn_and_sb_limp17.png"))
BB_btn_or_sb_open11_16_img  = ImageTk.PhotoImage(Image.open(cwd + "\\spin_ranges\\BB_btn_or_sb_open11_16.png"))
BB_btn_or_sb_open17_img     = ImageTk.PhotoImage(Image.open(cwd + "\\spin_ranges\\BB_btn_or_sb_open17.png"))
BB_sb_limp10_img            = ImageTk.PhotoImage(Image.open(cwd + "\\spin_ranges\\BB_sb_limp10.png"))
BB_sb_limp11_16_img         = ImageTk.PhotoImage(Image.open(cwd + "\\spin_ranges\\BB_sb_limp11_16.png"))
BB_sb_limp17_img            = ImageTk.PhotoImage(Image.open(cwd + "\\spin_ranges\\BB_sb_limp17.png"))
BB_sb_open11_16_img         = ImageTk.PhotoImage(Image.open(cwd + "\\spin_ranges\\BB_sb_open11_16.png"))
BB_sb_open17_25_img         = ImageTk.PhotoImage(Image.open(cwd + "\\spin_ranges\\BB_sb_open17_25.png"))

# A Radiobutton to toggle between images
position = IntVar()
bigblinds = IntVar()
action = IntVar()

def call():
    canvas.delete(ALL)
    if position.get() == 4:
        #heads up
        if bigblinds.get() == 10:
            canvas.create_image((2, 2), image=pushfold_img, anchor=NW)
        else:
            canvas.create_image((2, 2), image=hu_img, anchor=NW)
    elif position.get() == 1:
        #btn spingo
        if bigblinds.get() == 11:
            canvas.create_image((2, 2), image=BTN_open11_15_img, anchor=NW)
        elif bigblinds.get() == 17:
            canvas.create_image((2, 2), image=BTN_open17_img, anchor=NW)
        else:
            canvas.create_image((2, 2), image=BTN_open10_img, anchor=NW)
    elif position.get() == 2:
        #sb spingo
        if bigblinds.get() == 11 and action.get() == 5:
            canvas.create_image((2, 2), image=SB_btn_folds11_16_img, anchor=NW)
        elif bigblinds.get() == 17 and action.get() == 5:
            canvas.create_image((2, 2), image=SB_btn_folds17_img, anchor=NW)
        elif bigblinds.get() == 10 and action.get() == 5:
            canvas.create_image((2, 2), image=pushfold_img, anchor=NW)
        elif bigblinds.get() == 11 and action.get() == 6:
            canvas.create_image((2, 2), image=SB_btn_limp11_16_img, anchor=NW)
        elif bigblinds.get() == 17 and action.get() == 6:
            canvas.create_image((2, 2), image=SB_btn_limp17_25_img, anchor=NW)
        elif bigblinds.get() == 10 and action.get() == 7:
            canvas.create_image((2, 2), image=SB_btn_open10_img, anchor=NW)
        elif bigblinds.get() == 11 and action.get() == 7:
            canvas.create_image((2, 2), image=SB_btn_open11_16_img, anchor=NW)
        elif bigblinds.get() == 17 and action.get() == 7:
            canvas.create_image((2, 2), image=SB_btn_open17_img, anchor=NW) 
        else:
            canvas.create_image((2, 2), image=notsupported_img, anchor=NW)
    elif position.get() == 3:
        #bb spingo
        if bigblinds.get() == 11 and action.get() == 1:
            canvas.create_image((2, 2), image=BB_btn_and_sb_limp11_16_img, anchor=NW)
        elif bigblinds.get() == 17 and action.get() == 1:
            canvas.create_image((2, 2), image=BB_btn_and_sb_limp17_img, anchor=NW)
        elif bigblinds.get() == 11 and action.get() == 2:
            canvas.create_image((2, 2), image=BB_btn_or_sb_open11_16_img, anchor=NW)
        elif bigblinds.get() == 17 and action.get() == 2:
            canvas.create_image((2, 2), image=BB_btn_or_sb_open17_img, anchor=NW)
        elif bigblinds.get() == 10 and action.get() == 3:
            canvas.create_image((2, 2), image=BB_sb_limp10_img, anchor=NW)
        elif bigblinds.get() == 11 and action.get() == 3:
            canvas.create_image((2, 2), image=BB_sb_limp11_16_img, anchor=NW)
        elif bigblinds.get() == 17 and action.get() == 3:
            canvas.create_image((2, 2), image=BB_sb_limp17_img, anchor=NW)
        elif bigblinds.get() == 11 and action.get() == 4:
            canvas.create_image((2, 2), image=BB_sb_open11_16_img, anchor=NW)
        elif bigblinds.get() == 17 and action.get() == 4:
            canvas.create_image((2, 2), image=BB_sb_open17_25_img, anchor=NW)
        else:
            canvas.create_image((2, 2), image=notsupported_img, anchor=NW)
    else:
        canvas.create_image((2, 2), image=notsupported_img, anchor=NW)

            

#Description
#L1=Label(root, text ="R=raise  G=call  B=fold").grid(row=0, column=0, columnspan=5, sticky=S)

#Position selection
R1=Radiobutton(root, text="BTN", variable=position, value=1, command=call)
R1.grid(row=0, column=0, sticky=N+E)
R2=Radiobutton(root, text="SB", variable=position, value=2, command=call)
R2.grid(row=0, column=1, sticky=N+E)
R3=Radiobutton(root, text="BB", variable=position, value=3, command=call)
R3.grid(row=0, column=2, sticky=N+E)
R3=Radiobutton(root, text="HU", variable=position, value=4, command=call)
R3.grid(row=0, column=3, sticky=N+E)
R3.select()

#Big blinds selection
R4=Radiobutton(root, text="10", variable=bigblinds, value=10, command=call)
R4.grid(row=1, column=0, sticky=N+E)
R5=Radiobutton(root, text="11-16", variable=bigblinds, value=11, command=call)
R5.grid(row=1, column=1, sticky=N+E)
R6=Radiobutton(root, text="17+", variable=bigblinds, value=17, command=call)
R6.grid(row=1, column=2, sticky=N+E)
R6.select()

#Action selection
R7=Radiobutton(root, text="btn & sb limp", variable=action, value=1, command=call)
R7.grid(row=2, column=0, sticky=N+E)
R8=Radiobutton(root, text="btn or sb open", variable=action, value=2, command=call)
R8.grid(row=2, column=1, sticky=N+E)
R9=Radiobutton(root, text="sb limp", variable=action, value=3, command=call)
R9.grid(row=3, column=0, sticky=N+E)
R10=Radiobutton(root, text="sb open", variable=action, value=4, command=call)
R10.grid(row=3, column=1, sticky=N+E)
R11=Radiobutton(root, text="btn folds", variable=action, value=5, command=call)
R11.grid(row=4, column=0, sticky=N+E)
R12=Radiobutton(root, text="btn limp", variable=action, value=6, command=call)
R12.grid(row=4, column=1, sticky=N+E)
R13=Radiobutton(root, text="btn open", variable=action, value=7, command=call)
R13.grid(row=4, column=2, sticky=N+E)

# A canvas for mouse events and image drawing
canvas = Canvas(root, height=500, width=500,)
canvas.grid(column=5, row=0, rowspan=6, sticky=W)
canvas.create_image((2, 2), image=hu_img, anchor=NW)

# Enter event loop
root.mainloop()