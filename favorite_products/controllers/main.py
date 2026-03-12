from odoo import http
from odoo.http import request

#Déclaration du contrôleur
class FavoriteProductPortal(http.Controller):

#Affichage des favoris

    @http.route('/my/favorites', type='http', auth='user', website=True)
    def portal_my_favorites(self, **kwargs):
        user = request.env.user

        # Envoie directement les objets favoris (recordsets)
        favorites = request.env['favorite.product'].sudo().search([('user_id', '=', user.id)])

        # Récupération de tous les produits pour le formulaire d'ajout
        all_products = request.env['product.template'].sudo().search([])

        return request.render('favorite_products.portal_favorite_products', {
            'favorites': favorites,
            'products': all_products,
        })

#ajout  des favoris
    @http.route('/my/favorites/add', type='http', auth='user', website=True, methods=['POST'])
    def add_to_favorites(self, product_id, **kwargs):
        product = request.env['product.template'].sudo().browse(int(product_id))
        if product.exists():
            product.add_to_favorites()
        return request.redirect('/my/favorites')
    
#suppression des favoris
    @http.route('/my/favorites/remove', type='http', auth='user', website=True, methods=['POST'])
    def remove_from_favorites(self, product_id, **kwargs):
        product = request.env['product.template'].sudo().browse(int(product_id))
        if product.exists():
            product.remove_from_favorites()
        return request.redirect('/my/favorites')
    
    
    # -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# Contrôleur : Gestion des Produits Favoris via le Portail Utilisateur
# -------------------------------------------------------------------------
# Ce fichier définit un contrôleur web personnalisé dans Odoo pour gérer
# l’affichage, l’ajout et la suppression des produits favoris d’un utilisateur.
# Il s’agit d’une interface côté portail (accessible via /my/favorites).
#
# Trois routes sont définies :
#
# 1. /my/favorites (GET)
#    - Affiche la liste des produits ajoutés en favoris par l’utilisateur connecté.
#    - Affiche également tous les produits disponibles afin d’en ajouter d’autres.
#
# 2. /my/favorites/add (POST)
#    - Permet à l’utilisateur d’ajouter un produit à ses favoris.
#    - Utilise la méthode add_to_favorites() du modèle product.template.
#
# 3. /my/favorites/remove (POST)
#    - Permet à l’utilisateur de retirer un produit de ses favoris.
#    - Utilise la méthode remove_from_favorites() du modèle product.template.
#
# Ce contrôleur repose sur deux modèles :
# - favorite.product : modèle personnalisé qui stocke les favoris (lié à un utilisateur et un produit).
# - product.template : modèle standard des produits dans Odoo, étendu avec des fonctionnalités de favoris.
#
# Le rendu HTML utilise un template défini dans favorite_products.portal_favorite_products.
# -------------------------------------------------------------------------

