import tkinter as tk
from vue_principale import VuePrincipale

class VueJeu(VuePrincipale):
    def __init__(self, root, modele):
        self.modele = modele  # On passe l'instance de la classe mastermind
        self.couleurs = self.modele.ListeCouleur
        
        # On stocke l'état des lignes (couleurs choisies par le joueur)
        # 12 lignes de 4 pions, initialisées avec la première couleur
        self.etat_pions = [[self.couleurs[0] for _ in range(4)] for _ in range(12)]
        
        # Pour stocker les identifiants des objets graphiques
        self.pions_graphiques = [] 
        self.resultats_graphiques = [] # Pour cacher/montrer les ronds rouges/blancs
        
        super().__init__(root)

    def dessiner_menu(self):
        """Remplit la barre latérale à droite"""
        tk.Label(self.zone_laterale, text="OPTIONS", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=20)
        tk.Button(self.zone_laterale, text="Quitter", command=self.root.quit, bg="#e95e50", fg="white").pack(side="bottom", fill="x", padx=10, pady=10)

    def dessiner_jeu(self):
        """Crée le plateau de jeu (Rectangle marron, 12 lignes, boutons)"""
        # 1. Création du Canvas pour le plateau
        self.canvas = tk.Canvas(self.zone_centrale, bg="#8B4513", width=500, height=580, highlightthickness=0)
        self.canvas.pack(pady=10)

        hauteur_ligne = 45
        offset_y = 20

        for i in range(12):
            y_ligne = offset_y + (i * hauteur_ligne)
            
            # --- GAUCHE : Bouton Valider ---
            # On utilise une "closure" (i=i) pour que le bouton connaisse son numéro de ligne
            btn_valider = tk.Button(self.zone_centrale, text="Valider", 
                                     command=lambda ligne=i: self.valider_ligne(ligne))
            # On place le bouton sur le canvas via une fenêtre (window)
            self.canvas.create_window(50, y_ligne + 20, window=btn_valider)

            # --- CENTRE : Les 4 boules ---
            ligne_pions = []
            for j in range(4):
                x_pion = 120 + (j * 50)
                # Création du cercle (pion)
                pion = self.canvas.create_oval(x_pion, y_ligne + 5, x_pion + 30, y_ligne + 35, 
                                               fill=self.etat_pions[i][j], outline="white", width=2)
                ligne_pions.append(pion)
                
                # Rendre le pion cliquable pour changer de couleur
                self.canvas.tag_bind(pion, "<Button-1>", lambda event, l=i, p=j: self.changer_couleur(l, p))
            
            self.pions_graphiques.append(ligne_pions)

            # --- DROITE : Zone résultats (Rouge / Blanc) ---
            # On crée un groupe d'objets qu'on cache au début (state='hidden')
            r_rouge = self.canvas.create_oval(350, y_ligne + 10, 370, y_ligne + 30, fill="red", state='hidden')
            t_rouge = self.canvas.create_text(380, y_ligne + 20, text="0", fill="white", state='hidden')
            
            r_blanc = self.canvas.create_oval(410, y_ligne + 10, 430, y_ligne + 30, fill="white", state='hidden')
            t_blanc = self.canvas.create_text(440, y_ligne + 20, text="0", fill="white", state='hidden')
            
            self.resultats_graphiques.append({
                "objets": [r_rouge, t_rouge, r_blanc, t_blanc],
                "textes": {"rouge": t_rouge, "blanc": t_blanc}
            })

            # --- TRAIT BLANC de délimitation ---
            self.canvas.create_line(10, y_ligne + hauteur_ligne, 490, y_ligne + hauteur_ligne, fill="white")

    def changer_couleur(self, ligne, index_pion):
        """Cycle les couleurs de la liste au clic"""
        couleur_actuelle = self.etat_pions[ligne][index_pion]
        index_couleur = self.couleurs.index(couleur_actuelle)
        prochaine_couleur = self.couleurs[(index_couleur + 1) % len(self.couleurs)]
        
        # Mise à jour de l'état et de l'affichage
        self.etat_pions[ligne][index_pion] = prochaine_couleur
        id_graphique = self.pions_graphiques[ligne][index_pion]
        self.canvas.itemconfig(id_graphique, fill=prochaine_couleur)

    def valider_ligne(self, ligne):
        """Calcule les résultats via le modèle et affiche les ronds de score"""
        proposition = self.etat_pions[ligne]
        rouges, blancs = self.modele.verification_proposition(proposition)
        
        # Mise à jour des textes
        res = self.resultats_graphiques[ligne]
        self.canvas.itemconfig(res["textes"]["rouge"], text=str(rouges))
        self.canvas.itemconfig(res["textes"]["blanc"], text=str(blancs))
        
        # Affichage des éléments masqués
        for obj in res["objets"]:
            self.canvas.itemconfig(obj, state='normal')

# Pour tester :
if __name__ == "__main__":
    from mastermind import mastermind # Import de ton fichier model
    root = tk.Tk()
    jeu = mastermind()
    jeu.Combinaison_secrete() # On génère la solution
    app = VueJeu(root, jeu)
    root.mainloop()