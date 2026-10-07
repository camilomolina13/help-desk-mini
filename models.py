from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    #Accede a los tickets
    tickets = db.relationship('Ticket', backref='user')
    def __repr__(self):
        return f"<User {self.id}: {self.username}, Password : {self.password}> "

class Ticket(db.Model):
    __tablename__ = 'ticket'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    status = db.Column(
        db.Enum("Abierto", "En progreso", "Cerrado"),
        nullable=False,
        default="Abierto"
    )   
    #Para acceder al usuario
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self):
        return f"<Note {self.id}: {self.title}>"