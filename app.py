import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from extensions import db, migrate, jwt
from applications import user


load_dotenv(os.path.join(os.path.expanduser('/Users/sjahn/workspace/sjahn.pythonanywhere.com'), '.env'))

def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv('SECRET_KEY')
    app.config['JSON_SORT_KEYS'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{0}:{1}@{2}/{3}?charset=utf8'.format(
        os.getenv('DB_USER'),
        os.getenv('DB_PASSWORD'),
        os.getenv('DB_HOST'),
        os.getenv('DB_NAME')
    )
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')  # Change this!
    app.config['JWT_TOKEN_LOCATION'] = ['headers'] # headers', 'cookies', 'query_string', 'json'
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    register_blueprints(app)
    return app

def register_blueprints(app):
    app.register_blueprint(user.web.blueprint)
    app.register_blueprint(user.api.blueprint)

app = create_app()

@app.route('/')
def index():
    return render_template('main/index.html')