class SaveInfo:
    # var1 = Tki.IntVar()
    # var2 = Tki.IntVar()
    # var3 = Tki.IntVar()
    def saved_txt(self, entry_name, entry_email, entry_birt, entry_age, entry_add, chk_vax1, chk_vax2, chk_con1, chk_con2, chk_sym1, chk_sym2):
        with open("contact_infos.csv", "w") as saved_file:
            name = saved_file.write("Name: " + entry_name.get() + "\n")
            email = saved_file.write("Email: " + entry_email.get() + "\n")
            birt = saved_file.write("Birthday: " + entry_birt.get() + "\n")
            age = saved_file.write("Age: " + entry_age.get() + "\n")
            add = saved_file.write("Address: " + entry_add.get()+ "\n")
            vax1 = saved_file.write("Have you been vaccinated?: \n" + "Yes: " + str(chk_vax1) + "\n")
            vax2 = saved_file.write(str(chk_vax2))
            con1 =saved_file.write(str(chk_con1))
            con2= saved_file.write(str(chk_con2))
            sym1= saved_file.write(str(chk_sym1))
            sym2 =saved_file.write(str(chk_sym2))
            return name, email, birt, age, add, vax1, vax2, con1, con2, sym1, sym2
            
            
    # def vax(chk_vax1, chk_vax2):
    #     with open("contact_infos.txt", "a") as saved_file: 
    #         if var1.get():
    #             vax1 = saved_file.write("/" + chk_vax1)
    #         else:
    #             vax2 = saved_file.write("/" + chk_vax2)
    #         return vax1, vax2

    # def vax(chk_vax1, chk_vax2, chk_con1, chk_con2, chk_sym1, chk_sym2):     
    #     with open("contact_infos.txt", "a") as saved_file: 
    
    #         return 
