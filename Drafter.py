import random

Civit = ["Morocco", "Goths", "Greece", "Assyria", "Songhai", "Rome", "Germany", "Celts", "Poland", "Russia",
         "Franks", "Persia", "Carthage", "Australia", "England", "Jerusalem", "Indonesia", "India",
         "Sumeria", "Sweden", "Vietnam", "Ethiopia", "Denmark", "Norway", "Iroquoes", "Spain", "Polynesia",
         "Belgium", "Portugal", "Austria", "Aztec", "Hitties", "Babylon", "Manchuria", "Japan", "Maya", "Inca",
         "Brazil", "Shoshone", "Egypt", "Siam", "Canada", "Ayybis", "Korea", "Zulu", "Sioux", "Ottoman", "Byzantum",
         "Italy", "America", "Netherlands", "China", "Ukraine", "Normandy", "Boeres"]
valinta = []


for i in range(0, 8*4):
    x = random.choice(Civit)
    while x in valinta:
        x = random.choice(Civit)
    valinta.append(x)

print("pelaaja 1: "+str(valinta[0:3]))
print("pelaaja 2: "+str(valinta[4:7]))
print("pelaaja 3: "+str(valinta[8:11]))
print("pelaaja 4: "+str(valinta[12:15]))
print("pelaaja 5: "+str(valinta[16:19]))
print("pelaaja 6: "+str(valinta[20:23]))
print("pelaaja 7: "+str(valinta[24:27]))
print("pelaaja 8: "+str(valinta[28:31]))

