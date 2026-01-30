import tkinter as tk
from tkinter import messagebox

class VueJeu:
    def __init__(self, parent_frame, modele):
        self.parent = parent_frame
        self.modele = modele
        self.couleurs = self.modele.ListeCouleur
        self.ligne_actuelle = 0
        self.etat_pions = [[self.couleurs[0] for _ in range(4)] for _ in range(12)]
        self.pions_graphiques = [] 
        self.boutons_valider = []
        self.resultats_graphiques = [] 
        self.hauteur_ligne = 45
        self.offset_y = 20
        self.parent = parent_frame
        self.modele = modele
        self.controleur = controleur
        self.canvas = tk.Canvas(self.parent, bg="#8B4513", width=500, height=580, highlightthickness=0)
        self.canvas.pack(pady=10)
        self.dessiner_nouvelle_ligne(0)#on dessine la première ligne au démarrage 

    def redessiner_sur_parent(self, nouveau_parent):
        self.parent = nouveau_parent
        self.canvas.pack(in_=self.parent, pady=10)

    def dessiner_nouvelle_ligne(self, i):
        y_ligne = self.offset_y + (i * self.hauteur_ligne)
        btn = tk.Button(self.parent, text="Valider", state="normal",disabledforeground="gray70", command=lambda l=i: self.valider_ligne(l)) #pas de fonction pour grisé automatiquement donc j'ai mit du gris 
        self.canvas.create_window(50, y_ligne + 20, window=btn)
        self.boutons_valider.append(btn)

        ligne_pions_ids = []
        for j in range(4):
            x_pion = 120 + (j * 50)
            pion_id = self.canvas.create_oval(x_pion, y_ligne + 5, x_pion + 30, y_ligne + 35, fill=self.etat_pions[i][j], outline="white", width=2)
            ligne_pions_ids.append(pion_id)
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

        self.canvas.create_line(10, y_ligne + self.hauteur_ligne, 490, y_ligne + self.hauteur_ligne, fill="white")

    def changer_couleur(self, ligne, index_pion):
        if ligne != self.ligne_actuelle:
            return
        couleur_actuelle = self.etat_pions[ligne][index_pion]
        index_couleur = self.couleurs.index(couleur_actuelle)
        prochaine_couleur = self.couleurs[(index_couleur + 1) % len(self.couleurs)]
        self.etat_pions[ligne][index_pion] = prochaine_couleur
        self.canvas.itemconfig(self.pions_graphiques[ligne][index_pion], fill=prochaine_couleur)

    def valider_ligne(self, ligne):
        proposition = self.etat_pions[ligne]
        rouges, blancs = self.modele.verification_proposition(proposition)
        res = self.resultats_graphiques[ligne]
        self.canvas.itemconfig(res["textes"]["rouge"], text=str(rouges))
        self.canvas.itemconfig(res["textes"]["blanc"], text=str(blancs))
        for obj in res["objets"]:
            self.canvas.itemconfig(obj, state='normal')
        
        self.boutons_valider[ligne].config(state="disabled")# Désactivation de la ligne terminée : on peut plus la modifier
        for pion_id in self.pions_graphiques[ligne]:
            self.canvas.tag_unbind(pion_id, "<Button-1>")
        
        if self.modele.victoire(proposition):#vérification de la victoire à chaque fois qu'on valide une ligne
            messagebox.showinfo("BRAVO !", f"Victoire en {ligne + 1} essais !")
            return
        self.ligne_actuelle += 1# Passage à la ligne suivante
        if self.ligne_actuelle < 12:
            self.dessiner_nouvelle_ligne(self.ligne_actuelle)
        else:
            messagebox.showwarning("PERDU", "Vous avez utilisé vos 12 essais !")