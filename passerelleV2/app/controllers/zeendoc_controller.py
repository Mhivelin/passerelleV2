from flask import jsonify, request, redirect, Blueprint
# from app.models.database import get_db_connection
from app.models.zeendoc import Zeendoc
from flask import render_template
from flask_login import login_required



# Création d'un Blueprint pour le zeendoc controller
zeendoc_bp = Blueprint('zeendoc', __name__)



@zeendoc_bp.route('/get_classeurs_zeendoc', methods=['GET'])
@login_required
def get_classeurs_zendoc():

    # Récupérer l'identifiant du client à partir des paramètres de l'URL
    client_id = request.args.get('id')
    client = Zeendoc(client_id)
    
    
    return jsonify(client.right['Collections'])


# Route qui recupere les index d'un client avec son id et son classeur
@zeendoc_bp.route('/get_index_zeendoc', methods=['GET'])
@login_required
def get_index_zeendoc():

    # Récupérer l'identifiant du client à partir des paramètres de l'URL
    client_id = request.args.get('id')
    client = Zeendoc(client_id)
    
    index = client.getIndex()
    
    
    return render_template('dropdown.html', index=index)


@zeendoc_bp.route('/set_coll_Zeendoc', methods=['POST'])
@login_required
def set_coll_Zeendoc():
    
    print(request.get_json())
    data = request.get_json()
    client_id = data.get('id')
    classeur = data.get('classeur')
        
    client = Zeendoc(client_id)
    client.setClasseur(classeur)
    
    return jsonify({'message': 'Classeur Zeendoc mis à jour avec succès'})