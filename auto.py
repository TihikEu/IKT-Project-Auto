class Auto:

    def __init__(self, marka, tipus, loero):
        self.__marka = marka
        self.__tipus = tipus
        self.__loero = loero

    def getMarka(self):
        return self.__marka
    
    def getTipus(self):
        return self.__tipus
    
    def getLoero(self):
        return self.__loero
    
    def __str__(self):
        return f"{self.__marka} {self.__tipus} {self.__loero}"

def adatVaneSzoveg():
    while True:
        a = input("\t| : ").strip()
        if len(a) == 0:
            print("\tHIBA: Üresen hagyta a mezőt!")
        else:
            try:
                b = int(a)
                print("\tHIBA: Az adat nem lehet szám!")
            except ValueError:
                try:
                    b = float(a)
                    print("\tHIBA: Az adat nem lehet szám!") 
                except ValueError:
                    return a

def adatVaneSzam():
    while True:
        a = input("\t| : ").strip()
        if len(a) == 0:
            print("\tHIBA: Üresen hagyta a mezőt!")
        else:
            try:
                b = int(a)  
                if b <= 0 or b > 2000:
                    print("\tHIBA: Az intervallum (1 - 2000)!")
                else:
                    return b
            except ValueError:
                try:
                    b = float(a)
                    print("\tHIBA: Az adatnak egesz szamnak kell lennie!") 
                except ValueError:
                    print("\tHIBA: Az adatnak szamnak kell lennie!")

def adatKiiratas():
    lista = []
    with open("autok.txt", "r", encoding="utf-8") as fajl:
        for sor in fajl:
            reszek = sor.strip()
            lista.append(reszek)
    return lista

def minLoero(tomb):
    minimum = tomb[0]
    for a in tomb:
        if a.getLoero() < minimum.getLoero():
            minimum = a
    return f"Min: {minimum.getMarka()} {minimum.getTipus()} | {minimum.getLoero()} |"

def maxLoero(tomb):
    maximum = tomb[0]
    for a in tomb:
        if a.getLoero() > maximum.getLoero():
            maximum = a
    return f"Max: {maximum.getMarka()} {maximum.getTipus()} | {maximum.getLoero()} |"

autok = []
with open('autok.txt', 'r', encoding='utf-8') as fajl:
    for sor in fajl:
        reszek = sor.strip().split(" ")
        if len(reszek) % 2 == 0:
            marka = reszek[0]
            tipus = ""
            for i in range(1, len(reszek)-2):
                tipus += f" {reszek[i]}"
            loreo = int(reszek[-1])
        else:
            marka = reszek[0]
            tipus = reszek[1]
            loreo = int(reszek[-1])

        autok.append(Auto(marka, tipus, loreo))

print("\nA(z) 'autok.txt' fajl:\n")
for a in adatKiiratas():
    print(f"\t{a}")

vege = False
darab = len(autok)
db = 1
print(f"\nAdjon meg adatokat:| Marka - Tipus - Loero ( 1 - 2000 ) |\nHa a 'Marka' helyere 'VÉGE' szöveget adja meg, akkor a bevitel leáll!")
while not vege:
    print(f"\n{db}. Auto:\n")
    marka = adatVaneSzoveg()
    if marka.upper() == "VÉGE":
        vege = True
    else:
        print(f"\tElfogadva: | {marka} |")
        tipus = adatVaneSzoveg()
        print(f"\tElfogadva: | {tipus} |")
        loero = adatVaneSzam()
        print(f"\tElfogadva: | {loero} |")
    
        adat = Auto(marka, tipus, loero)
        autok.append(adat)
        db += 1
        with open('autok.txt', 'a', encoding='utf-8') as fajl:
            fajl.write(f"\n{adat}")

if len(autok) > darab:
    print("\nA frissitett 'autok.txt' fajl:\n")
    for a in adatKiiratas():
        print(f"\t{a}")
else:
    print("\nA 'autok.txt' fajlban nem tortent adat frissites!\n")
    for a in adatKiiratas():
        print(f"\t{a}")

print(f"\n{maxLoero(autok)}\n{minLoero(autok)}")

with open('legerosebb_auto.txt', 'w', encoding='utf-8') as fajl:
    fajl.write(f"{maxLoero(autok)}\n{minLoero(autok)}")