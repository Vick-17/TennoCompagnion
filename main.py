import sys


def menu():

    pseudo = input("Pseudo ? ")
    rm = int(input("Rang de maitrise ? "))
    warframe = input("Waframe équipé ? ")
    arme = input("Arme princial ? ")
    credits = int(input("Credit ? "))
    platines = int(input("platine ? "))
    win_credit = int(input("Credit gagner lors de la mission ? "))

    def action_one():
        print("=== Tenno connecter ===")
        return print(
            f"Opérateur : {pseudo} | Rang de maitrise : {rm} | Warframe équipé : {warframe} | Arme principal : {arme} | credit actuelle : {credits} | Platines : {platines} | Nouveau solde de credits : {credits + win_credit}"
        )

    def action_two():
        print("=== Mes credits ===")
        return print(credits, "crédits")

    def action_tree():
        print("=== Ajouter  des credits ===")
        add_credit = int(input("Saisir credits à ajouter : "))
        if not add_credit <= 0:
            return credits + add_credit
        else:
            return credits

    def action_four():
        print("=== Dépenser des credits")
        spend_credit = int(input("Combien de credits voulez vous dépenser : "))
        if not spend_credit > credits:
            return credits - spend_credit
        else:
            return credits

    def stop_script():
        sys.exit("Arrêt du programme.")

    while True:

        print("=== TENNO COMPANION ===")
        print("1. Consulter mon profil")
        print("2. Consulter mes crédits")
        print("3. Ajouter des credits")
        print("4. Dépenser des crédits")
        print("5. Quitter")
        choose = int(input("Votre choix : "))

        if choose == 1:
            action_one()
        if choose == 2:
            action_two()
        if choose == 3:
            credits = action_tree()
        if choose == 4:
            credits = action_four()
            if credits <= 10000:
                print("Warning : solde inferieur a 10 000")
        if choose == 5:
            stop_script()


menu()
