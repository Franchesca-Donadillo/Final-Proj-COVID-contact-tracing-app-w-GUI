class SaveInfo:  
        def saved_txt(self, entry_name, entry_email, entry_birt, entry_age, entry_add):
            with open("contact_infos.txt", "a") as saved_file:
                name = saved_file.write(entry_name.get())
                email = saved_file.write(entry_email.get())
                birt = saved_file.write(entry_birt.get())
                age = saved_file.write(entry_age.get())
                add = saved_file.write(entry_add.get())
                #saved_file.write(chk_vax1.selection_own_get)
                # saved_file.write(chk_vax2.selection_get())
                # saved_file.write(chk_vax2.selection_get())
                # saved_file.write(chk_con1.selection_get())
                # saved_file.write(chk_con2.selection_get())
                # saved_file.write(chk_sym1.selection_get())
                # saved_file.write(chk_sym2.selection_get())
            return name, email,birt, age, add
