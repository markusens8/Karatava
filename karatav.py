from tkinter import *
from random import randint, choice

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
GARUMS = 350

LOGA_PLATUMS = 650
LOGA_GARUMS = 500


root = Tk()

root.bind("<F11>", lambda e: root.attributes("-fullscreen",True))
root.bind("<Escape>", lambda e: root.attributes("-fullscreen",False))

root.title("Karatavas")
root.geometry(f"{LOGA_PLATUMS}x{LOGA_GARUMS}")
root.resizable(FALSE, FALSE)
DrawSpace = Canvas(root, width=PLATUMS, height=GARUMS, bg='gray')
DrawSpace.place(x=0, y=0)


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



class Spele:
    def __init__(self):
        self.vards = choice(vardi)
        self.gajienu_skaits = 7
        self.izmantotie_burti = set()
        self.speles_renderetajs = SpeleGUI(self.vards)

    def parbauda_burtu(self, burts):
        # 1. jāizvada burts uz ekrāna <- šito citā funkcijā
        # 2. ja ir burts, tad ieliec to vārdā, ja nav, tad 3.
        # 3. gajienuskaits++, pieliec cilvēciņam detaļu, pārbauda vai ir vel gājienu ja nav, tad spele beidzas

        # Ja šāds burts ir jau minets
        if burts in self.izmantotie_burti:
            return

        if burts in self.vards:
            self.indexes = [i for i, c in enumerate(self.vards) if c == burts]
            self.speles_renderetajs.ieliec_burtu_varda(burts, self.indexes)
            print(type(self.gajienu_skaits))
        else:
            self.gajienu_skaits -= 1
            if self.gajienu_skaits < 1:
                self.spele_beidzas()

        self.izmantotie_burti.add(burts)
        self.speles_renderetajs.izvadi_burtu(burts)

    def spele_beidzas(self):
        root.quit()

# Atbild par spēles dinamisko GUI
class SpeleGUI:
    # inicializācijā izveido logu priekš vārda
    def __init__(self, vards):
        # Pagaidu variants vārda attēlošanai uz ekrāna
        self.minamais_vards = " ".join("_" * len(vards))
        self.label_minamais_vards = Label(root, text=self.minamais_vards, font=("Times new roman", 20), borderwidth=2, relief="solid")
        self.label_minamais_vards.place(relx=0.65, rely=0.45, anchor="center")
        self.izmantotie_burti_label = Label(root, text="", font=("Times new roman", 12))
        self.izmantotie_burti_label.place(relx=0.65, rely=0.75, anchor="center")

    # Izvada burtu izmantotajos burtos
    def izvadi_burtu(self, burts):
        current_text = self.izmantotie_burti_label.cget("text")
        new_text = current_text + " " + burts if current_text else burts
        self.izmantotie_burti_label.config(text=new_text)

    # Aizpilda minamo vārdu
    def ieliec_burtu_varda(self, burts, indexes):
        self.minamais_vards_list = self.minamais_vards.split()
        for i in indexes:
            self.minamais_vards_list[i] = burts

        self.minamais_vards = " ".join(self.minamais_vards_list)
        self.label_minamais_vards.config(text=self.minamais_vards)

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
        # Nosūta ievadīto burtu apstrādei
        def nosuti_burtu(event):
            self.burts = self.entry_burtu_ievade.get()
            self.entry_burtu_ievade.delete(0, END)
            root.after(100, lambda: self.jauna_spele.parbauda_burtu(self.burts))

        self.jauna_spele = Spele()
        self.cilveks = cilvecins()

        self.entry_burtu_ievade = Entry(root)
        self.entry_burtu_ievade.place(relx=0.65, rely=0.65, anchor="center")
        root.bind("<Return>", nosuti_burtu)

        DrawSpace = Canvas(root, width=PLATUMS, height=GARUMS, bg='gray')
        DrawSpace.place(relx=0.025, rely=0.025)

        self.izmantotie_burti_label = Label(root, text="Izmantotie burti:", font=("Times new roman", 12))
        self.izmantotie_burti_label.place(relx=0.65, rely=0.70, anchor="center")

    def noteikumu_ekrans(self):
        pass

    def nodzes_kadru(self):
        DrawSpace.delete('all')
        for widget in root.winfo_children():
            widget.destroy()

DrawSpace = Canvas(root, width=PLATUMS, height=GARUMS, bg='gray')
DrawSpace.place(x=0, y=0)

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
