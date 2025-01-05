# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Dynamic Popover',
    'version': '18.0.0.1',
    'category': 'Website/Website',
    'author': 'NHS',
    'summary': 'Multi dynamic popovers',
    'website': 'www.syrupsbiz.com',
    'description': """
- View image in list
- Multi dyanmic popover in website
- Enable and disable popover in website
    """,
    'depends': ['website'],
    'data': [
        'security/ir.model.access.csv',
        'views/dynamic_popover_view.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            'dynamic_popover/static/src/css/popover.css',
            'dynamic_popover/static/src/xml/popover.xml',
            'dynamic_popover/static/src/js/popover.js',
        ],
        'web.assets_backend': [
            'dynamic_popover/static/src/css/custom.css',
        ],
    },
    'images':  ['static/description/image_3.jpg'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3'
}
