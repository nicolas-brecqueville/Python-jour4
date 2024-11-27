def pair_impair(nombre):
    if nombre % 2 == 0:
        print(f"{nombre} est pair.")
    if nombre % 2 == 1:
        print(f"{nombre} est impair.")

nombre = int(input("Rentrez un nombre ici (positif et entier) : "))
while nombre <= 0:
    nombre = int(input("Rentrez un nombre ici (positif et entier) : "))

# assert nombre > 0, "Positif j'ai dis !!" (ce code repropose pas de re rentrer l'input)
pair_impair(nombre)