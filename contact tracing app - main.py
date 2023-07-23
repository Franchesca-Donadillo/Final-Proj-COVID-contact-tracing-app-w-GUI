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
        
        # name info
        lbl_name = tk.Label (title, text = "Name")
        lbl_name.place(x=10, y=55)
        entry_name = tk.Entry (title, width="30")
        entry_name.place(x=70,y=55)
        
        # email info
        lbl_email = tk.Label (title, text = "Email")
        lbl_email.place(x=10, y=85)
        entry_email = tk.Entry (title, width="30")
        entry_email.place(x=70,y=85)

        # birthday info
        lbl_birt = tk.Label (title, text = "Birthday")
        lbl_birt.place(x=10, y=115)
        entry_birt = tk.Entry (title, width="30")
        entry_birt.place(x=70,y=115)
        
        # age info
        lbl_age = tk.Label (title, text = "Age")
        lbl_age.place(x=10, y=145)
        entry_age = tk.Entry (title, width="30")
        entry_age.place(x=70,y=145)

        # address info
        lbl_add = tk.Label (title, text = "Address")
        lbl_add.place(x=10, y=175)
        entry_add = tk.Entry (title, width="30")
        entry_add.place(x=70,y=175)


    start_btn = tk.Button (title, text = "Start", width=15, height=4, activebackground= "cyan", command=win2 ) 
    start_btn.place (x=280, y=480)

win1()
title.mainloop()


