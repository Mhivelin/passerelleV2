"""
Controlleur pour les routes des vue liées aux clients
"""

from flask import Blueprint, render_template
from flask_login import login_required
from app.models import database


v_client_bp = Blueprint("v_client", __name__)

@v_client_bp.route("/form_add_client", methods=["GET"])
@login_required
def form_add_client():
    """Route pour afficher le formulaire d'ajout d'un client"""
    return render_template("client/add_client.html")


@v_client_bp.route("/fill_requiert/<int:id_client>", methods=["GET"])
@login_required
def form_add_multiple_requiert(id_client):
    """Route pour afficher le formulaire d'ajout de plusieurs clients"""
    fields = database.get_champ_by_client(id_client)
    return render_template("client/add_multiple_requiert.html", fields=fields, id_client=id_client)
