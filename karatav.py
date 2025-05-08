from tkinter import *
from random import randint, choice
import sys


if getattr(sys, 'frozen', False):
    import pyi_splash

 
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

PLATUMS = 200
GARUMS = 300

LOGA_PLATUMS = 650
LOGA_GARUMS = 350


root = Tk()

root.bind("<F11>", lambda e: root.attributes("-fullscreen",True))
root.bind("<Escape>", lambda e: root.attributes("-fullscreen",False))

root.title("Karatavas")
root.geometry(f"{LOGA_PLATUMS}x{LOGA_GARUMS}")
#root.resizable(FALSE, FALSE)


'''
class cilvecins:
    @staticmethod
    def draw_base():
        DrawSpace.create_line(50, 300, 150, 300, width=5)
    @staticmethod
    def draw_post():
        DrawSpace.create_line(50, 300, 50, 50, width=5)
    @staticmethod
    def draw_hangplatform():
        DrawSpace.create_line(50, 50, 150, 50, width=5)
        DrawSpace.create_line(150, 50, 150, 100, width=5)
    @staticmethod
    def draw_head():
        DrawSpace.create_oval(135, 100, 165, 130, width=5)
    @staticmethod
    def draw_body():
        DrawSpace.create_line(150, 130, 150, 200, width=5)
    @staticmethod
    def draw_arms():
        DrawSpace.create_line(150, 150, 170, 180, width=5)
        DrawSpace.create_line(150, 150, 130, 180, width=5)
    @staticmethod
    def draw_legs():
        DrawSpace.create_line(150, 200, 130, 250, width=5)
        DrawSpace.create_line(150, 200, 170, 250, width=5)

Dzīvības = [cilvecins.draw_legs, cilvecins.draw_arms, cilvecins.draw_body, cilvecins.draw_head, cilvecins.draw_hangplatform, cilvecins.draw_post, cilvecins.draw_base]
'''


class Spele:
    def __init__(self):
        self.vards = choice(vardi)
        self.gajienu_skaits : int = 7
        self.izmantotie_burti = set()

    def parbauda_burtu_varda(self, burts) -> bool:
        # parbauda vai burts ir jau ticis minets
        if burts not in self.izmantotie_burti:
            self.izmantotie_burti.add(burts)

            if burts in self.vards:
                return True
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
        pass


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
        self.label_minamais_vards = Label(self.frame_speles_lauks, text="_ _ _ _ _ _", font=("Arial",35))
        self.label_izmantotie_burti = Label(self.frame_speles_lauks, text="", font=("Arial", 25))
        entry_burtu_ievade = Entry(self.frame_speles_lauks, width=2, font=("Arial",30))

        self.canvas_cilvecina_zimejums.pack(padx=30,pady=20)
        self.label_minamais_vards.pack(pady=(0,20))
        self.label_izmantotie_burti.pack()
        entry_burtu_ievade.pack(pady=40)

        self.frame_cilvecins.pack(side="left", fill="y")
        self.frame_speles_lauks.pack(expand="True")

        #pamats
        self.canvas_cilvecina_zimejums.create_line(40,250,165,250, width=6)
        #stabs
        self.canvas_cilvecina_zimejums.create_line(100,250,100,50, width=6)
        #pa lab
        self.canvas_cilvecina_zimejums.create_line(100,50,175,50, width=6)
        #uz lej
        self.canvas_cilvecina_zimejums.create_line(175,50,175,80, width=6)

        entry_burtu_ievade.bind("<Return>", nosuti_burtu)




    def noteikumu_ekrans(self):
        pass

    def nodzes_kadru(self):
        #DrawSpace.delete('all')
        for widget in root.winfo_children():
            widget.destroy()

Vārds = choice(vardi)
Izpildīts_Burts = '_ ' * len(Vārds)
Uzminēts = False
Uzminētie_Burti = []
Uzminētie_Vārdi = []
Dzīvības = 7


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
