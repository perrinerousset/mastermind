"""
gestion de l'objet jeu et de ses attributs'
"""  # le ruff demande qu'on écrive ça c'est l'erreur C0114/5/6: Docstring manquante

from typing import Dict

from .score import Score


class Jeu:
    def __init__(
        self,
        id_partie,
        nb_tentatives=0,
        est_gagne=False,
        combinaison_secrete=None,
        historique_tentatives=None,
    ) -> None:
        self.historique_tentatives = historique_tentatives or []
        self.__id_partie = id_partie
        self.__nb_tentatives = (
            len(self.historique_tentatives)
            if self.historique_tentatives
            else nb_tentatives
        )
        self.__est_gagne = est_gagne
        self.combinaison_secrete = combinaison_secrete or []
        self.gestionnaire_score = Score()
        self.__score = 0
        self.__en_cours = True

    def get_id_partie(self) -> int:
        return self.__id_partie

    def get_nb_tentatives(self) -> int:
        return self.__nb_tentatives

    def get_est_gagne(self) -> bool:
        return self.__est_gagne

    def get_score(self) -> int:
        return self.__score

    def set_nb_tentatives(self, valeur: int) -> int:
        self.__nb_tentatives = valeur
        return self.__nb_tentatives

    def set_est_gagne(self, valeur: bool) -> bool:
        self.__est_gagne = valeur
        if valeur:
            self.en_cours = False
        return self.__est_gagne

    def set_score(self, v: int) -> int:
        self.__score = v
        return self.__score

    def terminer_partie(self, a_gagne: bool, nb_tours_finaux: int) -> int:
        self.set_est_gagne(a_gagne)
        self.set_nb_tentatives(nb_tours_finaux)
        self.set_score(
            self.gestionnaire_score.calculer(nb_tours_finaux) if a_gagne else 0
        )
        self.__en_cours = False
        return self.__score

    def ajouter_tentative(self, liste_couleurs_enum) -> None:
        noms = [
            c.name for c in liste_couleurs_enum
        ]  # On transforme l'objet Enum en String pour le JSON
        self.historique_tentatives.append(noms)

    def sauvegarder_partie(self) -> Dict:
        return {
            "id": self.__id_partie,
            "score": self.__score,
            "tentatives": self.__nb_tentatives,
            "victoire": self.__est_gagne,
            "solution": self.combinaison_secrete,
            "historique_couleurs": self.historique_tentatives,
            "en_cours": self.__en_cours,
        }
