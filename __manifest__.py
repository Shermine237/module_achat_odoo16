# -*- coding: utf-8 -*-
{
    'name': "achat",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Megane",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['purchase', 'purchase_stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        "wizards/purchase_order_recommendation_view.xml",
        "views/purchase_order_views.xml",
        'views/views.xml',
        'views/templates.xml',
        "views/res_partner.xml",
        "views/res_config_view.xml",
        'views/purchase_order_line_views.xml',
        #'reports/report.xml',
        #'reports/commande.xml',
        #'reports/pivot.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
