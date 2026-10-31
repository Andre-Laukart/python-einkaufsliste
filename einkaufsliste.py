# Einkaufsliste mit Eingabe, Anzeige, Entfernen, Hinzufügen und Beenden

einkaufsliste = []
eingabe = "y"

while eingabe == "y":
    einkaufsliste.append(input("Was möchtest du hinzufügen?: "))
    eingabe = input("Weiter? y / n: ")
    while eingabe not in ("y", "n"):
        eingabe = input("Fehler! Bitte y oder n eingeben: ")

while eingabe == "n":
    eingabe2 = input(
        "Was möchtest du machen? Anzeigen = a / Entfernen = e / "
        "Hinzufügen = h / Beenden = b: "
    )

    if eingabe2 == "a":
        print(einkaufsliste)
    elif eingabe2 == "e":
        loeschen = input("Möchtest du alles = a / eine Sache = e löschen?: ")
        while loeschen not in ("a", "e"):
            loeschen = input("Falsche Eingabe. Alles = a / eine Sache = e: ")

        if loeschen == "e":
            loeschen2 = input("Was möchtest du löschen?: ")
            if loeschen2 in einkaufsliste:
                einkaufsliste.remove(loeschen2)
                print("Wurde gelöscht.")
            else:
                antwort = input(
                    "Nicht in der Liste. Möchtest du es hinzufügen? y / n: "
                )
                if antwort == "y":
                    einkaufsliste.append(loeschen2)
        elif loeschen == "a":
            einkaufsliste.clear()
            print("Alles wurde gelöscht.")

    elif eingabe2 == "h":
        eingabe = "y"
        while eingabe == "y":
            einkaufsliste.append(input("Was möchtest du hinzufügen?: "))
            eingabe = input("Weiter? y / n: ")
            while eingabe not in ("y", "n"):
                eingabe = input("Fehler! Bitte y oder n eingeben: ")

    elif eingabe2 == "b":
        break

print("Beendet.")
