import tkinter as tk

from mvc.model.historique import Historique
from mvc.model.mastermind import Couleur


class VueJeu:
    def __init__(self, parent_frame, modele, controleur)-> None:
        self.parent = parent_frame
        self.modele = modele
        self.controleur = controleur
        self.frame_principale = tk.Frame(self.parent, bg="white")
        self.frame_principale.pack(expand=True, fill="both")
        self.zone_message = tk.Label(
            self.frame_principale,
            text="Bonne chance !",
            bg="#EEE8AA",
            font=("Arial", 12, "bold"),
            relief="solid",
            bd=2,
            padx=10,
            pady=5,
        )
        self.zone_message.pack(pady=(10, 0))
        self.canvas = tk.Canvas(
            self.frame_principale, bg="#8B4513", width=500, height=580
        )
        self.canvas.pack(pady=10)
        self.couleurs = self.modele.liste_couleur
        historique_couleurs = []
        if self.controleur.partie_objet:
            historique_couleurs = self.controleur.partie_objet.historique_tentatives
        self.ligne_actuelle = 0
        self.etat_pions = [[self.couleurs[0] for _ in range(4)] for _ in range(12)]
        self.pions_graphiques = []
        self.boutons_valider = []
        self.resultats_graphiques = []
        self.hauteur_ligne = 45
        self.offset_y = 20
        self.restaurer_visuel(historique_couleurs)

        self.btn_nouveau = tk.Button(
            self.frame_principale,
            text="Nouvelle Partie",
            command=self.controleur.nouvelle_partie,
            bg="#2ecc71",
            fg="white",
            font=("Arial", 10, "bold"),
        )
        self.btn_nouveau.pack(pady=10)
        self.canvas_solution = tk.Canvas(
            self.frame_principale,
            bg="white",
            width=400,
            height=60,
            highlightthickness=0,
        )
        self.canvas_solution.pack(pady=5)
        self.label_score = tk.Label(
            self.frame_principale,
            text="",
            bg="white",
            font=("Arial", 14, "bold"),
            fg="#2c3e50",
        )
        self.label_score.pack(pady=5)

    def redessiner_sur_parent(self, nouveau_parent)-> None:
        self.frame_principale.pack(in_=nouveau_parent, expand=True, fill="both")

    def dessiner_nouvelle_ligne(self, i)-> None:
        y_ligne = self.offset_y + (i * self.hauteur_ligne)
        btn = tk.Button(
            self.canvas,
            text="Valider",
            state="normal",
            disabledforeground="gray70",
            command=lambda lignev=i: self.valider_ligne(lignev),
        )
        self.canvas.create_window(50, y_ligne + 20, window=btn)
        self.boutons_valider.append(btn)

        ligne_pions_ids = []
        for j in range(4):
            x_pion = 120 + (j * 50)
            pion_id = self.canvas.create_oval(
                x_pion,
                y_ligne + 5,
                x_pion + 30,
                y_ligne + 35,
                fill=self.etat_pions[i][j].value,
                outline="white",
                width=2,
            )
            ligne_pions_ids.append(pion_id)
            self.canvas.tag_bind(
                pion_id,
                "<Button-1>",
                lambda event, lignev=i, p=j: self.changer_couleur(lignev, p),
            )

        self.pions_graphiques.append(ligne_pions_ids)

        r_rouge = self.canvas.create_oval(
            350, y_ligne + 10, 370, y_ligne + 30, fill="red", state="hidden"
        )
        t_rouge = self.canvas.create_text(
            380, y_ligne + 20, text="0", fill="white", state="hidden"
        )
        r_blanc = self.canvas.create_oval(
            410, y_ligne + 10, 430, y_ligne + 30, fill="white", state="hidden"
        )
        t_blanc = self.canvas.create_text(
            440, y_ligne + 20, text="0", fill="white", state="hidden"
        )

        self.resultats_graphiques.append(
            {
                "objets": [r_rouge, t_rouge, r_blanc, t_blanc],
                "textes": {"rouge": t_rouge, "blanc": t_blanc},
            }
        )

        self.canvas.create_line(
            10,
            y_ligne + self.hauteur_ligne,
            490,
            y_ligne + self.hauteur_ligne,
            fill="white",
        )

    def changer_couleur(self, ligne, index_pion)-> None:
        if ligne != self.ligne_actuelle:
            return
        couleur_actuelle = self.etat_pions[ligne][index_pion]
        index_couleur = self.couleurs.index(couleur_actuelle)
        prochaine_couleur = self.couleurs[(index_couleur + 1) % len(self.couleurs)]
        self.etat_pions[ligne][index_pion] = prochaine_couleur
        self.canvas.itemconfig(
            self.pions_graphiques[ligne][index_pion], fill=prochaine_couleur.value
        )

    def valider_ligne(self, ligne)-> None:
        proposition = self.etat_pions[ligne]
        rouges, blancs = self.modele.verification_proposition(proposition)
        res = self.resultats_graphiques[ligne]
        self.canvas.itemconfig(res["textes"]["rouge"], text=str(rouges))
        self.canvas.itemconfig(res["textes"]["blanc"], text=str(blancs))
        for obj in res["objets"]:
            self.canvas.itemconfig(obj, state="normal")

        self.boutons_valider[ligne].config(
            state="disabled"
        )  # Désactivation de la ligne terminée : on peut plus la modifier
        for pion_id in self.pions_graphiques[ligne]:
            self.canvas.tag_unbind(pion_id, "<Button-1>")
        self.controleur.partie_objet.set_nb_tentatives(self.ligne_actuelle + 1)
        self.controleur.partie_objet.ajouter_tentative(proposition)
        Historique().ajouter_au_fichier(self.controleur.partie_objet)
        if self.modele.victoire(
            proposition
        ):  # vérification de la victoire à chaque fois qu'on valide une ligne
            self.controleur.enregistrer_partie(True, ligne + 1)
            self.message("victoire")
            return
        self.ligne_actuelle += 1  # Passage à la ligne suivante
        if self.ligne_actuelle < 12:
            self.dessiner_nouvelle_ligne(self.ligne_actuelle)
            self.message("tentative")
        else:
            self.controleur.enregistrer_partie(False, 12)
            self.message("perdu")

    def message(self, etat)-> None:
        etat = etat.lower()
        if etat == "victoire":
            tentatives = self.ligne_actuelle + 1
            texte = f"VICTOIRE ! Gagné en {tentatives} tentative(s) !"
            couleur = "#90EE90"
            score_final = self.controleur.partie_objet.get_score()
            self.label_score.config(text=f"Score : {score_final}")
        elif etat == "tentative":
            restantes = 12 - self.ligne_actuelle
            texte = f"Il vous reste {restantes} tentative(s)"
            couleur = "#EEE8AA"
            self.label_score.config(text="")
        elif etat == "perdu":
            texte = "PERDU !"  # à rajouté ! mettre la solution !!
            couleur = "#F08080"
            self.dessiner_solution_finale()  # c'est bon je l'ai ajouté, je vais test
            self.label_score.config(text="Score : 0")
        else:
            texte = "À vous de jouer !"
            couleur = "#EEE8AA"
            self.label_score.config(text="")
        self.zone_message.config(text=texte, bg=couleur)

    def dessiner_solution_finale(self)-> None:
        self.canvas_solution.delete("all")
        y_centre = 30
        self.canvas_solution.create_text(
            70, y_centre, text="SOLUTION :", fill="#2c3e50", font=("Arial", 10, "bold")
        )
        for j, couleur_enum in enumerate(self.modele.combinaison_secrete_bis):
            x_pion = 130 + (j * 50)
            self.canvas_solution.create_oval(
                x_pion,
                y_centre - 15,
                x_pion + 30,
                y_centre + 15,
                fill=couleur_enum.value,
                outline="#8B4513",
                width=2,
            )

    def restaurer_visuel(self, historique_couleurs)-> None:
        self.ligne_actuelle = 0
        for i, noms_couleurs in enumerate(historique_couleurs):
            self.etat_pions[i] = [Couleur[nom] for nom in noms_couleurs]
            self.dessiner_nouvelle_ligne(i)
            rouges, blancs = self.modele.verification_proposition(self.etat_pions[i])
            res = self.resultats_graphiques[i]
            self.canvas.itemconfig(res["textes"]["rouge"], text=str(rouges))
            self.canvas.itemconfig(res["textes"]["blanc"], text=str(blancs))
            for obj in res["objets"]:
                self.canvas.itemconfig(obj, state="normal")
            self.boutons_valider[i].config(state="disabled")
            for pion_id in self.pions_graphiques[i]:
                self.canvas.tag_unbind(pion_id, "<Button-1>")
            self.ligne_actuelle = i + 1
        if self.ligne_actuelle < 12:
            self.dessiner_nouvelle_ligne(self.ligne_actuelle)
        else:
            self.message("perdu")
