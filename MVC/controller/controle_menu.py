import tkinter as tk
from mastermind import mastermind
from vue_principale import VuePrincipale
from vue_jeu import VueJeu
class Controleur:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mastermind Projet")
        self.modele = mastermind()
        self.vue_principale = VuePrincipale(self.root, self)
        self.afficher_accueil()
        self.root.mainloop()

    def afficher_accueil(self):
        self.vue_principale.nettoyer_zone_centrale()
        tk.Label(self.vue_principale.zone_centrale, text="Bienvenue !\nChoisissez une option à gauche.",
                 font=("Arial", 16), bg="white").pack(expand=True)

    def afficher_jeu(self):
        """Active la vue du plateau de jeu"""
        self.vue_principale.nettoyer_zone_centrale()
        self.modele.Combinaison_secrete()
        # On installe la VueJeu dans la zone centrale existante
        VueJeu(self.vue_principale.zone_centrale, self.modele)

    def afficher_historique(self):
        """Active la vue historique"""
        self.vue_principale.nettoyer_zone_centrale()
        tk.Label(self.vue_principale.zone_centrale, text="Historique des parties",
                 font=("Arial", 16), bg="white").pack(expand=True)

if __name__ == "__main__":
    Controleur()