from tkinter import *
from random import randint, choice
import sys

#TODO 
# smukaku sakuma ekranu


vardi = [
    "ābols", "banāns", "cilvēks", "durvis", "ēka", "frāze", "galds", "hokejs", "izglītība", "jūra",
    "koks", "laiva", "māja", "nakts", "ogle", "pilsēta", "rīts", "saule", "tēvs", "ūdens",
    "vārds", "zāle", "žogs", "ķirsis", "ļoti", "mēness", "nams", "opera", "pērle", "rūķis",
    "siena", "tornis", "ūpis", "viesis", "zieds", "žurnāls", "ķēde", "ļaudis", "mētelis", "naktsskapis",
    "ozols", "pulkstenis", "rati", "sēne", "tēja", "ūdensvīrs", "viesnīca", "zivs", "žurka", "ķirbis",
    "ļoti", "mēle", "nams", "opera", "pērle", "rūķis", "siena", "tornis", "ūpis", "viesis",
    "akmens", "balons", "cimdi", "dators", "ēdiens", "futbols", "grāmata", "horizonts", "indekss", "jautājums",
    "kaķis", "lampa", "maize", "nams", "ogas", "pulkstenis", "raksts", "saldējums", "tornis", "ūdenskrāns",
    "viesis", "zīmulis", "žurnāls", "ķirbis", "ļaudis", "mētelis", "nakts", "ozols", "pulkstenis", "rati",
    "sēne", "tēja", "ūdensvīrs", "viesnīca", "zivs", "žurka", "ķirbis", "ļoti", "mēle", "nams",
    "opera", "pērle", "rūķis", "siena", "tornis", "ūpis", "viesis", "zieds", "žurnāls", "ķēde"
]
alfabets = 'a ā b c č d e ē f g ģ h i ī j k ķ l ļ m n ņ o p r s š t u ū v z ž'

# Canva cilvecina zimesanas laukums
PLATUMS = 200
GARUMS = 300

# Visa loga izmers
LOGA_PLATUMS = 650
LOGA_GARUMS = 350


root = Tk()

root.bind("<F11>", lambda e: root.attributes("-fullscreen",True))
root.bind("<Escape>", lambda e: root.attributes("-fullscreen",False))

root.title("Karatavas")
root.geometry(f"{LOGA_PLATUMS}x{LOGA_GARUMS}")
#root.resizable(FALSE, FALSE)


class Spele:
    def __init__(self):
        self.vards = choice(vardi)
        self.gajienu_skaits = 7
        self.izmantotie_burti = set()
        self.cilveka_dalas = []  # Saraksts cilvēka daļu kontrolei

    def parbauda_burtu_varda(self, burts) -> bool:
        if burts not in self.izmantotie_burti:
            self.izmantotie_burti.add(burts)
            if burts in self.vards:
                # Pārbauda vai vārds ir pilnībā atminēts
                atminetie_burti = set(burts for burts in self.izmantotie_burti if burts in self.vards)
                if set(self.vards) <= atminetie_burti:
                    self.beidz_speli(True)
                return True
            else:
                self.gajienu_skaits -= 1
                if self.gajienu_skaits == 0:
                    self.beidz_speli(False)
                return False
        return None

    def dabu_index(self,burts) -> list:
        indeksi = []
        for index, char in enumerate(self.vards):
            if char == burts:
                indeksi.append(index)
        return indeksi

    def beidz_speli(self, uzvareja: bool):
        kadru_zimetajs.nomaina_kadru('beigu_ekrans', uzvareja)


class UzzimeKadrus:
    def nomaina_kadru(self, kadrs, info = None):
        self.nodzes_kadru()
        match kadrs:
            case 'sakuma_ekrans': self.sakuma_ekrans()
            case 'speles_ekrans': self.speles_ekrans()
            case 'noteikumu_ekrans': self.noteikumu_ekrans()
            case 'beigu_ekrans' : self.beigu_ekrans(info)
    

    def sakuma_ekrans(self):
        self.poga_sakt = Button(root, width=12, text="Sākt", command=lambda: self.nomaina_kadru('speles_ekrans'))
        self.poga_iziet = Button(root, width=12, text="Iziet", command=lambda: root.quit())
        self.poga_noteikumi = Button(root, width=12, text="Noteikumi", command= self.noteikumu_ekrans)

        self.poga_sakt.place(relx=0.1, y=LOGA_GARUMS-200)
        self.poga_iziet.place(relx=0.45, y=LOGA_GARUMS-200)
        self.poga_noteikumi.place(relx=0.8, y=LOGA_GARUMS-200)


    def speles_ekrans(self):
        self.jauna_spele = Spele()

        # Pārbauda ievadīto burtu un atjaunina GUI
        def nosuti_burtu(event):
            burts = entry_burtu_ievade.get().lower()
            if len(burts) != 1:  # Pārbauda vai ievadīts tikai viens burts
                entry_burtu_ievade.delete(0, END)
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

        self.frame_cilvecins = Frame(root)
        self.frame_speles_lauks = Frame(root, pady=20)

        self.canvas_cilvecina_zimejums = Canvas(self.frame_cilvecins, width=PLATUMS, height=GARUMS)
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
        self.label_gajienu_skaits.pack(pady=10)


    def beigu_ekrans(self, uzvareja:bool):
        if uzvareja:
            self.label_uzvareja = Label(root, text="TU UZVARĒJI!", font=("Arial",35))
            self.label_uzvareja.pack()
        else:
            self.label_zaudeja = Label(root, text="TU ZAUDĒJI!", font=("Arial",35))
            self.label_vārds = Label(root, text=f"Vārds bija: {self.jauna_spele.vards}", font=("Arial", 20))
            self.label_zaudeja.pack()
            self.label_vārds.pack()

        self.poga_turpinat = Button(root, text="turpināt", command= lambda: self.nomaina_kadru("sakuma_ekrans"))
        self.poga_turpinat.pack()


    def noteikumu_ekrans(self):
        noteikumi = Toplevel(root)
        noteikumi.title("Noteikumi")
        noteikumi.geometry(f'{LOGA_PLATUMS}x{LOGA_GARUMS}')
        
        t1 = Label(noteikumi,text="Tev ir 7 gājieni, lai nepakārtu cilvēku!", font=("Arial",10))
        t2 = Label(noteikumi, text="Ievadi, burtu norādītajā laukā, katrs nepareizais burts atņem tev vienu gājienu!", font=("Arial",10))
        t3 = Label(noteikumi, text="Atmini vārdu, lai uzvarētu!", font=("Arial",10))
        
        t1.pack(pady=(125,0))
        t2.pack()
        t3.pack()
        

    def nodzes_kadru(self):
        for widget in root.winfo_children():
            widget.destroy()

kadru_zimetajs = UzzimeKadrus()
kadru_zimetajs.sakuma_ekrans()
root.mainloop()
'''
# noteikumi
1) Vadi laukā burtus, lai atminētu vārdud.
2) Tev ir 7 dzīvības, par katru nepareizo minējumu zaudēsi dzīvību.
3) Lai spēlē uzvarētu tev jāuzmin apslēptais vārds.
4) Ja vārdu jau zini, tad to droši vadi iekšā.
VEISKMI!
'''
