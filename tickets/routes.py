from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import Ticket, User, db

tickets_bp = Blueprint('tickets', __name__)

@tickets_bp.route('/')
def home():

    # Verificar si el usuario inició sesión
    if 'user_id' not in session:
        flash('Debes iniciar sesión para acceder a los tickets.', 'warning')
        return redirect(url_for('auth.login'))

    tickets = Ticket.query.all()
    # users = User.query.all()

    return render_template(
        'home.html',
        tickets=tickets,
    )

@tickets_bp.route('/create', methods=['GET', 'POST'])
def create_ticket():

    # Verificar sesión
    if 'user_id' not in session:
        flash('Debes iniciar sesión para crear una nota.', 'warning')
        return redirect(url_for('auth.login'))

    if request.method == 'POST':

        title = request.form['title'].strip()
        description = request.form['description'].strip()


        # Validar longitud del título
        if len(title) < 10:
            flash('El título es muy corto. Mínimo 10 caracteres.', 'error')
            return render_template('create_.html')

        # Validar longitud del contenido
        if len(description) < 50:
            flash('El contenido es muy corto. Mínimo 50 caracteres.', 'error')
            return render_template('create_ticket.html')

        # Crear la nota solamente si las validaciones son correctas
        new_ticket = Ticket(
            title = title,
            description = description,
            user_id = 1
        )

        db.session.add(new_ticket)
        db.session.commit()

        flash('Ticket creado correctamente.', 'success')

        return redirect(url_for('tickets.home'))

    return render_template('create_ticket.html')


@tickets_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_ticket(id):
    if 'user_id' not in session:
            flash('Debes iniciar sesión para eliminar una nota.', 'warning')
            return redirect(url_for('auth.login'))
    ticket = Ticket.query.get_or_404(id)

    statuses = ["Abierto", "En progreso", "Cerrado"]

    if request.method == 'POST':
        title = request.form['title'].strip()
        description = request.form['description'].strip()
        status = request.form['status']

        if len(title) < 10:
            flash('El título es muy corto. Mínimo 10 caracteres.', 'error')
            return render_template(
                'edit_ticket.html',
                ticket=ticket,
                statuses=statuses
            )

        if len(description) < 50:
            flash('La descripción es muy corta. Mínimo 50 caracteres.', 'error')
            return render_template(
                'edit_ticket.html',
                ticket=ticket,
                statuses=statuses
            )

        ticket.title = title
        ticket.description = description
        ticket.status = status

        db.session.commit()

        flash('Ticket actualizado correctamente.', 'success')

        return redirect(url_for('tickets.home'))

    return render_template(
        'edit_ticket.html',
        ticket=ticket,
        statuses=statuses
    )


@tickets_bp.route('/delete/<int:id>', methods=['POST'])
def delete_ticket(id):

    # Verificar sesión
    if 'user_id' not in session:
        flash('Debes iniciar sesión para eliminar una nota.', 'warning')
        return redirect(url_for('auth.login'))

    ticket = Ticket.query.get_or_404(id)

    db.session.delete(ticket)
    db.session.commit()

    flash('Ticket eliminado correctamente.', 'success')

    return redirect(url_for('tickets.home'))