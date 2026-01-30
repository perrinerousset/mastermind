import pytest
import MVC.jeu

@pytest.fixture
def nouveau_jeu(self):
        """créer une instance de Jeu avant chaque test."""
        return Jeu(id_partie=1)
def test_initialisation(self, nouveau_jeu):
    """Vérifie objet correctement instancié."""
    assert nouveau_jeu.get_id_partie() == 1
    assert nouveau_jeu.get_nb_tentatives() == 0
    assert nouveau_jeu.get_est_gagnee() is False

def test_terminer_partie_victoire(self, nouveau_jeu):
    """Vérifie victoire."""
    nouveau_jeu.terminer_partie(a_gagne=True, nb_tours_finaux=5)
    assert nouveau_jeu.score == 800
    assert nouveau_jeu.get_est_gagnee() is True 

def test_terminer_partie_defaite(self, nouveau_jeu):
    nouveau_jeu.terminer_partie(a_gagne=False, nb_tours_finaux=12)
    assert nouveau_jeu.score == 0

def test_sauvegarder_partie(self, nouveau_jeu):
    donnees = nouveau_jeu.sauvegarder_partie()     
    keys_attendues = ["id", "score", "tentatives", "victoire"]
    for key in keys_attendues:
    assert key in donnees


