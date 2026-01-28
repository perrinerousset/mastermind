import tkinter as tk
from tkinter import messagebox
from abc import ABC, abstractmethod

class menu(vue_principale):
    def __init__(self, root):
        root.title("Mastermind - Projet")
        root.geometry("800x600")
        super().__init__(root)

    def dessiner_menu_lateral(self):
        tk.Label(self.zone_laterale, text="MASTERMIND", fg="white", bg="#2c3e50", 
                 font=("Arial", 14, "bold"), pady=20).pack()
        self.btn_jeu = tk.Button(self.zone_laterale, text="Jouer", command=self.clic_nouveau)
        self.btn_jeu.pack(fill="x", padx=10, pady=5)
        self.btn_historique = tk.Button(self.zone_laterale, text="Historique", command=self.clic_historique)
        self.btn_historique.pack(fill="x", padx=10, pady=5)


    def clic_nouveau(self):
        #définir dans une autre classe ? 

    def clic_reprendre(self):
        #définir dans une autre classe ? 

    def clic_historique(self):
        #définir dans une autre classe ? 

if __name__ == "__main__":
    fenetre = tk.Tk()
    application = Menu(fenetre)
    fenetre.mainloop()