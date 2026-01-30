import tkinter as tk
from model.mastermind import mastermind
from view.vue_principale import VuePrincipale
from view.console import VueJeu
from view.vue_historique import VueHistorique
from view.vue_regles_jeu import VueReglesJeu
from model.jeu import Jeu
from model.historique import historique

class Controleur:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mastermind Projet")
        self.modele = mastermind()
        self.vue_principale = VuePrincipale(self.root, self)
        self.partie_objet = None  
        self.vue_jeu_active = None 
        self.gestionnaire_historique = historique()
        self.historique_parties = []
        self.compteur_id = 1
        self.gestionnaire_historique = historique()   
        self.root.mainloop()
        
    def afficher_accueil(self):
        self.vue_principale.nettoyer_zone_centrale()
        tk.Label(self.vue_principale.zone_centrale, text="Bienvenue dans le Mastermind !\nCliquez sur 'Jouer' pour commencer.",font=("Arial", 16), bg="white").pack(expand=True)


    def nouvelle_partie(self):
            if self.partie_objet:
                try:
                    if hasattr(self, 'gestionnaire_historique'):
                        self.gestionnaire_historique.ajouter_au_fichier(self.partie_objet)
                    self.historique_parties.append(self.partie_objet)
                except Exception as e:
                    print(f"Note: Sauvegarde ignorée ou erreur : {e}")

            if self.vue_jeu_active:
                try:
                    self.vue_jeu_active.frame_principale.destroy()
                except:
                    pass
                self.vue_jeu_active = None

            self.vue_principale.nettoyer_zone_centrale()
            self.modele.Combinaison_secrete() 
            self.partie_objet = Jeu(id_partie=self.compteur_id)
            self.compteur_id += 1
            from view.console import VueJeu
            self.vue_jeu_active = VueJeu(self.vue_principale.zone_centrale, self.modele, self)
                    
    def afficher_jeu(self):
        self.vue_principale.nettoyer_zone_centrale()
        if self.vue_jeu_active:
            self.vue_jeu_active.redessiner_sur_parent(self.vue_principale.zone_centrale)
        else:
            self.nouvelle_partie()
        if self.vue_jeu_active is None:
            self.nouvelle_partie()

    def afficher_historique(self):
        self.vue_principale.nettoyer_zone_centrale()
        VueHistorique(self.vue_principale.zone_centrale, self.modele)

    def afficher_regles(self):
        self.vue_principale.nettoyer_zone_centrale()
        VueReglesJeu(self.vue_principale.zone_centrale, self.modele)

if __name__ == "__main__":
    Controleur()