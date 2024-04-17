##############################################################################################
# Description: Script permettant d'ajouter manuellement les informations de la base de données
##############################################################################################

import app.models.database as db

# ajout des logicels EBP et Zeendoc
db.add_logiciel("EBP")
db.add_logiciel("Zeendoc")
