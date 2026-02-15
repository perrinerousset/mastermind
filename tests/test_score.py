"""
test pour score
"""  # le ruff demande qu'on écrive ça c'est l'erreur C0114/5/6: Docstring manquante

import pytest

from mvc.model.score import Score


def test_score_initialisation():
    score = Score()

    assert score.get_valeur_score() == 0


@pytest.mark.parametrize(
    "nb_tentatives, score_attendu",
    [
        (1, 1200),
        (2, 1100),
        (5, 800),
        (12, 100),
        (13, 0),
    ],
)
def test_calculer_score(nb_tentatives, score_attendu):
    score = Score()

    resultat = score.calculer(nb_tentatives)

    assert resultat == score_attendu
    assert score.get_valeur_score() == score_attendu
