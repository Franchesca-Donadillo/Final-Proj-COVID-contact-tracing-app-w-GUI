# Franchesca Marie U. Donadillo
# BSCPE 1-5

# import tkinter
import tkinter as tk
from _tkinter import *

title = tk.Tk()

# create main window
title.title("COVID CONTACT TRACING")
title.geometry("500x500")
title = tk.Canvas(title, width=500, height=500)
title.pack()
background = tk.PhotoImage(file="C:\\Users\\63920\\Downloads\\covid\\covid2.png")
title.create_image(0,0, image= background)

def win1():
    def win2():
        start_btn.destroy() 
        btn1 = tk.Button (title, text = "Submit", width=8, height=2, activebackground= "cyan" ) 
        btn1.place (x=210, y=450)
        
        # title
        lbl_name = tk.Label (title, text = "CONTACT INFORMATION", font="arial")
        lbl_name.place(x=125)

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

        # vaccination
        lbl_vax = tk.Label (title, text = "Have you been vaccinated?")
        lbl_vax.place(x=10, y=205)
        chk_vax1 = tk.Checkbutton(title, text="Yes", activebackground="green")
        chk_vax1.place(x=170,y=205)
        chk_vax2 = tk.Checkbutton(title, text="No", activebackground="green")
        chk_vax2.place(x=215,y=205)

        # close contact
        lbl_con = tk.Label (title, text = "Have you had exposure to a probable or confirmed case in the last 14 days?")
        lbl_con.place(x=10, y=240)
        chk_con = tk.Checkbutton(title, text="Yes", activebackground="green")
        chk_con.place(x=170,y=260)
        chk_con = tk.Checkbutton(title, text="No", activebackground="green")
        chk_con.place(x=215,y=260)

        # experience symptoms
        lbl_sym = tk.Label (title, text = "Are you experiencing any COVID-19 symptoms in the past 7 days?")
        lbl_sym.place(x=10, y=290)
        chk_sym = tk.Checkbutton(title, text="Yes", activebackground="green")
        chk_sym.place(x=170,y=310)
        chk_sym = tk.Checkbutton(title, text="No", activebackground="green")
        chk_sym.place(x=215,y=310)
    
    start_btn = tk.Button (title, text = "Start", width=15, height=4, activebackground= "cyan", command=win2 ) 
    start_btn.place (x=188, y=310)

win1()
title.mainloop()


