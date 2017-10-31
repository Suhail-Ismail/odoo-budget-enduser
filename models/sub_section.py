# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons.budget_utilities.models.utilities import choices_tuple


class SubSection(models.Model):
    _name = 'budget.enduser.sub.section'
    _description = 'Sub Section'
    _inherit = ['budget.res.partner.mixin']

    # CHOICES
    # ----------------------------------------------------------

    # BASIC FIELDS
    # ----------------------------------------------------------

    # RELATIONSHIP
    # ----------------------------------------------------------
    section_id = fields.Many2one('budget.enduser.section', string='Section')

    # BUTTONS AND TRANSITIONS
    # ----------------------------------------------------------
