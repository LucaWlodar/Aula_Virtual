from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from .config import Config

# Inicializar extensiones
db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones con la app
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    # Configuración de Flask-Login
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Por favor, inicia sesión para acceder a esta página.'
    login_manager.login_message_category = 'info'

    # Importar y registrar blueprints
    from .routes import main_bp
    app.register_blueprint(main_bp)

    # Importar modelos para crear tablas (si es necesario)
    with app.app_context():
        from . import models
        db.create_all()

    return app
