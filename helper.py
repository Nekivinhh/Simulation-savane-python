from pprint import pprint
from random import randrange
import os
import json


#######################################
#        Generer des elements         #
#######################################


def generer_grille(taille: int) -> list:
    """
    Retourne une grille de taille x taille
    Returns:
        grille (list)
    """
    grille = [[0] * taille for _ in range(taille)]
    return grille


def generer_animaux() -> int:
    """
    retourne le nbr d'animaux
    Returns:
        animaux (int)
    """
    animaux = int(input("choisit le nrb d'animaux : "))
    while not 2 <= animaux <= 20:
        animaux = int(input("choisit le nrb d'animaux : "))
    print(f"vous avez ajouté {animaux}")
    return animaux


def generer_ressource(type: str) -> int:
    """
    retourne le nbr de ressource(eau, nourriture)
    Returns:
       ressource (int)
    """
    ressource = int(input(f"choisit le nrb de ressource ({type}): "))
    while not 1 <= ressource <= 10:
        ressource = int(input(f"choisit le nrb de ressource ({type}) : "))
    print(f"vous avez ajouté {ressource}")
    return ressource


def generer_savane() -> tuple[list[list[str]], list[list[int]], int]:
    """
    Retourne la grille de la savane, le tableau d'etat et la taille de la savane
    Returnes:
        grille_savane (list[list[str]])
        tableau_etat (list[list[int]])
        savane (int)
    """
    taille_savane = int(
        input("choisit la taille de ta savane (entre 10 - 50 et pair )")
    )
    while not 10 <= taille_savane <= 50 and taille_savane % 2 != 0:
        taille_savane = int(
            input("choisit la taille de ta savane (entre 10 - 50 et pair )")
        )

    grille_savane = [[" " for _ in range(taille_savane)] for _ in range(taille_savane)]
    # Alternative sans list comprehension
    # grille_savane = []
    # for _ in range(taille_savane):
    #     ligne = []
    #     for _ in range(taille_savane):
    #         ligne.append(' ')
    #     grille_savane.append(ligne)
    tableau_etat = [[0 for _ in range(taille_savane)] for _ in range(taille_savane)]
    print(f"la taille de la savane est de :{taille_savane}")

    return grille_savane, tableau_etat, taille_savane


#######################################
#        Ajouter des ressource        #
#######################################


def _generer_position(taille_savane: int) -> tuple[int, int]:
    """
    Retourne une position aleatoire dans la savane
    Returns:
        ligne (int)
        colonne (int)
    """
    return randrange(taille_savane), randrange(taille_savane)


TYPE_HERBIVORE = 1
TYPE_CARNIVORE = 2

TYPE_ANIMAUX = {
    TYPE_HERBIVORE: "herbivore",
    TYPE_CARNIVORE: "carnivore",
}

def _ajout_animaux(
    grille_savane, taille_savane, grille_etat, nbr_animaux, type_animaux=TYPE_HERBIVORE
):
    """
    Ajoute des animaux dans la savane
    Args:
        grille_savane (list[list[str]])
        taille_savane (int)
        grille_etat (list[list[int]])
        nbr_animaux (int)

    Returns:
        None
    """
    for _ in range(nbr_animaux):
        ligne, colonne = _generer_position(taille_savane)
        while grille_savane[ligne][colonne] != " ":
            ligne, colonne = _generer_position(taille_savane)
        grille_savane[ligne][colonne] = "A"
        grille_etat[ligne][colonne] = {
            "sexe": "M" if randrange(2) == 0 else "F",
            "type": type_animaux,
            "jour_sans_manger": 0,
            "jour_sans_boire": 0,
        }


def _ajout_eau(grille_savane, taille_savane, grille_etat, nbr_eau):
    """
    Ajoute des points d'eau dans la savane
    Args:
        grille_savane (list[list[str]])
        taille_savane (int)
        grille_etat (list[list[int]])
        nbr_eau (int)
    Returns:
        None
    """
    for _ in range(nbr_eau):
        ligne, colonne = _generer_position(taille_savane)
        while grille_savane[ligne][colonne] != " ":
            ligne, colonne = _generer_position(taille_savane)
        grille_savane[ligne][colonne] = "E"
        grille_etat[ligne][colonne] = 2


