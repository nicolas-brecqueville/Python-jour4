def fruit_ou_legume(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    if type == "fruits" and saison == "été":
        print("Poire, fraise, cassis")
    if type == "légumes" and saison == "hiver":
        print("carotte, topinambour, endive")
    if type == "légumes" and saison == "été":
        print("artichaut, aubergine,navet")

type = input("Ecrivez 'fruits' ou 'légumes' (sans les guillemets)")
saison = input("Ecrivez 'hiver' ou 'été' (sans les guillemets)")
fruit_ou_legume(type, saison)