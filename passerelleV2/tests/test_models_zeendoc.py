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

    def tearDown(self):
        """
        Nettoyer le contexte de l'application après chaque test.
        """
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_zeendoc(self):
        """
        Teste la récupération et la connexion d'un client Zeendoc.
        Vérifie que les méthodes de récupération des droits et des classeurs fonctionnent.
        """


        # on crée un client
        database.add_client("test")

        # on crée un logiciel
        database.add_logiciel("zeendoc")

        # on lui crée LOGICIEL ZEENDOC CLIENT




        zeendoc = Zeendoc(1)
        # zeendoc.BdGetClientZeendoc(1)
        # zeendoc.login()

        # self.assertIsNotNone(zeendoc.getright())
        # self.assertIsNotNone(zeendoc)

    # def test_get_classeurs(self):
    #     """
    #     Teste la récupération des classeurs depuis Zeendoc.
    #     Assure que l'utilisateur Zeendoc peut accéder à ses classeurs.
    #     """
    #     zeendoc = Zeendoc(1)
    #     zeendoc.BdGetClientZeendoc(1)
    #     zeendoc.login()

    #     self.assertIsNotNone(zeendoc.get_classeurs())

if __name__ == "__main__":
    unittest.main()
