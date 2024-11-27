def nombre(n1):
    if n1 < 0:
        print(f"{n1} est négatif")
    elif n1 > 0:
        print(f"{n1} est positif")

chiffre = int(input("Rentrez un nombre : "))
nombre(chiffre)