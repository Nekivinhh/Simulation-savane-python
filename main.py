import sys
import os
import json
from helper import (
    ajout_elements,
    COMMANDE_NEXT,
    COMMANDE_REPRENDRE,
    COMMANDE_STOP,
    generer_animaux,
    generer_ressource,
    generer_savane,
    simulation,
)


def main():
    jour_de_depart = None
    nb_jour_max_simulation = None
    status_simulation = COMMANDE_NEXT
    # verifier si une sauvegarde existe
    # Si oui demander si l'utilisateur veut reprendre la simulation
    if os.path.exists("sauvegarde.json"):
        status_simulation = input(
            f"Une sauvegarde existe voulez vous la reprendre ? {COMMANDE_REPRENDRE} / {COMMANDE_STOP}"
        )
        while status_simulation not in [COMMANDE_REPRENDRE, COMMANDE_STOP]:
            status_simulation = input(
                f"Une sauvegarde existe voulez vous la reprendre ? {COMMANDE_REPRENDRE} / {COMMANDE_STOP}"
            )
        if status_simulation == COMMANDE_REPRENDRE:
            with open("sauvegarde.json", "r") as file:
                # parse json to get values
                data = json.load(file)
                grille_savane = data["grille_savane"]
                grille_etat = data["grille_etat"]
                jour_de_depart = data["jour"]
                nb_jour_max_simulation = data["nb_jour_max_simulation"]

    if status_simulation in [COMMANDE_NEXT, COMMANDE_STOP]:
        nbr_animaux = generer_animaux()
        nbr_eau = generer_ressource('eau')
        nbr_nourriture = generer_ressource('nourriture')
        grille_savane, grille_etat, taille_savane = generer_savane()
        ajout_elements(
            grille_savane, grille_etat, taille_savane, nbr_animaux, nbr_eau, nbr_nourriture
        )

    simulation(grille_savane, grille_etat, jour_de_depart, nb_jour_max_simulation)


if __name__ == "__main__":
    sys.exit(main())
