# -*- coding: utf-8 -*-
# from odoo import http


# class Covid-module(http.Controller):
#     @http.route('/covid-module/covid-module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/covid-module/covid-module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('covid-module.listing', {
#             'root': '/covid-module/covid-module',
#             'objects': http.request.env['covid-module.covid-module'].search([]),
#         })

#     @http.route('/covid-module/covid-module/objects/<model("covid-module.covid-module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('covid-module.object', {
#             'object': obj
#         })
