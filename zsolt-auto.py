class Auto:
    def __init__(self,marka,tipus,loero):
        self.__marka= marka
        self.__tipus = tipus
        self.setLoero(loero)
    def setLoero(self, loero):
        self.__loero=loero
    def getMarka(self):
        return self.__marka
    def getTipus(self):
        return self.__tipus
    def getLoero(self):
        return self.__loero

    def __srt__(self):
        return f"{self.getMarka()} {self.getTipus()} {self.getLoero}"

def vege(szo):
    if szo=="VÉGE":
        return False
    elif szo.lower() == "vége" or szo.lower() == "vege":
        return "Próbálja mege ezt a karakter láncot: VÉGE"
    else:
        return " "

def beolvas():
    lista=[]
    with open('autok.txt', 'r', encoding='utf-8') as fajl:
        for sor in fajl:
            reszek=sor.strip().split()
            if len(reszek) == 4 :
                a=Auto(reszek[0], (reszek[1], reszek[2]) , int(reszek[3]))
            else:
                a=Auto(reszek[0], reszek[1], int(reszek[2]))
            lista.append(a)
    return lista