def _ajout_nourriture(grille_savane, taille_savane, grille_etat, nbr_nourriture):
    """
    Ajoute de la nourriture dans la savane
    Args:
        grille_savane (list[list[str]])
        taille_savane (int)
        grille_etat (list[list[int]])
        nbr_nourriture (int)
    Returns:
        None
    """
    for _ in range(nbr_nourriture):
        ligne, colonne = _generer_position(taille_savane)
        while grille_savane[ligne][colonne] != " ":
            ligne, colonne = _generer_position(taille_savane)
        grille_savane[ligne][colonne] = "N"
        grille_etat[ligne][colonne] = 1


def ajout_elements(
    grille_savane: list[list[str]],
    grille_etat: list[list[int]],
    taille_savane: int,
    nbr_animaux: int,
    nbr_eau: int,
    nbr_nourriture: int,
):
    """
    Ajoute les elements dans la savane
    Args:
        grille_savane (list[list[str]])
        grille_etat (list[list[int]])
        taille_savane (int)
        nbr_animaux (int)
        nbr_eau (int)
        nbr_nourriture (int)
    Returns:
        None
    """
    _ajout_animaux(grille_savane, taille_savane, grille_etat, nbr_animaux)
    _ajout_eau(grille_savane, taille_savane, grille_etat, nbr_eau)
    _ajout_nourriture(grille_savane, taille_savane, grille_etat, nbr_nourriture)
    # on ajoute 1/3 de carnivores proportionnellement au nombre d'herbivores
    nb_carnivores = randrange(int(nbr_animaux / 3))
    _ajout_animaux(
        grille_savane, taille_savane, grille_etat, nb_carnivores, TYPE_CARNIVORE
    )
    print(f"il y a {nb_carnivores} carnivores qui son apparu dans la savane")


#######################################
#             Simulation              #
#######################################


def _definir_nombre_de_jour_simulation() -> int:
    """
    Retourne le nombre de jour de simulation
    Returns:
        animaux (int)
    """
    jour = int(input("choisit le nrb de jour de simulation :"))
    while not 10 <= jour <= 1000:
        jour = int(input("choisit le nrb de jour de simulation :"))
    print(f"vous avez ajouté {jour} jour de simulation")
    return jour


def _afficher_information(grille_savane, jour):
    """
    Affiche les informations de la savane
    Args:
        grille_savane (list[list[str]])
        jour (int)
    Returns:
        None
    """
    print(f"jour {jour}")
    pprint(grille_savane)
    nbr_animaux = 0
    nbr_eau = 0
    nbr_nourriture = 0
    for ligne in grille_savane:
        for value in ligne:
            if value == "A":
                nbr_animaux += 1
            if value == "E":
                nbr_eau += 1
            if value == "N":
                nbr_nourriture += 1

    print(f"il y a : {nbr_animaux} animaux")
    print(f"il y a :{nbr_eau} point d'eau ")
    print(f"il y a :{nbr_nourriture} nourriture")


def _recherche_autour_animaux(grille_savane, ligne, colonne):
    """
    Retourne la position de l'eau et de la nourriture autour de l'animal
    Args:
        grille_savane (list[list[str]])
        ligne (int)
        colonne (int)
    Returns:
        eau (tuple[int, int])
        nourriture (tuple[int, int])
    """
    position_resource = {"nourriture": [], "eau": [], "animal": [], "libre": []}
    # On parcours les lignes autour de l'animal
    for i in range(-1, 2):
        # On parcours les colonnes autour de l'animal
        for j in range(-1, 2):
            # On verifie que la position n'est pas en dehors de la grille
            print("_recherche_autour_animaux", ligne+i , "i", i, "ligne", ligne)
            if 0 <= ligne + i < len(grille_savane) and 0 <= colonne + j < len(
                grille_savane
            ):
                # On verifie si la position est de la nourriture
                if grille_savane[ligne + i][colonne + j] == "N":
                    position_resource["nourriture"].append((ligne + i, colonne + j))
                # On verifie si la position est de l'eau
                if grille_savane[ligne + i][colonne + j] == "E":
                    position_resource["eau"].append((ligne + i, colonne + j))
                # On verifie si la position est un autre animal
                if grille_savane[ligne + i][colonne + j] == "A":
                    position_resource["animal"].append((ligne + i, colonne + j))
                # On verifie si la position est libre
                if grille_savane[ligne + i][colonne + j] == " ":
                    position_resource["libre"].append((ligne + i, colonne + j))

    # retourne le premier element de la nourriture et de l'eau si les taille du tableau == 0 on return None
    eau = position_resource["eau"][0] if len(position_resource["eau"]) > 0 else None
    nourriture = (
        position_resource["nourriture"][0]
        if len(position_resource["nourriture"]) > 0
        else None
    )
    return eau, nourriture, position_resource["animal"], position_resource["libre"]


