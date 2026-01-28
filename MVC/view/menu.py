class Menu:
    def __init__(self):
        # Liste des options pour la clarté du code
        self.options_accueil = {
            "1": "Nouvelle partie",
            "2": "Reprendre partie",
            "3": "Voir historique",
            "4": "Quitter"
        }

    def afficher_accueil(self):
        """Affiche la page d'accueil principale."""
        print("\n" + "="*30)
        print("      MASTERMIND - MENU")
        print("="*30)
        for touche, libelle in self.options_accueil.items():
            print(f" {touche} > {libelle}")
        print("="*30)
        return self.saisir_choix(self.options_accueil.keys())

    def afficher_menu_en_jeu(self):
        """Affiche un menu compact (déroulant) pendant la partie."""
        print("\n--- [M] Menu | [H] Aide | [Q] Quitter ---")
        return self.saisir_choix(['M', 'H', 'Q', '1', '2', '3', '4', '5', '6']) # Inclut les pions possibles

    def saisir_choix(self, options_valides):
        """Lit et valide l'entrée de l'utilisateur."""
        while True:
            choix = input("\nVotre action : ").strip().upper()
            if choix in options_valides:
                return choix
            print(f"Erreur : '{choix}' n'est pas une option valide.")

    def afficher_message(self, message):
        """Méthode utilitaire pour afficher des retours au joueur."""
        print(f"\n[INFO] : {message}")