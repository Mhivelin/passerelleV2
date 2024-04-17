import unittest
from app import create_app
from app.models import database

class TestModels(unittest.TestCase):
    """
    A test case class for testing the models in the database module.
    """

    def setUp(self):
        """
        Set up the application context and initialize the database before each test.
        """
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        database.create_database()

    def tearDown(self):
        """
        Tear down the application context after each test.
        """
        self.app_context.pop()


    # def test_drop_table(self):
    #     """
    #     Test the dropping of a table.
    #     """
    #     database.drop_all_tables()



    def test_create_database(self):
        """
        Test the creation of the database.
        """
        database.create_database()
        self.assertIsNotNone(database.get_all_passerelles())

    def test_passerelle_operations(self):
        """
        Test adding, retrieving, and deleting passerelle records.
        """
        database.add_passerelle("passerelle1", 1, 1)
        passerelle = database.get_passerelle_by_id(1)
        self.assertIsNotNone(passerelle)
        database.delete_passerelle(1)
        self.assertIsNone(database.get_passerelle_by_id(1))
        database.drop_table("PASSERELLE")

    def test_api_zeendoc_operations(self):
        """
        Test adding, retrieving, and deleting API Zeendoc records.
        """
        database.add_api_zeendoc(1, 1, "login", "password", "url_client")
        self.assertIsNotNone(database.get_api_zeendoc_by_id(1, 1))
        database.delete_api_zeendoc(1, 1)
        self.assertIsNone(database.get_api_zeendoc_by_id(1, 1))
        database.drop_table("API_ZEENDOC")

    def test_api_ebp_operations(self):
        """
        Test adding, retrieving, and deleting API EBP records.
        """
        database.add_api_ebp(1, 1, "client_id", "client_secret", "subscription_key")
        self.assertIsNotNone(database.get_api_ebp_by_id(1, 1))
        database.delete_api_ebp(1, 1)
        self.assertIsNone(database.get_api_ebp_by_id(1, 1))
        database.drop_table("API_EBP")

    def test_ebp_client_operations(self):
        """
        Test adding, retrieving, and deleting EBP client records.
        """
        # id_logiciel, id_client, id_logiciel_client, folder_id
        database.add_ebp_client(1, 1, 1, 1)
        self.assertIsNotNone(database.get_ebp_client_by_id(1, 1, 1))
        database.delete_ebp_client(1, 1, 1)
        self.assertIsNone(database.get_ebp_client_by_id(1, 1, 1))
        database.drop_table("EBP_CLIENT")
        
    def test_zeendoc_client_operations(self):
        """
        Test adding, retrieving, and deleting Zeendoc client records.
        """
        # id_logiciel, id_client, id_logiciel_client, index_statut_paiement, index_ref_doc, classeur = None,
        database.add_zeendoc_client(1, 1, 1, 1, 1)
        self.assertIsNotNone(database.get_zeendoc_client_by_id(1, 1, 1))
        database.delete_zeendoc_client(1, 1, 1)
        self.assertIsNone(database.get_zeendoc_client_by_id(1, 1, 1))
        database.drop_table("ZEENDOC_CLIENT")
        
        
    def test_client_passerelles_operations(self):
        """
        Test adding, retrieving, and deleting client passerelle records.
        """
        # id_logiciel, id_client, id_logiciel_client, id_passerelle
        database.add_client_passerelle(1, 1, 1, 1)
        self.assertIsNotNone(database.get_client_passerelle_by_id(1, 1, 1, 1))
        database.delete_client_passerelle(1, 1, 1, 1)
        self.assertIsNone(database.get_client_passerelle_by_id(1, 1, 1, 1))
        database.drop_table("CLIENT_PASSERELLE")
        
    def test_logiciel_operations(self):
        """
        Test adding, retrieving, and deleting logiciel records.
        """
        database.add_logiciel("logiciel1")
        self.assertIsNotNone(database.get_logiciel_by_id(1))
        database.delete_logiciel(1)
        self.assertIsNone(database.get_logiciel_by_id(1))
        database.drop_table("LOGICIEL")
        
        
    def test_logiciel_ebp_client_operations(self):
        """
        Test adding, retrieving, and deleting logiciel ebp client records.
        """
        # id_logiciel, id_client, id_logiciel_client
        database.add_logiciel_ebp_client(1, 1, 1)
        self.assertIsNotNone(database.get_logiciel_ebp_client_by_id(1, 1, 1))
        database.delete_logiciel_ebp_client(1, 1, 1)
        self.assertIsNone(database.get_logiciel_ebp_client_by_id(1, 1, 1))
        database.drop_table("LOGICIEL_EBP_CLIENT")
        
    def test_logiciel_zeendoc_client_operations(self):
        """
        Test adding, retrieving, and deleting logiciel zeendoc client records.
        """
        # id_logiciel, id_client, id_logiciel_client
        database.add_logiciel_zeendoc_client(1, 1, 1)
        self.assertIsNotNone(database.get_logiciel_zeendoc_client_by_id(1, 1, 1))
        database.delete_logiciel_zeendoc_client(1, 1, 1)
        self.assertIsNone(database.get_logiciel_zeendoc_client_by_id(1, 1, 1))
        database.drop_table("LOGICIEL_ZEENDOC_CLIENT")
        
    def test_api_ebp_operations(self):
        """
        Test adding, retrieving, and deleting logiciel api ebp records.
        """
        # id_logiciel, id_api, client_id, client_secret, subscription_key, token=None
        database.add_api_ebp(1, 1, "client_id", "client_secret", "subscription_key")
        self.assertIsNotNone(database.get_api_ebp_by_id(1, 1))
        database.delete_api_ebp(1, 1)
        self.assertIsNone(database.get_api_ebp_by_id(1, 1))
        database.drop_table("LOGICIEL_API_EBP")
        
    def test_api_zeendoc_operations(self):
        """
        Test adding, retrieving, and deleting logiciel api zeendoc records.
        """
        # id_logiciel, id_api, login, password, url_client, token=None
        database.add_api_zeendoc(1, 1, "login", "password", "url_client")
        self.assertIsNotNone(database.get_api_zeendoc_by_id(1, 1))
        database.delete_api_zeendoc(1, 1)
        self.assertIsNone(database.get_api_zeendoc_by_id(1, 1))
        database.drop_table("LOGICIEL_API_ZEENDOC")

    def test_get_all_client_passerelles_by_id_client(self):
        """
        Test getting all client passerelles by id client.
        """
        database.add_client_passerelle(1, 1, 1, 1)
        self.assertIsNotNone(database.get_all_client_passerelles_by_id_client(1))
        database.drop_table("CLIENT_PASSERELLE")




    if __name__ == "__main__":
        unittest.main()
