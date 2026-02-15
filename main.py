"""
Main
"""  # le ruff demande qu'on écrive ça c'est l'erreur C0114/5/6: Docstring manquante

from logger_config import setup_logger
from mvc.controller.controle_menu import Controleur

if __name__ == "__main__":
    setup_logger()
    Controleur()
