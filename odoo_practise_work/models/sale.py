from odoo import models, api, fields, _
from datetime import datetime, date
from odoo.exceptions import UserError

class SaleWork(models.Model):

    _inherit = "sale.order"

    @api.multi
    def action_confirm(self):
        print("This is the Override Function")
        res = super(SaleWork, self).action_confirm()
        return res

    sale_order = fields.Char(string="Sale Order")
