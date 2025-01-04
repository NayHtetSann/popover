from odoo import models, fields


class DynamicPopOver(models.Model):
    _name = 'dynamic.popup'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'image.mixin']
    _order = 'sequence desc'

    name = fields.Char('Description')
    image = fields.Binary('Popover Image')
    image_size = fields.Selection([('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')], string='Size', help='adjust image size')
    date_from = fields.Date('Date From', default=fields.Date.today())
    date_to = fields.Date('Date To', default=fields.Date.today())
    active = fields.Boolean('Active', default=True)
    sequence = fields.Integer('Sequence')
    user_id = fields.Many2one('res.users', string='Created By', default=lambda self: self.env.uid)
