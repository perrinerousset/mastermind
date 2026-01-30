from model.score import Score

class Jeu:
    def __init__(self, id_partie, nb_tentatives=0, est_gagne=False):
        self.__id_partie = id_partie
        self.__nb_tentatives = nb_tentatives
        self.__est_gagne = est_gagne

        self.gestionnaire_score = Score()
        self.__score = 0  # score courant de la partie

   
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
        self.set_score(self.gestionnaire_score.calculer(nb_tours_finaux) if a_gagne else 0)
        return self.__score

    def sauvegarder_partie(self):
        return {
            "id": self.get_id_partie(),
            "score": self.get_score(),
            "tentatives": self.get_nb_tentatives(),
            "victoire": self.get_est_gagne()
        }
