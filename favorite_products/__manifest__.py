# -*- coding: utf-8 -*-
{
    'name': "Gestion des Produits Favoris",
    'version': '17.0.0.1',
    'author': "khaoula",
    'category': 'E-commerce',
    'summary': "Module permettant aux utilisateurs d'ajouter, afficher et supprimer des produits favoris.",
    'description': """
        Ce module permet aux utilisateurs d'ajouter des produits à leur liste de favoris,
        de les afficher et de les supprimer. Utile pour les boutiques en ligne ou les gestionnaires de stock.
    """,
    'depends': ['base', 'product'],  # Ajout de 'product' pour la gestion des produits
    'data': [
    'security/ir.model.access.csv',  # Gestion des permissions
    'views/favorite_product_views.xml',  # Vue des favoris
    'data/favorite_product.xml',  # Définition du modèle
    'views/menu.xml',
    'views/portal_templates.xml',
    'views/portal_menu.xml',
    'views/favorite_product_portal_views.xml',
    'views/favorite_product_templates.xml',
],
    'images': ['static/description/icone.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}



# Le fichier __manifest__.py est un fichier de configuration essentiel pour le module Odoo. 
# Il contient des informations clés qui permettent à Odoo de reconnaître et de gérer le module correctement. 
# Les principales informations incluent :
# - 'name' : Le nom du module, affiché dans l'interface d'Odoo.
# - 'version' : La version actuelle du module.
# - 'author' : L'auteur du module.
# - 'category' : La catégorie à laquelle le module appartient dans Odoo.
# - 'summary' : Un résumé bref des fonctionnalités du module.
# - 'description' : Une explication détaillée de ce que fait le module.
# - 'depends' : Les modules dont dépend ce module pour fonctionner.
# - 'data' : La liste des fichiers XML, CSV, et autres à charger lors de l'installation du module.
# - 'images' : L'icône du module à afficher dans l'interface Odoo.
# - 'installable' : Indique si le module est installable.
# - 'application' : Définit si le module est une application complète dans Odoo.
# - 'auto_install' : Définit si le module s'installe automatiquement ou manuellement.

