import tkinter as tk

class VueJeu:
    def __init__(self, parent_frame, modele):
        self.parent = parent_frame
        self.modele = modele
        self.dessiner_plateau()

    def dessiner_plateau(self):
        self.canvas = tk.Canvas(self.parent, bg="#8B4513", width=500, height=580)
        self.canvas.pack(pady=10)