    #couleurs : 
    #0cb2af  bleu
    #a1c65d   vert
    #fac723 jaune
    #f29222 orange
    #e95e50 rouge
    #936fac violet


import random
class mastermind : 

    def __init__(self): 
        self.__ListeCouleur = ("#0cb2af","#a1c65d","#fac723","#f29222","#e95e50","#936fac")
        self.__CombinaisonSecrete = []
    
    
    @property
    def ListeCouleur(self):
        return self.__ListeCouleur

    @property
    def CombinaisonSecrete(self):
        return self.__CombinaisonSecrete
    
    def Combinaison_secrete(self): 
        self.__CombinaisonSecrete = random.choices(self.__ListeCouleur, k=4)

    def verification_proposition(self, ListeProposition):
        rouges = 0
        blancs = 0
        combi_secrete = list(self.__CombinaisonSecrete)
        liste_prop = list(ListeProposition)
        # Recherche des pionts bien placés (les rouges)
        for i in range(4):
            if liste_prop[i] == combi_secrete[i]:
                rouges += 1
                combi_secrete[i] = None
                liste_prop[i] = None
        #  Recherche des pions mal placés mais de la bonne couleur (les blancs)
        for i in range(4):
            if liste_prop[i] is not None:
                if liste_prop[i] in combi_secrete:
                    blancs += 1
                    combi_secrete.remove(liste_prop[i])
        return rouges, blancs
            
    def victoire(self, ListeProposition): 
        return list(ListeProposition) == list(self.__CombinaisonSecrete)

