'''
Created on Jan 15, 2017

@author: Marlon_2
'''
import tkinter as tk # import
from tkinter import ttk   # impork ttk from tkinter

win = tk.Tk();       # create instance

#add a title
win.title("Python Hospital Information System");

#add a label
#ttk.Label(win, text="Welcome to Python Hospital Information System").grid(column=0,row=0);

aLabel = ttk.Label(win, text="Welcome to Python Hospital Information System");
aLabel.grid(column=0,row=0);

def clickMe():
    action.configure(text="** I have been clicked **")
    aLabel.configure(foreground='red',background='yellow')
    action.configure(command=clickMeReset) # this is reconfigure
    
def clickMeReset():
    action.configure(text="** Click Me! **")
    aLabel.configure(foreground='black',background='white')
    action.configure(command=clickMe) # this is reconfigure

#Adding a button
action = ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=0, row=1);


    

#button click event callback function


#win.resizable(200, 100); # disable resizing of the GUI

win.mainloop(); # start GUI