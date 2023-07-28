from odoo import models, fields, api
import odoo.sql_db

class Customer(models.Model):
    _name='customer.customer'
    _order= 'id desc'
    
    #invoices = fields.One2Many('my_product.product', 'product_id', string='Invoices')
    
    name = fields.Char(
        string='Nombre', required=True
    )
    
    apellido = fields.Char(
        string='Apellido', required=True
    )
    
    cantidadcompra = fields.Integer(
        string='Total de ventas', store=True, compute='cantidad_ventas', required=True, default=0
    )
    
    cantidad_productos= fields.Integer(
         string='Cantidad productos comprados', store=True, compute='cantidad_productos_comprados', required=True, default=0
    )
    
    def cantidad_ventas(self):
        #data = self.env['bill'].search_count([('customer_id', 'in', self.ids)])
        data = self.env['bill']._read_group([('customer_id', 'in', self.ids)], ['customer_id'], ['customer_id'])
        mapped_data = dict([(customer['customer_id'][0], customer['customer_id_count']) for customer in data])
        for record in self:
            record.cantidadcompra = mapped_data.get(record.id, 0)
            
    def cantidad_productos_comprados(self):
        #data = self.env['bill'].search_count([('customer_id', 'in', self.ids)])
        data = self.env['bill']._read_group([('customer_id', 'in', self.ids)], ['cantidad_productos'], ['customer_id'])
        mapped_data = dict([(customer['customer_id'][0], customer['cantidad_productos']) for customer in data])
        for record in self:
            record.cantidad_productos = mapped_data.get(record.id, 0)
        
    
    