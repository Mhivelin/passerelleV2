# from app.models.user import User
import logging

from app.extensions import db
from app.models.user import User
from flask import Flask, render_template
from flask_login import LoginManager
from werkzeug.security import generate_password_hash

# from random import randint


def create_app():
    app = Flask(__name__)

    # Configurer la base de données
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////app/data/db.sqlite'

    # Configurez ici la clé secrète et d'autres configurations
    app.config["SECRET_KEY"] = "deltictmp"

    db.init_app(app)

    with app.app_context():
        db.create_all()

        # Configurer le niveau de log à DEBUG
        app.logger.setLevel(logging.DEBUG)

        # Initialiser Flask-Login
        login_manager = LoginManager()
        login_manager.login_view = "main.login"
        login_manager.init_app(app)

        if not User.query.filter_by(username="admin").first():

            password = "admin"
            new_user = User(username="admin",
                            password=generate_password_hash(password))

            db.session.add(new_user)
            db.session.commit()

        @login_manager.user_loader
        def load_user(user_id):
            # User est votre modèle d'utilisateur
            return User.query.get(int(user_id))

            # Potentiellement, gestion des erreurs 404, 500, etc.

        @app.errorhandler(404)
        def page_not_found(error):
            return render_template("error/404.html"), 404

        @app.errorhandler(500)
        def internal_server_error(error):
            return render_template("error/500.html"), 500

        with app.app_context():
            # Importer les Blueprints des contrôleurs
            from app.controllers.client_controller import client_bp
            from app.controllers.ebp_controller import ebp_bp
            from app.controllers.main_controller import main_bp
            from app.controllers.zeendoc_controller import zeendoc_bp
            from app.controllers.database_controller import database_bp

            # Enregistrer les Blueprints
            app.register_blueprint(main_bp)
            app.register_blueprint(client_bp)
            app.register_blueprint(ebp_bp)
            app.register_blueprint(zeendoc_bp)
            app.register_blueprint(database_bp)







            return app



