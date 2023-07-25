class SaveInfo:
    def saved_txt(self, entry_name, entry_email, entry_birt, entry_age, entry_add, vax1_val, vax2_val, con1_val, con2_val, sym1_val, sym2_val):
        with open("contact_infos.csv", "a") as saved_file:
            name = saved_file.write("Name: " + entry_name.get() + "\n")
            email = saved_file.write("Email: " + entry_email.get() + "\n")
            birt = saved_file.write("Birthday: " + entry_birt.get() + "\n")
            age = saved_file.write("Age: " + entry_age.get() + "\n")
            add = saved_file.write("Address: " + entry_add.get()+ "\n")

            # getting value of check boxes       
            chk_val_vax1 = vax1_val.get()
            chk_val_vax2 = vax2_val.get()
            chk_val_con1 = con1_val.get()
            chk_val_con2 = con2_val.get()
            chk_val_sym1 = sym1_val.get()
            chk_val_sym2 = sym2_val.get()
            
            # saving value of checkboxes in the file
            saved_file.write(f"Have you been vaccinated?: \n\tYes: {str(chk_val_vax1)}\n")
            saved_file.write(f"\tNo:  {str(chk_val_vax2)}\n")
            saved_file.write(f"Have you had exposure to a probable or confirmed case in the last 14 days? \n\tYes: {str(chk_val_con1)}\n")
            saved_file.write(f"\tNo:  {str(chk_val_con2)}\n")
            saved_file.write(f"Are you experiencing any COVID-19 symptoms in the past 7 days?\n\tYes: {str(chk_val_sym1)}\n")
            saved_file.write(f"\tNo:  {str(chk_val_sym2)}\n\n\n")
        return name, email, birt, age, add
            

            
        
    
    