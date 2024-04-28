# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class ResPartner(models.Model):
    _inherit = 'res.partner'

    customer_classification_id = fields.Many2one(comodel_name='customer_classification',
                                                 string='Custumer Classification',
                                                 tracking=True)


