def calculatrice():
    A = float(input("Veuillez saisir le premier nombre : "))
    op = input("Veuillez saisir l'opération souhaitée (+, -, /, *, **, %) : ")
    B = float(input("Veuillez saisir le deuxième nombre : "))

    if op == "+":
        print(f"Résultat {A} + {B} =", A + B)
    elif op == "-":
        print(f"Résultat {A} - {B} =", A - B)
    elif op == "/":
        if B != 0:
            print(f"Résultat {A} / {B} =", A / B)
    elif op == "*":
        if B != 0:
            print(f"Résultat {A} * {B} =", A * B)
    elif op == "**":
        if B != 0:
            print(f"Résultat {A} ** {B} =", A ** B)
    elif op == "%":
        if B != 0:
            print(f"Résultat {A} % {B} =", A % B)
        else:
            print("La division par 0 est impossible")
    elif op == "*":
        print(f"Résultat {A} * {B} =", A * B)
    else:
        print("L'opérateur est incorrect")

# Appel de la fonction
calculatrice()


