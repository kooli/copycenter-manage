# -*- coding: utf-8 -*-
{
    'name': "CopyCenter Uniflex",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Ferdinand KAKAM NGANGOUE, System Admin | Full Stack BackEnd & FrondEnd Developper ",
    'website': "http://www.meiji-cm.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/templates.xml',
        'views/type_transaction_view.xml',
        'views/credeb_view.xml',
        'views/abonnement.xml',
        'views/menu.xml',
        'views/views.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}