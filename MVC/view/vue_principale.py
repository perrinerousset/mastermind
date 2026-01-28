from abc import ABC, abstractmethod
import tkinter as tk

class vue_principale(ABC):
    def __init__(self, root):
        self.root = root
        self.zone_laterale = tk.Frame(self.root, bg="#2c3e50", width=200)
        self.zone_laterale.pack(side="left", fill="y")
        self.zone_laterale.pack_propagate(False)
        self.zone_centrale = tk.Frame(self.root, bg="white")
        self.zone_centrale.pack(side="right", expand=True, fill="both")
        self.dessiner_jeu()
        self.dessiner_menu()

    @abstractmethod
    def dessiner_jeu(self):
        pass

    @abstractmethod
    def dessiner_menu(self):
        pass