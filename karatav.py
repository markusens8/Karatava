from tkinter import *
from random import randint, choice
import sys


 
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
        self.gajienu_skaits : int = 7
        self.izmantotie_burti = set()

    def parbauda_burtu_varda(self, burts) -> bool:
        # ja burts vel nav ticis minets, tad to apstrada, ja ir, tad atgriez none 
        if burts not in self.izmantotie_burti:
            self.izmantotie_burti.add(burts)

            # Ja burta minejums atrodas varda, atgriež true
            if burts in self.vards:
                return True
            # Ja burta minejums nav varda, tad atgriez false
            else:
                self.gajienu_skaits -= 1
                if self.gajienu_skaits == 0:
                    self.beidz_speli()
                return False
        return None

    # Atgriež visus indeksus, kur ir sastopams noteikts burts
    def dabu_index(self,burts) -> list:
        indeksi = []
        for index, char in enumerate(self.vards):
            if char == burts:
                indeksi.append(index)
        return indeksi

    def beidz_speli(self):
        kadru_zimetajs.beigu_ekrans()


class UzzimeKadrus:
    def nomaina_kadru(self, kadrs):
        self.nodzes_kadru()
        match kadrs:
            case 'sakuma_ekrans': self.sakuma_ekrans()
            case 'speles_ekrans': self.speles_ekrans()
            case 'noteikumu_ekrans': self.noteikumu_ekrans()
    
    def sakuma_ekrans(self):
        self.poga_sakt = Button(root, width=12, text="Sākt", command=lambda: self.nomaina_kadru('speles_ekrans'))
        self.poga_iziet = Button(root, width=12, text="Iziet", command=lambda: root.quit())
        self.poga_noteikumi = Button(root, width=12, text="Noteikumi", command=lambda: self.nomaina_kadru('noteikumu_ekrans'))

        self.poga_sakt.place(relx=0.1, y=LOGA_GARUMS-200)
        self.poga_iziet.place(relx=0.45, y=LOGA_GARUMS-200)
        self.poga_noteikumi.place(relx=0.8, y=LOGA_GARUMS-200)

    # Uzzīmē spēles statisko GUI
    def speles_ekrans(self):
        self.jauna_spele = Spele()

        # Pārbauda ievadīto burtu un atjaunina GUI
        def nosuti_burtu(event):
            self.burts = entry_burtu_ievade.get().lower()
            self.burts_ir_varda = self.jauna_spele.parbauda_burtu_varda(self.burts)

            #Funkcija palaizas ja burts vel nav ticis minets
            if self.burts_ir_varda is not None:
                entry_burtu_ievade.delete(0, END)
                
                # Ja minetais burts ir varda
                if self.burts_ir_varda is True:
                    # parvers tekstu par sarakstu ar char, jo stringus pitona nevar mainit
                    self.teksts = list(self.label_minamais_vards["text"])

                    self.indeksi = self.jauna_spele.dabu_index(self.burts)
                    for indekss in self.indeksi:
                        self.teksts[indekss*2] = self.burts.upper()

                    self.label_minamais_vards["text"] = ''.join(self.teksts)

                # Ja minetais burts nav varda
                else:
                    self.label_izmantotie_burti["text"] = self.label_izmantotie_burti["text"] + f"{self.burts.upper()} "


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
        self.canvas_cilvecina_zimejums.create_line(175,50,175,80, width=6) # Uz leju
        self.canvas_cilvecina_zimejums.create_oval(160, 80, 190, 110) # Galva
        self.canvas_cilvecina_zimejums.create_line(175, 110, 175, 160) # Ķermenis
        self.canvas_cilvecina_zimejums.create_line(175, 110, 160, 140) # kreisā roka
        self.canvas_cilvecina_zimejums.create_line(175, 110, 190, 140) # Labā roka
        self.canvas_cilvecina_zimejums.create_line(175, 160, 160, 190) # kreisā kāja
        self.canvas_cilvecina_zimejums.create_line(175, 160, 190, 190) # Labā kāja

        entry_burtu_ievade.bind("<Return>", nosuti_burtu)

    def beigu_ekrans(self, uzvareja:bool, gajienu_skaits : int):
        if uzvareja:
            self.label_uzvara = Label(root, text="uzvara!")
            self.label_gajienu_skaits = Label(root, text=f"gajienu skaits: {gajienu_skaits}")
            
        else:
            pass

    def noteikumu_ekrans(self):
        noteikumi = Toplevel(root)
        noteikumi.title("Noteikumi")
        width, height = root.winfo_screenwidth(), root.winfo_screenheight()
        noteikumi.geometry(f'{width}x{height}')
        noteikumi.state("zoomed")
        
        t1 = Label(noteikumi,text="Tev ir 7 gājieni, lai nepakārtu cilvēku!")
        t2 = Label(noteikumi, text="Ievadi, burtu norādītajā laukā, katrs nepareizais burts atņem tev vienu gājienu!")
        t3 = Label(noteikumi, text="Atmini vārdu, lai uzvarētu!")
        t1.place(relx=0.5, rely = 0.48, anchor=CENTER)
        t2.place(relx = 0.5, rely=0.5, anchor=CENTER)
        t3.place(relx = 0.5, rely=0.52, anchor=CENTER)
        
            
        

    def nodzes_kadru(self):
        #DrawSpace.delete('all')
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
