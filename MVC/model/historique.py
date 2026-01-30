import json
import os

class historique:
    def __init__(self, filename="historique.json"):
        chemin_dossier = os.path.dirname(os.path.abspath(__file__))
        self.filename = os.path.join(chemin_dossier, filename)

    def ajouter_au_fichier(self, objet_jeu):
        """
        Récupère les données d'un objet Jeu et les ajoute au fichier JSON.
        """
        donnees_partie = objet_jeu.sauvegarder_partie()

        # Charger l'ancien historique
        donnees_globales = self.charger_historique()
        
        # Ajouter la nouvelle partie à la liste
        donnees_globales.append(donnees_partie)
        
        # Réécrire le fichier proprement
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(donnees_globales, f, indent=4, ensure_ascii=False)
        
        print(f"Partie {objet_jeu.id_partie} enregistrée dans l'historique.")

    def charger_historique(self):
        if not os.path.exists(self.filename):
            return [] 
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []