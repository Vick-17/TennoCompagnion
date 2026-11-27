def fonderie_test():
    ressourses = {
        "Ferrite": 5000,
        "Plastides": 1200,
        "Rubedo": 800,
        "Cellules Orokin": 3,
        "Neurodes": 8,
        "Morphics": 12,
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
                    print(weapon_name)
                choose_weapon = input("Choisiser l'arme a craft : ")
                return choose_weapon

    def is_buildable(weapon_name):
        if weapon_name in shemas:
            weapon_bp = shemas.get(weapon_name, {})
            resources_needed = weapon_bp.keys() & ressourses.keys()
            resources_available = ressourses.get(resources_needed)
            print(resources_available)

    def show_ressourc():
        for ressourses_name, infos in ressourses.items():
            print(ressourses_name, infos)

    is_buildable("Boltor prime")


fonderie_test()
