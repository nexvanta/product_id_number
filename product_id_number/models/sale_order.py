from odoo import models, fields

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    # প্রোডাক্ট মাস্টার থেকে আইডিটি অটোমেটিক নিয়ে আসার জন্য
    product_custom_id = fields.Char(
        related='product_id.product_custom_id', 
        string="Product ID", 
        store=True
    )