def _faire_manger_animaux(grille_savane, grille_etat):
    """
    Fonction qui permet de faire manger les animaux
    """
    for ligne, value_ligne in enumerate(grille_savane):
        for colonne, value_colonne in enumerate(value_ligne):
            if (
                value_colonne == "A"
                and grille_etat[ligne][colonne]["type"] == TYPE_HERBIVORE
            ):
                # On regarde autour de l'animal
                eau, nourriture, _, _ = _recherche_autour_animaux(
                    grille_savane, ligne, colonne
                )
                # Si l'animal a trouvé de la nourriture
                if nourriture:
                    # On decremnete la nourriture dans la grille d'etat
                    grille_etat[nourriture[0]][nourriture[1]] -= 1
                    # Si la nourriture est a 0 on la retire de la grille
                    if grille_etat[nourriture[0]][nourriture[1]] == 0:
                        grille_savane[nourriture[0]][nourriture[1]] = " "
                    # On remet le compteur de jour sans manger a 0
                    grille_etat[ligne][colonne]["jour_sans_manger"] = 0
                else:
                    # On incremente le compteur de jour sans manger
                    grille_etat[ligne][colonne]["jour_sans_manger"] += 1
                # Si l'animal a trouvé de l'eau
                if eau:
                    # On decremnete l'eau dans la grille d'etat
                    grille_etat[eau[0]][eau[1]] -= 1
                    # Si l'eau est a 0 on la retire de la grille
                    if grille_etat[eau[0]][eau[1]] == 0:
                        grille_savane[eau[0]][eau[1]] = " "
                    # On remet le compteur de jour sans boire a 0
                    grille_etat[ligne][colonne]["jour_sans_boire"] = 0
                else:
                    # On incremente le compteur de jour sans boire
                    grille_etat[ligne][colonne]["jour_sans_boire"] += 1
            # On regarde si le carnivore peux ce nourrire
            elif (
                value_colonne == "A"
                and grille_etat[ligne][colonne]["type"] == TYPE_CARNIVORE
            ):
                eau, _, position_animaux, _ = _recherche_autour_animaux(
                    grille_savane, ligne, colonne
                )
                if eau:
                    # On decremnete l'eau dans la grille d'etat
                    grille_etat[eau[0]][eau[1]] -= 1
                    # Si l'eau est a 0 on la retire de la grille
                    if grille_etat[eau[0]][eau[1]] == 0:
                        grille_savane[eau[0]][eau[1]] = " "
                    # On remet le compteur de jour sans boire a 0
                    grille_etat[ligne][colonne]["jour_sans_boire"] = 0
                else:
                    # On incremente le compteur de jour sans boire
                    grille_etat[ligne][colonne]["jour_sans_boire"] += 1
                # mange que les herbivores
                if len(position_animaux) > 0:
                    # On prend un animal qui est hebivore sinon rien
                    animal_a_manger = None
                    for animal in position_animaux:
                        if grille_etat[animal[0]][animal[1]]["type"] == TYPE_HERBIVORE:
                            animal_a_manger = animal
                            break
                    if animal_a_manger is None:
                        grille_etat[ligne][colonne]["jour_sans_manger"] += 1
                        continue
                    # On le retire de la grille
                    grille_savane[animal_a_manger[0]][animal_a_manger[1]] = " "
                    grille_etat[animal_a_manger[0]][animal_a_manger[1]] = 0
                    # On remet le compteur de jour sans manger a 0
                    grille_etat[ligne][colonne]["jour_sans_manger"] = 0
                    # Afficher quel animal est devorer avec son type et quel animal la devorer
                    print(
                        f"l'animal en position {animal_a_manger[0]}, {animal_a_manger[1]} a été devorer par l'animal en position {ligne}, {colonne}"
                    )
                else:
                    # On incremente le compteur de jour sans manger
                    grille_etat[ligne][colonne]["jour_sans_manger"] += 1


