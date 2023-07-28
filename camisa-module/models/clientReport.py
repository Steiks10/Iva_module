# -*- coding: utf-8 -*-

from odoo import models, fields, api

class clientReport(models.Model):
    _name = 'client.report'
    _auto = False

    customer_name = fields.Integer(
        string='Cliente'
    )
    
    date= fields.Datetime(
        'Fecha compra', readonly=True
    )

    cantidad_compras = fields.Integer(
        string='Cantidad compras', required=True
    )

    cantidad_productos_comprados = fields.Integer(
        string='Cantidad', required=False
    )
        
    @api.model
    def _select(self):
        return '''
            SELECT 
                SUM(cantidad_productos) AS cantidad_productos_comprados,
                COUNT(*) AS cantidad_compras, 
                c.nombre AS customer_name,
                b.fecha AS date
        '''

    @api.model
    def _from(self):
        return '''
            bill b
            JOIN customer_customer c ON b.customer_id = c.id
            
    '''
    
    @api.model
    def _group_by(self):
        return '''
            GROUP BY b.customer_id, c.name
        '''
    
    @property
    def _table_query(self):
        return '%s %s %s' % (self._select(), self._from(), self._group_by())
        