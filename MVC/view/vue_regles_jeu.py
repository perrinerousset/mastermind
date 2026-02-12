import tkinter as tk


class VueReglesJeu:
    def __init__(self, parent, modele_jeu=None):
        self.parent = parent
        self.frame_principale = tk.Frame(self.parent, bg="white")
        self.frame_principale.pack(fill="both", expand=True)
        self.contenu_centre = tk.Frame(
            self.frame_principale, bg="white", relief="ridge", bd=2, padx=30, pady=30
        )
        self.contenu_centre.place(
            relx=0.5, rely=0.5, anchor="center"
        )  # Centrage au milieu
        tk.Label(
            self.contenu_centre,
            text="RÈGLES DU JEU",
            font=("Helvetica", 22, "bold"),
            bg="white",
            fg="#2c3e50",
        ).pack(pady=(0, 20))
        regles_texte = (
            "BUT DU JEU :\n"
            "L'objectif du mastermind est de déterminer la combinaison"
            "secrète de 4 pions colorés choisie par l'ordinateur.\n\n"
            " DÉROULEMENT :\n"
            "À chaque tour, proposez une combinaison sur la ligne active en cliquant"
            "sur les pions afin de leur faire changer de couleur.\n"
            "Après validation, des indices s'affichent à droite :\n\n"
            "Pion Rouge : Une couleur est correcte et bien placée.\n"
            "Pion Blanc : Une couleur est correcte mais mal placée.\n\n"
            "CONDITIONS :\n"
            "Vous avez un maximum de 12 tentatives pour trouver la combinaison.\n"
            "Moins vous avez de tentatives, plus votre score est élevé !\n\n"
            "A vous de jouer !"
        )
        self.label_regles = tk.Label(
            self.contenu_centre,
            text=regles_texte,
            justify="left",
            font=("Arial", 12),
            bg="white",
            fg="#34495e",
            wraplength=500,
        )
        self.label_regles.pack()
