from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
from app.models import database
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user import User
from app.extensions import db

# Création d'un Blueprint pour le main controller
main_bp = Blueprint('main', __name__)


# db


# Route pour la page d'accueil
@main_bp.route('/')
@login_required
def home():
  
    clients = database.get_all_clients()
    
    
    return render_template('clients.html' , clients = clients)

# Route pour une page à propos (exemple)
@main_bp.route('/documentation')
def documentation():
    return render_template('documentation.html')






@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('main.home'))
        
        
        
        
    return render_template('login.html')
            
            
@main_bp.route('/register', methods=['GET', 'POST'])
#@login_required
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        new_user = User(username=username)
        new_user.set_password(password)
        
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('main.login'))
    return render_template('register.html')




@main_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))