from .score import Score


class Jeu:
    def __init__(
        self,
        id_partie,
        nb_tentatives=0,
        est_gagne=False,
        combinaison_secrete=None,
        historique_tentatives=None,
    ):
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

    def get_id_partie(self):
        return self.__id_partie

    def get_nb_tentatives(self):
        return self.__nb_tentatives

    def get_est_gagne(self):
        return self.__est_gagne

    def get_score(self):
        return self.__score

    def set_nb_tentatives(self, v: int):
        self.__nb_tentatives = v
        return self.__nb_tentatives

    def set_est_gagne(self, v: bool):
        self.__est_gagne = v
        return self.__est_gagne

    def set_score(self, v: int):
        self.__score = v
        return self.__score

    def terminer_partie(self, a_gagne: bool, nb_tours_finaux: int):
        self.set_est_gagne(a_gagne)
        self.set_nb_tentatives(nb_tours_finaux)
        self.set_score(
            self.gestionnaire_score.calculer(nb_tours_finaux) if a_gagne else 0
        )
        return self.__score

    def ajouter_tentative(self, liste_couleurs_enum):
        noms = [
            c.name for c in liste_couleurs_enum
        ]  # On transforme l'objet Enum en String pour le JSON
        self.historique_tentatives.append(noms)

    def sauvegarder_partie(self):
        return {
            "id": self.__id_partie,
            "score": self.__score,
            "tentatives": self.__nb_tentatives,
            "victoire": self.__est_gagne,
            "solution": self.combinaison_secrete,
            "historique_couleurs": self.historique_tentatives,
            "en_cours": not self.__est_gagne and self.__nb_tentatives < 12,
        }
