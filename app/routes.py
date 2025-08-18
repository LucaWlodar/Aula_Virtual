from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db, login_manager
from app.models import Usuario, Curso, Contenido, Evaluacion
from app.forms import LoginForm, RegistroForm, CursoForm, ContenidoForm, EvaluacionForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form.email.data).first()
        if usuario and usuario.password == form.password.data:
            login_user(usuario)
            return redirect(url_for('dashboard'))
        flash('Credenciales incorrectas')
    return render_template('login.html', form=form)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    form = RegistroForm()
    if form.validate_on_submit():
        usuario = Usuario(nombre=form.nombre.data, email=form.email.data, password=form.password.data, rol=form.rol.data)
        db.session.add(usuario)
        db.session.commit()
        flash('Registro exitoso')
        return redirect(url_for('login'))
    return render_template('registro.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.rol == 'profesor':
        cursos = Curso.query.filter_by(profesor_id=current_user.id).all()
    else:
        cursos = current_user.cursos_inscritos
    return render_template('dashboard.html', cursos=cursos)

# ... (agrega más rutas para gestión de cursos, contenidos, evaluaciones)