def _on_deplace_animaux(grille_savane, grille_etat):
    """
    Fonction qui permet de deplacer les animaux de 2 cases adjacente aleatoirement
    """
    for ligne, value_ligne in enumerate(grille_savane):
        for colonne, value_colonne in enumerate(value_ligne):
            if value_colonne == "A":
                # Il peuvent ce deplacer dans un carre de 3x3 atour de leur position
                # On genere un deplacement aleatoire
                ligne_deplacement = randrange(-2, 3)
                colonne_deplacement = randrange(-2, 3)
                # On verifie que la position n'est pas en dehors de la grille
                # ou n'est pas occupé sinon on recommence
                while (
                    not 0 <= ligne + ligne_deplacement < len(grille_savane)
                    or not 0 <= colonne + colonne_deplacement < len(grille_savane)
                    or grille_savane[ligne + ligne_deplacement][
                        colonne + colonne_deplacement
                    ]
                    != " "
                ):
                    ligne_deplacement = randrange(-2, 3)
                    colonne_deplacement = randrange(-2, 3)

                # On deplace l'animal sur la nouvelle position et dans la grille d'etat
                grille_savane[ligne + ligne_deplacement][
                    colonne + colonne_deplacement
                ] = "A"
                grille_etat[ligne + ligne_deplacement][
                    colonne + colonne_deplacement
                ] = grille_etat[ligne][colonne]
                grille_savane[ligne][colonne] = " "
                grille_etat[ligne][colonne] = 0


def _verifier_etat_animaux(grille_savane, grille_etat, jour):
    """
    Si un animal n'a pas mangé pendant 10 jours il meurt
    Si un animal n'a pas bu pendant 3 jours il meurt
    """
    for ligne, value_ligne in enumerate(grille_savane):
        for colonne, value_colonne in enumerate(value_ligne):
            if value_colonne == "A":
                type_animal = TYPE_ANIMAUX[grille_etat[ligne][colonne]['type']]
                if (
                    grille_etat[ligne][colonne]["jour_sans_manger"] == 10
                ):
                    grille_savane[ligne][colonne] = " "
                    grille_etat[ligne][colonne] = 0
                    print(
                        f"l'animal en position {ligne}, {colonne} ({type_animal}) est mort de faim le jour {jour}"
                    )
                if (
                    grille_etat[ligne][colonne] != 0 and grille_etat[ligne][colonne]["jour_sans_boire"] == 3
                ):
                    grille_savane[ligne][colonne] = " "
                    grille_etat[ligne][colonne] = 0
                    print(
                        f"l'animal en position {ligne}, {colonne} ({type_animal}) est mort de soif le jour {jour}"
                    )


def _accouple_animaux(grille_savane, grille_etat):
    """
    Fonction qui permet de faire accoupler les animaux
    A chaque tour de boucle si un animal de type herbivore est a coté d'un autre animal de type herbivore de sexe opposé
    """
    for ligne, value_ligne in enumerate(grille_savane):
        for colonne, value_colonne in enumerate(value_ligne):
            if value_colonne == "A" and grille_etat[ligne][colonne]["type"] == TYPE_HERBIVORE:
                # On regarde autour de l'animal
                _, _, position_animaux, _ = _recherche_autour_animaux(
                    grille_savane, ligne, colonne
                )
                # on selectionne un herbivore de sexe opposé qui n'a pas 10 en faim et 3 en soif
                partenaire = None
                for animal in position_animaux:
                    if (
                        grille_etat[animal[0]][animal[1]]["type"] == TYPE_HERBIVORE
                        and grille_etat[animal[0]][animal[1]]["sexe"]
                        != grille_etat[ligne][colonne]["sexe"]
                        and grille_etat[animal[0]][animal[1]]["jour_sans_manger"] < 10
                        and grille_etat[animal[0]][animal[1]]["jour_sans_boire"] < 3
                    ):
                        partenaire = animal
                        break
                if partenaire is not None:
                    # On ajoute un nouvel animal sur un case libre sinon ne pas faire de reproduction
                    _, _, _, position_libre = _recherche_autour_animaux(
                        grille_savane, ligne, colonne
                    )
                    if len(position_libre) > 0:
                        grille_savane[position_libre[0][0]][position_libre[0][1]] = "A"
                        grille_etat[position_libre[0][0]][position_libre[0][1]] = {
                            "sexe": "M" if randrange(2) == 0 else "F",
                            "type": TYPE_HERBIVORE,
                            "jour_sans_manger": 0,
                            "jour_sans_boire": 0,
                        }


