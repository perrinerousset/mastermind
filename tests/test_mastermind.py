import pytest
from MVC.model.mastermind import mastermind, Couleur


@pytest.fixture
def jeu():
    return mastermind()


def test_liste_couleur(jeu):
    assert jeu.ListeCouleur == list(Couleur)


def test_generation_combinaison_secrete(jeu):
    jeu.Combinaison_secrete()
    combinaison = jeu.CombinaisonSecrete
    assert len(combinaison) == 4
    for couleur in combinaison:
        assert couleur in Couleur


def test_verification_4_rouges(jeu):
    jeu._mastermind__CombinaisonSecrete = [
        Couleur.BLEU, Couleur.ROUGE, Couleur.VERT, Couleur.JAUNE
    ]

    proposition = [
        Couleur.BLEU, Couleur.ROUGE, Couleur.VERT, Couleur.JAUNE
    ]
    rouges, blancs = jeu.verification_proposition(proposition)

    assert rouges == 4
    assert blancs == 0


def test_verification_4_blancs(jeu):
    jeu._mastermind__CombinaisonSecrete = [
        Couleur.BLEU, Couleur.ROUGE, Couleur.VERT, Couleur.JAUNE
    ]

    proposition = [
        Couleur.ROUGE, Couleur.BLEU, Couleur.JAUNE, Couleur.VERT
    ]
    rouges, blancs = jeu.verification_proposition(proposition)

    assert rouges == 0
    assert blancs == 4


def test_verification_mixte(jeu):
    jeu._mastermind__CombinaisonSecrete = [
        Couleur.BLEU, Couleur.ROUGE, Couleur.VERT, Couleur.JAUNE
    ]

    proposition = [
        Couleur.BLEU, Couleur.VERT, Couleur.ROUGE, Couleur.ORANGE
    ]

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
    jeu._mastermind__CombinaisonSecrete = [
        Couleur.VIOLET, Couleur.ORANGE, Couleur.ROUGE, Couleur.BLEU
    ]

    assert jeu.victoire(proposition) is resultat_attendu

