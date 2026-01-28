import tkinter as tk
from tkinter import messagebox

class Menu:
    def __init__(self, root):
        self.root = root
        self.root.title("Mastermind - Projet")
        self.root.geometry("800x600")
        
        # Création du menu latéral
        self.sidebar = tk.Frame(self.root, bg="#2c3e50", width=200, height=600)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False) # Empêche le cadre de rétrécir

        # Titre du menu
        tk.Label(self.sidebar, text="MASTERMIND", fg="white", bg="#2c3e50", 
                 font=("Arial", 14, "bold"), pady=20).pack()

        # Boutons du menu 
        self.btn_nouveau = tk.Button(self.sidebar, text="Nouvelle Partie", command=self.clic_nouveau)
        self.btn_nouveau.pack(fill="x", padx=10, pady=5)

        self.btn_reprendre = tk.Button(self.sidebar, text="Reprendre", command=self.clic_reprendre)
        self.btn_reprendre.pack(fill="x", padx=10, pady=5)

        self.btn_historique = tk.Button(self.sidebar, text="Historique", command=self.clic_historique)
        self.btn_historique.pack(fill="x", padx=10, pady=5)

        self.btn_quitter = tk.Button(self.sidebar, text="Quitter", command=self.root.quit)
        self.btn_quitter.pack(side="bottom", fill="x", padx=10, pady=20)

        # Zone principale (à droite) 
        self.zone_jeu = tk.Frame(self.root, bg="#ecf0f1")
        self.zone_jeu.pack(side="right", expand=True, fill="both")
        
        self.label_info = tk.Label(self.zone_jeu, text="Bienvenue ! Choisissez une option à gauche.", bg="#ecf0f1")
        self.label_info.pack(expand=True)

    # Fonctions appelées lors du clic (à lier ensuite au contrôleur)
    def clic_nouveau(self):
        self.label_info.config(text="Lancement d'une nouvelle partie...")

    def clic_reprendre(self):
        messagebox.showinfo("Reprendre", "Recherche d'une sauvegarde...")

    def clic_historique(self):
        self.label_info.config(text="Affichage des anciens scores.")

#  Pour tester l'affichage immédiatement 
if __name__ == "__main__":
    fenetre = tk.Tk()
    application = Menu(fenetre)
    fenetre.mainloop()