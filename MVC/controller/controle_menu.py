import tkinter as tk
from model.mastermind import mastermind
from view.vue_principale import VuePrincipale
from view.console import VueJeu
from view.vue_historique import VueHistorique

class Controleur:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mastermind Projet")
        self.modele = mastermind()
        self.vue_principale = VuePrincipale(self.root, self)
        
        # Correction : On définit l'accueil
        self.afficher_accueil()
        
        self.root.mainloop()
        
    def afficher_accueil(self):
        self.vue_principale.nettoyer_zone_centrale()
        tk.Label(self.vue_principale.zone_centrale, 
                 text="Bienvenue dans le Mastermind !\nCliquez sur 'Jouer' pour commencer.",
                 font=("Arial", 16), bg="white").pack(expand=True)

    def afficher_jeu(self):
        self.vue_principale.nettoyer_zone_centrale()
        self.modele.Combinaison_secrete() 
        VueJeu(self.vue_principale.zone_centrale, self.modele)

    def afficher_historique(self):
        self.vue_principale.nettoyer_zone_centrale()
        VueHistorique(self.vue_principale.zone_centrale, self.modele)

if __name__ == "__main__":
    Controleur()