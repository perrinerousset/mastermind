import pytest
from MVC.model.jeu import Jeu
from MVC.model.score import Score

@pytest.fixture
def nouveau_jeu():
        return Jeu(id_partie=1)

def test_initialisation(nouveau_jeu):
    assert nouveau_jeu.get_id_partie() == 1
    assert nouveau_jeu.get_nb_tentatives() == 0
    assert nouveau_jeu.get_est_gagne() is False

def test_terminer_partie_victoire(nouveau_jeu):
    nouveau_jeu.terminer_partie(a_gagne=True, nb_tours_finaux=5)
    assert nouveau_jeu.get_score() == 800
    assert nouveau_jeu.get_est_gagne() is True 

def test_terminer_partie_defaite(nouveau_jeu):
    nouveau_jeu.terminer_partie(a_gagne=False, nb_tours_finaux=12)
    assert nouveau_jeu.get_score() == 0

# faire test pour sauvegarder partie 


