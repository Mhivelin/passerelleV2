import logging
from flask import Flask, render_template
from flask_login import LoginManager
from werkzeug.security import generate_password_hash
from app.extensions import db
from app.models.user import User

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
    app.config["SECRET_KEY"] = "deltictmp"
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = "main.login"
    login_manager.init_app(app)

    app.logger.setLevel(logging.DEBUG)

    with app.app_context():
        db.create_all()
        if not User.query.filter_by(username="admin").first():
            new_user = User(username="admin", password=generate_password_hash("admin"))
            db.session.add(new_user)
            db.session.commit()

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    app.register_error_handler(404, lambda error: (render_template("error/404.html"), 404))
    app.register_error_handler(500, lambda error: (render_template("error/500.html"), 500))

    from app.controllers.client_controller import client_bp
    from app.controllers.ebp_controller import ebp_bp
    from app.controllers.main_controller import main_bp
    from app.controllers.zeendoc_controller import zeendoc_bp
    from app.controllers.database_controller import database_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(client_bp)
    app.register_blueprint(ebp_bp)
    app.register_blueprint(zeendoc_bp)
    app.register_blueprint(database_bp)

    return app
