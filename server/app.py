"""contient les routes pour l'api"""
from flask import Flask, request
from flask_cors import CORS
from modules.database import Database, COMMANDS


app = Flask(__name__)
CORS(app)
database = Database("data/database.db")

@app.route("/datapull/<query_key>", methods=["GET"])
def datapull(query_key):
    """renvoie les données de la clef correspondant à la requête SQL"""
    if query_key not in COMMANDS.keys():
        return 404
    return database.pull(COMMANDS[query_key])

if __name__ == "__main__":
    app.run()