from app.extensions import db
from app.models import database
from app.models.user import User
from flask import Blueprint, redirect, render_template, request, url_for, flash
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

# Création d'un Blueprint pour le main controller
main_bp = Blueprint("main", __name__)

# db


# Route pour la page d'accueil
@main_bp.route("/")
@login_required
def home():

    clients = database.get_all_clients()

    return render_template("clients.html", clients=clients)


# Route pour une page à propos (exemple)


@main_bp.route("/documentation")
def documentation():
    return render_template("documentation.html")


@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.verify_password(password):
            login_user(user)
            flash('Logged in successfully.')
            return redirect(url_for('main.index')) 
        else:
            flash('Invalid username or password.')
            return redirect(url_for('main.login')) 
    return render_template('login.html')  


@main_bp.route("/register", methods=["GET", "POST"])
# @login_required
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        new_user = User(username=username)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("main.login"))
    return render_template("register.html")


@main_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.login"))
