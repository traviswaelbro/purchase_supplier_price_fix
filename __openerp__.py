# -*- coding: utf-8 -*-
{
    'name': 'Fix Purchase Price Bug',
    'summary': 'Fix $0.00 Unit Price for Suppliers',
    'description': "Fixes issue where unit price would be $0.00 on Purchase Orders when the supplier is set on the PO and the product, but the product's supplier has no 'Unit Price' specified",
    'category': 'Purchase Management',
    'version': '1.0',
    'website': 'https://mbs-standoffs.com',
    'author': 'Travis Waelbroeck',
    'depends': ['base','purchase'],
    'data': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
