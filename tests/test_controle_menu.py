"""
test pour controle_menu
"""

from mvc.controller.controle_menu import Controleur
from mvc.model.jeu import Jeu
from mvc.model.mastermind import Mastermind


class ControleurTestable(Controleur):

    def __init__(self) -> None:
        self.root = None
        self.modele = Mastermind()
        self.vue_principale = None
        self.partie_objet = None
        self.vue_jeu_active = None
        self.historique_parties = []
        self.compteur_id = 1

    def afficher_accueil(self) -> None:
        pass

    def afficher_jeu(self) -> None:
        pass

    def afficher_historique(self) -> None:
        pass

    def afficher_regles(self) -> None:
        pass

    def nouvelle_partie(self) -> None:
        self.modele.combinaison_secrete()
        solution_noms = [c.name for c in self.modele.combinaison_secrete_bis]
        self.partie_objet = Jeu(
            id_partie=self.compteur_id,
            combinaison_secrete=solution_noms,
        )
        self.compteur_id += 1


def test_initialisation():
    controle = ControleurTestable()
    assert controle.partie_objet is None
    assert controle.compteur_id == 1
    assert controle.historique_parties == []


def test_nouvelle_partie_cree_partie():
    controle = ControleurTestable()
    controle.nouvelle_partie()

    assert controle.partie_objet is not None
    assert isinstance(controle.partie_objet, Jeu)
    assert controle.compteur_id == 2


def test_enregistrer_partie_victoire():
    controle = ControleurTestable()
    controle.nouvelle_partie()

    controle.enregistrer_partie(victoire=True, tentatives=4)

    assert controle.partie_objet is None


def test_enregistrer_partie_sans_partie():
    controle = ControleurTestable()

    controle.enregistrer_partie(victoire=True, tentatives=3)

    assert controle.partie_objet is None


def test_compteur_id_incremente():
    controle = ControleurTestable()

    controle.nouvelle_partie()
    controle.nouvelle_partie()

    assert controle.compteur_id == 3