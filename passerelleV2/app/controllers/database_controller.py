from app.models import database
from flask import Blueprint, jsonify, redirect, request
from flask_login import login_required

# Création d'un Blueprint pour le ebp controller
database_bp = Blueprint("database", __name__)



# def row_to_json(row):
#     """
#     Convert a row to a JSON object.
#     """
#     res = dict(row)
#     return jsonify(res)




################################################################################################################################
#                                                     PASSERELLE                                                              #
################################################################################################################################


@database_bp.route("/get_all_passerelles", methods=["GET"])
@login_required
def get_all_passerelles():
    """
    Get all passerelles.
    """
    return jsonify(database.get_all_passerelles())

@database_bp.route("/get_passerelle_by_id/<int:id>", methods=["GET"])
@login_required
def get_passerelle_by_id(id):
    result = database.get_passerelle_by_id(id)
    if not result:
        return jsonify({}), 404  # Ou retournez une réponse appropriée si l'ID n'est pas trouvé
    
    
    print("result get_passerelle_by_id : ", result)
    
    return result


@database_bp.route("/add_passerelle", methods=["PUT"])
@login_required
def add_passerelle():

    data = request.get_json()
    database.add_passerelle(data["lib_passerelle"], data["id_logiciel"], data["id_logiciel_1"])
    return "Passerelle ajoutée avec succès", 201




@database_bp.route("/delete_passerelle/<int:id>", methods=["DELETE"])
@login_required
def delete_passerelle(id):
    """
    Delete passerelle.
    """
    database.delete_passerelle(id)
    return "Passerelle supprimée avec succès", 200





################################################################################################################################
#                                                     EBP CLIENT                                                              #
################################################################################################################################


@database_bp.route("/get_all_ebp_clients", methods=["GET"])
@login_required
def get_all_ebp_clients():
    """
    Get all ebp clients.
    """
    return jsonify(database.get_all_ebp_clients())

@database_bp.route("/get_ebp_client_by_id/<int:id_logiciel>/<int:id_client>/<int:id_logiciel_client>", methods=["GET"])
@login_required
def get_ebp_client_by_id(id_logiciel, id_client, id_logiciel_client):
    """
    Get ebp client by id.
    """
    return jsonify(database.get_ebp_client_by_id(id_logiciel, id_client, id_logiciel_client))


@database_bp.route("/add_ebp_client", methods=["PUT"])
@login_required
def add_ebp_client():
    """
    Add ebp client.
    """
    database.add_ebp_client(request.args.get("id_client"), request.args.get("id_logiciel"), request.args.get("id_logiciel_client"))
    return "Client EBP ajouté avec succès", 201

@database_bp.route("/delete_ebp_client", methods=["DELETE"])
@login_required
def delete_ebp_client():
    """
    Delete ebp client.
    """
    database.delete_ebp_client(request.args.get("id"))
    return redirect("/get_all_ebp_clients")



################################################################################################################################
#                                                     ZEENDOC CLIENT                                                          #
################################################################################################################################


@database_bp.route("/get_all_zeendoc_clients", methods=["GET"])
@login_required
def get_all_zeendoc_clients():
    """
    Get all zeendoc clients.
    """
    return jsonify(database.get_all_zeendoc_clients())

@database_bp.route("/get_zeendoc_client_by_id", methods=["GET"])
@login_required
def get_zeendoc_client_by_id():
    """
    Get zeendoc client by id.
    """
    return jsonify(database.get_zeendoc_client_by_id(request.args.get("id")))


################################################################################################################################
#                                                     CLIENT PASSERELLE                                                        #
################################################################################################################################


@database_bp.route("/get_all_client_passerelles", methods=["GET"])
@login_required
def get_all_client_passerelles():
    """
    Get all client passerelles.
    """
    return jsonify(database.get_all_client_passerelles())

@database_bp.route("/get_client_passerelle_by_id", methods=["GET"])
@login_required
def get_client_passerelle_by_id():
    """
    Get client passerelle by id.
    """
    return jsonify(database.get_client_passerelle_by_id(request.args.get("id")))

@database_bp.route("/add_client_passerelle", methods=["PUT"])
@login_required
def add_client_passerelle():
    """
    Add client passerelle.
    """
    database.add_client_passerelle(request.args.get("id_logiciel"), request.args.get("id_client"), request.args.get("id_logiciel_client"), request.args.get("id_passerelle"))
    return redirect("/get_all_client_passerelles")

@database_bp.route("/delete_client_passerelle", methods=["DELETE"])
@login_required
def delete_client_passerelle():
    """
    Delete client passerelle.
    """
    database.delete_client_passerelle(request.args.get("id"))
    return redirect("/get_all_client_passerelles")


################################################################################################################################
#                                                     LOGICIEL                                                                #
################################################################################################################################


@database_bp.route("/get_all_logiciels", methods=["GET"])
@login_required
def get_all_logiciels():
    """
    Get all logiciels.
    """
    return jsonify(database.get_all_logiciels())

@database_bp.route("/get_logiciel_by_id", methods=["GET"])
@login_required
def get_logiciel_by_id():
    """
    Get logiciel by id.
    """
    return jsonify(database.get_logiciel_by_id(request.args.get("id")))

@database_bp.route("/add_logiciel", methods=["PUT"])
@login_required
def add_logiciel():
    """
    Add logiciel.
    """
    database.add_logiciel(request.args.get("nom"))
    return redirect("/get_all_logiciels")

@database_bp.route("/delete_logiciel", methods=["DELETE"])
@login_required
def delete_logiciel():
    """
    Delete logiciel.
    """
    database.delete_logiciel(request.args.get("id"))
    return redirect("/get_all_logiciels")



