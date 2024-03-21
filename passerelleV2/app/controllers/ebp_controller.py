import os

# from app.models.database import get_db_connection
from app.models.ebp import EBP
from dotenv import find_dotenv, load_dotenv
from flask import Blueprint, jsonify, redirect, request, session, url_for
from flask_login import login_required
from requests_oauthlib import OAuth2Session

# Création d'un Blueprint pour le ebp controller
ebp_bp = Blueprint("ebp", __name__)


@ebp_bp.route("/get_folders_ebp", methods=["GET"])
@login_required
def get_folder_ebp():
    client_id = request.args.get("id")
    client = EBP(client_id)

    return jsonify({"folder_id": client.get_folders()})


@ebp_bp.route("/set_folder_ebp", methods=["POST"])
@login_required
def set_folder_ebp():
    data = request.get_json()
    client_id = data.get("id")
    folder_id = data.get("folder")

    print(data)

    client = EBP(client_id)
    client.setFolder(folder_id)

    return jsonify({"message": "Dossier EBP mis à jour avec succès"})


@ebp_bp.route("/login_ebp", methods=["GET"])
@login_required
def login_ebp():

    print("login_ebp")

    session.clear()
    # créer une variable d'environnement .env
    load_dotenv(find_dotenv())

    # afficher tout les arguments de la requête
    print(request.args)

    # récupérer l'id du client
    id = request.args.get("id")

    os.environ["id"] = str(id)

    with open(".env", "w") as f:
        f.write("id=" + str(id))

    client = EBP(id)
    # redirect_uri avec l'id du client
    redirect_uri = url_for("ebp.SinginRedirect", _external=True)
    authorization_base_url = "https://api-login.ebp.com/connect/authorize"
    scope = ["openid", "profile", "offline_access"]
    client_id = client.client_id

    oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)

    # Récupérez l'URL de redirection
    authorization_url, state = oauth.authorization_url(authorization_base_url)

    print(authorization_url)

    # Rediriger l'utilisateur vers l'URL de connexion
    return redirect(authorization_url)


@ebp_bp.route("/SinginRedirect", methods=["GET"])
def SinginRedirect():
    print("redirection reçue")

    code = request.args.get("code")
    id = os.environ.get("id")

    instance_client_ebp = EBP(id)
    instance_client_ebp.callback(code)

    # Rediriger l'utilisateur vers la page de mise à jour du client avec client_id en paramètre GET
    return redirect(url_for("client.form_update_client", client_id=id))
