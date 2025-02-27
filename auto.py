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

#Adat bekeres
lista = []

for i in range(1, 4):
    print(f"{i}. Auto:\n\tMarka:", end=" ")
    marka = adatVaneSzoveg()
    print("\tTipus: ", end=" ")
    tipus = adatVaneSzoveg()
    print("\tLoero: ", end=" ")
    loero = adatVaneSzam()
    
    adat = Auto(marka, tipus, loero)
    lista.append(adat)

#Maximum
maximum = lista[0]
for a in lista:
    if a.getLoero() > maximum.getLoero():
        maximum = a
        
print(f"Max: {maximum.getMarka()} - {maximum.getTipus()} | {maximum.getLoero()} |")