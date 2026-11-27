import sys


def invotory():

    ressourses = {
        "Ferrite": {"nbr": 5000},
        "Plastides": {"nbr": 1200},
        "Rubedo": {"nbr": 800},
        "Cellules Orokin": {"nbr", 3},
        "Neurodes": {"nbr": 8},
        "Morphics": {"nbr": 12},
    }

    shemas = {
        "Boltor prime": {"Ferrite": 2500, "Plastides": 1500, "Cellules Orokin": 5},
        "Brakk": {
            "Ferrite": 1000,
            "Plastides": 500,
            "Cellules Orokin": 2,
            "Neurodes": 3,
        },
        "Hate": {
            "Ferrite": 1500,
            "Plastides": 800,
            "Cellules Orokin": 4,
            "Neurodes": 5,
        },
    }

    def fonderie():

        while True:
            print("=== Fonderie ===")
            while True:
                for weapon_name in shemas:
                    print("weapon_name")
                choose_weapon = input("Choisiser l'arme a craft : ")
                return choose_weapon

    def is_buildable():
        for weapon_bp, request_resources in shemas.items():
            buildable = True
            for resourse_name, resourse_dispo in ressourses.items():
                if request_resources < resourse_dispo:
                    buildable = False

    def show_ressourc():
        for ressourses_name, infos in ressourses.items():
            print(ressourses_name, infos)

    while True:
        print("=== Inventaire ===")
        print("1. Consulter les ressourses disponible")
        print("2. Fonderie")
        print("3. Retourner au menu principal")
        choose = int(input("Votre choix"))

        if choose == 1:
            show_ressourc()


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
        print("5. Inventaire")
        print("6. Quitter")
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
            invotory()

        if choose == 6:
            stop_script()


menu()