def _on_regenerer_ressource(grille_savane, grille_etat, jour):
    """
    Fonction qui permet de regenerer les ressources
    1 par jour pour l'eau
    1 tous les 3 jours pour la nourriture
    """
    for ligne, value_ligne in enumerate(grille_savane):
        for colonne, value_colonne in enumerate(value_ligne):
            if value_colonne == "E":
                grille_etat[ligne][colonne] += 1
            if value_colonne == "N" and jour % 3 == 0:
                grille_etat[ligne][colonne] += 1


def _sauvegarde(grille_savane, grille_etat, jour_de_depart, nb_jour_max_simulation):
    """
    Fonction qui permet de sauvegarder les données de la simulation
    """
    data = {
        "grille_savane": grille_savane,
        "grille_etat": grille_etat,
        "jour": jour_de_depart,
        "nb_jour_max_simulation": nb_jour_max_simulation,
    }
    with open("sauvegarde.json", "w") as file:
        json.dump(data, file, indent=4)


COMMANDE_NEXT = "N"
COMMANDE_STOP = "S"
COMMNADE_SAUVEGARDER = "SA"
COMMANDE_REPRENDRE = "R"


def simulation(grille_savane, grille_etat, jour_de_depart, nb_jour_max_simulation):
    # verifier si les données de la sauvegarde existe
    if jour_de_depart is None and nb_jour_max_simulation is None:
        nb_jour_max_simulation = _definir_nombre_de_jour_simulation()
        jour_de_depart = 0

    for jour in range(jour_de_depart, nb_jour_max_simulation):
        # On affiche les informations de la savane
        _afficher_information(grille_savane, jour)
        # On demande à l'utilisateur de continuer ou d'arreter la simulation
        status_simulation = input(
            f"- Pour passer au jour suivant taper {COMMANDE_NEXT} \
                                  - Pour arreter taper {COMMANDE_STOP} \
                                  - Pour sauvegarder et quitter taper {COMMNADE_SAUVEGARDER}"
        )

        while status_simulation not in [
            COMMANDE_NEXT,
            COMMANDE_STOP,
            COMMNADE_SAUVEGARDER,
        ]:
            status_simulation = input(
                f"- Pour passer au jour suivant taper {COMMANDE_NEXT} \
                                  - Pour arreter taper {COMMANDE_STOP} \
                                  - Pour sauvegarder et quitter taper {COMMNADE_SAUVEGARDER}"
            )
        # Si l'utilisateur veut sauvegarder et quitter
        if status_simulation == COMMNADE_SAUVEGARDER:
            _sauvegarde(grille_savane, grille_etat, jour, nb_jour_max_simulation)
            return False

        # Si l'utilisateur veut arreter la simulation
        if status_simulation == COMMANDE_STOP:
            return False
        # On verifie l'etat des animaux
        _verifier_etat_animaux(grille_savane, grille_etat, jour)
        # On fait manger les animaux
        _faire_manger_animaux(grille_savane, grille_etat)
        # On deplace les animaux
        _on_deplace_animaux(grille_savane, grille_etat)
        _accouple_animaux(grille_savane, grille_etat)
        # On regenere les ressources
        _on_regenerer_ressource(grille_savane, grille_etat, jour)
