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
                
            if not entered.strip():
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
                        info.append("Address: " + splt_info[15])
                        info.append("Vaccinated: ")
                        info.append(splt_info[17] + splt_info[18])
                        info.append(splt_info[19] + splt_info[20])
                        info.append("Had exposure: ")
                        info.append(splt_info[22] + splt_info[23])
                        info.append(splt_info[24] + splt_info[25]) 
                        info.append("Has COVID-19 symptoms: ")
                        info.append(splt_info[28] + splt_info[29])
                        info.append(splt_info[30] + splt_info[31])

                if not info:
                    info.append("No Results Found") 
                                                    
            return info
