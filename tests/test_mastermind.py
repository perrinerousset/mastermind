import pytest

from MVC.model.mastermind import Couleur, Mastermind


@pytest.fixture
def jeu():
    return Mastermind()


def test_liste_couleur(jeu):
    assert jeu.liste_couleur == list(Couleur)


def test_generation_combinaison_secrete(jeu):
    jeu.combinaison_secrete()
    combinaison = jeu.combinaison_secrete_bis
    assert len(combinaison) == 4
    for couleur in combinaison:
        assert couleur in Couleur


def test_verification_4_rouges(jeu):
    jeu.combinaison_secrete_bis = [
        Couleur.BLEU,
        Couleur.ROUGE,
        Couleur.VERT,
        Couleur.JAUNE,
    ]

    proposition = [Couleur.BLEU, Couleur.ROUGE, Couleur.VERT, Couleur.JAUNE]
    rouges, blancs = jeu.verification_proposition(proposition)

    assert rouges == 4
    assert blancs == 0


def test_verification_4_blancs(jeu):
    jeu.combinaison_secrete_bis= [
        Couleur.BLEU,
        Couleur.ROUGE,
        Couleur.VERT,
        Couleur.JAUNE,
    ]

    proposition = [Couleur.ROUGE, Couleur.BLEU, Couleur.JAUNE, Couleur.VERT]
    rouges, blancs = jeu.verification_proposition(proposition)

    assert rouges == 0
    assert blancs == 4


def test_verification_mixte(jeu):
    jeu.combinaison_secrete_bis = [
        Couleur.BLEU,
        Couleur.ROUGE,
        Couleur.VERT,
        Couleur.JAUNE,
    ]

    proposition = [Couleur.BLEU, Couleur.VERT, Couleur.ROUGE, Couleur.ORANGE]

    rouges, blancs = jeu.verification_proposition(proposition)

    assert rouges == 1
    assert blancs == 2


@pytest.mark.parametrize(
    "proposition, resultat_attendu",
    [
        (
            [Couleur.VIOLET, Couleur.ORANGE, Couleur.ROUGE, Couleur.BLEU],
            True,
        ),
        (
            [Couleur.BLEU, Couleur.ORANGE, Couleur.ROUGE, Couleur.VIOLET],
            False,
        ),
    ],
)
def test_victoire(jeu, proposition, resultat_attendu):
    jeu.combinaison_secrete_bis = [
        Couleur.VIOLET,
        Couleur.ORANGE,
        Couleur.ROUGE,
        Couleur.BLEU,
    ]

    assert jeu.victoire(proposition) is resultat_attendu
