from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_hashing import Hashing

app = Flask(__name__)
# Secret key will protect against modifying cookies or cross-site request forgery attacks
app.config['SECRET_KEY'] = '6b7e7f17628fb3d6ecf968aedec3e844'
# Create a configuration of database by providing SQLAlchemy the path URI of the database.
# We're using SQLite for developement, and migrate to Postgres in production.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
hashing = Hashing(app)

from flaskblog import routes