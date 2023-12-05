def donnee_calculatrice(A, op, B, hist):
    if op == "+":
        print(f"Résultat {A} + {B} =", A + B)
    elif op == "-":
        print(f"Résultat {A} - {B} =", A - B)
    elif op == "/":
        if B != 0:
            print(f"Résultat {A} / {B} =", A / B)
        else:
            print("La division par 0 est impossible")
    elif op == "*":
        print(f"Résultat {A} * {B} =", A * B)
    elif op == "**":
        print(f"Résultat {A} ** {B} =", A ** B)
    elif op == "%":
        if B != 0:
            print(f"Résultat {A} % {B} =", A % B)
        else:
            print("La division par 0 est impossible")
    else:
        print("L'opérateur est incorrect")

    hist.append((A, op, B))

def calculatrice():
    hist = []
    n = -1
    while n != 0:
        print("1. Calculer")
        print("2. Afficher l'historique")
        print("0. Quitter")
        n = int(input("Choisissez une option : "))

        if n == 1:
            A = float(input("Veuillez saisir le premier nombre : "))
            op = input("Veuillez saisir l'opération souhaitée (+, -, /, *, **, %) : ")
            B = float(input("Veuillez saisir le deuxième nombre : "))
            donnee_calculatrice(A, op, B, hist)
        elif n == 2:
            print("Historique : ", hist)

# Appel de la fonction
calculatrice()

liste = [+, -, *]
len(liste)


