# -*- coding: utf-8 -*-
from odoo import models, fields, api


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'
    
    product_custom_id = fields.Char(
        string='Product ID',
        compute='_compute_product_custom_id',
        store=True,
        readonly=False
    )
    
    @api.depends('product_id', 'product_id.product_custom_id')
    def _compute_product_custom_id(self):
        for line in self:
            if line.product_id and hasattr(line.product_id, 'product_custom_id'):
                line.product_custom_id = line.product_id.product_custom_id
            else:
                line.product_custom_id = False