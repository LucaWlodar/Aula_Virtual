from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])

class RegistroForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    rol = SelectField('Rol', choices=[('estudiante', 'Estudiante'), ('profesor', 'Profesor')], validators=[DataRequired()])

class CursoForm(FlaskForm):
    nombre = StringField('Nombre del curso', validators=[DataRequired()])
    descripcion = TextAreaField('Descripción')

class ContenidoForm(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired()])
    archivo = StringField('Archivo', validators=[DataRequired()])

class EvaluacionForm(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired()])
    descripcion = TextAreaField('Descripción')
