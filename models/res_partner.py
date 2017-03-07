# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons.budget_utilities.models.utilities import choices_tuple


# TODO BE REMOVE UNTIL ALL DEPENDENCIES TO ALIAS IS OK
class Partner(models.Model):
    _inherit = 'res.partner'

    # CHOICES
    # ----------------------------------------------------------
    STATES = choices_tuple(['active', 'inactive'])

    # BASIC FIELDS
    # ----------------------------------------------------------
    state = fields.Selection(string='State', selection=STATES, default='active')
    alias = fields.Char(string="Alias")

    sub_section_ids = fields.One2many('res.partner',
                                      'sub_section_section_id',
                                      string="Sub Sections")

    sub_section_section_id = fields.Many2one('budget.enduser.section', string='Section')

    remark = fields.Text(string='Remarks')
    is_budget_section = fields.Boolean(string='Is Budget Section')
    is_budget_sub_section = fields.Boolean(string='Is Budget Section')

    # RELATIONSHIP
    # ----------------------------------------------------------

    # BUTTONS AND TRANSITIONS
    # ----------------------------------------------------------
