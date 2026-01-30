class Score:
    def __init__(self):  
        self.__valeur_score = 0
        self.__tentatives_max = 12

    def get_valeur_score(self):
        return self.__valeur_score
    
    def calculer(self, nb_tentatives):
        #Si le joueur trouve en 1 tour : 1200 points.
        #Si le joueur trouve en 12 tours : 100 point. bref c'est 1200 -100*tentatives
        if nb_tentatives > self.__tentatives_max:
            self.__valeur_score = 0
        else:
            self.__valeur_score = ((self.__tentatives_max - nb_tentatives) + 1) * 100
        return self.__valeur_score
    def reinitialiser(self):
        self.__valeur_score = 0