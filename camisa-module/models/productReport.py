# -*- coding: utf-8 -*-

from odoo import models, fields, api

class productReport(models.Model):
    _name = 'product.report'
    _auto = False

    product_name = fields.Integer(
        string='Cliente'
    )
    
    date= fields.Datetime(
        'Fecha compra', readonly=True
    )

    cantidad_producto_vendido = fields.Integer(
        string='Cantidad veces vendido', required=True
    )
        
    @api.model
    def _select(self):
        return '''
            SELECT 
                SUM(quantity) AS cantidad_producto_vendido,
                p.product AS product_name
                b.fecha AS date
        '''

    @api.model
    def _from(self):
        return '''
            bill_lines b
            JOIN product_shirt_product_shirt p ON b.customer_id = p.id 
            JOIN bill v ON b.bill_id = v.id           
    '''
    
    @api.model
    def _group_by(self):
        return '''
            GROUP BY b.product_id, p.product, v.fecha
        '''
    
    @property
    def _table_query(self):
        return '%s %s %s' % (self._select(), self._from(), self._group_by())
        