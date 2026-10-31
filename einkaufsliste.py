einkaufsliste = []
eingabe = "y"
eingabe3 = "h"


while eingabe == "y":
    einkaufsliste.append(input("Was möchtest du hinzufügen?: "))
    eingabe = input("weiter? y / n ")
    while eingabe not in ("y" , "n"):
        eingabe = input("fehler y / n ")

while eingabe == "n":
    eingabe2 = input("Was möchtest du machen?: / anzeigen = a / entfernen = e / hinzufügen = h / beenden = b / ")
    if eingabe2 == "a":
        print(einkaufsliste)
    elif eingabe2 == "e":               
        löschen = input("möchtest du: alles = a / eine Sache = e ")
        while löschen not in ("a", "e"):
            löschen = input("Falsche eingabe: alles = a / eine Sache = e ")
        if löschen == "e":
            löschen2 = input("was möchtest du löschen? ")
            if löschen2 in einkaufsliste:
                    einkaufsliste.remove(löschen2)
                    print("wurde gelöscht")
            elif löschen2 not in einkaufsliste:
                eingabe2 = input("Fehler nicht in der liste / möchtest du hinzufügen y / n ")
                if eingabe == "n":
                    einkaufsliste.append(löschen2)
        elif löschen == "a":
            einkaufsliste.clear()
            print("Alles wurde gelöscht")
    elif eingabe2 == "h":
        eingabe = "y"
        while eingabe == "y":
            einkaufsliste.append(input("Was möchtest du hinzufügen?: "))
            eingabe = input("weiter? y / n ")
            while eingabe not in ("y" , "n"):
                eingabe = input("fehler y / n ")
    elif eingabe2 == "b":
        break
print("beendet")
