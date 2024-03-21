"""
Ce module teste les fonctionnalités de la classe Zeendoc dans l'application.
Il contient des tests qui assurent le bon fonctionnement des interactions avec
l'API Zeendoc et la gestion des clients Zeendoc.
"""

import unittest
from app import create_app
from app.models.zeendoc import Zeendoc

class TestModels(unittest.TestCase):
    """
    Classe de tests pour vérifier le comportement des modèles dans le module Zeendoc.
    """

    def setUp(self):
        """Initialise l'application et le contexte pour les tests."""
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        """Nettoie les ressources après les tests."""
        self.app_context.pop()

    def test_zeendoc(self):
        """
        Teste la récupération et la connexion d'un client Zeendoc.
        Vérifie que les méthodes de récupération des droits et des classeurs fonctionnent.
        """
        zeendoc = Zeendoc(1)
        zeendoc.BdGetClientZeendoc(1)
        zeendoc.login()

        self.assertIsNotNone(zeendoc.getright())
        self.assertIsNotNone(zeendoc)

    def test_get_classeurs(self):
        """
        Teste la récupération des classeurs depuis Zeendoc.
        Assure que l'utilisateur Zeendoc peut accéder à ses classeurs.
        """
        zeendoc = Zeendoc(1)
        zeendoc.BdGetClientZeendoc(1)
        zeendoc.login()

        self.assertIsNotNone(zeendoc.get_classeurs())

if __name__ == "__main__":
    unittest.main()
