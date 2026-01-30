from .score import Score

class Jeu:
    def __init__(self, id_partie, nb_tentatives=0, est_gagne=False):
        self.__id_partie = id_partie
        self.__nb_tentatives = nb_tentatives
        self.__est_gagne = est_gagne
        self.gestionnaire_score = Score() 
        self.score = self.gestionnaire_score.get_valeur_score()

        #je met les gets vue que c'est private 
    def get_id_partie(self): 
        return self.__id_partie
    def get_nb_tentatives(self): 
        return self.__nb_tentatives
    def get_est_gagnee(self): 
        return self.__est_gagne    
    
    def terminer_partie(self, a_gagne, nb_tours_finaux):
        self.__est_gagne = a_gagne
        self.__nb_tentatives = nb_tours_finaux
        if self.__est_gagne:
            self.score = self.gestionnaire_score.calculer(nb_tours_finaux)
        else:
            self.score = 0
            
    def sauvegarder_partie(self):
        return {
            "id": self.get_id_partie(),
            "score": self.score,
            "tentatives": self.get_nb_tentatives(),
            "victoire": self.get_est_gagne()
        }
    