# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons.budget_utilities.models.utilities import choices_tuple


class Division(models.Model):
    _name = 'budget.enduser.division'
    _description = 'Division'
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
    section_ids = fields.One2many('budget.enduser.section',
                                  'division_id',
                                  string="Sections")

    # BUTTONS AND TRANSITIONS
    # ----------------------------------------------------------
    @api.one
    def set2active(self):
        self.state = 'active'

    @api.one
    def set2inactive(self):
        self.state = 'inactive'
