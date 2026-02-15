"""
Fait le lien entre l'appuit sur les boutons du menu
et l'action : remplissage des vues'
"""  # le ruff demande qu'on écrive ça c'est l'erreur C0114/5/6: Docstring manquante

import tkinter as tk

from mvc.model.historique import Historique
from mvc.model.jeu import Jeu
from mvc.model.mastermind import Couleur, Mastermind
from mvc.view.console import VueJeu
from mvc.view.vue_historique import VueHistorique
from mvc.view.vue_principale import VuePrincipale
from mvc.view.vue_regles_jeu import VueReglesJeu


class Controleur:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Mastermind Projet")
        self.modele = Mastermind()
        self.vue_principale = VuePrincipale(self.root, self)
        self.partie_objet = None
        self.vue_jeu_active = None
        self.historique_parties = []
        self.compteur_id = 1
        self.afficher_accueil()
        self.charger_derniere_session()
        self.root.mainloop()

    def afficher_accueil(self) -> None:
        self.vue_principale.nettoyer_zone_centrale()
        tk.Label(
            self.vue_principale.zone_centrale,
            text="Bienvenue dans le Mastermind !\nCliquez sur 'Jouer' pour commencer.",
            font=("Arial", 16),
            bg="white",
        ).pack(expand=True)

    def nouvelle_partie(self) -> None:
        if self.partie_objet:
            # Si la partie n'est pas gagnée et qu'il reste des essais, c'est un abandon
            essais_actuels = self.partie_objet.get_nb_tentatives()
            if not self.partie_objet.get_est_gagne() and essais_actuels < 12:
                self.enregistrer_partie(victoire=False, tentatives=essais_actuels)
        if self.vue_jeu_active:
            self.vue_jeu_active.frame_principale.destroy()
            self.vue_jeu_active = None
        self.vue_principale.nettoyer_zone_centrale()
        self.modele.combinaison_secrete()
        solution_noms = [c.name for c in self.modele.combinaison_secrete_bis]
        self.partie_objet = Jeu(
            id_partie=self.compteur_id, combinaison_secrete=solution_noms
        )
        self.compteur_id += 1
        Historique().ajouter_au_fichier(self.partie_objet)
        self.vue_jeu_active = VueJeu(
            self.vue_principale.zone_centrale, self.modele, self
        )

    def afficher_jeu(self) -> None:
        self.vue_principale.nettoyer_zone_centrale()
        if self.vue_jeu_active:
            self.vue_jeu_active.redessiner_sur_parent(self.vue_principale.zone_centrale)
        elif self.partie_objet and self.vue_jeu_active is None:
            self.vue_jeu_active = VueJeu(
                self.vue_principale.zone_centrale, self.modele, self
            )
        else:
            self.nouvelle_partie()

    def afficher_historique(self) -> None:
        self.vue_principale.nettoyer_zone_centrale()
        VueHistorique(self.vue_principale.zone_centrale, self.modele)

    def afficher_regles(self) -> None:
        self.vue_principale.nettoyer_zone_centrale()
        VueReglesJeu(self.vue_principale.zone_centrale, self.modele)

    def enregistrer_partie(self, victoire: bool, tentatives: int) -> None:
        if not self.partie_objet:
            return
        self.partie_objet.terminer_partie(victoire, tentatives)
        Historique().ajouter_au_fichier(self.partie_objet)
        self.partie_objet = None

    def charger_derniere_session(self) -> None:
        h = Historique()
        donnees_totales = h.charger_historique()
        if donnees_totales:
            id_max = max(p.get("id", 0) for p in donnees_totales)
            self.compteur_id = id_max + 1
        else:
            self.compteur_id = 1

        sauvegarde = h.charger_partie_en_cours()

        if sauvegarde:
            solution_enums = [Couleur[nom] for nom in sauvegarde["solution"]]
            self.modele.combinaison_secrete_bis = solution_enums
            self.partie_objet = Jeu(
                id_partie=sauvegarde["id"],
                nb_tentatives=sauvegarde["tentatives"],
                combinaison_secrete=sauvegarde["solution"],
                historique_tentatives=sauvegarde["historique_couleurs"],
            )
            self.afficher_jeu()
        else:
            self.nouvelle_partie()


if __name__ == "__main__":
    Controleur()
