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
        self.assertIsNotNone(database.get_passerelle_by_id(1))
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

    # Continue with similar structured test methods for the remaining functions...

    if __name__ == "__main__":
        unittest.main()
