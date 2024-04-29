"""
Ce fichier contient les tests unitaires pour faire des tests d'insertion dans la base de données.
"""



import unittest
from app import create_app
from app.models import database

class TestModels(unittest.TestCase):
    """
    CLasse de test pour les opérations de la base de données.
    """

    def setUp(self):
        """
        mettre en place le contexte de l'application avant chaque test.
        """
        # Créer une instance de l'application
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

        # Créer la base de données
        database.create_database()

    def tearDown(self):
        """
        Nettoyer le contexte de l'application après chaque test.
        """
        self.app_context.pop()


    # def test_drop_table(self):
    #     """
    #     Test de la suppression de la table. (à ne pas exécuter si on veut conserver
    #     les données)
    #     """
    #     database.drop_all_tables()

    def test_ajout_manuel(self):
        """
        Test d'ajout manuel des informations dans la base de données.
        """

        # ajout des logicels EBP et Zeendoc
        database.add_logiciel("EBP")
        database.add_logiciel("Zeendoc")

        # ajout des champs requis pour les logiciels EBP et Zeendoc
        database.add_champ("EBP_Client_ID", "EBP")
        database.add_champ("EBP_Client_Secret", "EBP")
        database.add_champ("EBP_Subscription_Key", "EBP")

        database.add_champ("Zeendoc_Login", "Zeendoc")
        database.add_champ("Zeendoc_URL_Client", "Zeendoc")
        database.add_champ("Zeendoc_CPassword", "Zeendoc")


        idChamp = database.get_id_champ_by_lib_champ("EBP_Client_ID")
        idLogiciel = database.get_id_logiciel_by_lib_logiciel("EBP")
        database.add_requiert_logiciel(idChamp, idLogiciel)

        idChamp = database.get_id_champ_by_lib_champ("EBP_Client_Secret")
        idLogiciel = database.get_id_logiciel_by_lib_logiciel("EBP")
        database.add_requiert_logiciel(idChamp, idLogiciel)

        idChamp = database.get_id_champ_by_lib_champ("EBP_Subscription_Key")
        idLogiciel = database.get_id_logiciel_by_lib_logiciel("EBP")
        print(idChamp)
        print(idLogiciel)
        database.add_requiert_logiciel(idChamp, idLogiciel)

        idChamp = database.get_id_champ_by_lib_champ("Zeendoc_Login")
        idLogiciel = database.get_id_logiciel_by_lib_logiciel("Zeendoc")
        database.add_requiert_logiciel(idChamp, idLogiciel)

        idChamp = database.get_id_champ_by_lib_champ("Zeendoc_URL_Client")
        idLogiciel = database.get_id_logiciel_by_lib_logiciel("Zeendoc")
        database.add_requiert_logiciel(idChamp, idLogiciel)

        idChamp = database.get_id_champ_by_lib_champ("Zeendoc_CPassword")
        idLogiciel = database.get_id_logiciel_by_lib_logiciel("Zeendoc")

        database.add_requiert_logiciel(idChamp, idLogiciel)

        # ajout des passerelles
        lsource = database.get_id_logiciel_by_lib_logiciel("EBP")
        ldestination = database.get_id_logiciel_by_lib_logiciel("Zeendoc")
        database.add_passerelle_with_connectors("remontée de paiement", lsource, ldestination)

        # ajout des champs requis pour les passerelles
        database.add_champ("EBP_FOLDER_ID", "remontée de paiement")
        database.add_champ("Zeendoc_CLASSEUR", "remontée de paiement")

        idChamp = database.get_id_champ_by_lib_champ("EBP_FOLDER_ID")
        idPasserelle = database.get_id_passerelle_by_lib_passerelle("remontée de paiement")
        print("idPasserelle")
        print(idPasserelle)
        database.add_requiert_passerelle(idChamp, idPasserelle)

        idChamp = database.get_id_champ_by_lib_champ("Zeendoc_CLASSEUR")
        idPasserelle = database.get_id_passerelle_by_lib_passerelle("remontée de paiement")
        print("idPasserelle")
        print(idPasserelle)
        database.add_requiert_passerelle(idChamp, idPasserelle)

