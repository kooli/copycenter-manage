# -*- coding: utf-8 -*-
from odoo import http

# class CopycenterUniflex(http.Controller):
#     @http.route('/copycenter_uniflex/copycenter_uniflex/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/copycenter_uniflex/copycenter_uniflex/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('copycenter_uniflex.listing', {
#             'root': '/copycenter_uniflex/copycenter_uniflex',
#             'objects': http.request.env['copycenter_uniflex.copycenter_uniflex'].search([]),
#         })

#     @http.route('/copycenter_uniflex/copycenter_uniflex/objects/<model("copycenter_uniflex.copycenter_uniflex"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('copycenter_uniflex.object', {
#             'object': obj
#         })