from flask import jsonify, request, redirect, Blueprint
from app.models import database
from flask_login import login_required


# Création d'un Blueprint pour le ebp controller
database_bp = Blueprint( database , __name__ )


@database_bp.route('/get_passerelles', methods=['GET'] )
@login_required
def get_passerelles():
    passerelles = database.get_all_passerelles
    
    return jsonify( { 'passerelles': passerelles } )


@database_bp.route("/add_passerelle", methods=["POST" ] )
@login_required
def  add_passerelle() : 
    data = request.get_json()
    
    libelle = data["libelle"]
    description = data["description"]
    
    database.add_passerelle(libelle, description)
    
    return redirect("/")

    
    
    
    
    
    
    
