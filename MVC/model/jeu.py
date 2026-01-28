from score import Score

class Jeu:
    def __init__(self, id_partie, nb_tentatives=0, est_gagne=False):
        self.id_partie = id_partie
        self.nb_tentatives = nb_tentatives
        self.est_gagne = est_gagne
        
        # On lie à la class score
        self.gestionnaire_score = Score() 
        
        # Le score de la partie est récupéré depuis l'objet Score
        self.score = self.gestionnaire_score.valeur_score

    def terminer_partie(self, a_gagne, nb_tours_finaux):
        """
        Met à jour l'objet et calcule automatiquement le score.
        """
        self.est_gagne = a_gagne
        self.nb_tentatives = nb_tours_finaux
        
        # On utilise l'objet Score lié pour calculer les points
        if self.est_gagne:
            self.score = self.gestionnaire_score.calculer(nb_tours_finaux)
        else:
            self.score = 0
            
    def sauvegarder_partie(self):
        donnees = {
            "id": self.id_partie,
            "score": self.score,
            "tentatives": self.nb_tentatives,
            "victoire": self.est_gagne
        }
        return donnees
    

if __name__ == "__main__":
    # On crée une partie
    ma_partie = Jeu(id_partie=42)
    
    # On la termine en 3 tours
    ma_partie.terminer_partie(a_gagne=True, nb_tours_finaux=3)
    
    print(f"Partie ID: {ma_partie.id_partie}")
    print(f"Victoire: {ma_partie.est_gagne}")
    print(f"Score calculé : {ma_partie.score} points") 
    # Devrait afficher 1000 points car (12-3+1)*100 = 1000