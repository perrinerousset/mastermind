import tkinter as tk
from MVC.model.mastermind import mastermind
from MVC.view.vue_principale import VuePrincipale
from MVC.view.console import VueJeu
from MVC.view.vue_historique import VueHistorique
from MVC.view.vue_regles_jeu import VueReglesJeu
from MVC.model.jeu import Jeu
from MVC.model.historique import historique
from MVC.model.mastermind import Couleur

class Controleur:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mastermind Projet")
        self.modele = mastermind()
        self.vue_principale = VuePrincipale(self.root, self)
        self.partie_objet = None  
        self.vue_jeu_active = None 
        self.historique_parties = []
        self.compteur_id = 1
        self.afficher_accueil()   
        self.charger_derniere_session()
        self.root.mainloop()
        
    def afficher_accueil(self):
        self.vue_principale.nettoyer_zone_centrale()
        tk.Label(self.vue_principale.zone_centrale, text="Bienvenue dans le Mastermind !\nCliquez sur 'Jouer' pour commencer.",font=("Arial", 16), bg="white").pack(expand=True)


    def nouvelle_partie(self):
        if self.partie_objet:
            self.historique_parties.append(self.partie_objet)
        if self.vue_jeu_active:
            self.vue_jeu_active.frame_principale.destroy()
            self.vue_jeu_active = None     
        self.vue_principale.nettoyer_zone_centrale()
        self.modele.Combinaison_secrete() 
        solution_noms = [c.name for c in self.modele.CombinaisonSecrete]
        self.partie_objet = Jeu(
            id_partie=self.compteur_id, 
            combinaison_secrete=solution_noms
        )
        self.compteur_id += 1
        historique().ajouter_au_fichier(self.partie_objet)
        self.vue_jeu_active = VueJeu(self.vue_principale.zone_centrale, self.modele, self)
                    
    def afficher_jeu(self):
        self.vue_principale.nettoyer_zone_centrale()
        if self.vue_jeu_active:
            self.vue_jeu_active.redessiner_sur_parent(self.vue_principale.zone_centrale)
        elif self.partie_objet and self.vue_jeu_active is None:
            self.vue_jeu_active = VueJeu(self.vue_principale.zone_centrale, self.modele, self)
        else:
            self.nouvelle_partie()

    def afficher_historique(self):
        self.vue_principale.nettoyer_zone_centrale()
        VueHistorique(self.vue_principale.zone_centrale, self.modele)

    def afficher_regles(self):
        self.vue_principale.nettoyer_zone_centrale()
        VueReglesJeu(self.vue_principale.zone_centrale, self.modele)
    
    def enregistrer_partie(self, victoire: bool, tentatives : int):
        if not self.partie_objet:
            return
        self.partie_objet.terminer_partie(victoire, tentatives)
        historique().ajouter_au_fichier(self.partie_objet)
        
    def charger_derniere_session(self):
        h = historique()
        donnees_totales = h.charger_historique()
        if donnees_totales:
            id_max = max(p.get("id", 0) for p in donnees_totales)
            self.compteur_id = id_max + 1
        else:
            self.compteur_id = 1
        sauvegarde = h.charger_partie_en_cours()
        if sauvegarde:
            solution_enums = [Couleur[nom] for nom in sauvegarde["solution"]]
            self.modele.CombinaisonSecrete = solution_enums
            self.partie_objet = Jeu(
                id_partie=sauvegarde["id"],
                nb_tentatives=sauvegarde["tentatives"],
                combinaison_secrete=sauvegarde["solution"], 
                historique_tentatives=sauvegarde["historique_couleurs"]
            )

if __name__ == "__main__":
    Controleur()