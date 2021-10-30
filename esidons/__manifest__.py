# -*- coding: utf-8 -*-
{
    'name': "dons",

    'summary': """Lancer et collecter des dons""",

    'description': """
         Dons module pour gérer les collectes des dons:
            - Lancement des collecte.
            - Affectation des dons.           
    """,

    'author': "KESSI et KETFI",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'templates.xml',
        'views/esidons.xml',
        'reports.xml',
        'report_recap.xml'

    ],

    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
   
}
