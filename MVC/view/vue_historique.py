import tkinter as tk
from model.historique import historique


class VueHistorique:
    def __init__(self, parent, modele_jeu=None):
        
        self.parent = parent
        
        
        self.frame_principale = tk.Frame(self.parent, bg="white")
        self.frame_principale.pack(fill="both", expand=True)

       
        tk.Label(self.frame_principale, text="HISTORIQUE DES SCORES", 
                 font=("Helvetica", 20, "bold"), bg="white", fg="#2c3e50", pady=20).pack()

        
        self.liste_frame = tk.Frame(self.frame_principale, bg="white")
        self.liste_frame.pack(fill="both", expand=True, padx=40, pady=10)

        # Barre de défilement
        self.scrollbar = tk.Scrollbar(self.liste_frame)
        self.scrollbar.pack(side="right", fill="y")

        # Listbox pour afficher les parties
        self.liste_box = tk.Listbox(self.liste_frame, font=("Courier New", 12), 
                                    bg="#f8f9fa", fg="#34495e",
                                    height=15, borderwidth=0, highlightthickness=1,
                                    yscrollcommand=self.scrollbar.set)
        self.liste_box.pack(side="left", fill="both", expand=True)
        self.scrollbar.config(command=self.liste_box.yview)

       
        self.btn_retour = tk.Button(self.frame_principale, text="Actualiser", 
                                    command=self.charger_et_afficher,
                                    bg="#3498db", fg="white", font=("Arial", 10, "bold"),
                                    padx=20, pady=5)
        self.btn_retour.pack(pady=20)

      
        self.charger_et_afficher()

    def charger_et_afficher(self):
        
        self.liste_box.delete(0, tk.END) 
        
        # On utilise ta classe modèle historique
        h = historique()
        parties = h.charger_historique()

        if not parties:
            self.liste_box.insert(tk.END, " Aucun historique disponible.")
            return

       
        header = f"{'ID':<6} | {'RÉSULTAT':<12} | {'SCORE':<10} | {'TENTATIVES'}"
        self.liste_box.insert(tk.END, header)
        self.liste_box.insert(tk.END, "-" * 50)

        # On affiche les parties (les plus récentes en haut)
        for p in reversed(parties):
            res = "SUCCÈS" if p.get('victoire') else "ÉCHEC"
            ligne = (f" #{p.get('id', '?'):<4} | "
                     f"{res:<12} | "
                     f"{p.get('score', 0):<10} | "
                     f"{p.get('tentatives', 0)}/12")
            self.liste_box.insert(tk.END, ligne)
            
            
            if res == "SUCCÈS":
                self.liste_box.itemconfig(tk.END, fg="#27ae60")
            else:
                self.liste_box.itemconfig(tk.END, fg="#e74c3c")