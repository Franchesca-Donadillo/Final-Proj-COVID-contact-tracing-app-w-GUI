class Window:
    def win1_des(self, lbl_main, start_btn):
        lbl_main.destroy()
        start_btn.destroy()
        
    def win2_des(self, lbl_titl, btn1, lbl_surname, entry_surname, entry_first_name, lbl_first_name, entry_mid_name, lbl_mid_name, lbl_email, entry_email, lbl_birt, entry_birt, lbl_age, entry_age, lbl_add, entry_add, lbl_vax, chk_vax1, chk_vax2, lbl_con, chk_con1, chk_con2, lbl_sym, chk_sym1, chk_sym2):
            lbl_titl.destroy()
            btn1.destroy()
            lbl_surname.destroy()
            entry_surname.destroy()
            lbl_first_name.destroy()
            entry_first_name.destroy()
            lbl_mid_name.destroy()
            entry_mid_name.destroy()
            lbl_email.destroy()
            entry_email.destroy()
            lbl_birt.destroy()
            entry_birt.destroy()
            lbl_age.destroy()
            entry_age.destroy()
            lbl_add.destroy()
            entry_add.destroy()
            lbl_vax.destroy()
            chk_vax1.destroy()
            chk_vax2.destroy()
            lbl_con.destroy()
            chk_con1.destroy()
            chk_con2.destroy()
            lbl_sym.destroy()
            chk_sym1.destroy()
            chk_sym2.destroy()

    def win2_reset(self, vax1_val, vax2_val, con1_val, con2_val, sym1_val, sym2_val):
        vax1_val.set(0)
        vax2_val.set(0)
        con1_val.set(0)
        con2_val.set(0)
        sym1_val.set(0)
        sym2_val.set(0)
         

    def win3_des(self, lbl_rec, btn_rec, btn_quit):
        lbl_rec.destroy()
        btn_rec.destroy()
        btn_quit.destroy()

    def win4_des(self, entry_search, btn_search):
        entry_search.destroy()
        btn_search.destroy()

    def win5_des(self, data_list, entry_search, btn_rec, btn_search, btn_quit1):
        data_list.destroy()
        entry_search.destroy()
        btn_rec.destroy()
        btn_search.destroy()
        btn_quit1.destroy()