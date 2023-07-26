# Franchesca Marie U. Donadillo
# BSCPE 1-5

# import tkinter
import tkinter as tk
from _tkinter import *
from PIL import Image, ImageTk

# import functions
from input_file import SaveInfo
from window_des import Window

title = tk.Tk()
info = SaveInfo()
win_des = Window()

# assign int value to checkbox 
vax1_val = tk.IntVar()
vax2_val = tk.IntVar()
con1_val = tk.IntVar()
con2_val = tk.IntVar()
sym1_val = tk.IntVar()
sym2_val = tk.IntVar()

# create main window
title.title("COVID CONTACT TRACING")
title.geometry("500x500")
title = tk.Canvas(title, width=500, height=500)
title.pack()
background = tk.PhotoImage(file="C:\\Users\\63920\\Downloads\\covid\\covid2.png")
title.create_image(0,0, image= background)
btn_img = ImageTk.PhotoImage(Image.open("C:\\Users\\63920\\Downloads\\covid\\search.png").resize((15,15)))

def win1():
    def win2():
        def win3():
            def win4():
                # def win5():
                    
                    
                    # return win5

                # destroy window 3
                win_des.win3_des(lbl_rec, btn_rec, btn_quit)    

                # call window 1 to return to first page
                win1()
                
            # destroy window 2
            win_des.win2_des(lbl_titl, btn1, lbl_name, entry_name, lbl_email, entry_email, lbl_birt, entry_birt, lbl_age, entry_age, lbl_add, entry_add, lbl_vax, chk_vax1, chk_vax2, lbl_con, chk_con1, chk_con2, lbl_sym, chk_sym1, chk_sym2)
            
            # Recorded message to user
            lbl_rec = tk.Label (title, text = "RESPONSE HAS BEEN RECORDED", font="arial", bg="white", foreground="black")
            lbl_rec.place(x=95, y=55)

            # Button to return to main menu
            btn_rec = tk.Button (title, text = "Return to Main Menu", width=20, height=3, activebackground= "cyan", command=win4)
            btn_rec.place (x=170, y=350)

            # Butoon to quit
            btn_quit = tk.Button (title, text = "Quit", width=20, height=3, activebackground= "cyan", command=title.quit)
            btn_quit.place (x=170, y=400)

        # destroy window 1
        win_des.win1_des(lbl_main, start_btn, entry_search, btn_search)
        
        # title
        lbl_titl = tk.Label (title, text = "CONTACT INFORMATION", font="arial", bg="white", foreground="black")
        lbl_titl.place(x=125, y=5)

        # name info
        lbl_name = tk.Label (title, text = "Name", bg="white")
        lbl_name.place(x=10, y=55)
        entry_name = tk.Entry (title, width="30")
        entry_name.place(x=70,y=55)
        
        # email info
        lbl_email = tk.Label (title, text = "Email", bg="white")
        lbl_email.place(x=10, y=85)
        entry_email = tk.Entry (title, width="30")
        entry_email.place(x=70,y=85)

        # birthday info
        lbl_birt = tk.Label (title, text = "Birthday", bg="white")
        lbl_birt.place(x=10, y=115)
        entry_birt = tk.Entry (title, width="30")
        entry_birt.place(x=70,y=115)
        
        # age info
        lbl_age = tk.Label (title, text = "Age", bg="white")
        lbl_age.place(x=10, y=145)
        entry_age = tk.Entry (title, width="30")
        entry_age.place(x=70,y=145)

        # address info
        lbl_add = tk.Label (title, text = "Address", bg="white")
        lbl_add.place(x=10, y=175)
        entry_add = tk.Entry (title, width="30")
        entry_add.place(x=70,y=175)

        # vaccination
       
        lbl_vax = tk.Label (title, text = "Have you been vaccinated?", bg="white")
        lbl_vax.place(x=10, y=205)
        chk_vax1 = tk.Checkbutton(title, text="Yes", activebackground="green", bg="white",variable=vax1_val)
        chk_vax1.place(x=170,y=205)
        chk_vax2 = tk.Checkbutton(title, text="No", activebackground="green", bg="white")
        chk_vax2.place(x=215,y=205)

        # close contact
        lbl_con = tk.Label (title, text = "Have you had exposure to a probable or confirmed case in the last 14 days?", bg="white")
        lbl_con.place(x=10, y=240)
        chk_con1 = tk.Checkbutton(title, text="Yes", activebackground="green", bg="white")
        chk_con1.place(x=170,y=260)
        chk_con2 = tk.Checkbutton(title, text="No", activebackground="green", bg="white")
        chk_con2.place(x=215,y=260)

        # experience symptoms
        lbl_sym = tk.Label (title, text = "Are you experiencing any COVID-19 symptoms in the past 7 days?", bg="white")
        lbl_sym.place(x=10, y=290)
        chk_sym1 = tk.Checkbutton(title, text="Yes", activebackground="green", bg="white")
        chk_sym1.place(x=170,y=310)
        chk_sym2 = tk.Checkbutton(title, text="No", activebackground="green", bg="white")
        chk_sym2.place(x=215,y=310)

        # transfer data to a text file
        info.saved_txt(entry_name, entry_email, entry_birt, entry_age, entry_add, vax1_val, vax2_val, con1_val, con2_val, sym1_val, sym2_val)

        # submit button to save infos
        btn1 = tk.Button (title, text = "Submit", width=8, height=2, activebackground= "cyan", command=lambda: [info.saved_txt(entry_name, entry_email, entry_birt, entry_age, entry_add, vax1_val, vax2_val, con1_val, con2_val, sym1_val, sym2_val), win3()])
        btn1.place (x=210, y=450)

    # search box
    entry_search = tk.Entry (title, width="60")
    entry_search.place(x=50,y=20)

    # search button
    btn_search = tk.Button (master=title, image=btn_img , width=15, height=15, activebackground= "cyan")
    btn_search.place (x=425, y=18)


    # start button
    lbl_main= tk.Label (title, text = "COVID CONTACT TRACING APP", bg="white", foreground="blue", font="helvetica")
    lbl_main.pack(padx=40, pady=40)
    lbl_main.place(x=100, y=250)
    start_btn = tk.Button (title, text = "Start", width=15, height=4, activebackground= "cyan", command=win2, padx=10 ) 
    start_btn.place (x=180, y=310)

win1()
title.mainloop()


