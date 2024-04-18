"""
Ce module contient les tests des routes liées à la base de données de l'application.
"""
# permet de désactiver les avertissements inutiles de pylint
# nombre maximum de méthodes autorisées :
# pylint: disable=R0904

from flask_testing import TestCase
from flask_login import login_user
from app import create_app, db
from app.models.user import User
from app.models import database



class TestRoutes(TestCase):
    """
    Classe de test pour les routes liées à la base de données.
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




    def login(self, username, password):
        """
        Fonction de connexion pour les tests
        """

        user = User.query.filter_by(username=username).first()
        if user and user.verify_password(password):
            login_user(user)
            return True
        return False


    def test_drop_table(self):
        """
        Test de la suppression de la table. (à ne pas exécuter si on veut conserver
        les données)
        """
        database.drop_all_tables()


    def test_login(self):
        """
        Teste la route login
        """
        response = self.client.post("/login", data={
            "username": "admin",
            "password": "admin"
        }, follow_redirects=True)


        self.assertEqual(response.status_code, 200)
        self.assertIn('Liste des Clients', response.data.decode())

###### PASSERELLE ######

    def test_get_all_passerelles(self):
        """
        Teste la route get_all_passerelles
        """
        response = self.client.get("/database/passerelle")
        self.assertEqual(response.status_code, 200)
        self.assertIn('[', response.data.decode())


    def test_get_passerelle_by_id(self):
        """
        Teste la route get_passerelle_by_id
        """
        # ajout d'une passerelle
        database.add_passerelle("passerelle1")

        response = self.client.get("/database/passerelle/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn('1', response.data.decode())

        # suppression de la passerelle
        database.delete_passerelle(1)


    def test_add_passerelle_json(self):
        """
        Teste la route add_passerelle avec des données JSON
        """
        response = self.client.post("/database/passerelle", json={"lib_passerelle": "passerelle1"})
        self.assertEqual(response.status_code, 200)


        # vérification de l'ajout de la passerelle
        passerelle = database.get_passerelle_by_id(1)
        self.assertIsNotNone(passerelle)


        # suppression de la passerelle
        database.delete_passerelle(1)


    def test_add_passerelle_form(self):
        """
        Teste la route add_passerelle avec des données form-data
        """
        response = self.client.post("/database/passerelle", data={"lib_passerelle": "passerelle1"})
        self.assertEqual(response.status_code, 200)


        # vérification de l'ajout de la passerelle
        passerelle = database.get_passerelle_by_id(1)
        self.assertIsNotNone(passerelle)


        # suppression de la passerelle
        database.delete_passerelle(1)


    def test_remove_passerelle(self):
        """
        Teste la route delete_passerelle
        """
        # ajout d'une passerelle
        database.add_passerelle("passerelle1")

        response = self.client.delete("/database/passerelle/1")
        self.assertEqual(response.status_code, 200)


        # vérification de la suppression de la passerelle
        passerelle = database.get_passerelle_by_id(1)
        self.assertIsNone(passerelle)

###### CONNECTEURS ######

    def test_connecteur_source_operations(self):
        """
        Teste les opérations CRUD sur les connecteurs source.
        """
        # ajout d'une passerelle et d'un logiciel
        database.add_passerelle("passerelle1")
        database.add_logiciel("logiciel1")

        # ajout d'un connecteur source
        response = self.client.post(
            "/database/connecteur_source",
            json={"id_passerelle": 1, "id_logiciel": 1})
        self.assertEqual(response.status_code, 200)

        # vérification de l'ajout du connecteur source
        response = self.client.get("/database/connecteur_source/1")
        self.assertEqual(response.status_code, 200)

        # suppression du connecteur source
        self.client.delete("/database/connecteur_source/1")


        # vérification de la suppression du connecteur source
        response = self.client.get("/database/connecteur_source/1")
        self.assertIn("null", response.data.decode())

        # suppression de la passerelle et du logiciel
        database.delete_passerelle(1)
        database.delete_logiciel(1)


    def test_connecteur_destination_operations(self):
        """
        Teste les opérations CRUD sur les connecteurs destination.
        """
        # ajout d'une passerelle et d'un logiciel
        database.add_passerelle("passerelle1")
        database.add_logiciel("logiciel1")

        # ajout d'un connecteur destination
        response = self.client.post(
            "/database/connecteur_destination",
            json={"id_passerelle": 1,
                  "id_logiciel": 1})
        self.assertEqual(response.status_code, 200)

        # vérification de l'ajout du connecteur destination
        response = self.client.get("/database/connecteur_destination/1")
        self.assertEqual(response.status_code, 200)

        # suppression du connecteur destination
        self.client.delete("/database/connecteur_destination/1")


        # vérification de la suppression du connecteur destination
        response = self.client.get("/database/connecteur_destination/1")
        self.assertIn("null", response.data.decode())

        # suppression de la passerelle et du logiciel
        database.delete_passerelle(1)
        database.delete_logiciel(1)

###### CLIENT ######

    def test_get_all_clients(self):
        """
        Teste la route get_all_clients
        """
        response = self.client.get("/database/client")
        self.assertEqual(response.status_code, 200)
        self.assertIn('[', response.data.decode())


    def test_get_client_by_id(self):
        """
        Teste la route get_client_by_id
        """
        # ajout d'un client
        database.add_client("client1")

        response = self.client.get("/database/client/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn('1', response.data.decode())

        # suppression du client
        database.delete_client(1)


    def test_add_client_json(self):
        """
        Teste la route add_client avec des données JSON
        """
        response = self.client.post("/database/client", json={"lib_client": "client1"})
        self.assertEqual(response.status_code, 200)


        # vérification de l'ajout du client
        client = database.get_client_by_id(1)
        self.assertIsNotNone(client)


        # suppression du client
        database.delete_client(1)


    def test_add_client_form(self):
        """
        Teste la route add_client avec des données form-data
        """
        response = self.client.post("/database/client", data={"lib_client": "client1"})
        self.assertEqual(response.status_code, 200)


        # vérification de l'ajout du client
        client = database.get_client_by_id(1)
        self.assertIsNotNone(client)


        # suppression du client
        database.delete_client(1)

###### LOGICIEL ######

    def test_get_all_logiciels(self):
        """
        Teste la route get_all_logiciels
        """
        response = self.client.get("/database/logiciel")
        self.assertEqual(response.status_code, 200)
        self.assertIn('[', response.data.decode())


    def test_get_logiciel_by_id(self):
        """
        Teste la route get_logiciel_by_id
        """
        # ajout d'un logiciel
        database.add_logiciel("logiciel1")

        response = self.client.get("/database/logiciel/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn('1', response.data.decode())

        # suppression du logiciel
        database.delete_logiciel(1)


    def test_add_logiciel_json(self):
        """
        Teste la route add_logiciel avec des données JSON
        """
        response = self.client.post("/database/logiciel", json={"lib_logiciel": "logiciel1"})
        self.assertEqual(response.status_code, 200)


        # vérification de l'ajout du logiciel
        logiciel = database.get_logiciel_by_id(1)
        self.assertIsNotNone(logiciel)


        # suppression du logiciel
        database.delete_logiciel(1)


    def test_add_logiciel_form(self):
        """
        Teste la route add_logiciel avec des données form-data
        """
        response = self.client.post("/database/logiciel", data={"lib_logiciel": "logiciel1"})
        self.assertEqual(response.status_code, 200)


        # vérification de l'ajout du logiciel
        logiciel = database.get_logiciel_by_id(1)
        self.assertIsNotNone(logiciel)


        # suppression du logiciel
        database.delete_logiciel(1)


    def test_remove_logiciel(self):
        """
        Teste la route delete_logiciel
        """
        # ajout d'un logiciel
        database.add_logiciel("logiciel1")

        response = self.client.delete("/database/logiciel/1")
        self.assertEqual(response.status_code, 200)


        # vérification de la suppression du logiciel
        logiciel = database.get_logiciel_by_id(1)
        self.assertIsNone(logiciel)


