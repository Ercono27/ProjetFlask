from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SECRET_KEY'] = '3ad8697643cdf6bd212258ffd836b27f'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://Anonyme:1234@localhost/Projet'
db = SQLAlchemy(app)
from . import routes
