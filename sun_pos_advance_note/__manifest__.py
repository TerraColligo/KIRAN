{
    'name': 'POS Note (Advance)',
    'version': '12.0.1',
    'category': 'Point of Sale',
    'summary': 'With this module you can add advance note for fully order and product wise note.',
    'description': """ With this module you can add advance note for fully order and product wise note.""",
    'price': 9,
    'currency': 'EUR',
    'author': "Kiran Kantesariya",
    'license': 'AGPL-3',
    'depends': ['base', 'point_of_sale'],
    "data": [
        'views/point_of_sale.xml',
        'views/sun_pos_advance_note.xml'
    ],
    'qweb': ['static/src/xml/pos.xml'],
    'installable': True,
    'auto_install': False,
    'images': ['static/description/main_screenshot.png'],
}
