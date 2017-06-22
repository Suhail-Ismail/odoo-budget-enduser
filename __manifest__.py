# -*- coding: utf-8 -*-
{
    'name': "End User",
    'version': '0.1',
    'summary': 'End User Management',
    'sequence': 2,
    'description': """
Odoo Module
===========
Specifically Designed for Etisalat-TBPC

Contractor Management
---------------------
- Region
- Division
- Section
- Access Users
        - Dependent - Can readonly
        - User - General Usage except delete power, can Edit recurrence but not create
        - Manager - All power to manipulate data
    """,
    'author': "Marc Philippe de Villeres",
    'website': "https://github.com/mpdevilleres",
    'category': 'TBPC Budget',
    'depends': [
        'budget_utilities',
    ],
    'data': [
        'security/budget_enduser.xml',
        'security/ir.model.access.csv',

        'views/division.xml',
        'views/section.xml',
        'views/sub_section.xml',
        'views/region.xml',
        'views/menu.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
