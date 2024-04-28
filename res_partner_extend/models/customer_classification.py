from odoo import fields, models, api, _


class CustomerClassification(models.Model):
    _name = 'customer_classification'
    _description = 'Customer Classification'

    name = fields.Char(string='Name')
    code = fields.Char(string='Code')
    description = fields.Text(string='Description', size='100')

    _sql_constraints = [
        ('unique_name', 'unique(name)', _('The name must be unique. This name already exists.')),
    ]




