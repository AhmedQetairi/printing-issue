# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class app-print_without_download(models.Model):
#     _name = 'app-print_without_download.app-print_without_download'
#     _description = 'app-print_without_download.app-print_without_download'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
