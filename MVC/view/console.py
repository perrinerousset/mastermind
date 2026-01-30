import tkinter as tk
from tkinter import messagebox

class VueJeu:
    def __init__(self, parent_frame, modele, controleur): # Ajoutez controleur ici
        self.parent = parent_frame
        self.modele = modele
        self.controleur = controleur # Important pour communiquer avec le controleur
        self.couleurs = self.modele.ListeCouleur
        self.ligne_actuelle = 0
        self.etat_pions = [[self.couleurs[0] for _ in range(4)] for _ in range(12)]
        self.pions_graphiques = [] 
        self.boutons_valider = []
        self.resultats_graphiques = [] 
        self.hauteur_ligne = 45
        self.offset_y = 20
        
        self.canvas = tk.Canvas(self.parent, bg="#8B4513", width=500, height=580, highlightthickness=0)
        self.canvas.pack(pady=10)
        self.dessiner_nouvelle_ligne(0)
        self.zone_message = tk.Label(self.parent,text="Bonne chance !",bg="#EEE8AA",fg="black",font=("Arial", 12, "bold"),relief="solid",bd=2,padx=10,pady=5)
        self.zone_message.pack(pady=(10, 0))

    def redessiner_sur_parent(self, nouveau_parent):
            self.parent = nouveau_parent
            if self.canvas.winfo_exists():
                self.canvas.pack(in_=self.parent, pady=10)
            else:
                print("Erreur : Le canvas a été détruit ")#pour le debug là 

    def dessiner_nouvelle_ligne(self, i):
        y_ligne = self.offset_y + (i * self.hauteur_ligne)
        btn = tk.Button(self.canvas, text="Valider", state="normal", disabledforeground="gray70", command=lambda l=i: self.valider_ligne(l))
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
            self.message("victoire")
            return
        self.ligne_actuelle += 1# Passage à la ligne suivante
        if self.ligne_actuelle < 12:
            self.dessiner_nouvelle_ligne(self.ligne_actuelle)
            self.message("Tentative")
        else:
            self.message("Perdu")

    def message(self, etat):
        if etat == "victoire":
            tentatives = self.ligne_actuelle + 1
            texte = f"Vous avez gagné en {tentatives} tentative(s) !"
            couleur = "#90EE90"
        elif etat == "tentative":
            restantes = 11 - self.ligne_actuelle
            texte = f"Il vous reste {restantes} tentative(s)"
            couleur = "#EEE8AA"
        elif etat == "perdu":
            texte = "Vous avez perdu ! Réessayez !"
            couleur = "#F08080"
        else:
            texte = ""
            couleur = "#EEE8AA"
        self.zone_message.config(text=texte, bg=couleur)
