# -*- coding: utf-8 -*-
#
# Autor: Julián Toscano
# Desarrollador y Consultor Odoo
# linkedin: https://www.linkedin.com/in/jotate70/
# Email: jotate70@gmail.com
# Github: jotate70
# Cel. +57 3147754740

{
    'name': "Customer classification",

    'summary': """ Example.
        """,

    'description': """
        15.0.0.0 Initial.
    """,

    'author': "Julián Toscano",
    'website': "https://linktic.com",

    'category': 'base',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'contacts',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/customer_classification_view_extend.xml',
        'views/res_partner_inherit_view.xml',
    ],

    'installable': True,
    'application': True,

    'license': 'LGPL-3',
}


