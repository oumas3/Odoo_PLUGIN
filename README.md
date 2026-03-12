#  Favorite Products — Odoo Plugin

> A seamless Odoo module that lets customers save and manage their favorite products directly from the customer portal.

---

##  Overview

**Favorite Products** is a custom Odoo 16/17 module that enhances the customer experience by allowing users to bookmark products they love. Built with simplicity and performance in mind, it integrates natively into Odoo's portal and backend with zero configuration hassle.

---

##  Features

- 🔖 **Save Favorites** — Customers can mark any product as a favorite from the portal
- 👤 **Per-User Lists** — Each customer has their own personal favorites list
- 🖥️ **Portal Integration** — Dedicated portal page to view and manage saved products
- 🛠️ **Backend Management** — Admins can view and manage all favorites from the Odoo backend
- 🔐 **Access Control** — Secure permission model via Odoo's access rights system
- ⚡ **REST Controller** — Lightweight HTTP controller for smooth frontend interactions

---

## 🗂️ Module Structure

```
favorite_products/
├── controllers/
│   └── main.py                        # HTTP routes & portal logic
├── data/
│   └── favorite_product.xml           # Default data
├── models/
│   └── favorite_product.py            # Core data model
├── security/
│   └── ir.model.access.csv            # Access rights
├── static/description/
│   └── icon.png                       # Module icon
├── views/
│   ├── favorite_product_views.xml     # Backend views
│   ├── favorite_product_portal_views.xml
│   ├── favorite_product_templates.xml
│   ├── portal_templates.xml           # Portal UI
│   ├── portal_menu.xml                # Portal navigation
│   └── menu.xml                       # Backend menu
├── __manifest__.py                    # Module metadata
└── __init__.py
```

---

## 🚀 Installation

1. **Clone the repository** into your Odoo addons directory:
   ```bash
   git clone https://github.com/oumas3/Odoo_PLUGIN.git
   ```

2. **Add the path** to your `odoo.conf`:
   ```ini
   addons_path = /path/to/Odoo_PLUGIN, ...
   ```

3. **Restart Odoo** and go to:
   `Settings → Activate Developer Mode → Apps → Update App List`

4. **Search for** `Favorite Products` and click **Install** ✅

---

## 🧩 Requirements

| Requirement | Version |
|-------------|---------|
| Odoo | 16.0 or 17.0 |
| Python | 3.10+ |

---

## 👤 Author

**Oumas** — [github.com/oumas3](https://github.com/oumas3)
**ELater Khaoula** — [github.com/oumas3](https://github.com/ELATER-KHAOULA)



---

## 📄 License

This project is licensed under the [LGPL-3.0 License](https://www.gnu.org/licenses/lgpl-3.0.html).

---

<p align="center">Made with ❤️ for the Odoo community</p>
