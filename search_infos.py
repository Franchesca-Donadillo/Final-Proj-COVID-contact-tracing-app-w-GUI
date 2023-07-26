class Search:
        def upd_info(self, data_list, info):
            data_list.delete(0, END)

            for line in info:
                data_list.insert(END, line)

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
                          info.append(line)
                          
 

#     # def searching(self,shown_text,  entry_search):
#     #     personal_info = entry_search.get()
#     #     shown_text.config(state=Tki.NORMAL)
#     #     shown_text.delete(1.0, Tki.END)

    
#         #     for line in search_file:
#         #         if personal_info.lower() in line.lower():
#         #             shown_text.insert(Tki.END, line)

#     #     shown_text.config(state=Tki.DISABLED)

#     information = search_file
    

#     upd_info(information)
