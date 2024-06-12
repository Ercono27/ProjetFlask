from flask import render_template, url_for, redirect, request, flash
from . import app, models
from .models import Produit


@app.route('/')
@app.route('/accueil')
def accueil():
    produits = models.vue_produits_cat_marque.query.all()
    return render_template('accueil.html', title='Bienvenue sur LCLD', produits=produits)


@app.route('/tous_produits')
def tous_produits():
    liste_produits = models.vue_produits_cat_marque.query.all()
    return render_template('tous_produits.html', title='Nos produits', liste_prod=liste_produits)


@app.route('/categories')
def categories():
    liste_categories = models.Categorie.query.distinct('nom_categorie')
    return render_template('categories.html', title='Nos categories', liste=type(liste_categories),
                           liste_cat=liste_categories)


@app.route('/marques')
def marques():
    liste_marques = models.Marque.query.distinct('nom_marque')
    return render_template('marques.html', title='Nos Marques', liste=type(liste_marques), liste_marques=liste_marques)


@app.route('/produits_categories')
def produits_categories():
    id_categorie = request.args.get('id_categories')
    liste_produits = models.vue_produits_cat_marque.query.filter_by(id_categorie=id_categorie)
    return render_template('produits_categorie.html', title='Nos produits', produits=liste_produits,
                           typeprod=type(liste_produits))


@app.route('/produits_marques')
def produits_marques():
    id_marque = request.args.get('id_marques')
    liste_produits = models.vue_produits_cat_marque.query.filter_by(id_marque=id_marque)
    return render_template('produits_marque.html', title='Nos produits', produits=liste_produits,
                           typeprod=type(liste_produits))


@app.route('/produit')
def produit():
    id_produit = request.args.get('id_produit')
    produit = models.Produit.query.filter_by(id_produit=id_produit).first()
    if produit:
        title = produit.nom_produit
        return render_template('produit.html', title=title, produit=produit)
    else:
        flash("Produit non trouvé", "error")
        return redirect(url_for('accueil'))
