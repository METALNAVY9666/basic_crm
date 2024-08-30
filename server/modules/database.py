"""module permettant de gérer la base de données"""
import sqlite3

COMMANDS = {
    "get_interventions": "select * from interventions"
    }

class Database:
    """gère la base de données"""
    def __init__(self, filename: str):
        self.connexion = sqlite3.connect(filename)
        self.cursor = self.connexion.cursor

    def pull(self, query: str) -> list:
        """récupère des données de la database avec la requête en argument"""
        return self.connexion.execute(query).fetchall()
