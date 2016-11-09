# -*- coding: utf-8 -*-

from odoo import models, fields, api
from utils import choices_tuple

class SubSection(models.Model):
    _inherit = 'res.partner'
    _rec_name = 'name'
    _description = 'Sub Section'

    # CHOICES
    # ----------------------------------------------------------
    STATES = choices_tuple(['active', 'inactive'])
    # BASIC FIELDS
    # name exist already
    # alias exist already
    # ----------------------------------------------------------
    state = fields.Selection(string='State', selection=STATES, default='active')
    is_budget_sub_section = fields.Boolean(string='Is Budget Sub Section')

    # RELATIONSHIP
    # ----------------------------------------------------------
    sub_section_section_id = fields.Many2one('res.partner', string='Section',
                                 domain=[('is_budget_section','=',True)])

    # BUTTONS AND TRANSITIONS
    # ----------------------------------------------------------
    @api.one
    def set2active(self):
        self.state = 'active'

    @api.one
    def set2inactive(self):
        self.state = 'inactive'
