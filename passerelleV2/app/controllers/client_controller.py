import json
import sqlite3

# from app.models.database import get_db_connection
from app.models.client import Client
from flask import Blueprint, jsonify, redirect, render_template, request
from flask_login import login_required

# Création d'un Blueprint pour le client controller
client_bp = Blueprint("client", __name__)

# @client_bp.route('/clients', methods=['GET'])
# @login_required
# def get_clients():
#     conn = get_db_connection()
#     try:
#         # selectionner tous les clients, liés à leur client EBP et client Zeendoc
#         clients = conn.execute("SELECT  CLIENT.id AS ClientID, CLIENT.username AS ClientUsername, CLIENT.LastUpdate AS ClientLastUpdate, CLIENT_EBP.TOKEN IS NOT NULL AS TokenDefined, CLIENT_ZEENDOC.ZEENDOC_CLASSEUR AS ClasseurDefined FROM CLIENT LEFT JOIN CLIENT_EBP ON CLIENT.id_2 = CLIENT_EBP.id LEFT JOIN CLIENT_ZEENDOC ON CLIENT.id_1 = CLIENT_ZEENDOC.id;")
#         # afficher les clients
#         print(clients)
#         # Convertir les objets Row en dictionnaires
#         clients_list = [dict(client) for client in clients]
#         return jsonify(clients_list)
#     except sqlite3.Error as e:
#         print(e)
#         return jsonify({'error': str(e)}), 500
#     finally:
#         conn.close()


# route pour récupérer les données d'un client par son id
@client_bp.route("/client", methods=["GET"])
@login_required
def get_client():
    client_id = request.args.get("id")
    client = client(client_id)

    ebp = client.clientEBP.BdGetClientEBP(client_id)
    zeendoc = client.clientZeendoc.BdGetClientZeendoc(client_id)

    return jsonify({"clientId": client_id, "ebp": ebp, "zeendoc": zeendoc})


# @client_bp.route('/add_client_p1', methods=['POST'])
# @login_required
# def add_client_p1():
#     username = request.form.get('username')
#     idPasserelle = 1
#     ebp_client_id = request.form.get('EBP_CLIENT_ID')
#     ebp_client_secret = request.form.get('EBP_CLIENT_SECRET')
#     ebp_subscription_key = request.form.get('EBP_SUBSCRIPTION_KEY')
#     zeendoc_login = request.form.get('ZEENDOC_LOGIN')
#     zeendoc_urlclient = request.form.get('ZEENDOC_URLCLIENT')
#     zeendoc_cpassword = request.form.get('ZEENDOC_CPASSWORD')

#     conn = get_db_connection()
#     try:
#         cur = conn.cursor()
#         cur.execute("INSERT INTO CLIENT (username, idPasserelle) VALUES (?, ?)",
#                     (username, idPasserelle))
#         client_id = cur.lastrowid

#         cur.execute("INSERT INTO CLIENT_EBP (EBP_CLIENT_ID, EBP_CLIENT_SECRET, EBP_SUBSCRIPTION_KEY) VALUES (?, ?, ?)",
#                     (ebp_client_id, ebp_client_secret, ebp_subscription_key))
#         ebp_id = cur.lastrowid

#         cur.execute("INSERT INTO CLIENT_ZEENDOC (ZEENDOC_LOGIN, ZEENDOC_URLCLIENT, ZEENDOC_CPASSWORD) VALUES (?, ?, ?)",
#                     (zeendoc_login, zeendoc_urlclient, zeendoc_cpassword))
#         zeendoc_id = cur.lastrowid

#         cur.execute("UPDATE CLIENT SET id_1 = ?, id_2 = ? WHERE id = ?",
#                     (zeendoc_id, ebp_id, client_id))

#         conn.commit()
#         return jsonify({'message': 'Client ajouté avec succès', 'client_id': client_id})
#     except sqlite3.Error as e:
#         conn.rollback()
#         return jsonify({'error': str(e)}), 500
#     finally:
#         conn.close()


@client_bp.route("/form_add_client", methods=["GET"])
@login_required
def form_add_client():
    return render_template("add_client/add_client_p1.html")


