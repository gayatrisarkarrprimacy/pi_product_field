{
    'name': 'Product Inventory Fields',
    'version': '18.0.1.0.0',
    'category': 'Inventory',
    'summary': 'Add Primary and Secondary UOM fields to Product Logistics',
    'description': """
        This module adds four new fields to the product logistics section:
        - Primary UOM
        - Primary Qty
        - Secondary UOM  
        - Secondary Qty
    """,
    'author': 'Primacy Infotech Pvt. Ltd.',
    'depends': ['stock', 'product', 'sale', 'uom', 'base'],
    'data': [
        'views/product_template_views.xml',
        'views/sale_order_views.xml',
        'reports/sale_report_templates.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
