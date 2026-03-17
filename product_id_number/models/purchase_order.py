from odoo import models, fields

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    product_custom_id = fields.Char(
        related='product_id.product_custom_id', 
        string='Product ID', 
        store=True
    )