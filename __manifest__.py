# __manifest__.py

{
    'name': 'Invoice CKT Extension',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Adds a CKT field to invoices',
    'depends': ['account'],
    'data': [
        'views/account_move_views.xml',  
    ],
}
