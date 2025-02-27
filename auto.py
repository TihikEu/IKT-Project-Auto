class Auto:

    def __init__(self, marka, tipus, loero):
        self.marka = marka
        self.tipus = tipus
        self.loero = loero
    
    def setMarka(self, marka):
        self.__marka = marka
    
    def setTipus(self, tipus):
        self.__tipus = tipus
    
    def setLoero(self, loero):
        self.__loero = loero

    def getMarka(self):
        return self.__marka
    
    def getTipus(self):
        return self.__tipus
    
    def getLoero(self):
        return self.__loero
    
    def __str__(self):
        return f"Marka: {self.__marka}, Tipus: {self.__tipus}, Loero: {self.__loero}"

def adatVaneSzoveg():
    while True:
        a = input("Adat: ")
        if len(a) == 0:
            print("Hibas adat!")
        else:
            try:
                b = float(a)
                if b.is_integer():
                    print("Hibas adat")  
            except ValueError:
                print(f"Elfogadva | {a} |")  
                return a
    
def adatVaneSzam():
    while True:
        a = input("Adat: ")
        if len(a) == 0:
            print("Hibas adat!")
        else:
            try:
                b = float(a)  
                if b.is_integer():
                    if b < 0 or b > 2000:
                        print("Hibas adat")
                    else:
                        print(f"Elfogadva | {int(a)} |") 
                        return int(a)
                else:
                    print("Hibas adat")
            except ValueError:
                print("Hibas adat")
                
marka = adatVaneSzoveg()
tipus = adatVaneSzoveg()
loero = adatVaneSzam()