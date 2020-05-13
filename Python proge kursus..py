#Esimene ülesanne
print("Tere, maailm!" )
#Ülesanne 1.2
aasta = 2020
liblikas = "teelehe-mosaiikliblikas"
lause_keskosa =  ".aasta liblikas on " 
lause = str(aasta) + lause_keskosa + liblikas
print(lause)
#Ülesanne 1.3
algarv = int(input("algarv arv: "))
astendaja = int(input("astendaja arv:"))
Aste = (algarv**astendaja)
print(Aste)
#Ülesanne 1.4(a)
Ainepunktide_arv = int(input("Sisestage ainepunktide arv: "))
Nädalate_arv = int(input ("Sisestage nädalate arv: "))
Ajakulu = Ainepunktide_arv*26/Nädalate_arv
Ajakulu = round(Ajakulu)
print(Ajakulu)
