import unittest
from app import create_app
from app.models import database


class TestModels(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        database.create_database()

    def tearDown(self):
        self.app_context.pop()

    def test_create_database(self):
        database.create_database()
        data = database.get_all_passerelles()

    def test_PASSERELLE(self):
        database.add_passerelle("passerelle1", 1, 1)

        data = database.get_all_passerelles()
        # print("data get_all_passerelles", data)

        data = database.get_passerelle_by_id(1)
        # print("data get_passerelle_by_id", data)

        database.delete_passerelle(1)
        data = database.get_all_passerelles()
        # print("data get_all_passerelles", data)

        database.drop_table("PASSERELLE")

    def test_API_ZEENDOC(self):
        database.add_api_zeendoc(1, 1, "login", "password", "url_client")
        data = database.get_all_api_zeendoc()
        # print("data get_all_api_zeendoc", data)

        data = database.get_api_zeendoc_by_id(1, 1)
        # print("data get_api_zeendoc_by_id", data)

        database.delete_api_zeendoc(1, 1)
        data = database.get_all_api_zeendoc()
        # print("data get_all_api_zeendoc", data)

        database.drop_table("API_ZEENDOC")

    def test_API_EBP(self):
        database.add_api_ebp(1, 1, 1, "folder_id", "subscription_key")
        data = database.get_all_api_ebp()
        # print("data get_all_api_ebp", data)

        data = database.get_api_ebp_by_id(1, 1)
        # print("data get_api_ebp_by_id", data)

        database.delete_api_ebp(1, 1)

        data = database.get_all_api_ebp()
        # print("data get_all_api_ebp", data)

        database.drop_table("API_EBP")

    def test_EBP_CLIENT(self):
        database.add_ebp_client(1, 1, "client_id", "client_name")
        data = database.get_all_ebp_clients()
        # print("data get_all_ebp_clients", data)

        data = database.get_ebp_client_by_id(1, 1, 1)
        # print("data get_ebp_client_by_id", data)

        database.delete_ebp_client(1, 1, 1)
        data = database.get_all_ebp_clients()
        # print("data get_all_ebp_clients", data)

        database.drop_table("EBP_CLIENT")

    def test_ZEENDOC_CLIENT(self):
        # id_logiciel, id_client, id_logiciel_client, index_statut_paiement, index_ref_doc, classeur
        database.add_zeendoc_client(
            1, 1, 1, "index_statut_paiement", "index_ref_doc", "classeur")
        data = database.get_all_zeendoc_clients()
        # print("data get_all_zeendoc_clients", data)

        data = database.get_zeendoc_client_by_id(1, 1, 1)
        # print("data get_zeendoc_client_by_id", data)

        database.delete_zeendoc_client(1, 1, 1)

        data = database.get_all_zeendoc_clients()
        # print("data get_all_zeendoc_clients", data)

        database.drop_table("ZEENDOC_CLIENT")

    def test_CLIENT_PASSERELLE(self):
        # id_logiciel, id_client, id_logiciel_client, id_passerelle
        database.add_client_passerelle(1, 1, 1, 1)
        data = database.get_all_client_passerelles()
        # print("data get_all_client_passerelles", data)

        data = database.get_client_passerelle_by_id(1, 1, 1, 1)
        # print("data get_client_passerelle_by_id", data)

        database.delete_client_passerelle(1, 1, 1, 1)

        data = database.get_all_client_passerelles()
        # print("data get_all_client_passerelles", data)

        database.drop_table("CLIENT_PASSERELLE")

    def test_LOGICIEL(self):
        database.add_logiciel("logiciel_name")
        data = database.get_all_logiciels()
        # print("data get_all_logiciels", data)

        data = database.get_logiciel_by_id(1)
        # print("data get_logiciel_by_id", data)

        database.delete_logiciel(1)

        data = database.get_all_logiciels()
        # print("data get_all_logiciels", data)

        database.drop_table("LOGICIEL")

    def test_LOGICIEL_EBP_CLIENT(self):
        # id_logiciel, id_client, id_logiciel_client
        database.add_logiciel_ebp_client(1, 1, 1)
        data = database.get_all_logiciel_ebp_clients()
        # print("data get_all_logiciel_ebp_clients", data)

        data = database.get_logiciel_ebp_client_by_id(1, 1, 1)
        # print("data get_logiciel_ebp_client_by_id", data)

        database.delete_logiciel_ebp_client(1, 1, 1)

        data = database.get_all_logiciel_ebp_clients()
        # print("data get_all_logiciel_ebp_clients", data)

        database.drop_table("LOGICIEL_EBP_CLIENT")

    def test_LOGICIEL_ZEENDOC_CLIENT(self):
        # id_logiciel, id_client, id_logiciel_client
        database.add_logiciel_zeendoc_client(1, 1, 1)
        data = database.get_all_logiciel_zeendoc_clients()
        # print("data get_all_logiciel_zeendoc_clients", data)

        data = database.get_logiciel_zeendoc_client_by_id(1, 1, 1)
        # print("data get_logiciel_zeendoc_client_by_id", data)

        database.delete_logiciel_zeendoc_client(1, 1, 1)

        data = database.get_all_logiciel_zeendoc_clients()
        # print("data get_all_logiciel_zeendoc_clients", data)

        database.drop_table("LOGICIEL_ZEENDOC_CLIENT")

    def test_API_EBP(self):
        # id_logiciel, id_api, client_id, client_secret, subscription_key, token = None
        database.add_api_ebp(
            1, 1, "client_id", "client_secret", "subscription_key")
        data = database.get_all_api_ebp()
        # print("data get_all_api_ebp", data)

        data = database.get_api_ebp_by_id(1, 1)
        # print("data get_api_ebp_by_id", data)

        database.delete_api_ebp(1, 1)

        data = database.get_all_api_ebp()
        # print("data get_all_api_ebp", data)

        database.drop_table("API_EBP")

    def test_API_ZEENDOC(self):
        # id_logiciel, id_api, login, password, url_client
        database.add_api_zeendoc(1, 1, "login", "password", "url_client")
        data = database.get_all_api_zeendoc()
        # print("data get_all_api_zeendoc", data)

        data = database.get_api_zeendoc_by_id(1, 1)
        # print("data get_api_zeendoc_by_id", data)

        database.delete_api_zeendoc(1, 1)

        data = database.get_all_api_zeendoc()
        # print("data get_all_api_zeendoc", data)

        database.drop_table("API_ZEENDOC")

    def test_get_all_client_passerelles_by_id_client(self):
        # creation type
        # logiciel
        database.add_logiciel("EBP")
        database.add_logiciel("ZEENDOC")

        # passerelle
        database.add_passerelle("passerelle1", 1, 1)

        # api
        database.add_api_ebp(
            1, 1, "client_id", "client_secret", "subscription_key")
        database.add_api_zeendoc(1, 1, "login", "password", "url_client")

        # client
        database.add_ebp_client(1, 1, "client_id", "client_name")
        database.add_zeendoc_client(
            1, 1, 1, "index_statut_paiement", "index_ref_doc", "classeur")

        # client_passerelle
        database.add_client_passerelle(1, 1, 1, 1)
        database.add_client_passerelle(1, 1, 1, 2)

        # id_client
        data = database.get_all_client_passerelles_by_id_client(1)

        print("data get_all_client_passerelles_by_id_client", data)

        # database.drop_all_tables()

    def test_select_all_from_all_tables(self):

        # # creation type
        # # logiciel
        # database.add_logiciel("EBP")
        # database.add_logiciel("ZEENDOC")

        # # passerelle
        # database.add_passerelle("passerelle1", 1, 1)

        # # api
        # database.add_api_ebp(1, 1, "client_id", "client_secret", "subscription_key")
        # database.add_api_zeendoc(1, 1, "login", "password", "url_client")

        # # client
        # database.add_ebp_client(1, 1, "client_id", "client_name")
        # database.add_zeendoc_client(1, 1, 1, "index_statut_paiement", "index_ref_doc", "classeur")

        # # client_passerelle
        # database.add_client_passerelle(1, 1, 1, 1)
        # database.add_client_passerelle(1, 1, 1, 2)

        data = database.select_all_from_all_tables()
        print("data select_all_from_all_tables", data)

        if __name__ == '__main__':
            unittest.main()
