import tkinter as tk


class VueReglesJeu:
    def __init__(self, parent, modele_jeu=None):
        self.parent = parent
        self.frame_principale = tk.Frame(self.parent, bg="white")
        self.frame_principale.pack(fill="both", expand=True)

       
        tk.Label(self.frame_principale, text="REGLES DU JEU", 
                 font=("Helvetica", 20, "bold"), bg="white", fg="#2c3e50", pady=20).pack()

        
        self.liste_frame = tk.Frame(self.frame_principale, bg="white")
        self.liste_frame.pack(fill="both", expand=True, padx=40, pady=10)

        regles_texte = (
            "1. Le but est blabla.\n"
            "2. ensuite :\n"
            "   couleurs rouges.\n"
            "   couleur blanc.\n"
            "3. tant d'essais !"
        )
        tk.Label(self.frame_principale, text=regles_texte, justify="left", wraplength=550).pack(pady=10)
   