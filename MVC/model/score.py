class Score:
    def __init__(self):  
        self.valeur_score = 0
        self.tentatives_max = 12
    
    def calculer(self, nb_tentatives):
        #Si le joueur trouve en 1 tour : 1200 points.
        #Si le joueur trouve en 12 tours : 100 point. bref c'est 1200 -100*tentatives
        if nb_tentatives > self.tentatives_max:
            self.valeur_score = 0
        else:
            self.valeur_score = ((self.tentatives_max - nb_tentatives) + 1) * 100
        return self.valeur_score
    def reinitialiser(self):
        self.valeur_score = 0