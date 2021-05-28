import os
from tkinter import *
from PIL import ImageTk,Image  

global cwd
cwd = os.getcwd()

root = Tk() 

#load 2 images for stamping
tkimg = ImageTk.PhotoImage(Image.open(cwd + "\\spin_ranges\\test.png"))     # Test image
tkimg2 = ImageTk.PhotoImage(Image.open(cwd + "\\spin_ranges\\test2.png"))    # Test image

# A Radiobutton to toggle between images
v = IntVar()
def call():
    canvas.delete(ALL)
    if v.get() == 1:
        canvas.create_image((2, 2), image=tkimg, anchor=NW)
    else:
        canvas.create_image((2, 2), image=tkimg2, anchor=NW)

Label(root, text ="Select an image to place.").grid(row=1, column=0, columnspan=5, sticky=S)
R1=Radiobutton(root, text="range 1", variable=v, value=1, command=call)
R1.grid(row=2, column=0, sticky=N+E)
R1.select()
R2=Radiobutton(root, text="range 2", variable=v, value=2, command=call)
R2.grid(row=2, column=1, sticky=N+E)

# A canvas for mouse events and image drawing
canvas = Canvas(root, height=500, width=500,)
canvas.grid(column=5, row=0, rowspan=4, sticky=W)
canvas.create_image((2, 2), image=tkimg, anchor=NW)

# Enter event loop
root.mainloop()