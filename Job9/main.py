def moyenne(note1, note2, note3):
    moyenneEleve = (note1 + note2 + note3) / 3

    return moyenneEleve

def appreciation(moyenne):
    if 20 >= moyenne >= 15:
        print("Très bon élève")
    elif 15 > moyenne >= 11:
        print("Bon élève")
    elif 11 > moyenne >= 8:
        print("Élève moyen")
    elif 8 > moyenne >= 0:
        print("Élève devant faire des efforts")
    
    return print(f"La moyenne de l'élève est : {moyenne(note1, note2, note3)}")


note1 = int(input("Rentrez la note 1 de l'élève :"))
note2 = int(input("Rentrez la note 2 de l'élève :"))
note3 = int(input("Rentrez la note 2 de l'élève :"))

appreciation(moyenne(note1, note2, note3))
