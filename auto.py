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

#Adat ellenorzes SZOVEGES
def adatVaneSzoveg():
    while True:
        a = input()
        if len(a) == 0:
            print("\tHIBAS")
        else:
            try:
                b = float(a)
                if b.is_integer():
                    print("\tHIBAS")  
            except ValueError:
                print(f"\tElfogadva | {a} |")  
                return a

#Adat ellenorzes SZAMOS
def adatVaneSzam():
    while True:
        a = input()
        if len(a) == 0:
            print("\tHIBAS")
        else:
            try:
                b = float(a)  
                if b.is_integer():
                    if b < 0 or b > 2000:
                        print("\tHIBAS")
                    else:
                        print(f"\tElfogadva | {int(a)} |") 
                        return int(a)
                else:
                    print("\tHIBAS")
            except ValueError:
                print("\tHIBAS")

#
auto_adat = []

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

        auto_adat.append(Auto(marka, tipus, loreo))

print("\nA(z) 'autok.txt' fajl:\n")
for a in auto_adat:
    print(f"\t{a}")

#
vege = False
db = 1
while not vege:
    print(f"\n{db}. Auto:\n\tMarka:", end=" ")
    marka = adatVaneSzoveg()
    if marka.upper() == "VEGE":
        vege = True
    else:
        print("\tTipus: ", end=" ")
        tipus = adatVaneSzoveg()
        print("\tLoero: ", end=" ")
        loero = adatVaneSzam()
    
        adat = Auto(marka, tipus, loero)
        auto_adat.append(adat)
        db += 1
        with open('autok.txt', 'a', encoding='utf-8') as fajl:
            fajl.write(f"{adat}")

print("\nA(z) 'autok.txt' fajl:\n")
for a in auto_adat:
    print(f"\t{a}")

#
maximum = auto_adat[0]
for a in auto_adat:
    if a.getLoero() > maximum.getLoero():
        maximum = a
        
print(f"\nMax: {maximum.getMarka()} - {maximum.getTipus()} | {maximum.getLoero()} |")

#
with open('legerosebb_auto.txt', 'w', encoding='utf-8') as fajl:
    fajl.write(f"{maximum.getMarka()} - {maximum.getTipus()} | {maximum.getLoero()} |")