from odoo import models, fields, api

class billModel(models.Model):
    _name= 'bill'
    
    customer_id = fields.Many2one('customer.customer', string='Cliente') 
    fecha = fields.Datetime(string='Date Time', required=True, default=fields.Datetime.now())
    bill_lines_ids = fields.One2many('bill.lines', 'bill_id', string='Productos')  
    cantidad_productos = fields.Integer(string='Cantidad Productos', store=True, compute='set_total_cantidad', required=True, default=0)
    cantidad_total = fields.Float(string='Total', compute='set_total',required=True, default=0)
    cantidad_IVA = fields.Float(string='IVA', compute='set_IVA', required=True, default=0)
    cantidad_total_compra = fields.Float(string='Cantidad total de compra', compute='set_total_compra', required=True, default=0)

    @api.depends('bill_lines_ids.quantity', 'bill_lines_ids.product_id')
    def set_total(self):
        for record in self:
            total = 0.0
            for item in record.bill_lines_ids:
                total += item.quantity * item.product_id.price
            record.cantidad_total = total

    @api.depends('bill_lines_ids.quantity')
    def set_total_cantidad(self):
        for record in self:
            total = 0
            for item in record.bill_lines_ids:
                total += item.quantity
            record.cantidad_productos = total

    def set_IVA(self):
        for record in self:
            record.cantidad_IVA= record.cantidad_total*0.16
    
    def set_total_compra(self):
        for record in self:
            record.cantidad_total_compra= record.cantidad_total+ record.cantidad_IVA
    
    
class billLines(models.Model):
    _name='bill.lines'
    
    bill_id=fields.Many2one('bill', string='bill')
    product_id = fields.Many2one('product_shirt.product_shirt', string='Productos')
    quantity = fields.Integer(string='Cantidad', default=1, required=True)
    
    
    # @api.model
    # def add_bill_line(self):
    #     self.ensure_one()
    #     self.bill_lines_ids.create({'bill_id': self.id})
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': 'Productos',
    #         'res_model': 'bill.lines',
    #         'view_type': 'form',
    #         'view_mode': 'form',
    #         'target': 'current',
    #         'context': {'default_bill_id': self.id},
    #     }
    
    # @api.model
    # def create_bill_line_and_clear_form(self):
    #     self.ensure_one()
    #     self.bill_lines_ids.create({'bill_id': self.id})
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': 'Producto',
    #         'res_model': 'bill.lines',
    #         'view_type': 'form',
    #         'view_mode': 'form',
    #         'target': 'current',
    #         'context': {'default_bill_id': self.id},
    #     }