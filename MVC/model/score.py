class Score:
    def __init__(self):
        
        self.valeur_score = 0
        self.tentatives_max = 12
    
    def calculer(self, nb_tentatives):
        """
        Calcule le score selon la règle : moins de tours = plus de points.
        Si le joueur trouve en 1 tour : 1200 points.
        Si le joueur trouve en 12 tours : 100 point.
        """
        if nb_tentatives > self.tentatives_max:
            self.valeur_score = 0
        else:
            # Plus nb_tentatives est petit, plus le résultat est grand
            self.valeur_score = ((self.tentatives_max - nb_tentatives) + 1) * 100
        
        return self.valeur_score
    
    def reinitialiser(self):
        """Remet le score à zéro pour une nouvelle partie."""
        self.valeur_score = 0


if __name__ == "__main__":
    sc = Score()
    
    # Cas 1 : Le meilleur score (trouvé du premier coup)
    print(f"Test 1 tour : {sc.calculer(1)} ")
    
    # Cas 2 : Le score minimum (trouvé au dernier tour)
    print(f"Test 12 tours : {sc.calculer(12)} ")
    
    # Cas 3 : Cas d'échec (plus de 12 tours)
    print(f"Test 13 tours : {sc.calculer(13)} ")