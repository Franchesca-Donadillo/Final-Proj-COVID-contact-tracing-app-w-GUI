class Search:
        def upd_info(self, data_list, inform):
            data_list.delete(0, "end")

            for line in inform:
                data_list.insert("end", line)

        def check(self, entry_search):
            with open("contact_infos.txt", "r") as search_file:
                information = search_file.readlines()

            # get user entry
            entered = entry_search.get()
                
            if entered == " ":
                info = information

            else:
                info =[]
                for line in information:
                    if entered.lower() in line.lower():
                        splt_info = line.split()
                        info.append("Surname: " + splt_info[1])
                        info.append("First Name: " + splt_info[4])
                        info.append("Middle Name: " + splt_info[7])
                        info.append("Email: " + splt_info[9])
                        info.append("Birthday: " + splt_info[11])
                        info.append("Age: " + splt_info[13])
                        info.append("Address: " + splt_info[15] + splt_info[16])
                        info.append("Vaccinated: ")
                        info.append(splt_info[18] + splt_info[19])
                        info.append(splt_info[20] + splt_info[21])
                        info.append("Had exposure: ")
                        info.append(splt_info[23] + splt_info[24])
                        info.append(splt_info[25] + splt_info[26]) 
                        info.append("Has COVID-19 symptoms: ")
                        info.append(splt_info[29] + splt_info[30])
                        info.append(splt_info[31] + splt_info[32])
                    
                    elif entered != information:
                        info.append("No Results Found")


            return info
