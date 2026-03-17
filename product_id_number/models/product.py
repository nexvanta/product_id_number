# -*- coding: utf-8 -*-
from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    product_custom_id = fields.Char(
        string='Product Custom ID',
        help='Custom Product ID Number'
    )

class ProductProduct(models.Model):
    _inherit = 'product.product'
    
    product_custom_id = fields.Char(
        string='Product Custom ID',
        related='product_tmpl_id.product_custom_id',
        store=True,
        readonly=False
    )

class StockQuant(models.Model):
    _inherit = 'stock.quant'

    # ইনভেন্টরি রিপোর্টে প্রোডাক্ট আইডি দেখানোর জন্য রিলেটেড ফিল্ড
    product_custom_id = fields.Char(
        related='product_id.product_custom_id', 
        string='Product ID', 
        store=True
    )
    