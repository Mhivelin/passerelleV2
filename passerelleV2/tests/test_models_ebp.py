import unittest
from app import create_app
from app.models.ebp import EBP

class TestModels(unittest.TestCase):
    """
    Classe de cas de test pour vérifier le bon fonctionnement des modèles relatifs à EBP.
    """

    def setUp(self):
        """
        Initialise l'application et le contexte avant chaque test.
        """
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        """
        Nettoie le contexte après chaque test.
        """
        self.app_context.pop()

    def test_get_folders(self):
        """
        Teste la récupération des dossiers depuis l'instance EBP.
        """
        ebp = EBP(1)
        ebp.BdGetClientEBP(1)
        ebp.login()

        folders = ebp.get_folders()
        print(folders)

        self.assertIsNotNone(folders)

    def test_get_suppliers(self):
        """
        Teste la récupération des fournisseurs depuis l'instance EBP.
        """
        ebp = EBP(1)
        ebp.BdGetClientEBP(1)
        ebp.login()

        suppliers = ebp.get_suppliers()
        print(suppliers)

        self.assertIsNotNone(suppliers)

if __name__ == "__main__":
    unittest.main()
