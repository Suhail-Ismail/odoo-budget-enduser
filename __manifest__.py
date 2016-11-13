# -*- coding: utf-8 -*-
{
    'name': "End User",
    'version': '0.1',
    'summary': 'End User Management',
    'sequence': 1,
    'description': """
Odoo Module
===========
Specifically Designed for Etisalat-TBPC

Contractor Management
---------------------
- Region
- Section
- Sub Section
- Contacts
    """,
    'author': "Marc Philippe de Villeres",
    'website': "https://github.com/mpdevilleres",
    'category': 'TBPC Budget',
    'depends': [
        'base',
        'mail',
    ],
    'data': [
        'security/budget_enduser.xml',
        'security/ir.model.access.csv',

        'views/section.xml',
        'views/sub_section.xml',
        'views/region.xml',
        'views/menu.xml',
    ],
    'demo': [
        'demo/budget.region.csv',
        'demo/res.partner.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
