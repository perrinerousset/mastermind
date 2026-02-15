import json
import logging
import os
from typing import Optional

logger = logging.getLogger(__name__)


class Historique:
    def __init__(self, filename="historique.json"):
        base_dir = os.path.dirname(__file__)
        self.filename = os.path.join(base_dir, filename)

    def ajouter_au_fichier(self, objet_jeu):
        donnees_partie = objet_jeu.sauvegarder_partie()
        donnees_globales = self.charger_historique()
        partie_trouvee = False
        for i, p in enumerate(donnees_globales):
            if p.get("id") == donnees_partie.get("id"):
                donnees_globales[i] = donnees_partie
                partie_trouvee = True
                break
        if not partie_trouvee:
            donnees_globales.append(donnees_partie)
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(donnees_globales, f, indent=4, ensure_ascii=False)
            logger.info(
                "Partie %s synchronisée dans l'historique.",
                donnees_partie.get("id", "?"),
            )

    def charger_historique(self) -> Optional[dict]:
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def charger_partie_en_cours(self) -> Optional[dict]:
        donnees = self.charger_historique()
        for partie in reversed(donnees):
            if partie.get("en_cours"):
                return partie
        return None

    def charger_parties_terminees(self) -> list:
        donnees = self.charger_historique()
        parties_a_afficher = []
        for p in donnees:
            if not p.get("en_cours") or "en_cours" not in p:
                parties_a_afficher.append(p)
        return parties_a_afficher
