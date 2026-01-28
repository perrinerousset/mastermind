from abc import ABC, abstractmethod
import tkinter as tk

class VuePrincipale(ABC):
    def __init__(self, root):
        self.root = root
        self.zone_centrale = tk.Frame(self.root, bg="white", width=600, height=600)
        self.zone_centrale.pack(side="left", expand=True, fill="both")
        self.zone_laterale = tk.Frame(self.root, bg="#f0f0f0", width=200, height=600)
        self.zone_laterale.pack(side="right", fill="y")
        self.dessiner_jeu()
        self.dessiner_menu()

    @abstractmethod
    def dessiner_jeu(self):
        """Cette méthode doit être implémentée par la classe fille pour afficher le plateau."""
        pass

    @abstractmethod
    def dessiner_menu(self):
        """Cette méthode doit être implémentée par la classe fille pour afficher les boutons."""
        pass