import random
from enum import Enum

class Couleur(Enum):
    BLEU = "#0cb2af"
    VERT = "#a1c65d"
    JAUNE = "#fac723"
    ORANGE = "#f29222"
    ROUGE = "#e95e50"
    VIOLET = "#936fac"

class mastermind : 

    def __init__(self): 
        self.__ListeCouleur = list(Couleur)
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
        if not self.__CombinaisonSecrete or len(self.__CombinaisonSecrete) != 4: #ça beugait des fois :
            return 0, 0
        combi_secrete = list(self.__CombinaisonSecrete)
        liste_prop = list(ListeProposition)
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

    @CombinaisonSecrete.setter
    def CombinaisonSecrete(self, liste_enums):#on focre la combi secrete car sinon ba ça prend une nouvelle... 
        self.__CombinaisonSecrete = liste_enums