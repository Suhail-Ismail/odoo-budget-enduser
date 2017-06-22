# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons.budget_utilities.models.utilities import choices_tuple


class SubSection(models.Model):
    _name = 'budget.enduser.sub.section'
    _description = 'Sub Section'
    _rec_name = 'name'
    _inherit = ['partner.mixin']

    # CHOICES
    # ----------------------------------------------------------
    STATES = choices_tuple(['active', 'inactive'])

    # BASIC FIELDS
    # name exist already
    # ----------------------------------------------------------
    state = fields.Selection(string='State', selection=STATES, default='active')

    alias = fields.Char(string="Alias")

    remark = fields.Text(string='Remarks')

    # RELATIONSHIP
    # ----------------------------------------------------------
    section_id = fields.Many2one('budget.enduser.section', string='Section')

    # BUTTONS AND TRANSITIONS
    # ----------------------------------------------------------
    @api.one
    def set2active(self):
        self.state = 'active'

    @api.one
    def set2inactive(self):
        self.state = 'inactive'
