"""
Ce module teste les fonctionnalités de la classe Zeendoc dans l'application.
Il contient des tests qui assurent le bon fonctionnement des interactions avec
l'API Zeendoc et la gestion des clients Zeendoc.
"""

import unittest
from app import create_app, db
from app.models.zeendoc import Zeendoc
from app.models import database


class TestModels(unittest.TestCase):
    """
    Classe de tests pour vérifier le comportement des modèles dans le module Zeendoc.
    """

    def create_app(self):
        """
        Créer une instance de l'application pour les tests.
        """
        app = create_app()
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False  # Désactiver CSRF pour les tests
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
        database.create_database()
        return app



    def setUp(self):
        """
        mettre en place le contexte de l'application avant chaque test.
        """
        super().setUp()
        self.app = self.create_app()
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()
            self.client.post('/login', data={"username": "admin", "password": "admin"})


        # Creation d'un client et d'un logiciel pour les tests
        # on crée un client
        database.add_client("test")

        # on crée un logiciel
        database.add_logiciel("zeendoc")

        # on lui crée LOGICIEL ZEENDOC CLIENT

        #id_logiciel, id_client, id_logiciel_client, login, password, url_client
        database.add_logiciel_zeendoc_client(1, 1, "tests_webservices@zeendoc.com", "tests01", "tests_webservices")

        # initialisation de la classe zeendoc
        self.zeendoc = Zeendoc(1)


    def tearDown(self):
        """
        Nettoyer le contexte de l'application après chaque test.
        """
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

        # on efface les données
        database.delete_client(1)
        database.delete_logiciel(1)
        database.delete_logiciel_client(1)
        database.delete_logiciel_zeendoc_client(1)


    # def test_drop_table(self):
    #     """
    #     Test de la suppression de la table. (à ne pas exécuter si on veut conserver
    #     les données)
    #     """
    #     database.drop_all_tables()







    def test_zeendoc_login(self):
        """
        Teste la connexion à l'API Zeendoc.
        """

        co = self.zeendoc.login()

        self.assertIn('Result":0,"Cookie_Duration":"38880s","Error_Msg":""', co)




    def test_zeendoc_get_rights(self):
        """
        Teste la récupération des droits d'un utilisateur Zeendoc.
        """

        rights = self.zeendoc.get_rights()

        self.assertEqual(rights['Result'], 0)



    def test_zeendoc_get_classeurs(self):
        """
        Teste la récupération des classeurs d'un utilisateur Zeendoc.
        """

        classeurs = self.zeendoc.get_classeurs()

        self.assertIsNotNone(classeurs)



if __name__ == "__main__":
    unittest.main()
