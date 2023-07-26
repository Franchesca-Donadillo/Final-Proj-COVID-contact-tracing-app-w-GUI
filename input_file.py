class SaveInfo:
    def saved_txt(self, entry_name, entry_email, entry_birt, entry_age, entry_add, vax1_val, vax2_val, con1_val, con2_val, sym1_val, sym2_val):
        with open("contact_infos.txt", "a") as saved_file:
            name = saved_file.write("Name: " + entry_name.get() + "\t")
            email = saved_file.write("Email: " + entry_email.get() + "\t")
            birt = saved_file.write("Birthday: " + entry_birt.get() + "\t")
            age = saved_file.write("Age: " + entry_age.get() + "\t")
            add = saved_file.write("Address: " + entry_add.get()+ "\t")
            
            # saving value of checkboxes in the file
            saved_file.write(f"Vaccinated:\tYes: {str(vax1_val.get())}  ")
            saved_file.write(f"No:  {str(vax2_val.get())}\t")
            saved_file.write(f"Exposure:\tYes: {str(con1_val.get())}  ")
            saved_file.write(f"No:  {str(con2_val.get())}\n")
            saved_file.write(f"COVID-19 symptoms:\tYes: {str(sym1_val.get())}  ")
            saved_file.write(f"No:  {str(sym2_val.get())}\n\n")
        return name, email, birt, age, add
            

            
        
    
    