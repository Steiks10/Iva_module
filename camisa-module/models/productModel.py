# -*- coding: utf-8 -*-

from odoo import models, fields, api

class productShirt(models.Model):
    _name = 'product_shirt.product_shirt'
    _order = 'id desc'
    _rec_name = 'product'



    sleeve = fields.Selection(
        [("MangaL","Manga Larga"), ("MangaC", "Manga Corta")],
        string="Tipo de manga"
    )

    product = fields.Char(
        string='Nombre', required=True
    )
    
    price = fields.Integer(
        string='Precio', required=True
    )
    
    description = fields.Char(
        string='Descripcion', required= False
    )
    
    fabric = fields.Char(
        string='Tela', required=False
    )
    
    image = fields.Binary(
        string='Imagen'
    )

    color = fields.Char(
        string="Color", required=False
    )
    
    cantidadVendida = fields.Integer(
        string="Cantidad veces vendida", compute='cantidad_vendida', readonly=False, store=True, default=0
    )
    
    def cantidad_vendida(self):
        #data = self.env['bill'].search_count([('customer_id', 'in', self.ids)])
        data = self.env['bill.lines']._read_group([('product_id', 'in', self.ids)], ['quantity'], ['product_id'])
        mapped_data = dict([(product['product_id'][0], product['quantity']) for product in data])
        for record in self:
            record.cantidadVendida = mapped_data.get(record.id, 0)
    
    
        
