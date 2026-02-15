import tkinter as tk


class VuePrincipale:
    def __init__(self, root, controleur) -> None:
        self.root = root
        self.controleur = controleur

        self.zone_laterale = tk.Frame(self.root, bg="#2c3e50", width=200, height=600)
        self.zone_laterale.pack(side="left", fill="y")
        self.zone_laterale.pack_propagate(False)  #

        self.zone_centrale = tk.Frame(self.root, bg="white", width=600, height=600)
        self.zone_centrale.pack(side="right", expand=True, fill="both")

        self.dessiner_menu_permanent()

    def dessiner_menu_permanent(self) -> None:
        tk.Label(
            self.zone_laterale,
            text="MASTERMIND",
            fg="white",
            bg="#2c3e50",
            font=("Arial", 14, "bold"),
            pady=20,
        ).pack()

        # Les boutons appellent le contrôleur
        tk.Button(
            self.zone_laterale, text="Jouer", command=self.controleur.afficher_jeu
        ).pack(fill="x", padx=10, pady=5)

        tk.Button(
            self.zone_laterale,
            text="Historique",
            command=self.controleur.afficher_historique,
        ).pack(fill="x", padx=10, pady=5)

        tk.Button(
            self.zone_laterale,
            text="Règles du jeu",
            command=self.controleur.afficher_regles,
        ).pack(fill="x", padx=10, pady=5)

    def nettoyer_zone_centrale(self) -> None:
        for widget in self.zone_centrale.winfo_children():
            if (
                self.controleur.vue_jeu_active
                and widget == self.controleur.vue_jeu_active.frame_principale
            ):
                widget.pack_forget()
            else:
                widget.destroy()
