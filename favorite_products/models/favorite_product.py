from odoo import models, fields, api
from odoo.exceptions import UserError

class FavoriteProduct(models.Model):
    _name = 'favorite.product'
    _description = 'Produits Favoris'

    user_id = fields.Many2one(
        'res.users',
        string='Utilisateur',
        required=True,
        default=lambda self: self.env.user
    )
    product_tmpl_id = fields.Many2one(
        'product.template',
        string='Produit',
        required=True
    )

    list_price = fields.Float(related='product_tmpl_id.list_price', string='Prix', store=True)
    categ_id = fields.Many2one(related='product_tmpl_id.categ_id', string='Catégorie', store=True)
    image_1920 = fields.Binary(related='product_tmpl_id.image_1920', string='Image', store=True)
    name = fields.Char(related='product_tmpl_id.name', string='Nom du Produit', store=True)
    product_id = fields.Integer(related='product_tmpl_id.id', string='ID du Produit', store=True)

    _sql_constraints = [
        ('user_product_unique', 'unique(user_id, product_tmpl_id)', 'Ce produit est déjà dans vos favoris.')
    ]


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_favorite = fields.Boolean(string='Favori', compute='_compute_is_favorite', store=True)

    #@api.depends('product_variant_ids')
    
    def _compute_is_favorite(self):
        user = self.env.user
        # Si l'utilisateur est un administrateur, on lui donne accès à tous les produits favoris
        if user.has_group('base.group_system'):
            # L'administrateur peut voir tous les produits favoris de tous les utilisateurs
            favorite_product_ids = self.env['favorite.product'].search([]).mapped('product_tmpl_id.id')
        else:
            # Autre utilisateur : on ne voit que ses propres favoris
            favorite_product_ids = self.env['favorite.product'].search([
                ('user_id', '=', user.id)
            ]).mapped('product_tmpl_id.id')

        # Marquer chaque produit comme favori ou non
        for product in self:
            product.is_favorite = product.id in favorite_product_ids

    def add_to_favorites(self):
        for product in self:
            existing = self.env['favorite.product'].search_count([
                ('user_id', '=', self.env.user.id),
                ('product_tmpl_id', '=', product.id)
            ])
            if existing:
                raise UserError("Ce produit est déjà dans vos favoris.")
            self.env['favorite.product'].create({
                'user_id': self.env.user.id,
                'product_tmpl_id': product.id
            })
            product.is_favorite = True
        return True

    def remove_from_favorites(self):
        for product in self:
            favorite_product = self.env['favorite.product'].search([
                ('user_id', '=', self.env.user.id),
                ('product_tmpl_id', '=', product.id)
            ])
            if favorite_product:
                favorite_product.unlink()
                product.is_favorite = False
        return True

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        args = args or []
        if name:
            args += [('name', operator, name)]
        return super(ProductTemplate, self).name_search(name, args, operator, limit)
