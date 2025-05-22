from tkinter import *
from random import choice
from time import sleep


vardi = ["kaķis", "suns", "zieds", "debess", "jūra", "upe", "mežs", "laiks", "mēness", "saule","mājas", "auto", "bērns",
        "cilvēks", "prieks", "asaras", "lietus", "sniegs", "vējš", "draugs", "ceļš", "darbs", "skola", "skriet", "iet", "rīts", "vakars",
        "spēks", "vājums", "daba", "dzīvnieks", "putns", "akmens", "ūdens", "zeme", "gaiss", "krāsas", "māksla", "kultūra", "raksts",
        "idejas", "ēdiens", "tēvs", "māte", "brālis", "māsa", "ģimene", "bērni", "dzīvot", "elpot", "just", "sapnis", "klusums",
        "strādāt", "mācīties", "nauda", "tirgus", "veikals", "iela", "parks", "dārzs", "laukums", "stacija", "kuģis",
        "auto", "braukt", "lēkt", "dejojot", "dziedāt", "runāt", "smiekli", "raudāt", "smaidīt", "mīlēt", "ienīst",
        "cerēt","saprast", "atrast", "iegūt", "zaudēt","dot", "ņemt", "mirt", "augt",
        "palīdzēt", "būt", "radīt", "veidot", "šķirties", "tikt", "izprast", "dzīvība", "brīvība", "zīme", "zāle", "smiltis",
        "vērsis", "silts", "skats", "pasaka", "nakts", "gaisma", "spēles", "vārdi", "jēga", "tīrs", "burvība", "mūža", "ciems",
        "dzīvot", "staigāt", "brīvs", "laiks", "miers", "dziedāt", "ziedi", "prāts", "saule", "zeme", "kalns", "jūra",
        "smiltis", "atslēga", "sveiks", "atvērts", "brīvs", "sveiks","tēja", "ziedi", "mīlestība", "cerība", "mīlēt",
        "ziedu", "nakts", "rīta", "burvība", "svētki","brīnums", "spēks", "cīņa", "uzvara", "zaudējums", "kārta",
        "rūpes", "sajūta", "prāts", "sirds", "miers", "siltums","māja", "ceļš","nakts", "rīts",
        "vēlēšanās", "pārdzīvojums", "uzmanība", "radošs", "galva", "garša", "sapnis", "smiekli", "grāmata", "ilgas", "gaisma", "mūzika", "ērts", "smaids"]

alfabets = 'a ā b c č d e ē f g ģ h i ī j k ķ l ļ m n ņ o p r s š t u ū v z ž'

# Canva cilvecina zimesanas laukums
PLATUMS = 200
GARUMS = 300

# Visa loga izmers
LOGA_PLATUMS = 600
LOGA_GARUMS = 350
BACKGROUND = "#808080"

root = Tk()
root.resizable(FALSE, FALSE)
root.option_add("*Background", f"{BACKGROUND}")


root.title("Karatavas")
root.geometry(f"{LOGA_PLATUMS}x{LOGA_GARUMS}")
root.configure(bg="#808080")


class Spele:
    def __init__(self):
        #self.vards = choice(vardi)
        self.vards = choice(vardi)
        self.gajienu_skaits = 7
        self.izmantotie_burti = set()
        self.cilveka_dalas = []  # Saraksts cilvēka daļu kontrolei


    def parbauda_burtu_varda(self, burts) -> bool:
        if burts not in self.izmantotie_burti:
            self.izmantotie_burti.add(burts)
            if burts in self.vards:
                return True
            else:
                self.gajienu_skaits -= 1
                return False
        return None
    
    # 1 = spele beidzas ar uzvaru
    # 0 = spele beidzas ar zaudi
    # None = spele nav beigusies
    def parbauda_vai_cauri(self) -> bool:
        if set(self.vards) <= self.izmantotie_burti:
            return True
        if self.gajienu_skaits == 0:
            return False
        return None


    def dabu_index(self,burts) -> list:
        indeksi = []
        for index, char in enumerate(self.vards):
            if char == burts:
                indeksi.append(index)
        return indeksi


