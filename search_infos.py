class Search:
        def upd_info(self, data_list, inform, end):
            data_list.delete(0, end)

            for line in inform:
                data_list.insert(end, line)

        def check(self, entry_search):
            with open("contact_infos.txt", "r") as search_file:
                information = search_file.readlines()

            # get user entry
            entered = entry_search.get()
                
            if entered == " ".split("\n"):
                info = information

            else:
                info =[]
                for line in information:
                     if entered.lower() in line.lower():
                          info.append(line)
                          
            return info
