# Franchesca Marie U. Donadillo
# BSCPE 1-5

# import tkinter
import tkinter as tk
from _tkinter import *

title = tk.Tk()

# create main window
title.title("COVID CONTACT TRACING")
title.geometry("670x670")

def win1():
    def win2():
        start_btn.destroy() 
        btn1 = tk.Button (title, text = "Submit", width=8, height=2, activebackground= "cyan" ) 
        btn1.place (x=300, y=620)
        lbl_name = tk.Label (title, text = "name")
        lbl_name.place(x=10, y=15)

    start_btn = tk.Button (title, text = "Start", width=15, height=4, activebackground= "cyan", command=win2 ) 
    start_btn.place (x=280, y=480)

win1()
title.mainloop()


