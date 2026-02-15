import logging
import random
from enum import Enum
from typing import List, Tuple

logger = logging.getLogger(__name__)


class Couleur(Enum):
    BLEU = "#0cb2af"
    VERT = "#a1c65d"
    JAUNE = "#fac723"
    ORANGE = "#f29222"
    ROUGE = "#e95e50"
    VIOLET = "#936fac"


class Mastermind:
    def __init__(self)-> None:
        self.__ListeCouleur = list(Couleur)
        self.__CombinaisonSecrete = []
        logger.debug("Initialisation du modèle Mastermind")

    @property
    def liste_couleur(self):
        return self.__ListeCouleur

    @property
    def combinaison_secrete_bis(self):
        return self.__CombinaisonSecrete

    def combinaison_secrete(self):
        self.__CombinaisonSecrete = random.choices(self.__ListeCouleur, k=4)
        logger.debug(
            "Nouvelle combinaison secrète générée (DEBUG uniquement) : %s",
            self.__CombinaisonSecrete,
        )

    def verification_proposition(self, liste_proposition)-> Tuple[int, int]:
        logger.debug("Vérification proposition : %s", liste_proposition)
        rouges = 0
        blancs = 0
        if (
            not self.__CombinaisonSecrete or len(self.__CombinaisonSecrete) != 4
        ):  # ça beugait des fois :
            logger.warning("Tentative de vérification sans combinaison secrète valide.")
            return 0, 0
        combi_secrete = list(self.__CombinaisonSecrete)
        liste_prop = list(liste_proposition)
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

    def victoire(self, liste_proposition)-> bool:
        return list(liste_proposition) == list(self.__CombinaisonSecrete)

    @combinaison_secrete_bis.setter
    def combinaison_secrete_bis(self, liste_enums):  
        # on focre la combi secrete car sinon ba ça prend une nouvelle...
        self.__CombinaisonSecrete = liste_enums