class UzzimeKadrus:
    def nomaina_kadru(self, kadrs, info = None):
        self.nodzes_kadru()
        match kadrs:
            case 'sakuma_ekrans': self.sakuma_ekrans()
            case 'speles_ekrans': self.speles_ekrans()
            case 'noteikumu_ekrans': self.noteikumu_ekrans()
            case 'beigu_ekrans' : self.beigu_ekrans(info)
    

    def sakuma_ekrans(self):
        self.font = ("Arial", 15)
        self.outline = "black"       

        self.main_menu = PhotoImage(file="main_menu.png")
        self.main_menu_label = Label(root, image=self.main_menu)
        self.main_menu_label.pack(side="top", fill="both", expand="yes")

        self.poga_sakt = Button(root, width=15, text="Sākt", borderwidth=5, command=lambda: self.nomaina_kadru('speles_ekrans'))
        self.poga_iziet = Button(root, width=15, text="Iziet", borderwidth=5, command=lambda: root.quit())
        self.poga_noteikumi = Button(root, width=15, text="Noteikumi", borderwidth=5, command= self.noteikumu_ekrans)

        self.poga_sakt.config(font=self.font)
        self.poga_iziet.config(font=self.font)
        self.poga_noteikumi.config(font=self.font)

        self.poga_sakt.place(relx=0.7, rely=0.38, anchor=CENTER)
        self.poga_noteikumi.place(relx=0.7, rely=0.53, anchor=CENTER)
        self.poga_iziet.place(relx=0.7, rely=0.68, anchor=CENTER)
        

    def speles_ekrans(self):
        self.jauna_spele = Spele()

        # Pārbauda ievadīto burtu un atjaunina GUI
        def nosuti_burtu(event):
            burts = entry_burtu_ievade.get().lower()
            if len(burts) != 1:
                return
            
            burts_ir_varda = self.jauna_spele.parbauda_burtu_varda(burts)
            
            if burts_ir_varda is not None:
                entry_burtu_ievade.delete(0, END)
                
                if burts_ir_varda:
                    teksts = list(self.label_minamais_vards["text"])
                    indeksi = self.jauna_spele.dabu_index(burts)
                    for indekss in indeksi:
                        teksts[indekss*2] = burts.upper()
                    self.label_minamais_vards["text"] = ''.join(teksts)
                else:
                    # Parāda nākamo cilvēka daļu
                    dalas_indekss = 6 - self.jauna_spele.gajienu_skaits
                    if dalas_indekss < len(self.cilveka_dalas):
                        self.canvas_cilvecina_zimejums.itemconfig(
                            self.cilveka_dalas[dalas_indekss],
                            state='normal'
                        )
                    self.label_izmantotie_burti["text"] += f"{burts.upper()} "
                
                # Atjaunina atlikušo gājienu skaitu
                self.label_gajienu_skaits["text"] = f"Atlikuši gājieni: {self.jauna_spele.gajienu_skaits}"
            
            self.vai_cauri = self.jauna_spele.parbauda_vai_cauri()

            match self.vai_cauri:
                case True:
                    self.nomaina_kadru("beigu_ekrans", True)
                case False:
                    self.blink_time = 100
                    for i in len(5):
                        for item in self.canvas_cilvecina_zimejums:
                            self.canvas_cilvecina_zimejums.itemconfigure(item, state="hidden")
                        sleep(self.blink_time)
                        for item in self.canvas_cilvecina_zimejums:
                            self.canvas_cilvecina_zimejums.itemconfigure(item, state="normal")
                    self.kadru
                case None:
                    pass
            

        self.frame_cilvecins = Frame(root, bg=BACKGROUND, borderwidth=0,)
        self.frame_speles_lauks = Frame(root, pady=20, bg=BACKGROUND)

        self.canvas_cilvecina_zimejums = Canvas(self.frame_cilvecins, width=PLATUMS, height=GARUMS, highlightthickness=0)
        self.label_minamais_vards = Label(self.frame_speles_lauks, text=f"_ " * len(self.jauna_spele.vards), font=("Arial",35))
        self.label_izmantotie_burti = Label(self.frame_speles_lauks, text="", font=("Arial", 25))
        entry_burtu_ievade = Entry(self.frame_speles_lauks, width=2, font=("Arial",30))

        self.canvas_cilvecina_zimejums.pack(padx=30,pady=20)
        self.label_minamais_vards.pack(pady=(0,20))
        self.label_izmantotie_burti.pack()
        entry_burtu_ievade.pack(pady=40)

        self.frame_cilvecins.pack(side="left", fill="y")
        self.frame_speles_lauks.pack(expand="True")

        self.canvas_cilvecina_zimejums.create_line(40,250,165,250, width=6) # Pamats
        self.canvas_cilvecina_zimejums.create_line(100,250,100,50, width=6) # Stabs
        self.canvas_cilvecina_zimejums.create_line(100,50,175,50, width=6) # Pa labi
        

        # Zīmējam cilvēka daļas sākotnēji neredzamas
        self.cilveka_dalas = [
            self.canvas_cilvecina_zimejums.create_line(175,50,175,80, width=6, state="hidden"), # Uz leju
            self.canvas_cilvecina_zimejums.create_oval(160, 80, 190, 110, state='hidden'),  # Galva
            self.canvas_cilvecina_zimejums.create_line(175, 110, 175, 160, state='hidden'),  # Ķermenis
            self.canvas_cilvecina_zimejums.create_line(175, 110, 160, 140, state='hidden'),  # Kreisā roka
            self.canvas_cilvecina_zimejums.create_line(175, 110, 190, 140, state='hidden'),  # Labā roka
            self.canvas_cilvecina_zimejums.create_line(175, 160, 160, 190, state='hidden'),  # Kreisā kāja
            self.canvas_cilvecina_zimejums.create_line(175, 160, 190, 190, state='hidden'),  # Labā kāja
            self.canvas_cilvecina_zimejums.create_oval(165, 85, 170, 90, state='hidden')     # Acs
        ]

        entry_burtu_ievade.bind("<Return>", nosuti_burtu)

        # Pievieno gājienu skaita rādītāju
        self.label_gajienu_skaits = Label(self.frame_speles_lauks, 
                                         text=f"Atlikuši gājieni: {self.jauna_spele.gajienu_skaits}",
                                         font=("Arial", 20))
        self.label_gajienu_skaits.pack()


    def beigu_ekrans(self, uzvareja:bool):
        if uzvareja:
            self.label_uzvareja = Label(root, text="TU UZVARĒJI!", font=("Arial",35))
            self.label_uzvareja.pack(pady=(75,0))
        else:
            self.label_zaudeja = Label(root, text="TU ZAUDĒJI!", font=("Arial",35))
            self.label_vārds = Label(root, text=f"Vārds bija: {self.jauna_spele.vards}", font=("Arial", 20))
            self.label_zaudeja.pack(pady=(75,0))
            self.label_vārds.pack()

        self.poga_turpinat = Button(root, text="turpināt", font=("Arial",15), command= lambda: self.nomaina_kadru("sakuma_ekrans"))
        self.poga_turpinat.pack(pady=20)


    def noteikumu_ekrans(self):
        noteikumi = Toplevel(root)
        noteikumi.title("Noteikumi")
        noteikumi.geometry(f'{LOGA_PLATUMS}x{LOGA_GARUMS}')
        
        self.label_noteikumi = Label(noteikumi,
                                      text="1. Tev ir 7 gājieni, lai nepakārtu cilvēku! \n" \
                                      "2. Ievadi, burtu norādītajā laukā, katrs nepareizais burts atņem tev vienu gājienu! \n" \
                                      "3. Atmini vārdu, lai uzvarētu! \n",
                                      wraplength=600,
                                      font=("Arial",20),
                                      justify=LEFT)
        
        self.label_noteikumi.pack(pady=(100,0))
        
    def nodzes_kadru(self):
        for widget in root.winfo_children():
            # neizdzest noteikumu ekranu
            if isinstance(widget, Toplevel):
                continue
            widget.destroy()

kadru_zimetajs = UzzimeKadrus()
kadru_zimetajs.sakuma_ekrans()
root.mainloop()