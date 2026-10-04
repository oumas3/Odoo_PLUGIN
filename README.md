# Favorite Products · Odoo Module

A collaborative Odoo module for saving products to a user's favorites list. It connects a custom ORM model, authenticated HTTP routes, and QWeb templates to provide a French-language portal page for adding, viewing, and removing favorites.

![Python](https://img.shields.io/badge/Python-3D314A?style=flat-square&logo=python&logoColor=FFD9E2)
![Odoo](https://img.shields.io/badge/Odoo-B76E79?style=flat-square&logo=odoo&logoColor=white)
![XML](https://img.shields.io/badge/XML_%2F_QWeb-8E5572?style=flat-square)

**Status:** development prototype. The manifest uses version `17.0.0.1`; installation and multi-user behavior have not been independently verified on a fresh Odoo 17 database. Compatibility with other Odoo versions is not established.

## Implemented features

- A `favorite.product` model linking `res.users` to `product.template`.
- A SQL uniqueness constraint preventing duplicate user/product pairs.
- Product methods for adding and removing the current user's favorites.
- An authenticated `/my/favorites` page with a product selector and favorite cards.
- POST routes for addition and removal, with CSRF tokens in the portal forms.
- A portal-home link and backend action for favorite records.
- Related product fields for names, prices, categories, and images.

These are source-level features, not a claim of a tested deployment or a fully secured permission model. The controllers render HTML and redirect; they are not a JSON REST API.

## Main implementation

| File | Purpose |
| --- | --- |
| [Manifest](favorite_products/__manifest__.py) | Module metadata, dependencies, and XML loading order |
| [Models](favorite_products/models/favorite_product.py) | Favorite records, uniqueness constraint, and product methods |
| [Controller](favorite_products/controllers/main.py) | Authenticated list, add, and remove routes |
| [Active portal template](favorite_products/views/favorite_product_templates.xml) | Favorite cards and forms rendered by `/my/favorites` |
| [Portal navigation](favorite_products/views/portal_menu.xml) | Link from the portal home page |
| [Backend menu](favorite_products/views/menu.xml) | Action opening `favorite.product` records |
| [Access permissions](favorite_products/security/ir.model.access.csv) | Model-level access declarations |

The controller filters the favorites page by the current user's ID. This filter applies to that route; it does not replace ownership record rules for other ORM access paths.

## Setup for evaluation

Use a disposable development database with an existing Odoo server. This repository is an add-on, not a standalone Python application.

1. Clone the repository onto the Odoo server:

   ```bash
   git clone https://github.com/oumas3/Odoo_PLUGIN.git
   ```

2. Append the **absolute path to `Odoo_PLUGIN`**, which contains the `favorite_products` folder, to your existing `addons_path`. Preserve the paths already configured for Odoo's standard add-ons.
3. Prepare the portal, website/eCommerce, and stock features before evaluating the module. The current manifest declares only `base` and `product`, but templates reference `portal.portal_my_home`, `portal.portal_layout`, `website.layout`, stock quantity `qty_available`, and shop URLs. These undeclared dependencies need reconciliation for a reliable installation.
4. Restart Odoo, enable developer mode, and use **Apps → Update Apps List**.
5. Search for the manifest's display name **Gestion des Produits Favoris**, or its technical name **favorite_products**, and install it in the development database.

This procedure matches the repository layout and Odoo's module-discovery workflow. Installation remains unverified; it is not a guaranteed clean-server setup. See [Odoo 17's app/module instructions](https://www.odoo.com/documentation/17.0/applications/general/apps_modules.html).

## Trying the portal

After a successful installation:

1. Create or select a product and sign in with a test user.
2. Open `/my/favorites` on your local Odoo instance.
3. Select a product and submit **Ajouter aux favoris**.
4. Check that the product appears, then use **Supprimer** to remove it.

The intended result is one favorite record per user/product pair. Portal cards display a product image when available, price, stock quantity, and a shop link. The price suffix is currently hard-coded as euros.

## Verification and known gaps

Python syntax and XML well-formedness can be checked without running Odoo. Those checks do not validate view inheritance, module installation, access control, or portal behavior. No automated Odoo tests or CI workflow were found in the inspected repository.

Before treating this module as ready for deployment:

- **Restrict record access:** the group-less ACL grants read/write/create/delete access, and no ownership record rules are supplied. The separate portal read-only ACL does not cancel the broader grant.
- **Review elevated access:** portal routes use `sudo()`, and the product selector searches all product templates without publication or company filters. Product visibility and permitted actions need explicit checks.
- **Correct favorite-state handling:** `is_favorite` is a stored field derived from the current user, without declared recomputation dependencies. One shared product field cannot reliably represent each user's state.
- **Declare dependencies and validate views:** reconcile portal/website/stock requirements; check portal XPath inheritance and backend button visibility on the intended Odoo version.
- **Validate requests:** handle malformed product IDs and duplicate additions with clear responses.
- **Align metadata:** the manifest references `static/description/icone.png`, while the committed image is `icon.png`. Python bytecode caches are also tracked.

A useful acceptance check is to test two independent users: add the same product for both, remove it for one, and confirm the other user's favorite and displayed state remain intact. Separately test ownership through ORM access, not only through the filtered portal page.

These are identified follow-up tasks; this documentation does not claim they are fixed.

## Collaboration and license

The existing project README credits **Oumaima Ouayres** ([oumas3](https://github.com/oumas3)) and **ELater Khaoula** ([ELATER-KHAOULA](https://github.com/ELATER-KHAOULA)). The manifest currently lists `khaoula` as its author. Both credits are retained here; individual implementation responsibilities are not inferred.

The existing README identifies [LGPL-3.0](https://www.gnu.org/licenses/lgpl-3.0.html). No standalone license file was found in the inspected tree. This documentation preserves the existing attribution and license statement without selecting or changing a license.
