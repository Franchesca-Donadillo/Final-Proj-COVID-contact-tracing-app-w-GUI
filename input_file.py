class SaveInfo:
    def saved_txt(self, entry_name, entry_email, entry_birt, entry_age, entry_add, chk_vax1, chk_vax2, chk_con1, chk_con2, chk_sym1, chk_sym2):
        with open("contact_infos.txt", "w") as saved_file:
            name = saved_file.write("Name: " + entry_name.get() + "\n")
            email = saved_file.write("Email: " + entry_email.get() + "\n")
            birt = saved_file.write("Birthday: " + entry_birt.get() + "\n")
            age = saved_file.write("Age: " + entry_age.get() + "\n")
            add = saved_file.write("Address: " + entry_add.get()+ "\n")
            vax1 = saved_file.write(chk_vax1.get())
            vax2 = saved_file.write(chk_vax2.get())
            con1 =saved_file.write(chk_con1.get())
            con2= saved_file.write(chk_con2.get())
            sym1= saved_file.write(chk_sym1.get())
            sym2 =saved_file.write(chk_sym2.get())
            return name, email, birt, age, add, vax1, vax2, con1, con2, sym1, sym2
