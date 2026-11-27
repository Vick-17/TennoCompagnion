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
        for weapon_bp, request_resources in shemas.items():
            if weapon_name == weapon_bp:
                for (
                    request_resources_name,
                    request_resources_needed,
                ) in request_resources.items():
                    for (
                        ressourses_available_name,
                        ressourses_available_nbr,
                    ) in ressourses.items():
                        if (
                            request_resources_name == ressourses_available_name
                            and ressourses_available_nbr >= request_resources_needed
                        ):
                            print(
                                "Stock: ",
                                ressourses_available_name,
                                ressourses_available_nbr,
                                "Need: ",
                                request_resources_name,
                                request_resources_needed,
                            )
                            continue
                        else:
                            print(
                                "Need: ",
                                request_resources_name,
                                request_resources_needed,
                                "Available: ",
                                ressourses_available_name,
                                ressourses_available_nbr,
                            )
                            break

    def show_ressourc():
        for ressourses_name, infos in ressourses.items():
            print(ressourses_name, infos)

    is_buildable("Boltor prime")


fonderie_test()
