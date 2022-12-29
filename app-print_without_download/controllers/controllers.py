# -*- coding: utf-8 -*-
# from odoo import http


# class App-printWithoutDownload(http.Controller):
#     @http.route('/app-print_without_download/app-print_without_download', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/app-print_without_download/app-print_without_download/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('app-print_without_download.listing', {
#             'root': '/app-print_without_download/app-print_without_download',
#             'objects': http.request.env['app-print_without_download.app-print_without_download'].search([]),
#         })

#     @http.route('/app-print_without_download/app-print_without_download/objects/<model("app-print_without_download.app-print_without_download"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('app-print_without_download.object', {
#             'object': obj
#         })
