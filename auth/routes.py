from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import User, db

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        # Buscar usuario por email
        user = User.query.filter_by(username=username).first()

        # Verificar usuario y contraseña
        if user and user.password == password:

            # Guardar información del usuario en la sesión
            session['user_id'] = user.id
            session['username'] = user.username

            flash(f'Bienvenido, {user.username}!', 'success')

            return redirect(url_for('tickets.home'))

        flash('Correo o contraseña incorrectos.', 'error')

    return render_template('login.html')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        # Verificar si ya existe el correo
        existing_username = User.query.filter_by(username=username).first()

        if existing_username:
            flash('El username ya está registrado.', 'warning')
            return render_template('register.html')

        # Crear usuario
        new_user = User(
            username=username,
            password=password
        )

        # Guardar usuario
        db.session.add(new_user)
        db.session.commit()

        flash(
            'Usuario registrado correctamente. Ahora puedes iniciar sesión.',
            'success'
        )

        return redirect(url_for('auth.login'))

    return render_template('register.html')

@auth_bp.route('/logout') 
def logout(): # Eliminar los datos de la sesión 
    session.pop("user_id", None)
    flash('Has cerrado sesión correctamente.', 'success') 
    return redirect(url_for('auth.login'))
