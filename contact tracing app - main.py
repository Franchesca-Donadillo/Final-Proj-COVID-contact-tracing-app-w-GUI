# Franchesca Marie U. Donadillo
# BSCPE 1-5

# import tkinter
import tkinter as tk
from _tkinter import *

title = tk.Tk()

# create main window
title.title("COVID CONTACT TRACING")
title.geometry("670x670")

start_btn = tk.Button (title, text = "Start", width=15, height=4, activebackground= "cyan" ) 
start_btn.place (x=280, y=480)
title.mainloop()
