import json
import os

class historique:
    def __init__(self, filename="historique.json"):
        self.filename = filename

    def sauvegarder_partie(self, gagne, score, tentatives):
        nouvelle_entree = {
            "victoire": gagne,
            "score": score,
            "tentatives": tentatives
        }

        donnees = self.charger_historique()
        donnees.append(nouvelle_entree)
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(donnees, f, indent=4, ensure_ascii=False)
        print("Partie sauvegardée avec succès !")

    def charger_historique(self):
        if not os.path.exists(self.filename):
            return [] 
        
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []