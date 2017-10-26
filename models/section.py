# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons.budget_utilities.models.utilities import choices_tuple


class Section(models.Model):
    _name = 'budget.enduser.section'
    _description = 'Section'
    _inherit = ['budget.enduser.res.partner.mixin']

    # CHOICES
    # ----------------------------------------------------------

    # BASIC FIELDS
    # ----------------------------------------------------------

    # RELATIONSHIP
    # ----------------------------------------------------------
    division_id = fields.Many2one('budget.enduser.division', string='Division')
    sub_section_ids = fields.One2many('budget.enduser.sub.section',
                                      'section_id',
                                      string="Sub Sections")

    # BUTTONS AND TRANSITIONS
    # ----------------------------------------------------------
