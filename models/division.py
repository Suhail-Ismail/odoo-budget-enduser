# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons.budget_utilities.models.utilities import choices_tuple


class Division(models.Model):
    _name = 'budget.enduser.division'
    _description = 'Division'
    _inherit = ['budget.res.partner.mixin']

    # CHOICES
    # ----------------------------------------------------------

    # BASIC FIELDS
    # ----------------------------------------------------------

    # RELATIONSHIP
    # ----------------------------------------------------------
    section_ids = fields.One2many('budget.enduser.section',
                                  'division_id',
                                  string="Sections")

    # BUTTONS AND TRANSITIONS
    # ----------------------------------------------------------
