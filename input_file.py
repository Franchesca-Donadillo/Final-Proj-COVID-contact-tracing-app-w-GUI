class SaveInfo:
    def saved_txt(self, entry_name, entry_email, entry_birt, entry_age, entry_add, vax1_val, vax2_val, con1_val, con2_val, sym1_val, sym2_val):
        with open("contact_infos.txt", "a+") as saved_file:
            name = saved_file.write("Name: " + entry_name.get() + "\n")
            email = saved_file.write("Email: " + entry_email.get() + "\n")
            birt = saved_file.write("Birthday: " + entry_birt.get() + "\n")
            age = saved_file.write("Age: " + entry_age.get() + "\n")
            add = saved_file.write("Address: " + entry_add.get()+ "\n")
            
            # saving value of checkboxes in the file
            saved_file.write(f"Have you been vaccinated?: \n\tYes: {str(vax1_val.get())}\n")
            saved_file.write(f"\tNo:  {str(vax2_val.get())}\n")
            saved_file.write(f"Have you had exposure to a probable or confirmed case in the last 14 days? \n\tYes: {str(con1_val.get())}\n")
            saved_file.write(f"\tNo:  {str(con2_val.get())}\n")
            saved_file.write(f"Are you experiencing any COVID-19 symptoms in the past 7 days?\n\tYes: {str(sym1_val.get())}\n")
            saved_file.write(f"\tNo:  {str(sym2_val.get())}\n\n")
        return name, email, birt, age, add
            

            
        
    
    