@client_bp.route("/update_client", methods=["POST"])
@login_required
def update_client():

    client_id = request.form.get("client_id")

    username = request.form.get("username")
    LastUpdate = request.form.get("LastUpdate")
    EBP_CLIENT_ID = request.form.get("EBP_CLIENT_ID")
    EBP_CLIENT_SECRET = request.form.get("EBP_CLIENT_SECRET")
    EBP_SUBSCRIPTION_KEY = request.form.get("EBP_SUBSCRIPTION_KEY")
    EBP_FOLDER_ID = request.form.get("EBP_FOLDER_ID")
    ZEENDOC_LOGIN = request.form.get("ZEENDOC_LOGIN")
    ZEENDOC_URLCLIENT = request.form.get("ZEENDOC_URLCLIENT")
    ZEENDOC_CLASSEUR = request.form.get("ZEENDOC_CLASSEUR")
    ZEENDOC_CPASSWORD = request.form.get("ZEENDOC_CPASSWORD")

    client = Client(client_id)

    client.update_client(
        username,
        LastUpdate,
        EBP_CLIENT_ID,
        EBP_CLIENT_SECRET,
        EBP_SUBSCRIPTION_KEY,
        EBP_FOLDER_ID,
        ZEENDOC_LOGIN,
        ZEENDOC_URLCLIENT,
        ZEENDOC_CLASSEUR,
        ZEENDOC_CPASSWORD,
    )

    return redirect("/")


# @client_bp.route('/delete_client', methods=['POST'])
# @login_required
# def delete_client():
#     client_id = request.form.get('client_id')

#     conn = get_db_connection()
#     try:
#         cur = conn.cursor()

#         # Supprimer les données de la table CLIENT_EBP
#         cur.execute("DELETE FROM CLIENT_EBP WHERE id IN (SELECT id_2 FROM CLIENT WHERE id = ?)", (client_id,))

#         # Supprimer les données de la table CLIENT_ZEENDOC
#         cur.execute("DELETE FROM CLIENT_ZEENDOC WHERE id IN (SELECT id_1 FROM CLIENT WHERE id = ?)", (client_id,))

#         # Supprimer les données de la table CLIENT
#         cur.execute("DELETE FROM CLIENT WHERE id = ?", (client_id,))

#         conn.commit()
#         return redirect("/")

#     except sqlite3.Error as e:
#         conn.rollback()
#         return jsonify({'error': str(e)}), 500
#     finally:
#         conn.close()


@client_bp.route("/form_update_client", methods=["GET", "POST"])
@login_required
def form_update_client():

    # si le type de requête est GET, on récupère l'id du client
    if request.method == "GET":
        client_id = request.args.get("id")

    # si le type de requête est POST, on récupère l'id du client
    elif request.method == "POST":
        client_id = request.form["client_id"]

    client_instance = Client(client_id)

    data_ebp = client_instance.clientEBP.BdGetClientEBP(client_id)
    if data_ebp["TOKEN_DEFINED"] == 0:
        client_instance.clientEBP.login()

    ebp = client_instance.clientEBP.BdGetClientEBP(client_id)
    # on transforme le résultat en dictionnaire pour pouvoir l'envoyer dans le template
    ebp = dict(ebp)
    zeendoc = client_instance.clientZeendoc.BdGetClientZeendoc(client_id)
    zeendoc = dict(zeendoc)

    client_data = {"ebp": ebp, "zeendoc": zeendoc}

    try:
        folders = client_instance.clientEBP.get_folders()

        # folders = folders.text

    except Exception as e:
        folders = "Erreur lors de la récupération des dossiers ebp: " + str(e)

    try:
        classeurs = client_instance.clientZeendoc.get_classeurs()
    except:
        classeurs = "Erreur lors de la récupération des classeurs zeendoc"

    print("classeurs", classeurs)

    return render_template(
        "update_client/update_client_p1.html",
        client=client_data,
        client_id=client_id,
        folders=folders,
        classeurs=classeurs,
        client_name=client_instance.username,
    )


@client_bp.route("/launch_routine", methods=["POST"])
@login_required
def launch_routine():
    client_id = request.form.get("client_id")
    client = Client(client_id)
    client.routine()
    return redirect("/")
