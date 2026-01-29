import tkinter as tk
from tkinter import messagebox

class VueJeu:
    def __init__(self, parent_frame, modele):
        self.parent = parent_frame
        self.modele = modele
        self.couleurs = self.modele.ListeCouleur
        self.ligne_actuelle = 0# On suit la ligne où se trouve le joueur
        self.etat_pions = [[self.couleurs[0] for _ in range(4)] for _ in range(12)]
        self.pions_graphiques = [] 
        self.boutons_valider = []
        self.resultats_graphiques = [] 
        self.dessiner_plateau()

    def dessiner_plateau(self):
        self.canvas = tk.Canvas(self.parent, bg="#8B4513", width=500, height=580, highlightthickness=0)
        self.canvas.pack(pady=10)
        hauteur_ligne = 45
        offset_y = 20

        for i in range(12):
            y_ligne = offset_y + (i * hauteur_ligne)
            etat_initial = "normal" if i == 0 else "disabled"
            
            btn = tk.Button(self.parent, text="Valider", state=etat_initial,
                            command=lambda l=i: self.valider_ligne(l))
            
            self.canvas.create_window(50, y_ligne + 20, window=btn)
            self.boutons_valider.append(btn) # On stocke pour changer l'état plus tard
            ligne_pions_ids = []
            for j in range(4):#création des pions même si c'est un peu moche
                x_pion = 120 + (j * 50)
                pion_id = self.canvas.create_oval(x_pion, y_ligne + 5, x_pion + 30, y_ligne + 35, 
                                                  fill=self.etat_pions[i][j], outline="white", width=2)
                ligne_pions_ids.append(pion_id)
                if i == 0:
                    self.canvas.tag_bind(pion_id, "<Button-1>", lambda event, l=i, p=j: self.changer_couleur(l, p))
            self.pions_graphiques.append(ligne_pions_ids)
            r_rouge = self.canvas.create_oval(350, y_ligne + 10, 370, y_ligne + 30, fill="red", state='hidden')
            t_rouge = self.canvas.create_text(380, y_ligne + 20, text="0", fill="white", state='hidden')
            r_blanc = self.canvas.create_oval(410, y_ligne + 10, 430, y_ligne + 30, fill="white", state='hidden')
            t_blanc = self.canvas.create_text(440, y_ligne + 20, text="0", fill="white", state='hidden')
            
            self.resultats_graphiques.append({
                "objets": [r_rouge, t_rouge, r_blanc, t_blanc],
                "textes": {"rouge": t_rouge, "blanc": t_blanc}
            })

            self.canvas.create_line(10, y_ligne + hauteur_ligne, 490, y_ligne + hauteur_ligne, fill="white")

    def changer_couleur(self, ligne, index_pion):
        if ligne != self.ligne_actuelle:# On ne change la couleur que si c'est la ligne active
            return

        couleur_actuelle = self.etat_pions[ligne][index_pion]
        index_couleur = self.couleurs.index(couleur_actuelle)
        prochaine_couleur = self.couleurs[(index_couleur + 1) % len(self.couleurs)]
        
        self.etat_pions[ligne][index_pion] = prochaine_couleur
        self.canvas.itemconfig(self.pions_graphiques[ligne][index_pion], fill=prochaine_couleur)

    def valider_ligne(self, ligne):
        # 1. Récupération de la proposition et calcul des scores
        proposition = self.etat_pions[ligne]
        rouges, blancs = self.modele.verification_proposition(proposition)
        
        # 2. Affichage des indices (ronds rouges/blancs)
        res = self.resultats_graphiques[ligne]
        self.canvas.itemconfig(res["textes"]["rouge"], text=str(rouges))
        self.canvas.itemconfig(res["textes"]["blanc"], text=str(blancs))
        for obj in res["objets"]:
            self.canvas.itemconfig(obj, state='normal')
        
        # 3. Désactivation de la ligne venant d'être jouée
        self.boutons_valider[ligne].config(state="disabled") # Grise le bouton
        for pion_id in self.pions_graphiques[ligne]:
            self.canvas.tag_unbind(pion_id, "<Button-1>") # Empêche de rechangers les couleurs
            
        # 4. Vérification de la victoire
        if self.modele.victoire(proposition):
            messagebox.showinfo("BRAVO !", f"Victoire en {ligne + 1} essais !")
            self.bloquer_tout()
            return

        # 5. Passage à la ligne suivante ou fin de partie
        self.ligne_actuelle += 1
        if self.ligne_actuelle < 12:
            # On active le bouton suivant
            self.boutons_valider[self.ligne_actuelle].config(state="normal")
            # On active les clics sur les nouveaux pions
            for j, pion_id in enumerate(self.pions_graphiques[self.ligne_actuelle]):
                self.canvas.tag_bind(pion_id, "<Button-1>", 
                                     lambda event, l=self.ligne_actuelle, p=j: self.changer_couleur(l, p))
        else:
            messagebox.showwarning("PERDU", "Vous avez utilisé vos 12 essais !")

    def bloquer_tout(self):
        """Désactive tout le plateau en fin de partie"""
        for btn in self.boutons_valider:
            btn.config(state="disabled")
        for ligne in self.pions_graphiques:
            for pion_id in ligne:
                self.canvas.tag_unbind(pion_id, "<Button-1>")