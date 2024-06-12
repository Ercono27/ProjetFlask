from . import app, db
from flask_sqlalchemy import SQLAlchemy

class vue_produits_cat_marque(db.Model):
    id_produit = db.Column(db.Integer, primary_key=True)
    nom_produit = db.Column(db.String(25), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(300), nullable=False)
    id_categorie = db.Column(db.Integer, db.ForeignKey('categorie.id_categorie'), nullable=False)
    nom_categorie = db.Column(db.String(30), nullable=False)
    id_marque = db.Column(db.Integer, db.ForeignKey('marque.id_marque'), nullable=False)
    nom_marque = db.Column(db.String(30), nullable=False)

class Categorie(db.Model):
    __tablename__ = 'categorie'
    id_categorie = db.Column(db.Integer, primary_key=True)
    nom_categorie = db.Column(db.String(30), nullable=False)
    image= db.Column(db.String(300), nullable=False)

class Marque(db.Model):
    __tablename__ = 'marque'
    id_marque = db.Column(db.Integer, primary_key=True)
    nom_marque = db.Column(db.String(30), nullable=False)
    image = db.Column(db.String(300), nullable=False)

class Produit(db.Model):
    __tablename__ = 'produit'
    id_produit = db.Column(db.Integer, primary_key=True)
    nom_produit = db.Column(db.String(25), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    id_categorie = db.Column(db.Integer, db.ForeignKey('categorie.id_categorie'), nullable=False)
    id_marque = db.Column(db.Integer, db.ForeignKey('marque.id_marque'), nullable=False)
    image = db.Column(db.String(300), nullable=False)
    description= db.Column(db.String(300), nullable=False)