################################################################################################################################
#                                                LOGICIEL EBP CLIENT                                                           #
################################################################################################################################


@database_bp.route("/get_all_logiciel_ebp_clients", methods=["GET"])
@login_required
def get_all_logiciel_ebp_clients():
    """
    Get all logiciel ebp clients.
    """
    return jsonify(database.get_all_logiciel_ebp_clients())

@database_bp.route("/get_logiciel_ebp_client_by_id", methods=["GET"])
@login_required
def get_logiciel_ebp_client_by_id():
    """
    Get logiciel ebp client by id.
    """
    return jsonify(database.get_logiciel_ebp_client_by_id(request.args.get("id")))

@database_bp.route("/add_logiciel_ebp_client", methods=["PUT"])
@login_required
def add_logiciel_ebp_client():
    """
    Add logiciel ebp client.
    """
    database.add_logiciel_ebp_client(request.args.get("id_logiciel"), request.args.get("id_client"), request.args.get("id_logiciel_client"))
    return redirect("/get_all_logiciel_ebp_clients")

@database_bp.route("/delete_logiciel_ebp_client", methods=["DELETE"])
@login_required
def delete_logiciel_ebp_client():
    """
    Delete logiciel ebp client.
    """
    database.delete_logiciel_ebp_client(request.args.get("id"))
    return redirect("/get_all_logiciel_ebp_clients")

################################################################################################################################
#                                             LOGICIEL ZEENDOC CLIENT                                                          #
################################################################################################################################


@database_bp.route("/get_all_logiciel_zeendoc_clients", methods=["GET"])
@login_required
def get_all_logiciel_zeendoc_clients():
    """
    Get all logiciel zeendoc clients.
    """
    return jsonify(database.get_all_logiciel_zeendoc_clients())

@database_bp.route("/get_logiciel_zeendoc_client_by_id", methods=["GET"])
@login_required
def get_logiciel_zeendoc_client_by_id():
    """
    Get logiciel zeendoc client by id.
    """
    return jsonify(database.get_logiciel_zeendoc_client_by_id(request.args.get("id")))

@database_bp.route("/add_logiciel_zeendoc_client", methods=["PUT"])
@login_required
def add_logiciel_zeendoc_client():
    """
    Add logiciel zeendoc client.
    """
    database.add_logiciel_zeendoc_client(request.args.get("id_logiciel"), request.args.get("id_client"), request.args.get("id_logiciel_client"))
    return redirect("/get_all_logiciel_zeendoc_clients")

@database_bp.route("/delete_logiciel_zeendoc_client", methods=["DELETE"])
@login_required
def delete_logiciel_zeendoc_client():
    """
    Delete logiciel zeendoc client.
    """
    database.delete_logiciel_zeendoc_client(request.args.get("id"))
    return redirect("/get_all_logiciel_zeendoc_clients")

################################################################################################################################
#                                                     API EBP                                                                 #
################################################################################################################################


@database_bp.route("/get_all_api_ebp", methods=["GET"])
@login_required
def get_all_api_ebp():
    """
    Get all api ebp.
    """
    return jsonify(database.get_all_api_ebp())

@database_bp.route("/get_api_ebp_by_id", methods=["GET"])
@login_required
def get_api_ebp_by_id():
    """
    Get api ebp by id.
    """
    return jsonify(database.get_api_ebp_by_id(request.args.get("id")))

@database_bp.route("/add_api_ebp", methods=["PUT"])
@login_required
def add_api_ebp():
    """
    Add api ebp.
    """
    database.add_api_ebp(request.args.get("id_logiciel"), request.args.get("id_api"), request.args.get("client_id"), request.args.get("client_secret"), request.args.get("subscription_key"))
    return redirect("/get_all_api_ebp")

@database_bp.route("/delete_api_ebp", methods=["DELETE"])
@login_required
def delete_api_ebp():
    """
    Delete api ebp.
    """
    database.delete_api_ebp(request.args.get("id"))
    return redirect("/get_all_api_ebp")



################################################################################################################################
#                                                     API ZEENDOC                                                             #
################################################################################################################################


@database_bp.route("/get_all_api_zeendoc", methods=["GET"])
@login_required
def get_all_api_zeendoc():
    """
    Get all api zeendoc.
    """
    return jsonify(database.get_all_api_zeendoc())

@database_bp.route("/get_api_zeendoc_by_id", methods=["GET"])
@login_required
def get_api_zeendoc_by_id():
    """
    Get api zeendoc by id.
    """
    return jsonify(database.get_api_zeendoc_by_id(request.args.get("id")))

@database_bp.route("/add_api_zeendoc", methods=["PUT"])
@login_required
def add_api_zeendoc():
    """
    Add api zeendoc.
    """
    database.add_api_zeendoc(request.args.get("id_logiciel"), request.args.get("id_api"), request.args.get("login"), request.args.get("password"), request.args.get("url_client"))
    return redirect("/get_all_api_zeendoc")

@database_bp.route("/delete_api_zeendoc", methods=["DELETE"])
@login_required
def delete_api_zeendoc():
    """
    Delete api zeendoc.
    """
    database.delete_api_zeendoc(request.args.get("id"))
    return redirect("/get_all_api_zeendoc")



################################################################################################################################
#                                                     Requête plus complexe                                                    #
################################################################################################################################


@database_bp.route("/get_all_client_passerelles_by_id_client", methods=["GET"])
@login_required
def get_all_client_passerelles_by_id_client():
    """
    Get all client passerelles by id client.
    """
    return jsonify(database.get_all_client_passerelles_by_id_client(request.args.get("id_client")))

