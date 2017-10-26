# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Region(models.Model):
    _name = 'budget.enduser.region'
    _rec_name = 'alias'
    _inherit = ['budget.enduser.res.partner.mixin']

    # BASIC FIELDS
    # ----------------------------------------------------------
