import json
import os
import pytest

from MVC.model.historique import historique

def test_charger_historique_fichier_absent(tmp_path):
    hist = historique(filename="faux.json")
    hist.filename = tmp_path / "faux.json"

    donnees = hist.charger_historique()

    assert donnees == []

def test_charger_historique_fichier(tmp_path):
    fichier = tmp_path / "historique.json"
    contenu = [
        {"id": 1, "score": 200, "tentatives": 11, "victoire": True}
    ]

    fichier.write_text(json.dumps(contenu), encoding="utf-8")

    hist = historique(filename="historique.json")
    hist.filename = fichier

    donnees = hist.charger_historique()

    assert donnees == contenu   