"""
Ce module contient les routes pour les différentes entités de la base de données.
"""



from app.models import database
from flask import Blueprint, jsonify, request, redirect, url_for
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


@database_bp.route("/database/passerelle_with_connectors", methods=["POST"])
@login_required
def add_passerelle_with_connectors():
    """
    Ajoute une passerelle à la base de données avec un connecteur source et un connecteur destination.
    """
    # obtenir les données de la requête (soit en JSON, soit en form-data)
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form

    # ajouter la passerelle
    result = database.add_passerelle_with_connectors(
        data["lib_passerelle"],
        data["id_logiciel_source"],
        data["id_logiciel_destination"]
    )
    return redirect(url_for("main.home"))



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

@database_bp.route(
    "/database/connecteur_destination/<int:connecteur_destination_id>",
    methods=["GET"])
@login_required
def get_connecteur_destination_by_id(connecteur_destination_id):
    """
    Obtient un connecteur destination par son ID.
    """
    connecteur_destination = database.get_connecteur_destination_by_id(connecteur_destination_id)
    return jsonify(connecteur_destination)

@database_bp.route(
    "/database/connecteur_destination/<int:connecteur_destination_id>",
    methods=["DELETE"])
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
    return redirect(url_for("main.home"))


@database_bp.route("/database/client/<int:client_id>", methods=["DELETE"])
@login_required
def delete_client(client_id):
    """
    Supprime un client de la base de données.
    """
    result = database.delete_client(client_id)
    print("result: ", result)
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


###################################################################################################
#                                   LOGICIEL CLIENT                                              #
###################################################################################################

@database_bp.route("/database/logiciel_client", methods=["GET"])
@login_required
def get_all_logiciels_client():
    """
    Obtient tous les logiciels client de la base de données.
    """
    logiciels_client = database.get_all_logiciels_client()
    return jsonify(logiciels_client)


@database_bp.route("/database/logiciel_client/<int:logiciel_client_id>", methods=["GET"])
@login_required
def get_logiciel_client_by_id(logiciel_client_id):
    """
    Obtient un logiciel client par son ID.
    """
    logiciel_client = database.get_logiciel_client_by_id(logiciel_client_id)
    return jsonify(logiciel_client)


@database_bp.route("/database/logiciel_client", methods=["POST"])
@login_required
def add_logiciel_client():
    """
    Ajoute un logiciel client à la base de données.
    """
    # obtenir les données de la requête (soit en JSON, soit en form-data)
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form

    # ajouter le logiciel client
    result = database.add_logiciel_client(data["id_logiciel"], data["id_client"])
    return jsonify(result)











###################################################################################################
#                                   LOGICIEL EBP CLIENT                                           #
###################################################################################################

@database_bp.route("/database/logiciel_ebp_client", methods=["GET"])
@login_required
def get_all_logiciels_ebp_client():
    """
    Obtient tous les logiciels ebp client de la base de données.
    """
    logiciels_ebp_client = database.get_all_logiciels_ebp_client()
    return jsonify(logiciels_ebp_client)


@database_bp.route("/database/logiciel_ebp_client/<int:logiciel_ebp_client_id>", methods=["GET"])
@login_required
def get_logiciel_ebp_client_by_id(logiciel_ebp_client_id):
    """
    Obtient un logiciel ebp client par son ID.
    """
    logiciel_ebp_client = database.get_logiciel_ebp_client_by_id(logiciel_ebp_client_id)
    return jsonify(logiciel_ebp_client)


@database_bp.route("/database/logiciel_ebp_client", methods=["POST"])
@login_required
def add_logiciel_ebp_client():
    """
    Ajoute un logiciel ebp client à la base de données.
    """
    # obtenir les données de la requête (soit en JSON, soit en form-data)
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form

    # ajouter le logiciel ebp client
    result = database.add_logiciel_ebp_client(data["id_logiciel"], data["id_client"])
    return jsonify(result)


@database_bp.route("/database/logiciel_ebp_client/<int:logiciel_ebp_client_id>", methods=["DELETE"])
@login_required
def delete_logiciel_ebp_client(logiciel_ebp_client_id):
    """
    Supprime un logiciel ebp client de la base de données.
    """
    result = database.delete_logiciel_ebp_client(logiciel_ebp_client_id)
    return jsonify(result)


###################################################################################################
#                                   LOGICIEL ZEENDOC CLIENT                                       #
###################################################################################################

@database_bp.route("/database/logiciel_zeendoc_client", methods=["GET"])
@login_required
def get_all_logiciels_zeendoc_client():
    """
    Obtient tous les logiciels zeendoc client de la base de données.
    """
    logiciels_zeendoc_client = database.get_all_logiciels_zeendoc_client()
    return jsonify(logiciels_zeendoc_client)


@database_bp.route(
    "/database/logiciel_zeendoc_client/<int:logiciel_zeendoc_client_id>",
    methods=["GET"])
@login_required
def get_logiciel_zeendoc_client_by_id(logiciel_zeendoc_client_id):
    """
    Obtient un logiciel zeendoc client par son ID.
    """
    logiciel_zeendoc_client = database.get_logiciel_zeendoc_client_by_id(logiciel_zeendoc_client_id)
    return jsonify(logiciel_zeendoc_client)


@database_bp.route("/database/logiciel_zeendoc_client", methods=["POST"])
@login_required
def add_logiciel_zeendoc_client():
    """
    Ajoute un logiciel zeendoc client à la base de données.
    """
    # obtenir les données de la requête (soit en JSON, soit en form-data)
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form

    # ajouter le logiciel zeendoc client
    result = database.add_logiciel_zeendoc_client(data["idLogicielClient"], data["Login"], data["Password"], data["UrlClient"])
    return jsonify(result)


@database_bp.route(
    "/database/logiciel_zeendoc_client/<int:logiciel_zeendoc_client_id>",
    methods=["DELETE"])
@login_required
def delete_logiciel_zeendoc_client(logiciel_zeendoc_client_id):
    """
    Supprime un logiciel zeendoc client de la base de données.
    """
    result = database.delete_logiciel_zeendoc_client(logiciel_zeendoc_client_id)
    return jsonify(result)


###################################################################################################
#                                   CLIENT PASSERELLE                                            #
###################################################################################################

@database_bp.route("/database/client_passerelle", methods=["GET"])
@login_required
def get_all_clients_passerelle():
    """
    Obtient tous les clients passerelle de la base de données.
    """
    clients_passerelle = database.get_all_clients_passerelle()
    return jsonify(clients_passerelle)


@database_bp.route("/database/client_passerelle/<int:client_passerelle_id>", methods=["GET"])
@login_required
def get_client_passerelle_by_id(client_passerelle_id):
    """
    Obtient un client passerelle par son ID.
    """
    client_passerelle = database.get_client_passerelle_by_id(client_passerelle_id)
    return jsonify(client_passerelle)


@database_bp.route("/database/client_passerelle", methods=["POST"])
@login_required
def add_client_passerelle():
    """
    Ajoute un client passerelle à la base de données.
    """
    # obtenir les données de la requête (soit en JSON, soit en form-data)
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form

    # ajouter le client passerelle
    result = database.add_client_passerelle(data["id_client"], data["id_passerelle"])
    return redirect(url_for("main.home"))


@database_bp.route("/database/client_passerelle/<int:id_client>/<int:id_passerelle>", methods=["DELETE"])
@login_required
def delete_client_passerelle(id_client, id_passerelle):
    """
    Supprime un client passerelle de la base de données.
    """
    result = database.delete_client_passerelle(id_client, id_passerelle)
    return jsonify(result)




