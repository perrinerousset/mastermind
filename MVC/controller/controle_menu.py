import tkinter as tk
from model.mastermind import mastermind
from view.vue_principale import VuePrincipale
from view.console import VueJeu
from view.vue_historique import VueHistorique
from view.vue_regles_jeu import VueReglesJeu
from model.jeu import Jeu

class Controleur:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mastermind Projet")
        self.modele = mastermind()
        self.vue_principale = VuePrincipale(self.root, self)
        self.partie_objet = None  
        self.vue_jeu_active = None 
        self.afficher_accueil()   
        self.root.mainloop()
        
    def afficher_accueil(self):
        self.vue_principale.nettoyer_zone_centrale()
        tk.Label(self.vue_principale.zone_centrale, text="Bienvenue dans le Mastermind !\nCliquez sur 'Jouer' pour commencer.",font=("Arial", 16), bg="white").pack(expand=True)


    def nouvelle_partie(self):
        self.vue_principale.nettoyer_zone_centrale()
        self.modele.Combinaison_secrete()
        id_p = 1 
        self.partie_objet = Jeu(id_partie=id_p)
        self.vue_jeu_active = VueJeu(self.vue_principale.zone_centrale, self.modele, self)
        
    def afficher_jeu(self):
        self.vue_principale.nettoyer_zone_centrale()
        if self.vue_jeu_active:
            self.vue_jeu_active.redessiner_sur_parent(self.vue_principale.zone_centrale)
        else:
            self.nouvelle_partie()

    def afficher_historique(self):
        self.vue_principale.nettoyer_zone_centrale()
        VueHistorique(self.vue_principale.zone_centrale, self.modele)

    def afficher_regles(self):
        self.vue_principale.nettoyer_zone_centrale()
        VueReglesJeu(self.vue_principale.zone_centrale, self.modele)

if __name__ == "__main__":
    Controleur()