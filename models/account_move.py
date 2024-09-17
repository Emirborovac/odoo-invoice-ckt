import logging
from odoo import models, fields, api


_logger = logging.getLogger(__name__)


file_handler = logging.FileHandler('C:\\Program Files\\Odoo 17.0.20240911\\server\\odoo\\addons\\invoice_ckt_extension\\account_move_logs.log')


file_handler.setLevel(logging.INFO)


formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)


_logger.addHandler(file_handler)


_logger.propagate = False

class AccountMove(models.Model):
    _inherit = 'account.move'

    ckt = fields.Selection(
        [('12K', '12K'), ('18K', '18K'), ('24K', '24K')],
        string="Company Karat Type (CKT)",
        default='24K',
    )

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    

    weight = fields.Float(
        string="Weight",
        help="Actual weight of the item in grams."
    )

    