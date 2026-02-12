import json
import os
import logging

logger = logging.getLogger(__name__)

class historique:
    def __init__(self, filename="historique.json"):
        base_dir = os.path.dirname(__file__)
        self.filename = os.path.join(base_dir, filename)
        

    def ajouter_au_fichier(self, objet_jeu):
       
        donnees_partie = objet_jeu.sauvegarder_partie()

        
        donnees_globales = self.charger_historique()
        
        
        donnees_globales.append(donnees_partie)
        
        # Réécrire fichier proprement
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(donnees_globales, f, indent=4, ensure_ascii=False)
            logger.info(
                "Partie %s enregistrée dans l'historique.",
                donnees_partie.get("id", "?")
            )

        
        #print(f"Partie {donnees_partie.get('id','?')} enregistrée dans l'historique.")
        

    def charger_historique(self):
        if not os.path.exists(self.filename):
            return [] 
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    
    def charger_partie_en_cours(self):
        donnees = self.charger_historique()
        for partie in reversed(donnees): # On regarde la plus récente
            if partie.get("en_cours") == True:
                return partie
        return None

    def charger_parties_terminees(self):
        donnees = self.charger_historique()
        parties_a_afficher = [] 
        for p in donnees:
            if p.get("en_cours") == False or "en_cours" not in p:
                parties_a_afficher.append(p)
        return parties_a_afficher
    
    
    