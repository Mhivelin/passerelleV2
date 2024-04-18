"""

"""



from app.models import database
from flask import Blueprint, jsonify, request
from flask_login import login_required

# Création d'un Blueprint pour le ebp controller
database_bp = Blueprint("database", __name__)



###################################################################################################
#                                        PASSERELLE                                              #
###################################################################################################

@database_bp.route("/database/passerelle", methods=["GET"])
@login_required
def get_all_passerelles():
    """
    Obtient toutes les passerelles de la base de données.
    """
    passerelles = database.get_all_passerelles()
    return jsonify(passerelles)


@database_bp.route("/database/passerelle/<int:passerelle_id>", methods=["GET"])
@login_required
def get_passerelle_by_id(passerelle_id):
    """
    Obtient une passerelle par son ID.
    """
    passerelle = database.get_passerelle_by_id(passerelle_id)
    return jsonify(passerelle)


@database_bp.route("/database/passerelle", methods=["POST"])
@login_required
def add_passerelle():
    """
    Ajoute une passerelle à la base de données.
    """
    # obtenir les données de la requête (soit en JSON, soit en form-data)
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form

    # ajouter la passerelle
    result = database.add_passerelle(data["lib_passerelle"])
    return jsonify(result)


@database_bp.route("/database/passerelle/<int:passerelle_id>", methods=["DELETE"])
@login_required
def delete_passerelle(passerelle_id):
    """
    Supprime une passerelle de la base de données.
    """
    result = database.delete_passerelle(passerelle_id)
    return jsonify(result)



###################################################################################################
#                                        CONNECTEURS                                              #
###################################################################################################

#### CONNECTEUR SOURCE ####

@database_bp.route("/database/connecteur_source", methods=["GET"])
@login_required
def get_all_connecteurs_source():
    """
    Obtient tous les connecteurs source de la base de données.
    """
    connecteurs_source = database.get_all_connecteurs_source()
    return jsonify(connecteurs_source)



@database_bp.route("/database/connecteur_source", methods=["POST"])
@login_required
def add_connecteur_source():
    """
    Ajoute un connecteur source à la base de données.
    """
    # obtenir les données de la requête (soit en JSON, soit en form-data)
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form

    # ajouter le connecteur source
    # add_connecteur_source(passerelle_id, logiciel_id):
    result = database.add_connecteur_source(data["id_passerelle"], data["id_logiciel"])
    return jsonify(result)

@database_bp.route("/database/connecteur_source/<int:connecteur_source_id>", methods=["GET"])
@login_required
def get_connecteur_source_by_id(connecteur_source_id):
    """
    Obtient un connecteur source par son ID.
    """
    connecteur_source = database.get_connecteur_source_by_id(connecteur_source_id)
    return jsonify(connecteur_source)


@database_bp.route("/database/connecteur_source/<int:connecteur_source_id>", methods=["DELETE"])
@login_required
def delete_connecteur_source(connecteur_source_id):
    """
    Supprime un connecteur source de la base de données.
    """
    result = database.delete_connecteur_source(connecteur_source_id)
    return jsonify(result)



#### CONNECTEUR DESTINATION ####


@database_bp.route("/database/connecteur_destination", methods=["GET"])
@login_required
def get_all_connecteurs_destination():
    """
    Obtient tous les connecteurs destination de la base de données.
    """
    connecteurs_destination = database.get_all_connecteurs_destination()
    return jsonify(connecteurs_destination)



@database_bp.route("/database/connecteur_destination", methods=["POST"])
@login_required
def add_connecteur_destination():
    """
    Ajoute un connecteur destination à la base de données.
    """
    # obtenir les données de la requête (soit en JSON, soit en form-data)
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form

    # ajouter le connecteur destination
    result = database.add_connecteur_destination(data["id_passerelle"], data["id_logiciel"])
    return jsonify(result)

@database_bp.route("/database/connecteur_destination/<int:connecteur_destination_id>", methods=["GET"])
@login_required
def get_connecteur_destination_by_id(connecteur_destination_id):
    """
    Obtient un connecteur destination par son ID.
    """
    connecteur_destination = database.get_connecteur_destination_by_id(connecteur_destination_id)
    return jsonify(connecteur_destination)

@database_bp.route("/database/connecteur_destination/<int:connecteur_destination_id>", methods=["DELETE"])
@login_required
def delete_connecteur_destination(connecteur_destination_id):
    """
    Supprime un connecteur destination de la base de données.
    """
    result = database.delete_connecteur_destination(connecteur_destination_id)
    return jsonify(result)


###################################################################################################
#                                        CLIENT                                                   #
###################################################################################################

@database_bp.route("/database/client", methods=["GET"])
@login_required
def get_all_clients():
    """
    Obtient tous les clients de la base de données.
    """
    clients = database.get_all_clients()
    return jsonify(clients)


@database_bp.route("/database/client/<int:client_id>", methods=["GET"])
@login_required
def get_client_by_id(client_id):
    """
    Obtient un client par son ID.
    """
    client = database.get_client_by_id(client_id)
    return jsonify(client)


@database_bp.route("/database/client", methods=["POST"])
@login_required
def add_client():
    """
    Ajoute un client à la base de données.
    """
    # obtenir les données de la requête (soit en JSON, soit en form-data)
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form

    # ajouter le client
    result = database.add_client(data["lib_client"])
    return jsonify(result)


@database_bp.route("/database/client/<int:client_id>", methods=["DELETE"])
@login_required
def delete_client(client_id):
    """
    Supprime un client de la base de données.
    """
    result = database.delete_client(client_id)
    return jsonify(result)


###################################################################################################
#                                        LOGICIEL                                                 #
###################################################################################################

@database_bp.route("/database/logiciel", methods=["GET"])
@login_required
def get_all_logiciels():
    """
    Obtient tous les logiciels de la base de données.
    """
    logiciels = database.get_all_logiciels()
    return jsonify(logiciels)


@database_bp.route("/database/logiciel/<int:logiciel_id>", methods=["GET"])
@login_required
def get_logiciel_by_id(logiciel_id):
    """
    Obtient un logiciel par son ID.
    """
    logiciel = database.get_logiciel_by_id(logiciel_id)
    return jsonify(logiciel)


@database_bp.route("/database/logiciel", methods=["POST"])
@login_required
def add_logiciel():
    """
    Ajoute un logiciel à la base de données.
    """
    # obtenir les données de la requête (soit en JSON, soit en form-data)
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form

    # ajouter le logiciel
    result = database.add_logiciel(data["lib_logiciel"])
    return jsonify(result)


@database_bp.route("/database/logiciel/<int:logiciel_id>", methods=["DELETE"])
@login_required
def delete_logiciel(logiciel_id):
    """
    Supprime un logiciel de la base de données.
    """
    result = database.delete_logiciel(logiciel_id)
    return jsonify(result)

