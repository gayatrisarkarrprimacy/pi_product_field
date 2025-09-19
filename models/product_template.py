from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # Primary UOM and Quantity fields
    primary_uom_id = fields.Many2one(
        'uom.uom',
        string='Primary UOM',
        help='Primary Unit of Measure for this product'
    )

    primary_qty = fields.Float(
        string='Primary Qty',
        digits='Product Unit of Measure',
        help='Primary quantity for this product'
    )

    # Secondary UOM and Quantity fields
    secondary_uom_id = fields.Many2one(
        'uom.uom',
        string='Secondary UOM',
        help='Secondary Unit of Measure for this product'
    )

    secondary_qty = fields.Float(
        string='Secondary Qty',
        digits='Product Unit of Measure',
        help='Secondary quantity for this product'
    )
