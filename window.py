# import tkinter as tk
# from _tkinter import *

# title = tk.Tk()

# class Window:
#     def win1():
#         def win2():
#             def win3():
#                 lbl_titl.destroy()
#                 btn1.destroy()
#                 lbl_name.destroy()
#                 lbl_name.destroy()
#                 entry_name.destroy()
#                 lbl_email.destroy()
#                 entry_email.destroy()
#                 lbl_birt.destroy()
#                 entry_birt.destroy()
#                 lbl_age.destroy()
#                 entry_age.destroy()
#                 lbl_add.destroy()
#                 entry_add.destroy()
#                 lbl_vax.destroy()
#                 chk_vax1.destroy()
#                 chk_vax2.destroy()
#                 lbl_con.destroy()
#                 chk_con1.destroy()
#                 chk_con2.destroy()
#                 lbl_sym.destroy()
#                 chk_sym1.destroy()
#                 chk_sym2.destroy()

#             lbl_main.destroy()
#             start_btn.destroy() 
#             btn1 = tk.Button (title, text = "Submit", width=8, height=2, activebackground= "cyan", command=win3) 
#             btn1.place (x=210, y=450)
            
#             # title
#             lbl_titl = tk.Label (title, text = "CONTACT INFORMATION", font="arial", bg="white", foreground="black")
#             lbl_titl.place(x=125, y=5)

#             # name info
#             lbl_name = tk.Label (title, text = "Name", bg="white")
#             lbl_name.place(x=10, y=55)
#             entry_name = tk.Entry (title, width="30")
#             entry_name.place(x=70,y=55)
            
#             # email info
#             lbl_email = tk.Label (title, text = "Email", bg="white")
#             lbl_email.place(x=10, y=85)
#             entry_email = tk.Entry (title, width="30")
#             entry_email.place(x=70,y=85)

#             # birthday info
#             lbl_birt = tk.Label (title, text = "Birthday", bg="white")
#             lbl_birt.place(x=10, y=115)
#             entry_birt = tk.Entry (title, width="30")
#             entry_birt.place(x=70,y=115)
            
#             # age info
#             lbl_age = tk.Label (title, text = "Age", bg="white")
#             lbl_age.place(x=10, y=145)
#             entry_age = tk.Entry (title, width="30")
#             entry_age.place(x=70,y=145)

#             # address info
#             lbl_add = tk.Label (title, text = "Address", bg="white")
#             lbl_add.place(x=10, y=175)
#             entry_add = tk.Entry (title, width="30")
#             entry_add.place(x=70,y=175)

#             # vaccination
#             lbl_vax = tk.Label (title, text = "Have you been vaccinated?", bg="white")
#             lbl_vax.place(x=10, y=205)
#             chk_vax1 = tk.Checkbutton(title, text="Yes", activebackground="green", bg="white")
#             chk_vax1.place(x=170,y=205)
#             chk_vax2 = tk.Checkbutton(title, text="No", activebackground="green", bg="white")
#             chk_vax2.place(x=215,y=205)

#             # close contact
#             lbl_con = tk.Label (title, text = "Have you had exposure to a probable or confirmed case in the last 14 days?", bg="white")
#             lbl_con.place(x=10, y=240)
#             chk_con1 = tk.Checkbutton(title, text="Yes", activebackground="green", bg="white")
#             chk_con1.place(x=170,y=260)
#             chk_con2 = tk.Checkbutton(title, text="No", activebackground="green", bg="white")
#             chk_con2.place(x=215,y=260)

#             # experience symptoms
#             lbl_sym = tk.Label (title, text = "Are you experiencing any COVID-19 symptoms in the past 7 days?", bg="white")
#             lbl_sym.place(x=10, y=290)
#             chk_sym1 = tk.Checkbutton(title, text="Yes", activebackground="green", bg="white")
#             chk_sym1.place(x=170,y=310)
#             chk_sym2 = tk.Checkbutton(title, text="No", activebackground="green", bg="white")
#             chk_sym2.place(x=215,y=310)
        
#         lbl_main= tk.Label (title, text = "COVID CONTACT TRACING APP", bg="white", foreground="blue", font="helvetica")
#         lbl_main.place(x=100, y=250)
#         start_btn = tk.Button (title, text = "Start", width=15, height=4, activebackground= "cyan", command=win2, padx=10 ) 
#         start_btn.place (x=188, y=310)