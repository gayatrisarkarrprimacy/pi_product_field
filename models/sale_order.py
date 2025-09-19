from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    # Alternative UOM fields
    alt_qty = fields.Float(
        string='Alt Qty',
        digits='Product Unit of Measure',
        compute='_compute_alternative_uom_data',
        store=True
    )

    alt_price = fields.Float(
        string='Alt Price',
        digits='Product Price',
        compute='_compute_alternative_uom_data',
        store=True
    )

    alt_uom = fields.Char(
        string='Alt UOM',
        compute='_compute_alternative_uom_data',
        store=True
    )

    @api.depends('product_id', 'product_uom_qty', 'product_uom', 'price_unit')
    def _compute_alternative_uom_data(self):
        for line in self:
            if line.product_id and line.product_uom_qty and line.product_uom:
                try:
                    product_tmpl = line.product_id.product_tmpl_id

                    # Initialize result
                    alt_qty = 0.0
                    alt_price = 0.0
                    alt_uom = ''

                    # Check if primary or secondary UOM is configured
                    if product_tmpl.primary_uom_id and product_tmpl.primary_qty > 0:
                        # Use primary UOM calculation
                        conversion_factor = product_tmpl.primary_qty
                        alt_qty = line.product_uom_qty / conversion_factor
                        alt_uom = product_tmpl.primary_uom_id.name

                    elif product_tmpl.secondary_uom_id and product_tmpl.secondary_qty > 0:
                        # Use secondary UOM calculation
                        conversion_factor = product_tmpl.secondary_qty
                        alt_qty = line.product_uom_qty / conversion_factor
                        alt_uom = product_tmpl.secondary_uom_id.name

                    # Calculate alternative price
                    if alt_qty > 0:
                        total_amount = line.price_unit * line.product_uom_qty
                        alt_price = total_amount / alt_qty

                    line.alt_qty = alt_qty
                    line.alt_price = alt_price
                    line.alt_uom = alt_uom

                except Exception:
                    line.alt_qty = 0.0
                    line.alt_price = 0.0
                    line.alt_uom = ''
            else:
                line.alt_qty = 0.0
                line.alt_price = 0.0
                line.alt_uom = ''