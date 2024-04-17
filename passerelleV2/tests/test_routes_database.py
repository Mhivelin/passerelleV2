from app import create_app, db
from flask_testing import TestCase
from flask_login import login_user, FlaskLoginClient, current_user
from app.models.user import User
from app.models import database



class TestRoutes(TestCase):
    
    
    
    
    def create_app(self):
        app = create_app()
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  
        app.config["LOGIN_DISABLED"] = False
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.test_client_class = FlaskLoginClient
        return app


    def setUp(self):
        super().setUp()
        self.app = self.create_app()
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()
            user = User(username='admin')
            user.set_password('admin')
            db.session.add(user)
            db.session.commit()

    def tearDown(self):
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



    def test_login(self):
        """
        Test the login route.
        """
        response = self.client.post("/login", data={
            "username": "admin",
            "password": "admin"
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Logged in successfully.', response.data.decode())  # Example of checking response text




    # def test_add_passerelle(self):
    #     """
    #     Test adding a passerelle and check redirection output.
    #     """
    #     with self.client:
    #         self.login("admin", "admin")  
    #         response = self.client.put("/add_passerelle", json={
    #             "lib_passerelle": "passerelle1",
    #             "id_logiciel": 1,
    #             "id_logiciel_1": 1
    #         }, follow_redirects=True, headers={"Content-Type": "application/json"})
            
    #         print("response.data add_passerelle :")
    #         print(response.data)
            
            
            
    #         self.assertEqual(response.status_code, 201)
            
    #         response = self.client.get("/get_passerelle_by_id/1", follow_redirects=True)
            
    #         print("response.data get_passerelle_by_id/1")
    #         print(response.data)