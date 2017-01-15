# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons.budget_utilities.models.utilities import choices_tuple

class Section(models.Model):
    _inherit = 'res.partner'
    _rec_name = 'name'
    _description = 'Section'

    # CHOICES
    # ----------------------------------------------------------
    STATES = choices_tuple(['active', 'inactive'])

    # BASIC FIELDS
    # name exist already
    # ----------------------------------------------------------
    alias = fields.Char(string="Alias")
    is_budget_section = fields.Boolean(string='Is Budget Section')

    state = fields.Selection(string='State', selection=STATES, default='active')

    note = fields.Text(string='Note')

    # RELATIONSHIP
    # ----------------------------------------------------------
    sub_section_ids = fields.One2many('res.partner',
                                  'sub_section_section_id',
                                  string="Sub Sections")

    # BUTTONS AND TRANSITIONS
    # ----------------------------------------------------------
    @api.one
    def set2active(self):
        self.state = 'active'

    @api.one
    def set2inactive(self):
        self.state = 'inactive'
