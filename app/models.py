from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    rol = db.Column(db.String(20), nullable=False)  # 'estudiante' o 'profesor'

    def __repr__(self):
        return f'<Usuario {self.nombre}>'

class Curso(db.Model):
    __tablename__ = 'cursos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)
    profesor_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    profesor = db.relationship('Usuario', backref='cursos_impartidos')

    def __repr__(self):
        return f'<Curso {self.nombre}>'

class Contenido(db.Model):
    __tablename__ = 'contenidos'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    archivo = db.Column(db.String(200), nullable=False)
    curso_id = db.Column(db.Integer, db.ForeignKey('cursos.id'))
    curso = db.relationship('Curso', backref='contenidos')

    def __repr__(self):
        return f'<Contenido {self.titulo}>'

class Evaluacion(db.Model):
    __tablename__ = 'evaluaciones'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)
    curso_id = db.Column(db.Integer, db.ForeignKey('cursos.id'))
    curso = db.relationship('Curso', backref='evaluaciones')

    def __repr__(self):
        return f'<Evaluacion {self.titulo}>'
