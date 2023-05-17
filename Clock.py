from tkinter import *

from tkinter.ttk import * 
from time import strftime

root = Tk()

root.title('Digital Clock')

def time():

string=strftime("%H:%M:%S %p') lbl.config(text = tick)

lbl.after(1000, clock)

lbl Label(root, font = ('franklin gothic', 60, 'bold'),background = 'black', foreground = 'white')

lbl.pack(anchor = 'center')

clock()

mainloop()
