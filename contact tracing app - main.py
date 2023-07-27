# Franchesca Marie U. Donadillo
# BSCPE 1-5

# import tkinter
import tkinter as tk
from _tkinter import *
from PIL import Image, ImageTk
from tkinter import scrolledtext

# import functions
from input_file import SaveInfo
from window_des import Window
from search_infos import Search

title = tk.Tk()
info = SaveInfo()
win_des = Window()
srch_info = Search()

# assign int value to checkbox 
vax1_val = tk.IntVar()
vax2_val = tk.IntVar()
con1_val = tk.IntVar()
con2_val = tk.IntVar()
sym1_val = tk.IntVar()
sym2_val = tk.IntVar()
end = tk.END

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
                def win5():
                    def win6():
                        # destroy window 5
                        win_des.win5_des(data_list, entry_search, btn_search, btn_rec, btn_quit1)

                        # call window 1 to return to first page
                        win1()
                    
                    # destroy data_list1
                    data_list1.destroy()

                    # list box for the searched data 
                    data_list = tk.Listbox(title, width = 80, height=165) 
                    data_list.pack(pady=50, padx=50)
                    

                    entry_search.bind("<KeyRelease>", lambda: srch_info.check(entry_search, data_list))

                    info = srch_info.check(entry_search)

                    srch_info.upd_info(data_list,info)
                    
                    # Button to return to main menu
                    btn_rec = tk.Button (title, text = "Return to Main Menu", width=20, height=2, activebackground= "cyan", command=win6)
                    btn_rec.place (x=110, y=430)

                    # button to exit the
                    btn_quit1 = tk.Button (title, text = "Quit", width=10, height=2, activebackground= "cyan", command=title.quit)
                    btn_quit1.place (x=270, y=430)

                # destroy window 3
                win_des.win3_des(lbl_rec, btn_rec, btn_quit) 

                # search box
                entry_search = tk.Entry (title, width="60")
                entry_search.place(x=50,y=20)

                # search button
                btn_search = tk.Button (master=title, image=btn_img , width=15, height=15, activebackground= "cyan", command=win5)
                btn_search.place (x=425, y=18)

                # list of read line in txt file
                data_list1 = tk.Listbox(title, width = 80, height=165) 
                data_list1.pack(pady=50, padx=50)
                
            # destroy window 2
            win_des.win2_des(lbl_titl, btn1, lbl_surname, entry_surname, entry_first_name, lbl_first_name, entry_mid_name, lbl_mid_name, lbl_email, entry_email, lbl_birt, entry_birt, lbl_age, entry_age, lbl_add, entry_add, lbl_vax, chk_vax1, chk_vax2, lbl_con, chk_con1, chk_con2, lbl_sym, chk_sym1, chk_sym2)            

            # Recorded message to user
            lbl_rec = tk.Label (title, text = "RESPONSE HAS BEEN RECORDED", font="arial", bg="white", foreground="black")
            lbl_rec.place(x=95, y=105)

            # Button to return to main menu
            btn_rec = tk.Button (title, text = "Search Entry", width=20, height=3, activebackground= "cyan", command=win4)
            btn_rec.place (x=170, y=350)

            # Butoon to quit
            btn_quit = tk.Button (title, text = "Quit", width=20, height=3, activebackground= "cyan", command=title.quit)
            btn_quit.place (x=170, y=410)

        # destroy window 1
        win_des.win1_des(lbl_main, start_btn)
        
        # title
        lbl_titl = tk.Label (title, text = "CONTACT INFORMATION", font="arial", bg="white", foreground="black")
        lbl_titl.place(x=125, y=5)

        # surname info
        lbl_surname = tk.Label (title, text = "Surame", bg="white")
        lbl_surname.place(x=10, y=55)
        entry_surname = tk.Entry (title, width="60")
        entry_surname.place(x=100,y=55)

         # first name info
        lbl_first_name = tk.Label (title, text = "First name", bg="white")
        lbl_first_name.place(x=10, y=85)
        entry_first_name = tk.Entry (title, width="60")
        entry_first_name.place(x=100,y=85)

         # middle name info
        lbl_mid_name = tk.Label (title, text = "Middle name", bg="white")
        lbl_mid_name.place(x=10, y=115)
        entry_mid_name = tk.Entry (title, width="60")
        entry_mid_name.place(x=100,y=115)
        
        # email info
        lbl_email = tk.Label (title, text = "Email", bg="white")
        lbl_email.place(x=10, y=145)
        entry_email = tk.Entry (title, width="60")
        entry_email.place(x=100,y=145)

        # birthday info
        lbl_birt = tk.Label (title, text = "Birthday", bg="white")
        lbl_birt.place(x=10, y=175)
        entry_birt = tk.Entry (title, width="60")
        entry_birt.place(x=100,y=175)
        
        # age info
        lbl_age = tk.Label (title, text = "Age", bg="white")
        lbl_age.place(x=10, y=205)
        entry_age = tk.Entry (title, width="60")
        entry_age.place(x=100,y=205)

        # address info
        lbl_add = tk.Label (title, text = "Address", bg="white")
        lbl_add.place(x=10, y=235)
        entry_add = tk.Entry (title, width="60")
        entry_add.place(x=100,y=235)

        # vaccination
       
        lbl_vax = tk.Label (title, text = "Have you been vaccinated?", bg="white")
        lbl_vax.place(x=10, y=265)
        chk_vax1 = tk.Checkbutton(title, text="Yes", activebackground="green", bg="white",variable=vax1_val)
        chk_vax1.place(x=170,y=265)
        chk_vax2 = tk.Checkbutton(title, text="No", activebackground="green", bg="white", variable=vax2_val)
        chk_vax2.place(x=215,y=265)

        # close contact
        lbl_con = tk.Label (title, text = "Have you had exposure to a probable or confirmed case in the last 14 days?", bg="white")
        lbl_con.place(x=10, y=295)
        chk_con1 = tk.Checkbutton(title, text="Yes", activebackground="green", bg="white", variable=con1_val)
        chk_con1.place(x=170,y=310)
        chk_con2 = tk.Checkbutton(title, text="No", activebackground="green", bg="white", variable=con2_val)
        chk_con2.place(x=215,y=310)

        # experience symptoms
        lbl_sym = tk.Label (title, text = "Are you experiencing any COVID-19 symptoms in the past 7 days?", bg="white")
        lbl_sym.place(x=10, y=340)
        chk_sym1 = tk.Checkbutton(title, text="Yes", activebackground="green", bg="white", variable=sym1_val)
        chk_sym1.place(x=170,y=355)
        chk_sym2 = tk.Checkbutton(title, text="No", activebackground="green", bg="white", variable=sym2_val)
        chk_sym2.place(x=215,y=355)

        # transfer data to a text file
        info.saved_txt(entry_surname,entry_first_name,entry_mid_name, entry_email, entry_birt, entry_age, entry_add, vax1_val, vax2_val, con1_val, con2_val, sym1_val, sym2_val)

        # submit button to save infos
        btn1 = tk.Button (title, text = "Submit", width=8, height=2, activebackground= "cyan", command=lambda: [info.saved_txt(entry_surname, entry_first_name, entry_mid_name, entry_email, entry_birt, entry_age, entry_add, vax1_val, vax2_val, con1_val, con2_val, sym1_val, sym2_val), win3()])
        btn1.place (x=210, y=450)

    # start button
    lbl_main= tk.Label (title, text = "COVID CONTACT TRACING APP", bg="white", foreground="blue", font="Verdana")
    lbl_main.pack(padx=40, pady=40)
    lbl_main.place(x=100, y=250)
    start_btn = tk.Button (title, text = "Start", width=15, height=4, activebackground= "cyan", command=win2, padx=10 ) 
    start_btn.place (x=180, y=310)

win1()
title.mainloop()


