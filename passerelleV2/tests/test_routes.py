from flask_testing import TestCase
from app import create_app

class TestRoutes(TestCase):
    def create_app(self):
        # Configurez votre application Flask pour les tests
        app = create_app()
        app.config['TESTING'] = True
        return app

    def test_index_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Liste des Clients', response.data.decode())
        
    def test_get_classeurs_zendoc_route(self):
        response = self.client.get('/get_classeurs_zeendoc?id=1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Index', response.data.decode())
        
    def test_get_index_zeendoc_route(self):
        response = self.client.get('/get_index_zeendoc?id=1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('select', response.data.decode())
        
        
    def test_404_route(self):
        response = self.client.get('/testpage')
        self.assertEqual(response.status_code, 404)
        self.assertIn('Erreur 404', response.data.decode())
        
        
    def test_form_update_client_route(self):
        response = self.client.get('/form_update_client?client_id=1')
        self.assertEqual(response.status_code, 200)
        
        # afficher les variables du response
        print(response)
        
        
        # self.assertIn('Modification de', response.data.decode())
        
        
    def test_clients_route(self):
        response = self.client.get('/clients')
        print(response)




if __name__ == '__main__':
    import unittest
    unittest.main()
